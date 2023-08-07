# -*- coding: utf-8 -*-
from odoo import models, fields, api
class ContactData(models.Model):
    _inherit = 'res.partner'
    @api.model
    def get_data_model(self):
        record = self.env['res.partner']
        result = record.search_read([],fields=['phone'])
        return result

class DataCompany(models.Model):
    _inherit = "res.company"  
    @api.model
    def get_data_com_model(self):
        record_com = self.env['res.company']
        rsl = record_com.search_read([],fields=['name','phone','email','website','street'])
        return rsl


# class tutorial_snippets(models.Model):
#     _name =ModelName_snippets.tutorial_snippets'
#     _description = 'tutorial_snippets.tutorial_snippets'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
