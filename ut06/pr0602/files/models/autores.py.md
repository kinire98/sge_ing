# `models/autores.py`

```python
# -*- coding: utf-8 -*-

from odoo import models, fields, api #type: ignore


class Autores(models.Model):
    _name = "library_ing.autores"
    _description = "library_ing.library_ing"

    name = fields.Char(string = "Nombre")
    phone = fields.Char(required = True, size = 9, string = "Teléfono")
    origin_country = fields.Many2one(
            comodel_name = "res.country",
            string = "País de origen"
            )
    author = fields.Many2many(
            comodel_name = "library_ing.libros",
            relation = "book_authors",
            column1 = "autores_id",
            column2 = "libros_id",
            string = "Autor de:"
            )
    revisor = fields.Many2many (
            comodel_name = "library_ing.libros",
            relation = "book_revisors",
            column1 = "autores_id",
            column2 = "libros_id",
            string = "Revisor de:"
            )
```