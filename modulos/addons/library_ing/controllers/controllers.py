# -*- coding: utf-8 -*-
# from odoo import http


# class LibraryIng(http.Controller):
#     @http.route('/library_ing/library_ing', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_ing/library_ing/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_ing.listing', {
#             'root': '/library_ing/library_ing',
#             'objects': http.request.env['library_ing.library_ing'].search([]),
#         })

#     @http.route('/library_ing/library_ing/objects/<model("library_ing.library_ing"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_ing.object', {
#             'object': obj
#         })
