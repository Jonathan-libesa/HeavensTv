from django.contrib import admin

from .models import*



class DonateAdmin(admin.ModelAdmin):
   list_display=('Name','email','amount','date_created')
   search_fields=['Name','email']
   #prepopulated_fields={'slug':('Title',)}

   
admin.site.register(Donate, DonateAdmin)
admin.site.register(Partner)
