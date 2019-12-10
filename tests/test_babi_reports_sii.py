# This file is part babi_reports_sii module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest


from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class BabiReportsSiiTestCase(ModuleTestCase):
    'Test Babi Reports Sii module'
    module = 'babi_reports_sii'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            BabiReportsSiiTestCase))
    return suite
