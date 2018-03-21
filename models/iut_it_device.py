# -*- coding: utf-8 -*-

from odoo import models, fields


class iut_it_device(models.Model):
    _name = 'iut.it.device'
    name = fields.Char(string='nom')
    date_allocation = fields.Date(string='Date allocation')
    serial_number = fields.Char(string='numeros serie')
    date_purchase = fields.Date(string='date achat')
    date_warranty = fields.Date(string='date garantie')
