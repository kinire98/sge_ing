# `models/autor.py`

```python
# -*- coding: utf-8 -*-

from odoo import models, fields, api #type: ignore


class autor(models.Model):
    _name = 'modulo_biblioteca.autor'
    _description = 'Gestion autores'

    nombre = fields.Text()
    fecha_nac = fields.Date()
    biografia = fields.Text()
    libros = fields.Text()
```