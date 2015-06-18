# -*- coding: utf-8 -*-
from openerp import models, fields, api


class legal_regulation(models.Model):

    """"""

    _name = 'legal.regulation'

    part_contact_ids = fields.Many2many(
        'res.partner', compute='get_contact', string='Contacts')
    date_regulation = fields.Date(string="Date of the regulation")
    beneficiary_id = fields.Many2one('res.partner', string='Beneficiary')
    forced_id = fields.Many2one('res.partner', string='Forced')
    concept = fields.Char(string='Concept')
    date_order = fields.Date(string="Date of the order")
    date_maturity = fields.Date(string="Date of the maturity")
    date_fulfillment = fields.Date(string="Date of the fulfillment")
    amount_regulation = fields.Float(string="Amount of regulation")
    observations = fields.Char(string='Observations')
    procese_id = fields.Many2one('legal.procese', string='Procese')

    @api.one
    @api.depends('procese_id', 'procese_id.part_ids')
    def get_contact(self):
        self.part_contact_ids = self.procese_id.part_ids.mapped('contact_id')
