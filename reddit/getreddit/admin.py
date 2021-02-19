from django.contrib import admin
from .models import GetReddit_Subreddit
from .models import GetReddit_UserInformation

# Register your models here.
admin.site.register(GetReddit_Subreddit)
admin.site.register(GetReddit_UserInformation)


