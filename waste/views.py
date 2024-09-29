from django.shortcuts import render,redirect

from django.views.generic import View,CreateView
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.conf import settings



# Create your views here.
# def indexx(request):
#     return render(request,"navbar.html")

def Complaint(request):
    if request.method=='POST':
        name=request.POST["Name"]
        email=request.POST["Email"]
        message=request.POST["Message"]
        query=Complaints(name=name,email=email,message=message)
        query.save()

        # return render(request,"navbar.html")
        return redirect("mh")


class MainHome(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")

class HomeMWasteView(View):

    def get(self,request,*args,**kwargs):
        f=HomeMWaste()
        return render(request,"home.html",{"form":f})
    def post(self,request,*args,**kwargs):
        form_data=HomeMWaste(data=request.POST)
        if form_data.is_valid():
            form_data.save()

class BioWasteView(View):

    def get(self,request,*args,**kwargs):
        f=BioMWaste()
        return render(request,"bio.html",{"form":f})
    def post(self,request,*args,**kwargs):
        form_data=BioMWaste(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect("hm")
            
class NonBioWasteView(View):

    def get(self,request,*args,**kwargs):
        f=NBioMWaste()
        return render(request,"nonbio.html",{"form":f})
    def post(self,request,*args,**kwargs):
        form_data=NBioMWaste(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect("hm")

class HWasteView(View):

    def get(self,request,*args,**kwargs):
        f=HazMWaste()
        return render(request,"hazardous.html",{"form":f})
    def post(self,request,*args,**kwargs):
        form_data=HazMWaste(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect("payment")

class HomeMWasteView(View):

    def get(self,request,*args,**kwargs):
        f=HomeMWaste()
        return render(request,"home.html",{"form":f})
    def post(self,request,*args,**kwargs):
        form_data=HomeMWaste(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect("payment")

# class ComplaintView(View):

#     def get(self,request,*args,**kwargs):
#         f=ComplaintMWaste()
#         return render(request,"navbar.html",{"form":f})
    
            
            
#     def post(self,request,*args,**kwargs):
#         form_data=ComplaintMWaste(data=request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             return redirect("mh")
# class ComplaintView(CreateView):
#     form_class=ComplaintMWaste
#     model=Complaints
#     template_name="navbar.html"
#     success_url=reverse_lazy("sin")
            


# class PaymentView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'payment_details.html', {'payment_success': False})

#     def post(self, request, *args, **kwargs):
        
#         return render(request, 'payment_details.html', {'payment_success': True})

class SignUpView(View):

    def get(self,request,*args,**kwargs):
        f=SignUpForm()
        return render(request,"reg.html",{"form":f})
    def post(self,request,*args,**kwargs):
        form_data=SignUpForm(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            # messages.success(request,"User registered sucessfully")
            
            return redirect("sin")
                      
        else:
            return render(request,"reg.html",{"f":form_data})

# def signup(request):
#     return render(request,'signup.html')

# def signup_post(request):
#     if request.method=='POST':
        # fullname=request.POST["fname"]
    #     username=request.POST["username"]
    #     email=request.POST["email"]
    #     password=request.POST["password"]
    #     repassword=request.POST["repassword"]
    #     if password!=repassword:
    #         return render(request,'reg.html',{"key":"password not match"})
    #     x=logins(username=username,password=password)
    #     x.save()
    #     user.objects.create(LOGIN=x,fullname=fullname,email=email)
    #     return render(request,'log.html')
    # else:
    #     return render(request,'reg.html')

# def login_post(request):
    # if request.method=='POST':


    #     username=request.POST["username"]
    #     password=request.POST["password"]
    # res=authenticate(request,username=username,password=password)
    #     res=logins.objects.filter(username=username,password=pasword)
    #     print(res)
    #     if res.exists():
    #         res1=logins.objects.get(username=username)
    #         return render(request,'navbar.html',{'data':res1})
    #     else:
    #         return render(request,'log.html')
    # else:
    #     return render(request,'log.html')


    # if res is not None:
    #     auth.login(request,res)
    #     return render(request,'navbar.html')
    # else:
    #     return render(request,'log.html')


class SigninView(View):
    def get(self,request,*args,**kwrgs):
        form_data=SigninForm()
        return render(request,"log.html",{"form":form_data})

    
    def post(self,request,*args,**kwrgs):
        form_data=SigninForm(request.POST)
        if form_data.is_valid():
            un=form_data.cleaned_data.get("username")
            pw=form_data.cleaned_data.get("password")
            user=authenticate(request,username=un,password=pw)
            if user:
                login(request,user)
                f=User.objects.get(username=un)
                return render(request,"navbar.html",{"data":f})
                # return redirect("mh")
            else:
                return redirect("sin")
        else:
            return render(request,"log.html",{"form":form_data})

# class SignUpView(CreateView):
#     form_class=SignUpForm
#     model=User
#     template_name="reg.html"
#     success_url=reverse_lazy("sin")


class LgOut(View):
    def get(self,request):
        logout(request)
        return redirect("sin")

class PaymentView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"payment.html")
    def post(self,request,*args,**kwargs):
        return redirect("payment")


def payment_details(request):
    return render(request, 'payment_details.html')

def post(self,request,*args,**kwargs):
        return redirect("payment")

# stripe.api_key = settings.STRIPE_SECRET_KEY

def payment(request):
    if request.method == 'POST':
        # Create a payment intent using Stripe API
        amount = 1000  # Example amount in cents (e.g., $10.00)
        try:
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='usd',
                payment_method=request.POST['payment_method_id'],
                confirm=True,
            )
            return render(request, 'payment_success.html')
        except stripe.error.CardError as e:
            error_message = e.error.message
            return render(request, 'payment_failure.html', {'error_message': error_message})

    # Render payment form for GET requests
    payment_forms = PaymentForm()
    return render(request, 'payment_form.html', {'payment_form': payment_form})



