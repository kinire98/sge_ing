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