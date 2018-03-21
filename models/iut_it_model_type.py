# -*- coding: utf-8 -*-

from odoo import models, fields


class iut_it_model_type(models.Model):
    _name = 'iut.it.model.type'
    name = fields.Char(string='nom')
