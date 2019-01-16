from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from cotidia.account import fixtures
from consult.models import Booking
from consult.factory import BookingFactory


class BookingAdminTests(TestCase):

    @fixtures.superuser
    def setUp(self):

        # Create a default object, to use with update, retrieve, list & delete
        self.object = BookingFactory.create()

        # Create the client and login the user
        self.c = Client()
        self.c.login(
            username=self.superuser.username,
            password=self.superuser_pwd)

    def test_add_booking(self):
        """Test that we can add a new object."""

        url = reverse('consult-admin:Booking-add')

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

        # Send data
        data = {
            "id": "<<SETME>>",
            "date": "<<SETME>>",
            "time": "<<SETME>>",
            "cost": "<<SETME>>",
            "service_type": "<<SETME>>",
            "first_visit": "<<SETME>>",
            "notes": "<<SETME>>",
            "member": "<<SETME>>",
            "customer": "<<SETME>>",
        }
        response = self.c.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Get the latest added object
        obj = Booking.objects.filter().latest('id')
        self.assertEqual(obj.id, "<<SETME>>")
        self.assertEqual(obj.date, "<<SETME>>")
        self.assertEqual(obj.time, "<<SETME>>")
        self.assertEqual(obj.cost, "<<SETME>>")
        self.assertEqual(obj.service_type, "<<SETME>>")
        self.assertEqual(obj.first_visit, "<<SETME>>")
        self.assertEqual(obj.notes, "<<SETME>>")
        self.assertEqual(obj.member, "<<SETME>>")
        self.assertEqual(obj.customer, "<<SETME>>")

    def test_update_booking(self):
        """Test that we can update an existing object."""

        url = reverse(
            'consult-admin:booking-update',
            kwargs={
                'pk': self.object.id
            }
        )

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

        # Send data
        data = {
            "id": "<<SETME>>",
            "date": "<<SETME>>",
            "time": "<<SETME>>",
            "cost": "<<SETME>>",
            "service_type": "<<SETME>>",
            "first_visit": "<<SETME>>",
            "notes": "<<SETME>>",
            "member": "<<SETME>>",
            "customer": "<<SETME>>",
        }
        response = self.c.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Get the latest added object
        obj = Booking.objects.get(id=self.object.id)

        self.assertEqual(obj.id, "<<SETME>>")
        self.assertEqual(obj.date, "<<SETME>>")
        self.assertEqual(obj.time, "<<SETME>>")
        self.assertEqual(obj.cost, "<<SETME>>")
        self.assertEqual(obj.service_type, "<<SETME>>")
        self.assertEqual(obj.first_visit, "<<SETME>>")
        self.assertEqual(obj.notes, "<<SETME>>")
        self.assertEqual(obj.member, "<<SETME>>")
        self.assertEqual(obj.customer, "<<SETME>>")

    def test_retrieve_booking(self):
        """Test that we can retrieve an object from its ID."""

        url = reverse(
            'consult-admin:booking-detail',
            kwargs={
                'pk': self.object.id
            }
        )

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_booking(self):
        """Test that we can list objects."""

        url = reverse('consult-admin:booking-list')

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete_booking(self):
        """Test that we can delete an object."""

        url = reverse(
            'consult-admin:booking-delete',
            kwargs={
                'pk': self.object.id
            }
        )

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

        # Action detail with POST call
        response = self.c.post(url)
        self.assertEqual(response.status_code, 302)

        # Test that the record has been deleted
        obj = Booking.objects.filter(id=self.object.id)
        self.assertEqual(obj.count(), 0)
