# Proyecto 2º Trimestre 
<a href="./subscription.zip" download="proyecto2_Iker_Nieto.zip">Descargar módulo</a>
## `controllers/__init__.py`
```python
# -*- coding: utf-8 -*-

from . import controllers
```
## `controllers/controllers.py`
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
## `models/__init__.py`
```python
# -*- coding: utf-8 -*-

from . import subscription
from . import metrics
```
## `models/metrics.py`
```python
# -*- coding: utf-8 -*-
from odoo import models, fields, api #type: ignore


class metrics(models.Model):
    _name = 'subscription.metrics'
    _description = 'Metricas para las subscripciones'

    date = fields.Date()
    active_subscriptions = fields.Integer()
    revenue_generated = fields.Float()
    renewal_fee = fields.Float(compute = '_calculate_renewal_fee') 
    cancelation_fee = fields.Float(compute = '_caculate_cancelation_fee') 
    renewals = fields.Integer()
    new_subscriptions = fields.Integer()
    canceled = fields.Integer()
    new_clients = fields.Integer()
    recurrent_clients = fields.Integer()
    average_revenue_by_user = fields.Float(compute = '_caculate_average_revenue_by_user') 
    conversion_fee = fields.Float()
    churn_rate = fields.Float()
    lifetime_value = fields.Float()
    client_adquisition_cost = fields.Float()
    notes = fields.Text()
    relation_with_model = fields.One2many(
            comodel_name = 'subscription.subscription',
            inverse_name = 'metrics_field'
            )
    
    @api.depends('renewal_fee', 'renewals', 'active_subscriptions')
    def _calculate_renewal_fee(self):
        for record in self:
            if record.active_subscriptions == 0:
                record.renewal_fee = 0
                continue
            record.renewal_fee = (record.renewals / record.active_subscriptions) * 100

    @api.depends('cancelation_fee', 'active_subscriptions', 'canceled')
    def _caculate_cancelation_fee(self):
        for record in self:
            if record.active_subscriptions == 0:
                record.cancelation_fee = 0
                continue
            record.cancelation_fee = (record.canceled / record.active_subscriptions) * 100

    @api.depends('average_revenue_by_user', 'revenue_generated', 'active_subscriptions')
    def _caculate_average_revenue_by_user(self):
        for record in self:
            if record.active_subscriptions == 0:
                record.average_revenue_by_user = 0
                continue
            record.average_revenue_by_user = (record.revenue_generated / record.active_subscriptions)
```
## `models/subscription.py`
```python
# -*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api #type: ignore


class subscription(models.Model):
    _name = 'subscription.subscription'
    _description = 'Gestión de las subscripciones'
    _sql_constraints = [
            ('unique_name', 'unique(name)', 'El nombre debe ser único')
            ]

    name = fields.Char( string = 'Nombre', required = True )
    customer_id = fields.Many2one( string = 'Identificador de cliente', comodel_name = 'res.partner', required = True )
    subscription_code = fields.Char( string = 'Código de susbcripción', required = True )
    start_date = fields.Date( string = 'Fecha de comienzo', required = True )
    end_date = fields.Date( string = 'Fecha de finalización' )
    renewal_date = fields.Date( string = 'Fecha de renovación' )
    status = fields.Selection(string='Estado', selection=[
        ('active', 'Activa'),
        ('expired', 'Expirada'),
        ('pending', 'Pendiente'),
        ('cancelled', 'Cancelada'),
        ])
    is_renewable = fields.Boolean(string='Renovable')
    auto_renewal = fields.Boolean(string='Auto renovable')
    price = fields.Float(string='Precio')

    usage_limit = fields.Integer(string='Límite de uso')
    current_usage = fields.Integer(string='Uso actual')
    use_percent = fields.Integer(string='Porcentaje de uso', compute = '_calculate_use_percent', default=0)
    metrics_field = fields.Many2one(comodel_name = 'subscription.metrics')

    @api.depends('usage_limit', 'current_usage')
    def _calculate_use_percent(self):
        for record in self:
            if record.usage_limit != 0:
                record.use_percent = int(record.current_usage / record.usage_limit * 100)
            else:
                record.use_percent = 0 
    def add_15_days(self):
        self.end_date = self.end_date + datetime.timedelta(days = 15);
```
## `security/ir.model.access.csv`
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_subscription_subscription,subscription.subscription,model_subscription_subscription,base.group_user,1,1,1,1
access_subscription_metrics,subscription.metrics,model_subscription_metrics,base.group_user,1,1,1,1
```
## `views/basic_subscription_view.xml`
```xml
<?xml version='1.0' encoding='utf-8'?>
<odoo>
    <data>
      <record model="ir.ui.view" id="subscription.basic_list">
        <field name="name">Lista de subscripciones</field>
        <field name="model">subscription.subscription</field>
        <field name="arch" type="xml">
          <tree editable="bottom" 
            decoration-danger="status=='expired'"
            decoration-warning="status=='cancelled'"
            limit="15">
            <field name="name" string="Nombre"/>
            <field name="customer_id" string="Identificador de cliente"/>
            <field name="subscription_code" string="Código de subscripcion"/>
            <field name="start_date" string="Fecha de comienzo"/>
            <field name="end_date" string="Fecha de finalización"
              widget="remaining_days"/>
            <field name="renewal_date" string="Fecha de renovación"/>
            <field name="status" string="Estado"
              widget="radio"/>
            <field name="is_renewable" string="Renovable"/>
            <field name="auto_renewal" string="Auto-renovable"/>
            <field name="price" string="Precio"
              attrs="{'invisible' : [('status', '=', 'cancelled')]}"/>
            <button name="add_15_days"
              type="object"
              string="Añadir 15 días"
              icon='fa-plus'/>
          </tree>
        </field>
      </record>

      <!-- actions opening views on models -->
      <record model="ir.actions.act_window" id="subscription.action_basic_list">
        <field name="name">Subscripciones (básico)</field>
        <field name="res_model">subscription.subscription</field>
        <field name="view_mode">tree,form</field>
        <field name="view_id" ref="subscription.basic_list"/>
      </record>
        
    </data>
</odoo>
```
## `views/form_view.xml`
```xml
<?xml version='1.0' encoding='utf-8'?>
<odoo>
    <data>
      <!-- Add you code here -->
      <!-- model.name form view -->
      <record id="subscription.view_form" model="ir.ui.view">
        <field name="name">Formulario de subscripción</field>
        <field name="model">subscription.subscription</field>
        <field name="arch" type="xml">
          <form string="Añadir subscripción">
            <sheet>
              <group>
                <!-- Add your fields here -->
                <field name="name" string="Nombre"/>
                <field name="customer_id" string="Identificador de cliente"/>
                <field name="subscription_code" string="Código de subscripcion"/>
              </group>
              <notebook>
                <page string="Fechas" name="dates">
                  <group>
                    <field name="start_date" string="Fecha de comienzo"/>
                    <field name="end_date" string="Fecha de finalización"/>
                    <field name="renewal_date" string="Fecha de renovación"/>
                  </group>
                </page>
                <page name="renewal" string="Renovación">
                  <group name="renewal_status" string="Estado renovación">
                    <field name="status" string="Estado"/>
                    <field name="is_renewable" string="Renovable"/>
                    <field name="auto_renewal" string="Auto-renovable"/>
                  </group>
                  <group name="renewal_price" string="Precio renovación">
                    <field name="price" string="Precio"/>
                  </group>
                </page>
                <page name="usage" string="Uso" cols="2">
                  <group>
                    <field name="usage_limit" 
                      string="Límite de uso"
                      colspan="2"/>
                    <field name="current_usage" 
                      string="Uso actual"
                      colspan="2"/>
                    <field name="use_percent"
                      string="Uso porcentual"
                      colspan="2"/>
                     </group>
                </page>
              </notebook>
            </sheet>
            
          </form>
        </field>
      </record>

      <record model="ir.actions.act_window" id="subscription.action_form">
        <field name="name">Añadir subscripción</field>
        <field name="res_model">subscription.subscription</field>
        <field name="view_mode">tree,form</field>
        <field name="view_id" ref="subscription.view_form"/>
      </record>
    </data>
</odoo>
```
## `views/menu.xml`
```xml
<?xml version='1.0' encoding='utf-8'?>
<odoo>
    <data>

    <!-- Top menu item -->
    <menuitem name="Subscripciones" id="subscription.menu_root"/>
    <!-- menu categories -->
    <menuitem name="Subscripción" id="subscription.menu_subscription" parent="subscription.menu_root"/>
    <menuitem name="Métricas" id="subscription.menu_metrics" parent="subscription.menu_root"/>
    <!-- actions -->
    <menuitem name="Básico" id="subscription.menu_subscription_basic_list" parent="subscription.menu_subscription"
              action="subscription.action_basic_list"/>
    <menuitem name="Uso" id="subscription.menu_subscription_usage_list" parent="subscription.menu_subscription"
              action="subscription.action_usage_list"/>
    <menuitem name="Añadir" id="subscription.menu_subscription_form" parent="subscription.menu_subscription"
              action="subscription.action_form"/>
    <menuitem  name="Ver" id="subscription.metric_field" parent="subscription.menu_metrics"
      action="subscription.metrics_form"/>
      
    </data>
</odoo>
```
## `views/metrics_tree.xml`
```xml
<?xml version='1.0' encoding='utf-8'?>
<odoo>
    <data>
      <record id="subscription.metrics_tree" model="ir.ui.view">
        <field name="name">Formulario de subscripción</field>
        <field name="model">subscription.metrics</field>
        <field name="arch" type="xml">
          <form string="Añadir subscripción">
            <sheet>
              <group>
                <!-- Add your fields here -->
                <field name="date" string="Fecha"/>
                <field name="active_subscriptions" string="Subscripciones activas"/>
                <field name="revenue_generated" string="Ingresos generados"/>
              </group>
              <notebook>
                <page name="data" string="Datos varios">
                  <group>
                    <field name="new_subscriptions" string="Nuevas subscripciones"/>
                    <field name="canceled" string="Canceladas"/>
                    <field name="new_clients" string="Nuevos clientes"/>
                    <field name="recurrent_clients" string="Clientes recurrentes"/>
                  </group>
                </page>
                <page string="Tasas" name="fees">
                  <group>
                    <field name="renewal_fee" string="Tasa de renovación"/>
                    <field name="cancelation_fee" string="Tasa de cancelación"/>
                    <field name="conversion_fee" string="Tasa de conversión"/>
                    <field name="churn_rate" string="Tasa de pérdida de clientes"/>
                  </group>
                </page>
                <page name="client_revenue_generation" string="Generación de ingresos de clientes">
                  <group>
                    <field name="lifetime_value" string="Ingresos generados"/>
                    <field name="client_adquisition_cost" string="Coste de adquisición de clientes"/>
                    <field name="average_revenue_by_user" string="Ingresos medios por usuario"/>
                  </group> 
                </page>
                <page name="notes_and_other" string="Notas y número de subscripciones">
                  <group>
                    <field name="notes" string="Notas"/>
                    <field name="relation_with_model"
                      string="Subscripciones"/>
                  </group>
                </page>
              </notebook>
            </sheet>
            
          </form>
        </field>
      </record>

      <record model="ir.actions.act_window" id="subscription.metrics_form">
        <field name="name">Formulario de subscripción</field>
        <field name="res_model">subscription.metrics</field>
        <field name="view_mode">tree,form</field>
        <field name="view_id" ref="subscription.metrics_tree"/>
      </record>
      
    </data> 
</odoo>
```
## `views/subscription_view.xml`
```xml
<odoo>
   <template id="subscription_list" name="Lista de subscripciones">
     <t t-call="web.html_container">
       <style>
         .sub-div {
          margin-block: 5vh;
         }
       </style>
       <div id="container">
        <h1>Subscripciones</h1>
        <t t-foreach="subs" t-as="sub">
          <div class="sub-div">
           <h2>Nombre de la subscripción: <t t-esc="sub.name"/></h2>
           <span>Codigo de la subscripción: <t t-esc="sub.subscription_code"/></span>
          </div> 
        </t>
       </div>
     </t>
   </template>
</odoo>
```
## `views/usage_subscription_view.xml`
```xml
<?xml version='1.0' encoding='utf-8'?>
<odoo>
    <data>
      <!-- Add you code here -->
      
      <record model="ir.ui.view" id="subscription.usage_list">
        <field name="name">Lista de subscripciones</field>
        <field name="model">subscription.subscription</field>
        <field name="arch" type="xml">
          <tree limit="15">
            <field name="name"/>
            <field name="usage_limit" 
              string="Límite de uso"/>
            <field name="current_usage" string="Uso actual"
              decoration-danger="use_percent&gt;80"
              avg="1"/>
            <field name="use_percent" string="Uso porcentual"
              widget="progressbar"/>
          </tree>
        </field>
      </record>
      <!-- actions opening views on models -->
      <record model="ir.actions.act_window" id="subscription.action_usage_list">
        <field name="name">Subscripciones (Uso)</field>
        <field name="res_model">subscription.subscription</field>
        <field name="view_mode">tree,form</field>
        <field name="view_id" ref="subscription.usage_list"/>
      </record>
    </data>
</odoo>
```
## `views/welcome_message.xml`
```xml
<odoo>
    <template id="welcome_message">
      <t t-call="web.html_container">
        <h1>Bienvenido</h1>
        <a href="./subscription_list">Ver subscripciones</a>
      </t>
    </template>
</odoo>
```
## `__init__.py`
```python
# -*- coding: utf-8 -*-

from . import controllers
from . import models
```
## `__manifest__.py`
```python
# -*- coding: utf-8 -*-
{
    'name': "subscription",

    'summary': """
    """,

    'description': """
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/basic_subscription_view.xml',
        'views/usage_subscription_view.xml',
        'views/form_view.xml',
        'views/welcome_message.xml',
        'views/subscription_view.xml',
        'views/metrics_tree.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
} #type: ignore
```