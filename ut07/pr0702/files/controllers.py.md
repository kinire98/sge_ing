# `controllers/controllers.py`
```python
# -*- coding: utf-8 -*-
from odoo import http #type: ignore
from odoo.http import request, Response #type: ignore
import json


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

    @http.route("/api/subscription", type="http", methods=["GET"], csrf=False)
    def get_subscriptions(self, **kwargs):
        status = request.params.get('status')
        page = request.params.get('page')
        if status:
            if status != 'pending' and status != 'expired' and status != 'cancelled' and status != 'active':
                return Response(
                    json.dumps({"res": "Bad request, wasn't a valid status"}),
                    content_type = 'application/json',
                    status = 400
                    )
        subscriptions = ''
        if not status:
            subscriptions = request.env['subscription.subscription'].search([])
        else:
            subscriptions = request.env['subscription.subscription'].sudo().search([('status', '=', status)])
        try:
            if not page:
                result = []
                for sub in subscriptions:
                    result.append({
                        "name": sub.name,
                        "subscription_code": sub.subscription_code,
                        "price": sub.price,
                        "status": sub.status
                        })
                return Response(
                        json.dumps(result),
                        content_type = 'application/json',
                        status = 200
                        )
            else:
                if len(subscriptions) < (int(page) - 1) * 10 + 1:
                    return Response(
                            json.dumps({'msg': f'No hay suficentes subscripciones para mostrar'}),
                            status = 200,
                            content_type = 'application/json'
                            )
                result = []
                subscriptions =  subscriptions[(int(page) - 1) * 10 : (int(page) - 1) * 10 + 10]
                for sub in subscriptions:
                    result.append({
                        "name": sub.name,
                        "subscription_code": sub.subscription_code,
                        "price": sub.price,
                        "status": sub.status
                        })
                return Response(
                        json.dumps(result),
                        content_type = 'application/json',
                        status = 200
                        )
        except Exception as e:
                return Response(
                    json.dumps({'msg': f"Error interno del servidor: {str(e)}"}),
                    content_type = 'application/json',
                    status = 500
                    )

    @http.route("/api/subscription/<string:name>", type="http", methods=['GET'], csrf=False)
    def get_subscriptions_by_name(self, name):
        try:
            subscriptions = request.env['subscription.subscription'].sudo().search([('name', '=', name)], limit = 1)
            result = []
            for sub in subscriptions:
                result.append({
                    "name": sub.name,
                    "subscription_code": sub.subscription_code,
                    "price": sub.price,
                    "status": sub.status
                    })
            return Response(
                json.dumps(result),
                content_type = 'application/json',
                status = 200
                )
        except Exception as e:
            return Response(
                    json.dumps({'msg': f"Error interno del servidor: {str(e)}"}),
                    content_type = 'application/json',
                    status = 500
                    )
```