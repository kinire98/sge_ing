# -*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api #type: ignore


class subscription(models.Model):
    _name = 'subscription.subscription'
    _description = 'Gestión de las subscripciones'
    _sql_constraints = [
            ('unique_name', 'unique(name)', 'El nombre debe ser único')
            ]

    name = fields.Char( string = 'Nombre', required = True )
    customer_id = fields.Many2one( string = 'Identificador de cliente', comodel_name = 'res.partner', required = True )
    subscription_code = fields.Char( string = 'Código de susbcripción', required = True )
    start_date = fields.Date( string = 'Fecha de comienzo', required = True )
    end_date = fields.Date( string = 'Fecha de finalización' )
    renewal_date = fields.Date( string = 'Fecha de renovación' )
    status = fields.Selection(string='Estado', selection=[
        ('active', 'Activa'),
        ('expired', 'Expirada'),
        ('pending', 'Pendiente'),
        ('cancelled', 'Cancelada'),
        ])
    is_renewable = fields.Boolean(string='Renovable')
    auto_renewal = fields.Boolean(string='Auto renovable')
    price = fields.Float(string='Precio')

    usage_limit = fields.Integer(string='Límite de uso')
    current_usage = fields.Integer(string='Uso actual')
    use_percent = fields.Integer(string='Porcentaje de uso', compute = '_calculate_use_percent', default=0)
    metrics_field = fields.Many2one(comodel_name = 'subscription.metrics')

    @api.depends('usage_limit', 'current_usage')
    def _calculate_use_percent(self):
        for record in self:
            if record.usage_limit != 0:
                record.use_percent = int(record.current_usage / record.usage_limit * 100)
            else:
                record.use_percent = 0 
    def add_15_days(self):
        self.end_date = self.end_date + datetime.timedelta(days = 15);

