from django.contrib import admin
from .models import BioModel,NonBioModel,HazModel,HomeModel,Complaints

# Register your models here.
admin.site.register(BioModel)
admin.site.register(NonBioModel)
admin.site.register(HazModel)
admin.site.register(HomeModel)
admin.site.register(Complaints)


