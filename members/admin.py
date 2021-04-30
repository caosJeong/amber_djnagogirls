from django.contrib import admin

# Register your models here.
from members.models import Member, Legs


@admin.register(Legs)
class LegsAdmin(admin.ModelAdmin):
    list_display = ['legs_type', 'legs_sub1_type', 'legs_sub2_type']


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'member_name']
