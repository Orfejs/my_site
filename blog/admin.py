from django.contrib import admin

from .models import Post
admin.site.register(Post)

from .models import ApiCall
admin.site.register(ApiCall)

from .models import Activity
admin.site.register(Activity)