from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import re

def signupviews(request):
    if request.method == "POST":
        email = request.POST.get('email', '').strip()
        password = request.POST.get('pass1', '').strip()
        confirm_password = request.POST.get('pass2', '').strip()

        # ✅ Validate email format
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            messages.error(request, "Invalid email format.")
            return render(request, 'signup.html')

        # ✅ Ensure passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')

        # ✅ Check password strength
        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return render(request, 'signup.html')

        # ✅ Ensure email is unique
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('/auth/signup/')

        # ✅ Create user (Use email as username)
        username = email.split('@')[0]  # Use part of email as username
        user = User.objects.create_user(username=username, email=email, password=password)

        # 🔥 No activation required!
        user.save()

        messages.success(request, "Account created successfully! You can now log in.")
        return redirect('/')  # Redirect to homepage immediately after signup

    return render(request, "signup.html")


def handlelogin(request):
    if request.method == "POST":
        email = request.POST.get('email', '').strip()
        password = request.POST.get('pass1', '').strip()

        # ✅ Ensure both fields are provided
        if not email or not password:
            messages.error(request, "Email and password are required.")
            return redirect('/auth/login/')

        # ✅ Find the user by email
        try:
            user = User.objects.get(email=email)  
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return redirect('/auth/login/')

        # ✅ Authenticate using username (not email)
        myuser = authenticate(request, username=user.username, password=password)

        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login successful!")
            return redirect('/')  # ✅ Directly open homepage
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('/auth/login/')

    return render(request, 'login.html')


def handlelogout(request):
    logout(request)  # Log the user out
    messages.success(request, "You have been logged out.")
    return redirect('/auth/login/')  # Redirect to login page after logout
