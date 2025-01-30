# -*- coding: utf-8 -*-
from odoo import models, fields, api #type: ignore


class metrics(models.Model):
    _name = 'subscription.metrics'
    _description = 'Metricas para las subscripciones'

    date = fields.Date()
    active_subscriptions = fields.Integer()
    revenue_generated = fields.Float()
    renewal_fee = fields.Float(compute = '_calculate_renewal_fee') 
    cancelation_fee = fields.Float(compute = '_caculate_cancelation_fee') 
    renewals = fields.Integer()
    new_subscriptions = fields.Integer()
    canceled = fields.Integer()
    new_clients = fields.Integer()
    recurrent_clients = fields.Integer()
    average_revenue_by_user = fields.Float(compute = '_caculate_average_revenue_by_user') 
    conversion_fee = fields.Float()
    churn_rate = fields.Float()
    lifetime_value = fields.Float()
    client_adquisition_cost = fields.Float()
    notes = fields.Text()
    relation_with_model = fields.One2many(
            comodel_name = 'subscription.subscription',
            inverse_name = 'metrics_field'
            )
    
    @api.depends('renewal_fee', 'renewals', 'active_subscriptions')
    def _calculate_renewal_fee(self):
        for record in self:
            if record.active_subscriptions == 0:
                record.renewal_fee = 0
                continue
            record.renewal_fee = (record.renewals / record.active_subscriptions) * 100

    @api.depends('cancelation_fee', 'active_subscriptions', 'canceled')
    def _caculate_cancelation_fee(self):
        for record in self:
            if record.active_subscriptions == 0:
                record.cancelation_fee = 0
                continue
            record.cancelation_fee = (record.canceled / record.active_subscriptions) * 100

    @api.depends('average_revenue_by_user', 'revenue_generated', 'active_subscriptions')
    def _caculate_average_revenue_by_user(self):
        for record in self:
            if record.active_subscriptions == 0:
                record.average_revenue_by_user = 0
                continue
            record.average_revenue_by_user = (record.revenue_generated / record.active_subscriptions)
