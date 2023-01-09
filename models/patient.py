from datetime import date
from  odoo import api, fields, models, _
from odoo.exceptions import ValidationError

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

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code("hospital.patient")
        return super(hospitalpatient, self).create(vals)

    # def write(self, vals):
    #     if not vals['ref']:
    #         vals['ref'] = self.env['ir.sequence'].next_by_code("hospital.patient")
    #         return super(hospitalpatient,  self).write(vals)
    
    def name_get(self):
        # patient_list = []
        return [(record.id, "%s : %s" %(record.name ,record.ref)) for record in self ]
        # for record in self:
        #     name = record.name +record.ref
        #     patient_list.append((record.id, name))
        # return patient_list
    @api.constrains('date_of_birth')
    def check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > date.today():
                raise ValidationError(_("Date of birth is not valid"))
        return 
