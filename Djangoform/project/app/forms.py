from django import forms 
from .models import Student


# class Studentform(forms.Form):
#     Name=forms.CharField(max_length=20)
#     Email=forms.EmailField(max_length=20)
#     Age=forms.IntegerField()
#     City=forms.CharField()

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
      















    # from django.core.exceptions import ValidationError
    # def clean(self):
    #     cleaned_data = super().clean()
    #     errors = {}

    #     name = cleaned_data.get('name')
    #     age = cleaned_data.get('age')
    #     email = cleaned_data.get('email')

    #     if name:
    #         if not name.isalpha():
    #             errors['name'] = "Name must contain only alphabets"
    #         elif len(name) < 3 or len(name) > 10:
    #             errors['name'] = "Name must be between 3 and 10 characters"

    #     if age:
    #         if age < 18 or age > 60:
    #             errors['age'] = "Age must be between 18 and 60"

    #     if email:
    #         if not email.endswith("@gmail.com"):
    #             errors['email'] = "Only Gmail email allowed"

    #     if errors:
    #         raise ValidationError(errors)

    #     return cleaned_data