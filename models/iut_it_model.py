# -*- coding: utf-8 -*-

from odoo import models, fields


class iut_it_model(models.Model):
    _name = 'iut.it.model'

    name = fields.Char(string='nom')
    ref = fields.Char(string='reference')
    type_ids = fields.Char(string='type')
