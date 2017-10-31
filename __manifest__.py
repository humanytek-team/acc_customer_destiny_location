# -*- coding: utf-8 -*-
{
    'name': 'Lista de almacenes destino en la cotizacion/pedido de venta',
    'version': '1.1',
    'author': 'Humanytek',
    'description': """
    Permite seleccionar un almacen destino en las cotizaciones / pedidos de venta para un cliente en particular.
    """,
    'depends': ['sale','base', 'account'],
    'data': [
        #'sale_order.xml',
        'account_invoice.xml',
        'client_warehouse.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: