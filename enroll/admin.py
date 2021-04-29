from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mobileno', 'guests', 'room', 'nightstay', 'indate', 'intime', 'outdate', 'outtime', 'amount', 'paymethod', 'photo', 'agree')