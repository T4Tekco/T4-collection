# -*- coding: utf-8 -*-
# from odoo import http


# class T4tekSalary(http.Controller):
#     @http.route('/t4tek_salary/t4tek_salary', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/t4tek_salary/t4tek_salary/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('t4tek_salary.listing', {
#             'root': '/t4tek_salary/t4tek_salary',
#             'objects': http.request.env['t4tek_salary.t4tek_salary'].search([]),
#         })

#     @http.route('/t4tek_salary/t4tek_salary/objects/<model("t4tek_salary.t4tek_salary"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('t4tek_salary.object', {
#             'object': obj
#         })
