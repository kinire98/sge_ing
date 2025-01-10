# -*- coding: utf-8 -*-

from odoo import models, fields, api # type: ignore

class cpus(models.Model):
    _name = 'cpu_management.cpus'
    _description = 'cpu_management.cpus'

    name = fields.Char()
    manufacturer = fields.Char()
    total_cores = fields.Integer()
    p_cores = fields.Integer()
    e_cores = fields.Integer()
    base_frecuency = fields.Float()
    max_frecuency = fields.Float(string='')
    
