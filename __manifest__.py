{
    'name': 'Hospital management',
    'version': '15.0.0.1',
    'summary': 'hospital management',
    'sequence': -100,
    'author':'code-ox',
    'description': """hospital management""",
    'website': 'https://code-ox.com',
    'category': 'Extra tools',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient.xml',
        'views/female.xml',
        'views/appointment.xml'

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}