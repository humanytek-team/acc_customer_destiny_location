# -*- coding: utf-8 -*-

from openerp import addons
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError


class sale_order(models.Model):
	_inherit = ['sale.order']

	client_warehouse_id = fields.Many2one('client.warehouse', string="Almacen de cliente", domain="[('partner_id', '=', partner_id)]")