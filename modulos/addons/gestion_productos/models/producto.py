# -*- coding: utf-8 -*-
from odoo import models, fields, api # type: ignore


class producto(models.Model):
    _name = 'gestion_productos.producto'
    _description = 'Producto'

    name = fields.Char( string='Nombre',
                            help='Introduce el nombre del producto' )
    description = fields.Char( string='Descripción',
                                    help='Introduce una breve descripción del producto' )
    code = fields.Char( string='Código del producto',
                            required=True,
                            help='Introduce el código de prodcto para que sirva de identificador único')
    image = fields.Image( string='Imagen de producto',
                            help='Introduce una imagen de producto' )
    category = fields.Selection(
            [
                ('electrónica', 'Electrónica'),
                ('ropa', 'Ropa'),
                ('alimentación', 'Alimentación')
            ],
            string='Categoría',
            required=True,
            default='electrónica',
            help='Selecciona una categoría de la lista'
        )
    destacable = fields.Boolean( string='Producto destacable',
                                help='¿Se puede destacar el producto?' )
    price = fields.Float( digits = (10, 3),
                                string='Precio',
                                help='Introduce el precio del producto' )
    stock = fields.Integer( string='Cantidad',
                                help='Introduce la cantidad de producto que hay en stock' )
    creation_date = fields.Date( default=fields.Date.today(), 
                                    string='Fecha de creación',
                                    help='Selecciona la fecha de creación' )
    update_date = fields.Date( default=fields.Date.today(),
                                string='Fecha de actualización',
                                help='Selecciona la fecha de actualización' )
    active = fields.Boolean( default=True,
                                string='Producto activo',
                                help='¿Se puede comprar el producto?' )
    weight = fields.Float( digits = (10, 2),
                            string='Peso del producto',
                            help='Introduce el peso del producto' )

