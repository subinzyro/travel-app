from django import forms 
from travelapp.models import Travel_reg,Travel_book

class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel_reg
        fields = "__all__"
        
class TravelBookForm(forms.ModelForm):
    class Meta():
        model=Travel_book
        fields = "__all__"