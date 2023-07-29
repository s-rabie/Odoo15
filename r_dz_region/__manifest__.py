# -*- coding: utf-8 -*-

{
    'name': """Algérie - 58 Wilayas | Algerian regions""",
    'version': '1.0.0.1',
    'summary': """Les 58 wilayas et leurs communes""",
    'description': """Les wilayas et les communes""",
    'category': 'Base',
    'author': 'Tech Wise Advisors',
    'website': '',
    'license': 'AGPL-3',
    'price': 5.0,
    'currency': 'USD',

    'depends': ['base', 'contacts'],
    'data': ['security/ir.model.access.csv', 'data/wilayas_data.xml', 'data/commune_data.xml',
             'views/res_commune.xml'
             ],
    'demo': [
    ],
    'images': ['static/description/odoo_r_banner.png'],

    'installable': True,
    'application': True,
    'auto_install': False,
}
