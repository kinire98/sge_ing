# -*- coding: utf-8 -*-
{
    'name': "Biblioteca Iker Nieto Garrido",

    'summary': """
        Biblioteca ejemplo con relaciones
        """,

    'description': """
        Biblioteca ejemplo con relaciones
    """,

    'author': "Iker Nieto Garrido",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/library_autores_views.xml',
        'views/library_generos_views.xml',
        'views/library_libros_views.xml',
        'views/library_socios_views.xml',
        'views/library_menu_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
} # type: ignore
