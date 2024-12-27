# -*- coding: utf-8 -*-

from odoo import models, fields, api #type: ignore
from odoo.exceptions import ValidationError #type: ignore


class Product(models.Model):
    _name = 'stock.product'
    _description = 'stock_management.stock_management'
    _sql_constraints = [
            ('unique_name', 'unique(name)', 'El nombre no se puede repetir'),
            ('unique_full_name', 'unique(name, category)', 'El nombre completo no se puede repetir'),
            ('positive_stock', 'CHECK(stock >= 0)', 'La cantidad en stock no puede ser una cantidad negativa'),
            ('min_name_size', 'CHECK(LENGTH(name) >= 3)', 'El nombre tiene que tener tres o más caracteres')
            ]

    name = fields.Char(String = 'Nombre')
    category = fields.Selection(
            [
                ('Microprocesarores', 'Microprocesarores'),
                ('Placas base', 'Placas base'),
                ('Memoria RAM', 'Memoria RAM')
            ],
            string = 'Categoría',
            default = 'Microprocesarores'
        )
    price = fields.Many2one(String = 'Precio', comodel_name = 'res.currency', currency_field = 'EUR')
    stock = fields.Integer(String = 'Cantidad')
    total_value = fields.Many2one(String = 'Precio total', comodel_name = 'res.currency', currency_field = 'EUR', compute = '_compute_total_value')
    full_name = fields.Char(String = 'Nombre completo', compute = '_compute_full_name') 


    @api.depends('price', 'stock')
    def _compute_total_value(self):
        for product in self:
            product.total_value = product.price * product.stock

    @api.depends('name', 'category')
    def _compute_full_name(self):
        for product in self:
            product.full_name = product.name + ' (' + product.category + ')'

    @api.constrains('price')
    def _check_price(self):
        for record in self:
            if record.price <= 0:
                raise ValidationError('El precio debe ser mayor que 0')

    @api.constrains('stock')
    def _check_stock(self):
        for record in self:
            if record.price < 0:
                raise ValidationError('El stock debe ser mayor o igual que 0')

    @api.constrains('total_value')
    def _check_total_value(self):
        for record in self:
            if record.total_value > 100000:
                raise ValidationError('El precio total no puede superar 100000€')

    @api.constrains('category')
    def _check_category(self):
        for record in self:
            if record.category == "":
                raise ValidationError('El campo categoría no puede estar vacío')
                


