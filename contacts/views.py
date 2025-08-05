from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect #redirect is simple step for httpresponseredirect and reverse
from .models import Contact
from .form import ContactForm
from django.urls import reverse


# Create your views here.

def index(request):
    all_contacts = Contact.objects.all().order_by('name')  #order by is like in sql 
    return render(request, "contacts/index.html",{
        "all_contacts": all_contacts
    })

def new_contact(request):
    form = ContactForm(request.POST or None)  #in this if request is get, it gives empty form, if request is POST, the form becomes data with user input 
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, "contacts/new_contact.html",{
        "form" : form
    })

def edit_contact(request, pk):
    contact = Contact.objects.get(pk = pk)
    form = ContactForm(request.POST or None, instance=contact) #here, instace help to prefill the form with pk's object data
                                                            #so it dont come as empty form and we can edit the form 
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, "contacts/new_contact.html",{
        "form": form
    })

def delete_contact(request, pk):
    contact = Contact.objects.get(pk = pk)
    if request.method == 'POST':
        contact.delete()
        return HttpResponseRedirect(reverse('index'))
    
    return render(request, "contacts/delete_contact.html",{
        "contact": contact
    })

