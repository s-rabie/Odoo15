# -*- coding: utf-8 -*-
from odoo import api, fields, models

#Afficher le montant en lettre dans le bon de commande achat
class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    def _compute_amount2words(self):
        for rec in self:
                rec.amount_words = str(rec.currency_id.amount_to_text(rec.amount_total))

    amount_words = fields.Char(string="Total en lettre : ", help=
        "Le montant total en lettres est généré automatiquement par le système", compute='_compute_amount2words')
