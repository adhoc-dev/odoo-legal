# -*- coding: utf-8 -*-
from openerp import models, fields
from datetime import date


class legal_news(models.Model):

    """"""

    _name = 'legal.news'
    _rec_name = 'description'

    description = fields.Char(string='Description')
    date = fields.Date(string='Date', default=date.today())
    type_id = fields.Many2one('legal.news.type', string='Type')
    prosecution_id = fields.Many2one('legal.prosecution', string='prosecution')


class legal_news_type(models.Model):

    """"""

    _name = 'legal.news.type'

    name = fields.Char(String="Name")
