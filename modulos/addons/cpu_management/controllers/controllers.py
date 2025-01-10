# -*- coding: utf-8 -*-
# from odoo import http


# class CpuManagement(http.Controller):
#     @http.route('/cpu_management/cpu_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cpu_management/cpu_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cpu_management.listing', {
#             'root': '/cpu_management/cpu_management',
#             'objects': http.request.env['cpu_management.cpu_management'].search([]),
#         })

#     @http.route('/cpu_management/cpu_management/objects/<model("cpu_management.cpu_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cpu_management.object', {
#             'object': obj
#         })
