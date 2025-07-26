from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Contact
from django.urls import reverse


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

def delete_contact(request):
    if request.method == 'POST':
        Contact.objects.get(pk = int(request.POST["contact"])).delete()
        return HttpResponseRedirect(reverse('show_contact'))
    
    return render(request, "contacts/delete_contact.html",{
        "contacts": Contact.objects.all()
    })

def edit_contact(request):
    if request.method == "POST":
        if 'form1' in request.POST:
            contact = Contact.objects.get(pk = int(request.POST["contact"]))
            return render(request, "contacts/edit_contact.html",{
                "contact":contact
            })
        elif 'form2' in request.POST:
            new_name = request.POST['name']
            new_mobile_no = request.POST["mobile_no"]
            new_email = request.POST["email"]
            edit_contact = Contact.objects.get(pk = int(request.POST["id"]))
            edit_contact.name = new_name
            edit_contact.mobile_no = new_mobile_no
            edit_contact.email = new_email
            edit_contact.save()
            return HttpResponseRedirect(reverse('show_contact'))
        
    return render(request, "contacts/edit_contact.html",{
        "contacts": Contact.objects.all()
    })