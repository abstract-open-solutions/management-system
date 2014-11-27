# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import fields, models, api


class mgmtsystem_nonconformity_origin(models.Model):
    """
    Origin of nonconformity of the management system
    """
    _name = "mgmtsystem.nonconformity.origin"
    _description = "Origin of nonconformity of the management system"
    _order = 'parent_id, sequence'

    id = fields.Integer('ID', readonly=True)
    name = fields.Char('Origin', required=True, translate=True)
    description = fields.Text('Description')
    sequence = fields.Integer(
        'Sequence',
        help="Defines the order to present items",
    )
    parent_id = fields.Many2one(
        'mgmtsystem.nonconformity.origin',
        'Group',
    )
    child_ids = fields.One2many(
        'mgmtsystem.nonconformity.origin',
        'parent_id',
        'Childs',
    )
    ref_code = fields.Char('Reference Code')

    @api.multi
    def name_get(self):
        reads = self.read(['name', 'parent_id'])
        res = []
        for record in reads:
            name = record['name']
            if record['parent_id']:
                name = record['parent_id'][1] + ' / ' + name
            res.append((record['id'], name))
        return res

    @api.multi
    def _name_get_fnc(self, prop, unknow_none):
        res = self.name_get()
        return dict(res)
