# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_print_new(self):
        return self.env.ref('r_print_taxes_separated.action_report_saleorder_new').report_action(self)
