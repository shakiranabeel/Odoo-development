{
    'name': 'Hospital management',
    'version': '15.0.0.1',
    'summary': 'hospital management',
    'sequence': -100,
    'author':'code-ox',
    'description': """hospital management""",
    'website': 'https://code-ox.com',
    'category': 'Extra tools',
    'depends': ['mail', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'data/patient.tag.csv',
        'data/patient_tag_data.xml',
        'data/sequence_data.xml',
        'wizard/cancel_appointment.xml',
        'views/menu.xml',
        'views/patient.xml',
        'views/female.xml',
        'views/appointment.xml',
        'views/tag.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}