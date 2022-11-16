from django.contrib import admin
from .models import AfternoonTea
from django_summernote.admin import SummernoteModelAdmin


@admin.register(AfternoonTea)
class AfternoonTeaAdmin(SummernoteModelAdmin):

    readonly_fields = ('booking_number', 'full_name', 'email',
                       'phone_number', 'date', 'time', 'notes',
                       'no_of_people')

    fields = ('booking_number', 'full_name', 'email',
              'phone_number', 'date', 'time', 'notes',
              'no_of_people',)

    list_display = ('booking_number', 'date', 'full_name', 'under_review',
                    'no_of_people')

    ordering = ('-date',)

    actions = ["approve_booking"]

    def approve_booking(self, request, queryset):
        queryset.update(under_review=False)

