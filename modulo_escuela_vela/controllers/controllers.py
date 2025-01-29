# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloEscuelaVela(http.Controller):
#     @http.route('/modulo__escuela_vela/modulo__escuela_vela', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo__escuela_vela/modulo__escuela_vela/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo__escuela_vela.listing', {
#             'root': '/modulo__escuela_vela/modulo__escuela_vela',
#             'objects': http.request.env['modulo__escuela_vela.modulo__escuela_vela'].search([]),
#         })

#     @http.route('/modulo__escuela_vela/modulo__escuela_vela/objects/<model("modulo__escuela_vela.modulo__escuela_vela"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo__escuela_vela.object', {
#             'object': obj
#         })

