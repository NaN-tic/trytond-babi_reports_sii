# This file is part babi_reports_sii module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import model


def register():
    Pool.register(
        model.Model,
        module='babi_reports_sii', type_='model')
