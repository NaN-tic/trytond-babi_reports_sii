# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta


class Model(metaclass=PoolMeta):
    __name__ = 'ir.model'

    @classmethod
    def __register__(cls, module_name):
        super(Model, cls).__register__(module_name)
        models = cls.search([('name', 'in', ['account.invoice',
                        'account.invoice.tax', 'aeat.sii.report.lines',
                        'aeat.sii.report.line.tax'])])
        if models:
            cls.write(models, {
                    'babi_enabled': True
                    })
