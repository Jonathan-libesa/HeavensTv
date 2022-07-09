from django.contrib import admin

from .models import*



class DonateAdmin(admin.ModelAdmin):
   list_display=('Name','email','amount','date_created')
   search_fields=['Name','email']
   #prepopulated_fields={'slug':('Title',)}

class ContributeAdmin(admin.ModelAdmin):
   list_display=('partner','amount','categories','date_created')
   search_fields=['partner','categories']
   
admin.site.register(Donate, DonateAdmin)
admin.site.register(Partner)
admin.site.register(Event)
admin.site.register(New)
admin.site.register(Contribute,ContributeAdmin)
admin.site.register(Category)