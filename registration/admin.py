from django.contrib import admin

from .models import User, Family, Result
# ...
admin.site.register(User)
admin.site.register(Family)
admin.site.register(Result)
