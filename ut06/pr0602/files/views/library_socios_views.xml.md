# `views/library_socios_views.xml`

```xml
<?xml version='1.0' encoding='utf-8'?>
<odoo>
  <data>

    <!-- explicit list view definition -->
    <record model="ir.ui.view" id="library_ing.add_socio">
      <field name="name">Añadir socio</field>
      <field name="model">library_ing.socios</field>
      <field name="arch" type="xml">
        <tree>
          <field name="name"/>
          <field name="phone"/>
          <field name="books"/>
        </tree>
      </field>
    </record>

    <!-- actions opening views on models -->
    <record model="ir.actions.act_window" id="library_ing.add_socio_action">
      <field name="name">Abrir menú adición socio</field>
      <field name="res_model">library_ing.socios</field>
      <field name="view_mode">tree,form</field>
    </record>
  </data>
</odoo>
```