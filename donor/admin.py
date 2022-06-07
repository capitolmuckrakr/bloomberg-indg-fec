from django.contrib import admin
from donor.models import *

class DonorAdmin(admin.ModelAdmin):
    search_fields = ['bindg_name']
    ordering = ('bindg_name',)
    list_display = ('bindg_name','contribution_total_2022')

admin.site.register(Donor, DonorAdmin)