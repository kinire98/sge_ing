# -*- coding: utf-8 -*-

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
    duration_months = fields.Integer( string = 'Duración en meses',  compute = '_calculate_duration_in_months')
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
    use_percent = fields.Float(string='Porcentaje de uso', compute = '_calculate_use_percent')

    @api.depends('start_date', 'end_date')
    def _calculate_duration_in_months(self):
        for record in self:
            if record.start_date and record.end_date: 
                record.duration_months = fields.Date.delta(record.start_date, record.end_date) / 30

    @api.depends('usage_limit', 'current_usage')
    def _calculate_use_percent(self):
        for record in self:
            if record.usage_limit != 0 and record.current_usage != 0:
                record.use_percent = float(record.current_usage / record.usage_limit) * 100

