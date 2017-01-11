# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AddFieldProduct (models.Model):# Name class
    _inherit = "product.template"    # Name parent object
 
    info = fields.Char('Info', size=50)       # campo character
    author = fields.Char('Author', size=50)       # Name field want you show to your xml with char type
    user_id = fields.Many2one('res.users', 'Responsible') # esempio lookup su customers
    date_deadline = fields.Date('Deadline')	# campo data
    is_done = fields.Boolean('Done?')           # campo booleano
    desc = fields.Text('Description')		# campo testo
    state = fields.Selection(
    [('draft','New'), ('open','Started'),
    ('done','Closed')],'State')
    docs = fields.Html('Documentation')         # campo a scelta multipla
    # Numeric fields:
    sequence = fields.Integer('Sequence')
    perc_complete = fields.Float('% Complete', (3, 2))
    # Date fields:
    date_effective = fields.Date('Effective Date')
    date_changed = fields.Datetime('Last Changed')
    # Other fields:
    image = fields.Binary('Image')

