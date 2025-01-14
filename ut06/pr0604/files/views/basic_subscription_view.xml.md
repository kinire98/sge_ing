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