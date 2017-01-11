# -*- coding: utf-8 -*-
from odoo import http

# class ProductAddfield(http.Controller):
#     @http.route('/product_addfield/product_addfield/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_addfield/product_addfield/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_addfield.listing', {
#             'root': '/product_addfield/product_addfield',
#             'objects': http.request.env['product_addfield.product_addfield'].search([]),
#         })

#     @http.route('/product_addfield/product_addfield/objects/<model("product_addfield.product_addfield"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_addfield.object', {
#             'object': obj
#         })