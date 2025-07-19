# -*- coding: utf-8 -*-
from . import controllers
from . import models
from odoo.addons.payment import setup_provider, reset_payment_provider


def post_init_hook(cr, registry):
    """Function to set up the payment provider 'CCAvenue' after
    module installation."""
    setup_provider(cr, registry, 'avenue')


def uninstall_hook(cr, registry):
    """Function to reset the payment provider 'CCAvenue' before module
    uninstallation."""
    reset_payment_provider(cr, registry, 'avenue')
