# -*- coding: utf-8 -*-
from openerp import models, fields, api


class account_invoice(models.Model):

    _inherit = 'account.invoice'

    prosecution_id = fields.Many2one('legal.prosecution', string='Prosecution')

    @api.onchange('prosecution_id')
    def _on_change_prosecution(self):
        if self.prosecution_id:
            self.reference = ' - '.join(
                [self.prosecution_id.folder_name or '', self.prosecution_id.caratula or ''])
