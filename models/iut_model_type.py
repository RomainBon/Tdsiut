# -*- coding: utf-8 -*-

from odoo import models, fields, api


class iut_model_tpye(models.Model):
    _name = 'iut.model.type'
    name = fields.Char(string='nom')
    # model_ids = fields.Many2many()