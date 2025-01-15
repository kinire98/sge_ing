# views/form_view.xml
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