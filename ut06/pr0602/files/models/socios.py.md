# `models/socios.py`

```python
# -*- coding: utf-8 -*-

from odoo import models, fields, api #type: ignore

class Socios(models.Model):
    _name = "library_ing.socios"
    _description = "Socios de la biblioteca. Pueden pedir libros prestados"

    name = fields.Char(required = True, string = "Nombre")
    phone = fields.Char(required = True, size = 9, string = "Teléfono")
    books = fields.Many2many(
            comodel_name="library_ing.libros",
            string = "Libros"
            )
```