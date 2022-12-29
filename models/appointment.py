from  odoo import api, fields, models

class appointmentpatient(models.Model):
    _name = 'appointment.patient'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "appointment patient"

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    appointment_date = fields.Datetime(string="Appointment date")
    booking_date = fields.Date(string="Booking date")
    

    
