from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Contactus

# Create your views here.


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        subject = request.POST.get('Subject')
        message = request.POST.get('Message')
        contact = Contactus(name=name, email=email,
                            subject=subject, message=message)
        contact.save()
        return render(request, 'pages/thankyou.html')
    return redirect('home')
