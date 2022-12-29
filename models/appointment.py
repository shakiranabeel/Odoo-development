from odoo import api, fields, models

class appointmentpatient(models.Model):
    _name = 'appointment.patient'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "appointment patient"

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    appointment_date = fields.Datetime(string="Appointment date", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking date", default = fields.Date.context_today)
    gender=fields.Selection([('male','Male'),('female','Female')], string="Gender", related ='patient_id.gender')
    ref = fields.Char(string = 'Reference')





    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref
