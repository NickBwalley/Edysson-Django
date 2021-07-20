from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import *



class UserAdmin(UserAdmin):
	list_display = ('username', 'email', 'date_joined', 'is_admin', 'is_staff', 'is_verified')
	search_fields = ('email', 'username')
	readonly_fields = ('id',  'country', 'date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(user, UserAdmin)
admin.site.register(Country)



