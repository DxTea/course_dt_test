from django.contrib import admin

from app.internal.admin.admin_user import AdminUserAdmin

from app.internal.models.user import User

admin.site.site_title = "Backend course"
admin.site.site_header = "Backend course"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'username', 'phone', 'register_date')
    search_fields = ('username', 'phone')
