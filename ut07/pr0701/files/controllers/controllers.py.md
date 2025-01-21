# controllers/controllers.py
```python
# -*- coding: utf-8 -*-
from odoo import http #type: ignore
from odoo.http import request #type: ignore


class Subscription(http.Controller):
    @http.route('/subscription/', auth='public', type='http', website=True)
    def index(self, **kw):
        return http.request.render('subscription.welcome_message', {})
    
    @http.route('/subscription/subscription_list', auth='public', type='http', website=True)
    def list(self, **kw):
        subs = request.env['subscription.subscription'].search([])
        return http.request.render('subscription.subscription_list', {
            'subs': subs
        })
```