# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PaymentProvider(models.Model):
    """    Inherit Payment Provider to add new payment into the Payment Provider
     page."""
    _inherit = 'payment.provider'

    code = fields.Selection(selection_add=[('avenue', 'avenue')],
                            ondelete={'avenue': 'set default'},
                            help="The technical code of this payment provider",
                            string="code")
    merchant_key = fields.Char(string='Merchant ID', groups='base.group_user',
                               help="CCAvenue Merchant id of the user")
    access_code = fields.Char(string='Access Code',
                              required_if_provider='avenue',
                              groups='base.group_user',
                              help="CCAvenue Access Code")
    working_key = fields.Char(string='Working Key',
                              required_if_provider='avenue',
                              groups='base.group_user',
                              help="CCAvenue Working key")

    @api.model
    def _get_payment_method_information(self):
        """Override to add CCAvenue payment method information to the
        existing methods.
        """
        res = super()._get_payment_method_information()
        res['avenue'] = {'mode': 'unique', 'domain': [('type', '=', 'bank')]}
        return res
