from datetime import date
from  odoo import api, fields, models, _
from odoo.exceptions import ValidationError
class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Cancel Appointment Wizard"

    @api.model
    def default_get(self, fields):

        res = super(CancelAppointmentWizard, self).default_get(fields)
        res['cancel_date'] = date.today()
        return res
        


    appointment_id = fields.Many2one('appointment.patient', string="Appointment Id")
    
    reason = fields.Text(string = "Reason")
    cancel_date = fields.Date(string= "Cancellation Date")
    

    
    def action_cancel(self):
        if self.appointment_id.booking_date == fields.date.today():
            raise ValidationError(_("Sorry, you can't cancel your appointment"))
        return 


        