from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):  #modelform autocreate form based on the model fields
    class Meta:   #it is a inner class used to give metadata about model to the django form, it tells django
        model = Contact  #which model to use
        fields = ['name', 'mobile_no', 'email'] #which fiels to include/exclude

        #modelform make the form values as a (object)instance for model, we can have control to validate, modify before saving 
        