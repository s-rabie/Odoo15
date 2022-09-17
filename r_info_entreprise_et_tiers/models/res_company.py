# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    fax_number = fields.Char(string="Fax")

    n_rc = fields.Char(string="Numéro RC")
    nif = fields.Char(string="NIF")
    nis = fields.Char(string="NIS")
    ai = fields.Char(string="Article d''imposition")

