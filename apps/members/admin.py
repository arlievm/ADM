from django.contrib import admin

from .models import Members, Sponsor, AttributeSponsors


admin.site.register(Members)
admin.site.register(Sponsor)
admin.site.register(AttributeSponsors)