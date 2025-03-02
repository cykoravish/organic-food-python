from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from authcart.models import Contact, Product, OrderUpdate, Orders, Blog, Review
from django.urls import reverse
from authcart.forms import ReviewForm
from django.contrib import messages
from math import ceil
from django.conf import settings
import razorpay  # Import Razorpay SDK
import json
from django.views.decorators.csrf import csrf_exempt

# Initialize Razorpay client
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def index(request):
    allProds = []
    categories = Product.objects.values_list('category', flat=True).distinct()
    for category in categories:
        products = Product.objects.filter(category=category)
        n = len(products)
        nSlides = (n + 3) // 4
        allProds.append([products, range(1, nSlides + 1), nSlides])
    return render(request, "index.html", {'allProds': allProds})

def products(request):
    allProds = []
    categories = Product.objects.values_list('category', flat=True).distinct()
    for category in categories:
        products = Product.objects.filter(category=category)
        n = len(products)
        nSlides = (n + 3) // 4
        allProds.append([products, range(1, nSlides + 1), nSlides])
    return render(request, "products.html", {'allProds': allProds})

def about(request):
    return render(request, 'about.html')

def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Login & Try Again")
        return redirect('/auth/login')

    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = int(float(request.POST.get('amt')) * 100)  # Razorpay expects amount in paise
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        Order = Orders(
            items_json=items_json,
            name=name,
            amount=amount / 100,
            email=email,
            address1=address1,
            address2=address2,
            city=city,
            state=state,
            zip_code=zip_code,
            phone=phone
        )
        Order.save()

        # Create Razorpay order
        razorpay_order = razorpay_client.order.create({
            "amount": amount,
            "currency": "INR",
            "payment_capture": "1"
        })

        return render(request, 'razorpay_payment.html', {
            'order_id': razorpay_order['id'],
            'amount': amount,
            'key_id': settings.RAZORPAY_KEY_ID,
            'name': name,
            'email': email,
            'phone': phone,
        })
    else:
        return render(request, 'checkout.html')

def blog_list(request):
    blog_posts = Blog.objects.all()
    return render(request, 'Blog.html', {'blog_posts': blog_posts})

def blog_detail(request, id):
    post = get_object_or_404(Blog, id=id)
    return render(request, 'blog_detail.html', {'post': post})

def review_page(request):
    if request.method == "POST":
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        review_text = request.POST.get('review_text')
        image = request.FILES.get('image')
        if name and rating and review_text:
            Review.objects.create(name=name, rating=rating, review_text=review_text, image=image)
            messages.success(request, "Thank you! Your review has been submitted.")
            return redirect('review_page')
    reviews = Review.objects.all().order_by('-id')
    return render(request, 'reviews.html', {'reviews': reviews})

def Feature(request):
    return render(request, 'Feature.html')

def contactview(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        message = request.POST.get('message')
        if name and email and phonenumber and message:
            Contact.objects.create(name=name, email=email, phonenumber=phonenumber, message=message)
            messages.success(request, "We will get back to you soon..")
        else:
            messages.error(request, "All fields are required!")
    return render(request, 'contact.html')
