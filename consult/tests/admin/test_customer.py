from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from cotidia.account import fixtures
from consult.models import Customer
from consult.factory import CustomerFactory


class CustomerAdminTests(TestCase):

    @fixtures.superuser
    def setUp(self):

        # Create a default object, to use with update, retrieve, list & delete
        self.object = CustomerFactory.create()

        # Create the client and login the user
        self.c = Client()
        self.c.login(
            username=self.superuser.username,
            password=self.superuser_pwd)

    def test_add_customer(self):
        """Test that we can add a new object."""

        url = reverse('consult-admin:Customer-add')

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

        # Send data
        data = {
            "id": "<<SETME>>",
            "address_line_1": "<<SETME>>",
            "address_line_2": "<<SETME>>",
            "address_line_3": "<<SETME>>",
            "address_city": "<<SETME>>",
            "address_state": "<<SETME>>",
            "address_postcode": "<<SETME>>",
            "address_country": "<<SETME>>",
            "lat": "<<SETME>>",
            "lng": "<<SETME>>",
            "point": "<<SETME>>",
            "title": "<<SETME>>",
            "first_name": "<<SETME>>",
            "last_name": "<<SETME>>",
            "dob": "<<SETME>>",
            "user": "<<SETME>>",
        }
        response = self.c.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Get the latest added object
        obj = Customer.objects.filter().latest('id')
        self.assertEqual(obj.id, "<<SETME>>")
        self.assertEqual(obj.address_line_1, "<<SETME>>")
        self.assertEqual(obj.address_line_2, "<<SETME>>")
        self.assertEqual(obj.address_line_3, "<<SETME>>")
        self.assertEqual(obj.address_city, "<<SETME>>")
        self.assertEqual(obj.address_state, "<<SETME>>")
        self.assertEqual(obj.address_postcode, "<<SETME>>")
        self.assertEqual(obj.address_country, "<<SETME>>")
        self.assertEqual(obj.lat, "<<SETME>>")
        self.assertEqual(obj.lng, "<<SETME>>")
        self.assertEqual(obj.point, "<<SETME>>")
        self.assertEqual(obj.title, "<<SETME>>")
        self.assertEqual(obj.first_name, "<<SETME>>")
        self.assertEqual(obj.last_name, "<<SETME>>")
        self.assertEqual(obj.dob, "<<SETME>>")
        self.assertEqual(obj.user, "<<SETME>>")

    def test_update_customer(self):
        """Test that we can update an existing object."""

        url = reverse(
            'consult-admin:customer-update',
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
            "address_line_1": "<<SETME>>",
            "address_line_2": "<<SETME>>",
            "address_line_3": "<<SETME>>",
            "address_city": "<<SETME>>",
            "address_state": "<<SETME>>",
            "address_postcode": "<<SETME>>",
            "address_country": "<<SETME>>",
            "lat": "<<SETME>>",
            "lng": "<<SETME>>",
            "point": "<<SETME>>",
            "title": "<<SETME>>",
            "first_name": "<<SETME>>",
            "last_name": "<<SETME>>",
            "dob": "<<SETME>>",
            "user": "<<SETME>>",
        }
        response = self.c.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Get the latest added object
        obj = Customer.objects.get(id=self.object.id)

        self.assertEqual(obj.id, "<<SETME>>")
        self.assertEqual(obj.address_line_1, "<<SETME>>")
        self.assertEqual(obj.address_line_2, "<<SETME>>")
        self.assertEqual(obj.address_line_3, "<<SETME>>")
        self.assertEqual(obj.address_city, "<<SETME>>")
        self.assertEqual(obj.address_state, "<<SETME>>")
        self.assertEqual(obj.address_postcode, "<<SETME>>")
        self.assertEqual(obj.address_country, "<<SETME>>")
        self.assertEqual(obj.lat, "<<SETME>>")
        self.assertEqual(obj.lng, "<<SETME>>")
        self.assertEqual(obj.point, "<<SETME>>")
        self.assertEqual(obj.title, "<<SETME>>")
        self.assertEqual(obj.first_name, "<<SETME>>")
        self.assertEqual(obj.last_name, "<<SETME>>")
        self.assertEqual(obj.dob, "<<SETME>>")
        self.assertEqual(obj.user, "<<SETME>>")

    def test_retrieve_customer(self):
        """Test that we can retrieve an object from its ID."""

        url = reverse(
            'consult-admin:customer-detail',
            kwargs={
                'pk': self.object.id
            }
        )

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_customer(self):
        """Test that we can list objects."""

        url = reverse('consult-admin:customer-list')

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete_customer(self):
        """Test that we can delete an object."""

        url = reverse(
            'consult-admin:customer-delete',
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
        obj = Customer.objects.filter(id=self.object.id)
        self.assertEqual(obj.count(), 0)
