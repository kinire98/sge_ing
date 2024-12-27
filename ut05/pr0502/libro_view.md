# `views/libro_view.xml`

```xml
<?xml version='1.0' encoding='utf-8'?>
<odoo>
  <data>
    <record model="ir.ui.view" id="modulo_biblioteca.libro">
      <field name="name">Libro</field>
      <field name="model">modulo_biblioteca.libro</field>
      <field name="arch" type="xml">
        <tree>
          <field name="nombre"/> 
          <field name="autor"/>
          <field name="fecha_nac"/>
          <field name="sinopsis"/>
          <field name="ISBN"/>
        </tree>
      </field>
    </record>
    <record model="ir.actions.act_window" id="modulo_biblioteca.action_libro">
      <field name="name">Añadir libro</field>
      <field name="res_model">modulo_biblioteca.libro</field>
      <field name="view_mode">tree,form</field>
    </record>
  </data>
</odoo>
```