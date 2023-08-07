# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Carousel(models.Model):
    _name="carousel.slide"
    _description="Carousel is no hope"

    image = fields.Binary("Cover",required=True)
    day_start = fields.Date(required=True)
    day_end = fields.Date(required=True)

    @api.model 
    def get_Slide_Model(self):
        records = self.env['carousel.slide']
        today = fields.Date.today()
        results = records.search_read([('day_start','<',today),('day_end','>',today)],fields=['id','image','day_start','day_end'])
        for record in results:
            record['image'] = "/web/image?model=carousel.slide&field=image&id=%s" % record['id']
        return results