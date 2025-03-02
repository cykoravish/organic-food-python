import razorpay
from django.conf import settings

def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Login & Try Again")
        return redirect('/auth/login')

    if request.method == "POST":
        amount = int(float(request.POST.get('amt')) * 100)  # Convert to paise
        currency = "INR"

        # Initialize Razorpay client
        razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        # Create order
        try:
            razorpay_order = razorpay_client.order.create({
                "amount": amount,
                "currency": currency,
                "payment_capture": "1"
            })
        except razorpay.errors.BadRequestError as e:
            return HttpResponse(f"Razorpay Authentication Failed: {str(e)}")

        context = {
            "order_id": razorpay_order["id"],
            "amount": amount,
            "currency": currency,
            "key_id": settings.RAZORPAY_KEY_ID
        }
        return render(request, 'razorpay_checkout.html', context)

    return render(request, 'checkout.html')
