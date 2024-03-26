from django import forms 
from travelapp.models import Travel_reg,Travel_book
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget

# class YourForm(forms.Form):
#     your_date_field = DateField(widget=AdminDateWidget)

class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel_reg
        fields = "__all__"
        
class TravelBookForm(forms.ModelForm):
    class Meta:
        model=Travel_book
        fields = "__all__"
        widgets = {
            'sdate': forms.DateInput(attrs={'type': 'date'}),
            'edate': forms.DateInput(attrs={'type': 'date'}),

        }

    def clean(self):
        cleaned_data = super().clean()
        location = cleaned_data.get("location")
        destination = cleaned_data.get("destination")
        if location ==  destination:
            raise forms.ValidationError("location should not be same as the destination!")
        return cleaned_data