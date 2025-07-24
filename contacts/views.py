from django.shortcuts import render
from .models import Contact

# Create your views here.

def index(request):
    return render(request, "contacts/index.html")

def new_contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobile_no = request.POST["mobile_no"]
        email = request.POST["email"]

        Contact.objects.create(name=name, mobile_no=mobile_no, email=email)
        return render(request, "contacts/new_contact.html", {
            "saved": "Contact saved"
        })

    return render(request, "contacts/new_contact.html")

def show_contact(request):
    all_contacts = Contact.objects.all()
    return render(request, "contacts/show_contact.html", {
        "all_contacts": all_contacts
    })