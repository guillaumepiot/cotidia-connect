from django.core.management import BaseCommand

from consult.factory import BookingFactory, CustomerFactory, ServiceTypeFactory
from cotidia.team.factory import DepartmentFactory, MemberFactory


class Command(BaseCommand):
    help = "Clear all demo test data."

    def handle(self, *args, **options):
        DepartmentFactory.create_batch(3)
        MemberFactory.create_batch(10)
        ServiceTypeFactory.create_batch(5)
        CustomerFactory.create_batch(250)
        BookingFactory.create_batch(500)
