from accounts.models import UserProfile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class AccountInLine(admin.StackedInline):
	model = UserProfile
	can_delete = False
	verbose_name_plural = 'profile'

class AccountAdmin(admin.ModelAdmin):
	fieldsets = [
			('User',	{'fields':['user']}),
			('DOB',	    {'fields':['birthday']}),
			('Major',	{'fields':['major']}),
			('School',	{'fields':['school']}),
			('Subject', {'fields':['fav_subj']}),
			('Leaves',  {'fields':['leaves']}),
			('Votes',   {'fields':['votes']})
		]

class UserProfileInline(admin.StackedInline):
	model = UserProfile

class UserAdmin(UserAdmin):
	inlines = (UserProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, AccountAdmin)
