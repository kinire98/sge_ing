# models/models.py
```python
# -*- coding: utf-8 -*-

from odoo import models, fields, api # type: ignore


class salas(models.Model):
    _name = 'gestion_salas.salas'
    _description = 'Modelo para las salas'

    nombre = fields.Text()
    capacidad = fields.Integer()
    fecha_reserva = fields.Datetime(string="Fecha de reserva")
    reservada = fields.Boolean("Reservada")
    comentarios = fields.Text()
```