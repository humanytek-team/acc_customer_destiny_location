# -*- coding: utf-8 -*-

from openerp import addons
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError


class account_invoice(models.Model):
	_inherit = ['account.invoice']

	client_warehouse_id = fields.Many2one('client.warehouse', string="Ubicacion de cliente", domain="[('partner_id', '=', partner_id)]")