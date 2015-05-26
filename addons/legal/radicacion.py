# -*- coding: utf-8 -*-
from openerp import models, fields


class legal_radication(models.Model):

    """"""

    _name = 'legal.radication'

    d_formed = fields.Char(string='D.formed')
    legal_office_id = fields.Many2one('legal.office', string='Legal Office')
    instance = fields.Selection(
        [('first', 'First'), ('second', 'Second'),
         ('third', 'Third'), ('filed', 'Filed')], string='Instance')
    num_1_ins = fields.Char(string='Num. 1°Ins')
    num_2_ins = fields.Char(string='Num. 2°Ins')
    num_3_ins = fields.Char(string='Num. 3°Ins')
    num_filed = fields.Char(string='Num. Filed')
    date = fields.Date(string='Date')
    procese_id = fields.Many2one('legal.procese', string='Procese')
