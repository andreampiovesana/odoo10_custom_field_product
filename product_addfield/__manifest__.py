# -*- coding: utf-8 -*-
{
    'name': "product_addfield",

    'summary': """
        Modulo per aggiungere campi personalizzati a product""",

    'description': """
        Modulo per aggiungere campi personalizzati a product.
        Dovrebbe gestire:
	    - un campo libero
	    - un campo onetomany verso la tabella contatti 
    """,

    'author': "Marcelo Frare",
    'website': "http://www.informaticapplications.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Others',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/add_field_product_view.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
}
