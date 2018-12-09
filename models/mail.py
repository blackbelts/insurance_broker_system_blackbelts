from odoo import models, fields, api ,_
from odoo.exceptions import ValidationError

class mailMessages(models.Model):
    _inherit = 'mail.mail'


    # @api.onchange('email_from')
    def _get_user_name(self):
        if self.email_from:
          print('***************')
          self.partner_from =self.env["res.partner"].search([('email', '=',self.email_from )])
          print(self.partner_from)

    partner_from = fields.Many2one('res.partner',default=_get_user_name)

