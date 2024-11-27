# -*- coding: utf-8 -*-
{
    'name': "Gestión salas y reservas",

    'summary': """
        Este módulo se utiliza para la gestión de las reservas y las salas de una empresa
        """,

    'description': """
        Este módulo se utiliza para la gestión de las reservas y las salas de una empresa, para así llevarlas a cabo de manera más ordenada y eficiente
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': False
} #type: ignore
