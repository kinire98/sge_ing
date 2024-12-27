# `views/library_generos_views.xml`

```xml
<?xml version='1.0' encoding='utf-8'?>
<odoo>
  <data>
    <!-- explicit list view definition -->
    <record model="ir.ui.view" id="library_ing.add_genero">
      <field name="name">Añadir libro</field>
      <field name="model">library_ing.generos</field>
      <field name="arch" type="xml">
        <tree>
          <field name="name"/>
        </tree>
      </field>
    </record>

    <!-- actions opening views on models -->
    <record model="ir.actions.act_window" id="library_ing.add_genero_action">
      <field name="name">Abrir menú adición género</field>
      <field name="res_model">library_ing.generos</field>
      <field name="view_mode">tree,form</field>
    </record>
  </data>
</odoo>
```