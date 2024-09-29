from django import forms
from .models import BioModel,NonBioModel,HazModel,HomeModel,User
from django.contrib.auth.forms import UserCreationForm


class BioMWaste(forms.ModelForm):
    class Meta:
        model=BioModel
        fields="__all__"
        widgets={
            "fullname":forms.TextInput(attrs={"class":"form-control"}),
            "wasteweight":forms.TextInput(attrs={"class":"form-control"}),
            "location":forms.TextInput(attrs={"class":"form-control"}),
            
        }
    
class NBioMWaste(forms.ModelForm):
    class Meta:
        model=NonBioModel
        fields="__all__"
        widgets={
            "fullname":forms.TextInput(attrs={"class":"form-control"}),
            "wasteweight":forms.TextInput(attrs={"class":"form-control"}),
            "location":forms.TextInput(attrs={"class":"form-control"}),
            
        }
    
    

class HazMWaste(forms.ModelForm):
    class Meta:
        model=HazModel
        fields="__all__"
        widgets={
            "fullname":forms.TextInput(attrs={"class":"form-control"}),
            "wasteweight":forms.TextInput(attrs={"class":"form-control"}),
            "location":forms.TextInput(attrs={"class":"form-control"}),
            
        }

class HomeMWaste(forms.ModelForm):
    class Meta:
        model=HomeModel
        fields="__all__"
        # widgets={
        #     "Name":forms.TextInput(attrs={"class":"form-control"}),
        #     "Weight In Kg Without Fractions":forms.TextInput(attrs={"class":"form-control"}),
        #     "Address":forms.Textarea(attrs={"class":"form-control"}),
        #     "City":forms.TextInput(attrs={"class":"form-control"}),
        #     "Phone":forms.IntegerField(),
        #     "State":forms.TextInput(attrs={"class":"form-control"}),
        #     "PinCode":forms.IntegerField()

        # }

# class ComplaintMWaste(forms.ModelForm):
#     class Meta:
#         model=Complaints
#         fields="__all__"
        # widgets={
        #     "Name":forms.TextInput(attrs={"class":"form-control"}),
        #     "Email":forms.EmailInput(attrs={"class":"form-control"}),
        #     "Message":forms.TextInput(attrs={"class":"form-control"}),
            
        # }
        

class SignUpForm(UserCreationForm):

    # first_name=forms.CharField(max_length=100,required=False,help_text='optional')
    # last_name=forms.CharField(max_length=100,required=False,help_text='optional')
    # email=forms.EmailField(max_length=100,help_text='Enter a valid email address')
    class Meta:
        model=User
        fields=['first_name','last_name','username','password1','password2']

class SigninForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control"}))

class PaymentForm(forms.Form):
    card_number = forms.CharField(label='Card Number', max_length=16, required=True)
    expiry_date = forms.CharField(label='Expiry Date', max_length=5, required=True)
    cvv = forms.CharField(label='CVV', max_length=4, required=True)

          

            



            
        
    
    
