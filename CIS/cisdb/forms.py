from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import *


STATE = (
    ("Choose...","Choose... "),
    ("Abia","Abia"),
    ("Adamawa","Adamawa"),
    ("Akwa Ibom","Akwa Ibom"),
    ("Anambra","Anambra"),
    ("Bauchi","Bauchi"),
    ("Bayelsa","Bayelsa"),
    ("Benue","Benue"),
    ("Borno","Cross River"),
    ("Cross River","Cross River"),
    ("Delata","Delta"),
    ("Ebonyi","Ebonyi"),
    ("Edo","Edo"),
    ("Ekiti","Ekiti"),
    ("Enugu","Enugu"),
    ("Gombe","Gombe"),
    ("Imo","Imo"),
    ("Jigawa","Jigawa"),
    ("Kaduna","Kano"),
    ("Katsina","Katsina"),
    ("Kebbi","Kebbi"),
    ("Kogi","Kogi"),
    ("Kwara","Kwara"),
    ("Lagos","Lagos"),
    ("Nasarawa","Nasarawa"),
    ("Niger","Niger"),
    ("Ogun","Ogun"),
    ("Ondo","Ondo"),
    ("Osun","Osun"),
    ("Oyo","Oyo"),
    ("Plateau","Plateau"),
    ("Rivers","Rivers"),
    ("Sokoto","Taraba"),
    ("Yobe",'Yobe'),
    ("Zamfara","Zamfara"),
)

GENDER = (
    ("Choose...","Choose... "),
    ("Male","Male"),
    ("Female","Female")
)

BLOOD_TYPE = (
    ("Choose...","Choose... "),
    ("A", 'A'),
    ("B", "B"),
    ("AB", "AB"),
    ("O", "O")
)

GENOTYPE = (
    ("Choose...","Choose... "),
    ("AA","AA"),
    ("AS","AS"),
    ("SS","SS"),
    ("Other","Others: CC, AC..")
)


MARITIAL_STATUS = (
    ("Choose...","Choose... "),
    ("Single","Single"),
    ("Married","Married"),
    ("Divorced","Divorced"),
    ("Widowed","Widowed"),
)


class CitizenForm(ModelForm):
    class Meta:
        model = Citizen
        exclude = ()

class ImageForm(forms.Form):
    image = forms.FileField()

class SearchForm(forms.Form):
    query = forms.CharField(help_text="Enter search query")

class QueryForm(forms.Form):
    gender = forms.ChoiceField(choices=GENDER)
    marital_status = forms.ChoiceField(choices=MARITIAL_STATUS)
    state = forms.ChoiceField(choices=STATE)
    state_residence = forms.ChoiceField(choices=STATE)
    genotype  = forms.ChoiceField(choices=GENOTYPE)
    blood_group = forms.ChoiceField(choices=BLOOD_TYPE)



