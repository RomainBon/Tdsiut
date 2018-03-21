# -*- coding: utf-8 -*-

from odoo import models, fields


class res_partner(models.Model):
    _inherit = 'res.partner'
    employee_ref = fields.Char(string='reference enployer')
    # device_ids = fields.Many2one('iut.it.device', required=True, ondelete='cascade', index=True, copy=False)
