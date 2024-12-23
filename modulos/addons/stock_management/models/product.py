# -*- coding: utf-8 -*-

from odoo import models, fields, api #type: ignore


class Product(models.Model):
    _name = 'stock.product'
    _description = 'stock_management.stock_management'

    name = fields.Char(String = 'nombre')
    category = fields.Selection(
            [
                (),
                (),
                ()
            ],
            string = '',
            default = ''
        )
    price = fields.Many2one(String = 'precio', comodel_name = 'res.currency', currency_field = 'EUR')
    stock = fields.Integer(String = '')
    total_value = fields.Many2one(String = 'Precio total', comodel_name = 'res.currency', currency_field = 'EUR', compute = '_compute_precio_total')


    @api.depends('price', 'stock')
    def _compute_precio_total(self):
        for product in self:
            product.total_value = product.price * product.stock


