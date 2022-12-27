from  odoo import api, fields, models

class hospiatlpatient(models.Model):
    _name = 'hospital.patient'
    _description = "hospial patient"

    name = fields.Char(string ='Name')
    age = fields.Integer(string = 'Age')
    gender=fields.Selection([('male','Male'),('female','Female')], string="Gender")
    address= fields.Text(string='Address')
    bloodgroup=fields.Char(string='Blood group')
    active=fields.Boolean(string="Active", default = True)


    
