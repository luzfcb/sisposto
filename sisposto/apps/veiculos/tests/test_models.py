# -*- coding: utf-8 -*-
import os
from django.test import TestCase


class VeiculoTest(TestCase):
    def test_modulo_existe(self):
        try:
            from apps.veiculos.models import Veiculo
        except ImportError:
            self.fail('Nao existe classe modelo Veiculo')
