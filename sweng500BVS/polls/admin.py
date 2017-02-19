from django.contrib import admin

# Register your models here.

from .models import Ballot, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class BallotAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['ballot_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Ballot, BallotAdmin)