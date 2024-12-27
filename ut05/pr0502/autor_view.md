# `views/autor_view.xml`

```xml
<?xml version='1.0' encoding='utf-8'?>
<odoo>
  <data>
    <record model="ir.ui.view" id="modulo_biblioteca.autor">
      <field name="name">Autor</field>
      <field name="model">modulo_biblioteca.autor</field>
      <field name="arch" type="xml">
        <tree>
          <field name="nombre"/>
          <field name="fecha_nac"/>
          <field name="biografia"/>
          <field name="libros"/>
        </tree>
      </field>
    </record>
    <record model="ir.actions.act_window" id="modulo_biblioteca.action_autor">
      <field name="name">Añadir autor</field>
      <field name="res_model">modulo_biblioteca.autor</field>
      <field name="view_mode">tree,form</field>
    </record>
  </data>
</odoo>
```