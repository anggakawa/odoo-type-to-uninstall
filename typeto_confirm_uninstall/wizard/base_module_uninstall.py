from odoo import api, fields, models, _
from odoo.exceptions import UserError


class InheritBaseModuleUninstall(models.TransientModel):
    _inherit = "base.module.uninstall"

    type_module_name = fields.Char('Technical Name to Uninstall')

    def action_uninstall(self):
        modules = self.module_id
        if modules.name == self.type_module_name:
            return modules.button_immediate_uninstall()
        else:
            raise UserError(_('Technical name is not correct'))
