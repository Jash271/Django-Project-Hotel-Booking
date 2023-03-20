from django.test import TestCase
from .models import rooms
# Create your tests here.
class RoomTestCase(TestCase):
	@classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        rooms.objects.create(Roomtypecode='520', Roomcode='520')
	def test_rooms(self):
		roomtypecode=Roomtypecode.get(id=1)
		field_label=roomtypecode._meta.get_field('roomtypecode').verbose_name
		self.assertEqual(field_label,'roomtypecode')