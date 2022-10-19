# -*- coding: utf-8 -*-

{
    'name': 'Eclater la taxe en plusieurs lignes dans les Devis et les Factures',
    'version': '15.0e',
    'author': 'L team & revu par Rabie Sakhri',
    'category': '',
    'sequence': 1,
    'website': '',
    'summary': '',
    'description': """
Dans le cas où l'entreprise utilise plus d'une taxe TVA, ce module affiche les deux taxes dans
le devis et la facture
    """,
    'images': ['static/description/odoo_r_banner.png', ],
    'depends': ['base', 'sale', 'account'],
    'web.assets_backend': [
    
    ],
    'data': [
        'reports/report_menu.xml',
        'reports/sale_order.xml',
        'reports/account_invoice_new.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
