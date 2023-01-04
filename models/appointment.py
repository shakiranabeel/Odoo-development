from odoo import api, fields, models

class appointmentpatient(models.Model):
    _name = 'appointment.patient'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "appointment patient"
    _rec_name ='patient_id'

    patient_id = fields.Many2one('hospital.patient', string = "Patient")
    appointment_date = fields.Datetime(string="Appointment date", default = fields.Datetime.now)
    doctor_id = fields.Many2one('doctor.appointment', string = "Doctor")
   
    booking_date = fields.Date(string = "Booking date", default = fields.Date.context_today)
    gender = fields.Selection([('male','Male'),('female','Female')], string = "Gender", related ='patient_id.gender', help = "Gender of the patient")
    ref = fields.Char(related ='patient_id.ref')
    appointment_pharmacy_line_ids = fields.One2many('appointment.pharmacy.line', 'appointment_id', string ='Pharmacy')
    prescription = fields.Html(string="Prescription")
    hide_price = fields.Boolean(string="Hide price")
    tag_ids = fields.Many2many('patient.tag', string = "Tag")

    priority = fields.Selection([
        ('0','Normal'),
        ('1','Low'),
        ('2','High'),
        ('3','Very high')], string="Priority")
    state = fields.Selection([
        ('draft','Draft'),
        ('in_consultation','In_consultation'),
        ('done','Done'),
        ('cancel','Cancelled')],default='draft', string="State")

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def object_test(self):
        return {
            'effect' : {
            'fadeout' :'slow',
            'message': 'Click Successful',
            'type' :'rainbow_man'
            }
        }
        
    def action_in_consultation(self):
        for rec in self:
            rec.state="in_consultation"
    def action_done(self):
        for rec in self:
            rec.state="done"
    def action_cancel(self):
        for rec in self:
            rec.state="cancel"       
    def action_reset(self):
        for rec in self:
            rec.state="draft"  


class AppointmentPharmacyLine(models.Model):
    _name = 'appointment.pharmacy.line'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Appointment Pharmacy Line"

    product_id = fields.Many2one('product.product', string="Product",required='True')
    price = fields.Float(related ='product_id.lst_price')
    qty = fields.Integer(string="Quantity", default=1)
    appointment_id = fields.Many2one('appointment.patient', string='Appointment')

class DoctorAppointment(models.Model):
    _name = 'doctor.appointment'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Doctor Appointment"

    name = fields.Char(string="Doctor")