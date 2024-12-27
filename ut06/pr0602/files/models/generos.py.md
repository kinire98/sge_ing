# `models/generos.py`

```python
# -*- coding: utf-8 -*-

from odoo import models, fields, api #type: ignore

class Generos(models.Model):
    _name = "library_ing.generos"
    _description = "Géneros literarios de los libros"

    name = fields.Char(required = True, string = "Nombre")
```