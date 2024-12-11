# -*- coding: utf-8 -*-

from odoo import models, fields, api #type: ignore


class libro(models.Model):
    _name = 'modulo_biblioteca.libro'
    _description = 'Gestion libros'

    nombre = fields.Text()
    autor = fields.Text()
    fecha_nac = fields.Date()
    sinopsis = fields.Text()
    ISBN = fields.Integer()
