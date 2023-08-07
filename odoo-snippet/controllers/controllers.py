# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
class GetData(http.Controller):
    @http.route('/get/data',type='json',auth='public',method=['GET','POST'])
    def getData(self,**kw):
        return self.getContact()
    
    def getContact(self):
        track = http.request.env['res.partner']
        return track.sudo().get_data_model()

class GetDataCompany(http.Controller):
    @http.route('/get/data_company',type='json',auth='public',method=['GET','POST'])
    def getData(self,**kw):
        return self.getDataCom()
    
    def getDataCom(self):
        track = http.request.env['res.company']
        return track.sudo().get_data_com_model()

class GetSlide(http.Controller):
    @http.route('/get/slide',type='json',auth='public',method=['GET','POST'])
    def getSlide(self,**kw):
        return self.getSlideImage()

    def getSlideImage(self):
        track = http.request.env['carousel.slide']
        return track.sudo().get_Slide_Model()


class GetDataUser(http.Controller):
    @http.route('/get/data/user',type='json',auth='public',method=['GET','POST'])
    def getData(self,**kw):
        return request.env.user.read(fields=['name','phone','email'])[0]


# class TutorialSnippets(http.Controller):
#     @http.route('/tutorial_snippets/tutorial_snippets', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tutorial_snippets/tutorial_snippets/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tutorial_snippets.listing', {
#             'root': '/tutorial_snippets/tutorial_snippets',
#             'objects': http.request.env['tutorial_snippets.tutorial_snippets'].search([]),
#         })

#     @http.route('/tutorial_snippets/tutorial_snippets/objects/<model("tutorial_snippets.tutorial_snippets"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tutorial_snippets.object', {
#             'object': obj
#         })
