from django.contrib import admin

from .models import Location, Stand, Hotel, Feedback, Contacts


admin.site.register(Location)
admin.site.register(Stand)
admin.site.register(Hotel)
admin.site.register(Feedback)
admin.site.register(Contacts)