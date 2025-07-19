# -*- coding: utf-8 -*-
{
    'name': 'CCAvenue Payment Acquirer',
    'version': '18.0.0.0.0',
    'category': 'eCommerce,Marketing',
    'summary': 'CCAvenue Payment Gateway For Website',
    'description': "This module enables seamless payments through CCAvenue, "
                   "ensuring secure and convenient online transactions.",
    'author': "Zahras Group",
    'company': 'Zahras Group',
    'maintainer': 'Zahras Group',
    'website': "https://www.zahras.ae",
    'depends': ['payment', 'account', 'website_sale'],
    'data': [
        'views/payment_provider_views.xml',
        'views/cc_avenue_templates.xml',
        'data/payment_provider_data.xml',
    ],
    'external_dependencies': {'python': ['pay_ccavenue']},
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
