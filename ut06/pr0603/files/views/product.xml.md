# `views/product.xml`

```xml
<?xml version='1.0' encoding='utf-8'?>
<odoo>
  <data>
    <!-- explicit list view definition -->
    <record model="ir.ui.view" id="stock_management.product_list">
      <field name="name">Producto</field>
      <field name="model">stock_management.product</field>
      <field name="arch" type="xml">
        <tree>
          <field name="name"/>
          <field name="category"/>
          <field name="price"/>
          <field name="stock"/>
          <field name="total_value"/>
          <field name="full_name"/>
          <field name="currency_id"/>
        </tree>
      </field>
    </record>

    <!-- actions opening views on models -->
    <record model="ir.actions.act_window" id="stock_management.product_action_window">
      <field name="name">Añadir producto</field>
      <field name="res_model">stock_management.product</field>
      <field name="view_mode">tree,form</field>
    </record>
-->

    <!-- server action to the one above -->
<!--
    <record model="ir.actions.server" id="stock_management.action_server">
      <field name="name">stock_management server</field>
      <field name="model_id" ref="model_stock_management_stock_management"/>
      <field name="state">code</field>
      <field name="code">
        action = {
          "type": "ir.actions.act_window",
          "view_mode": "tree,form",
          "res_model": model._name,
        }
      </field>
    </record>
-->

  </data>
</odoo>
```
