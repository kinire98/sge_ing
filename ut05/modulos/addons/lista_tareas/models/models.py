# -*- coding: utf-8 -*- 

from odoo import models, fields, api # type: ignore


class lista_tareas(models.Model):
    _name = 'lista_tareas.lista_tareas'
    _description = 'lista_tareas.lista_tareas'

    name = fields.Char()
    description = fields.Text()
    priority = fields.Integer()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
