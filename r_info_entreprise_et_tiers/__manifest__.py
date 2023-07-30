# -*- coding: utf-8 -*-

{
    'name': 'RC, NIF, NIS & AI des Tiers/Entreprise',
    'version': '1.0.0.1',
    'summary': """Ajouter le RC, NIF, NIS & AI dans les formes des tiers/Entreprise""",
    'description': """Ajouter le RC, NIF, NIS & AI dans les formes des tiers/Entreprise""",
    'category': 'Base',
    'author': 'Tech Wise Advisors',
    'website': "",
    'license': 'AGPL-3',
    'price': 0.0,
    'currency': 'USD',

    'depends': ['base'],

    'data': [
        'views/res_partner.xml',
        'views/res_company.xml',

    ],
    'demo': [

    ],
    'images': ['static/description/odoo_r_banner.png'],
    'qweb': [],

    'installable': True,
    'auto_install': False,
    'application': False,
}
