import pytz
import factory
import factory.fuzzy

from faker import Faker
from faker.providers import profile, address, geo, python, date_time

from django.utils import timezone

from cotidia.team.models import Member
from consult.models import Customer, ServiceType


fake = Faker("en_GB")
fake.add_provider(profile)
fake.add_provider(address)
fake.add_provider(geo)
fake.add_provider(python)
fake.add_provider(date_time)


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "consult.customer"

    title = factory.fuzzy.FuzzyChoice([c[0] for c in Customer.TITLE_CHOICES])
    first_name = factory.Faker("first_name", locale="en_GB")
    last_name = factory.Faker("last_name", locale="en_GB")
    email = factory.Faker("email", locale="en_GB")
    dob = factory.LazyFunction(lambda: fake.profile()["birthdate"])

    address_line_1 = factory.LazyFunction(lambda: fake.street_address())
    address_city = factory.LazyFunction(lambda: fake.city())
    address_postcode = factory.LazyFunction(lambda: fake.postcode())
    address_country = "GB"

    @factory.post_generation
    def post(obj, create, extracted, **kwargs):
        location = fake.local_latlng(country_code="GB")
        obj.lat = float(location[0])
        obj.lng = float(location[1])
        obj.save()


class ServiceTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "consult.servicetype"

    name = factory.LazyFunction(
        lambda: fake.words(nb=1, ext_word_list=None, unique=True)[0].title()
    )


class BookingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "consult.booking"

    datetime = factory.LazyFunction(lambda: timezone.now())

    cost = factory.fuzzy.FuzzyChoice(["20", "50", "80", "150"])
    service_type = factory.LazyFunction(
        lambda: ServiceType.objects.all().order_by("?").first()
    )
    first_visit = factory.LazyFunction(lambda: fake.pybool())
    notes = factory.LazyFunction(
        lambda: fake.text(max_nb_chars=200, ext_word_list=None)
    )
    member = factory.LazyFunction(lambda: Member.objects.all().order_by("?").first())
    customer = factory.LazyFunction(
        lambda: Customer.objects.all().order_by("?").first()
    )

    @factory.post_generation
    def post(obj, create, extracted, **kwargs):
        obj.datetime = fake.date_time_between(
            start_date="-150d", end_date="+150d", tzinfo=pytz.timezone("GMT")
        )
        obj.save()
