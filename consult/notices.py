from django.conf import settings

from cotidia.mail.notice import Notice


class BookingReminderNotice(Notice):
    name = "Booking reminder"
    identifier = "booking-reminder"
    html_template = "admin/consult/email/reminder.html"
    text_template = "admin/consult/email/reminder.txt"

    default_context = {"SITE_URL": settings.SITE_URL}

    subject = "Your booking is in 3 days, get ready!"

    # context_editable = [
    #     {
    #         "fieldset": "Customer",
    #         "fields": [{"name": "email", "type": "charfield", "required": True}],
    #     }
    # ]

    def get_subject(self):
        return "Your booking is in 3 days, get ready!"
