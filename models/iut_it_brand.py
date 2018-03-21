# -*- coding: utf-8 -*-

from odoo import models, fields


class iut_it_brand (models.Model):
    _name = 'iut.it.brand'
    name = fields.Char(string='nom')
    warranty_delay_month = fields.Integer(string='delais garantie')
    support_phone = fields.Char(string='telephone support')
