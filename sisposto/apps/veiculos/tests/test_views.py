# -*- coding: utf-8 -*-
import splinter

from django.core.urlresolvers import reverse_lazy
from django import test
from apps.users.models import User


class VeiculoTest(test.TestCase):
    def setUp(self):
        """
        Initializes the test client and logs it in.
        """
        self.password = "admin"
        self.user = User.objects.create_superuser(username='admin', email='admin@admin.com', password=self.password)
        self.logged_in = self.client.login(username=self.user.username, password=self.password)

    def test_view_create_existe(self):
        view_url = reverse_lazy('veiculo_add')
        print(view_url)
        response = self.client.get(view_url)
        self.assertEqual(response.status_code, 200)

    def test_view_list_existe(self):
        view_url = reverse_lazy('veiculo_list')
        print(view_url)
        response = self.client.get(view_url)
        self.assertEqual(response.status_code, 200)


# class VeiculoTestCase(test.LiveServerTestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.browser = splinter.Browser("firefox")
#         super(VeiculoTestCase, cls).setUpClass()
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.browser.quit()
#         super(VeiculoTestCase, cls).tearDownClass()
#
#     def test_preenche_formulario_e_envia_email(self):
#         self.browser.visit("%s/contato" % self.live_server_url)
#         self.browser.fill("nome", "Francisco Souza")
#         self.browser.fill("email", "fss@corp.globo.com")
#         self.browser.fill("mensagem", "Gostei do notebook azul")
#         self.browser.find_by_css("button").click()
#         email = mail.outbox[0]
#         self.assertEqual(u"Contato pelo site", email.subject)
#         self.assertEqual(u"Gostei do notebook azul", email.body)
#         self.assertEqual(u"fss@corp.globo.com", email.from_email)
#         self.assertEqual([settings.EMAIL_ADMIN], email.to)