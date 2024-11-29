# ` __manifest__.py`

```python
# -*- coding: utf-8 -*-
{
    'name': "Biblioteca",

    'summary': """
        Biblioteca
        """,

    'description': """
        Biblioteca
    """,

    'author': "Biblioteca S.A.",
    'website': "https://www.biblioteca.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/autor_view.xml',
        'views/libro_view.xml',
        'views/menu.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
} #type: ignore
```