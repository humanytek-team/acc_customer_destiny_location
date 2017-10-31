# -*- coding: utf-8 -*-

from openerp import addons
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError


class client_warehouse(models.Model):
	_name = 'client.warehouse'
	_description = 'Almacenes de cliente'

	name = fields.Char('Nombre de almacen', size=128, required=True)
	partner_id = fields.Many2one('res.partner', 'Cliente', required=True)
	