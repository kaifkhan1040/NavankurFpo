from django.contrib import admin
from .models import FPO,State,District,City,Farmer,Cbbo,Ia,FpoCeoEducation,Bank
# Register your models here.
admin.site.register(Farmer),
admin.site.register(FPO),
admin.site.register(State),
admin.site.register(District),
admin.site.register(City),
admin.site.register(Cbbo),
admin.site.register(Ia),
admin.site.register(FpoCeoEducation),
admin.site.register(Bank),