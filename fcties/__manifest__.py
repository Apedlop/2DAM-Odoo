# -*- coding: utf-8 -*-
{
    'name': "FCTIES",

    'summary': "Módulo para gestionar la información sobre los alumnos de FP y las empresas colaboradorasen la que están haciendo o han hecho prácticas de FCT.",

    'description': """
Módulo para gestionar la información sobre los alumnos de FP y las empresas colaboradorasen la que están haciendo o han hecho prácticas de FCT.
    """,

    'author': "Ángela Pedrera",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
    'icon': '/fcties/static/icon.jpg',
}

