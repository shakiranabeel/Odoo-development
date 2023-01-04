from datetime import date
from  odoo import api, fields, models

class hospitalpatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "hospital patient"
    image=fields.Image(string="Image")
    name = fields.Char(string ='Name', tracking = True)
    date_of_birth =fields.Date(string='Date of Birth')
    age = fields.Integer(string = 'Age', compute = '_compute_age')
    gender=fields.Selection([('male','Male'),('female','Female')], string="Gender")
    address= fields.Text(string='Address')
    bloodgroup=fields.Char(string='Blood group')
    active=fields.Boolean(string="Active", default = True)
    ref = fields.Char(string = 'Reference')
    
 

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today() 
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0




    
