from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from cotidia.account import fixtures
from consult.models import ServiceType
from consult.factory import ServiceTypeFactory


class ServiceTypeAdminTests(TestCase):

    @fixtures.superuser
    def setUp(self):

        # Create a default object, to use with update, retrieve, list & delete
        self.object = ServiceTypeFactory.create()

        # Create the client and login the user
        self.c = Client()
        self.c.login(
            username=self.superuser.username,
            password=self.superuser_pwd)

    def test_add_servicetype(self):
        """Test that we can add a new object."""

        url = reverse('consult-admin:ServiceType-add')

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

        # Send data
        data = {
            "id": "<<SETME>>",
            "name": "<<SETME>>",
        }
        response = self.c.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Get the latest added object
        obj = ServiceType.objects.filter().latest('id')
        self.assertEqual(obj.id, "<<SETME>>")
        self.assertEqual(obj.name, "<<SETME>>")

    def test_update_servicetype(self):
        """Test that we can update an existing object."""

        url = reverse(
            'consult-admin:servicetype-update',
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
            "name": "<<SETME>>",
        }
        response = self.c.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Get the latest added object
        obj = ServiceType.objects.get(id=self.object.id)

        self.assertEqual(obj.id, "<<SETME>>")
        self.assertEqual(obj.name, "<<SETME>>")

    def test_retrieve_servicetype(self):
        """Test that we can retrieve an object from its ID."""

        url = reverse(
            'consult-admin:servicetype-detail',
            kwargs={
                'pk': self.object.id
            }
        )

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_servicetype(self):
        """Test that we can list objects."""

        url = reverse('consult-admin:servicetype-list')

        # Test that the page load first
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete_servicetype(self):
        """Test that we can delete an object."""

        url = reverse(
            'consult-admin:servicetype-delete',
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
        obj = ServiceType.objects.filter(id=self.object.id)
        self.assertEqual(obj.count(), 0)
