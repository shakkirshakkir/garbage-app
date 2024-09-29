from django.urls import path
from .views import *
from.import views
urlpatterns=[

path('bio/',BioWasteView.as_view(),name="biow"),
path('nbioo/',NonBioWasteView.as_view(),name="nbiow"),
path('haz/',HWasteView.as_view(),name="hw"),
path('home/',HomeMWasteView.as_view(),name="home"),
# path('com/',ComplaintView.as_view(),name="co"),
path('payment/',PaymentView.as_view(),name="payment"),

# path('registration1',views.signup,name='registration1'),
# path('registration1_post',views.signup_post,name='registration1_post'),
path('sig/',SignUpView.as_view(),name="si"),
path('co',views.Complaint,name="com"),
path('ma/',MainHome.as_view(),name="mh"),
# path('si',views.signup_post,name="sig"),
# path('ind/',views.index,name="inde"),
# ignup',views.signup_post,name='signup'),
# path('login',views.login,name='login'),
# path('login_pos',views.login_post,name='sin'),
path('sigi/',SigninView.as_view(),name="sin"),
path('logo/',LgOut.as_view(),name="lo"),
path('payment-details/',payment_details, name='payment_details'),
path('payment/',payment, name='paymentt'),







]
