#!/usr/bin/env python
# This file is part sale_contact module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_depends


class SaleContactTestCase(unittest.TestCase):
    'Test Sale Contact module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('sale_contact')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleContactTestCase))
    return suite
