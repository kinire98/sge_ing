# `views/library_autores_views.xml`

```xml
<?xml version='1.0' encoding='utf-8'?>
<odoo>
  <data>
    <!-- explicit list view definition -->
    <record model="ir.ui.view" id="library_ing.add_autor">
      <field name="name">Añadir autor</field>
      <field name="model">library_ing.autores</field>
      <field name="arch" type="xml">
        <tree>
          <field name="name"/>
          <field name="phone"/>
          <field name="origin_country"/>
          <field name="author"/>
          <field name="revisor"/>
        </tree>
      </field>
    </record>

    <!-- actions opening views on models -->
    <record model="ir.actions.act_window" id="library_ing.add_autor_action">
      <field name="name">Abrir menú adición autor</field>
      <field name="res_model">library_ing.autores</field>
      <field name="view_mode">tree,form</field>
    </record>
  </data>
</odoo>
```