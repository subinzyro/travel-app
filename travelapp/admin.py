from django.contrib import admin
from travelapp.models import Travel_book,Travel_reg
# Register your models here.


class TravelAdmin(admin.ModelAdmin):
    list_display=("username","email")
admin.site.register(Travel_reg)

class TravelAdmin(admin.ModelAdmin):
    list_display=("username","phone","destination",)
admin.site.register(Travel_book)