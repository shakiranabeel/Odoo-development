from odoo import api, fields, models

class appointmentpatient(models.Model):
    _name = 'appointment.patient'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "appointment patient"
    _rec_name ='patient_id'

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    appointment_date = fields.Datetime(string="Appointment date", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking date", default = fields.Date.context_today)
    gender=fields.Selection([('male','Male'),('female','Female')], string="Gender", related ='patient_id.gender')
    ref = fields.Char(string = 'Reference')
    appointment_pharmacy_line_ids =fields.One2many('appointment.pharmacy.line', 'appointment_id', string ='Pharmacy')
    prescription =fields.Html(string="Prescription")
    priority = fields.Selection([
        ('0','Normal'),
        ('1','Low'),
        ('2','High'),
        ('3','Very high')], string="Priority")

class AppointmentPharmacyLine(models.Model):
    _name = 'appointment.pharmacy.line'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Appointment Pharmacy Line"

    product_id = fields.Many2one('product.product', string="Product",required='True')
    price = fields.Float(related ='product_id.lst_price')
    qty = fields.Integer(string="Quantity", default=1)
    appointment_id =fields.Many2one('appointment.patient', string='Appointment')


    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref
