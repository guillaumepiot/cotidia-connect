from django.core.management import BaseCommand

from consult.models import Booking, Customer, ServiceType
from cotidia.team.models import Department, Member


class Command(BaseCommand):
    help = "Clear all demo test data."

    def handle(self, *args, **options):
        Booking.objects.all().delete()
        Customer.objects.all().delete()
        ServiceType.objects.all().delete()
        Member.objects.all().delete()
        Department.objects.all().delete()
