from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact

class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Jasiel Serra',
            slug='jasiel-serra',
            photo='http://'
        )

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind = Contact.EMAIL,
                                        value = 'jasielserra@gmail.com'
        )

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, kind = Contact.PHONE,
                                        value = '75-99157-8787'
        )

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        '''Contact Kind should be limited to E or P.'''
        contact = Contact(speaker=self.speaker, kind='A', value = 'B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL,
                                         value='jasielserra@gmail.com'
                                         )
        self.assertEqual('jasielserra@gmail.com', str(contact))
