from django import forms
from crud.models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'email', 'dob']

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if dob > date.today():
            raise forms.ValidationError("Date of birth cannot be in the future.")
        return dob
