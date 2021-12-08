from django import forms

# creating a form
class InputForm(forms.Form):

    class_type = forms.CharField(max_length = 200)
    eyes = forms.CharField(max_length = 200)