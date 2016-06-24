from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribeEmail(TestCase):
    def setUp(self):
        data = dict(name='Jasiel Serra', cpf='12345678901',
                    email='jasiel_serra@hotmail.com', phone='75-99157-8787')

        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        subject = 'Confirmação de Inscrição'

        self.assertEqual(subject, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@mailinator.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@mailinator.com', 'jasiel_serra@hotmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):

        contents = ['Jasiel Serra',
                    '12345678901',
                    'jasiel_serra@hotmail.com',
                    '75-99157-8787']

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

