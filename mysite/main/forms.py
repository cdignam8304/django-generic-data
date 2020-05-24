from django import forms
from .models import Contact, Schema, Generic


class Contact_Form(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = [
            "first_name",
            "last_name",
            "email",
            "city",
            "dob",
            "contact_type",
            "mktg_opt_in",
            "is_active",
            ]


class Generic_Form(forms.ModelForm):
    
    class Meta:
        model = Generic
        fields = [field.name for field in Schema._meta.get_fields()]
        fields.remove("schema_name")
        fields.remove("generic")







