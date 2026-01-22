# -*- coding: utf-8 -*-
{
    'name': "SSC",

    'summary': """Desarrollos para ssc""",

    'description': """Desarrollos para ssc""",

    'author': "Silva Technologies",
    'website': "http://silvatechnologies.odoo.com",

    'category': 'Uncategorized',
    'version': '1.0',

    'depends': ['sale'],

    'data': [
        'security/produce_groups.xml',
        'security/ir.model.access.csv',
        'views/ssc_views.xml',
    ],

}