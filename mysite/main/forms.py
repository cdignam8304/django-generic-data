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


# Get field names and field values for a model instance
# https://stackoverflow.com/questions/2170228/iterate-over-model-instance-field-names-and-values-in-template


# Code to get list of fields for an instance of Schema:
# fieldnames = [field.name for field in Schema._meta.get_fields()[1:]]
# for field in fieldnames: 
#     fname = getattr(Schema.objects.all().filter(schema_name__exact="Fruit")[0], field) 
#         if fname != "": 
#             print(fname)


class Generic_Form(forms.ModelForm):
    
    class Meta:
        model = Generic
        fields = [
            'schema_name',
            'string1',
            'string2',
            'string3',
            'string4',
            'string5',
            'date1',
            'date2',
            'date3',
            'amount1',
            'amount2',
            'status',
            ]








