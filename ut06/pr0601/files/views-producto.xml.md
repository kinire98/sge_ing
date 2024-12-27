# `views/producto.xml`  
```xml
<odoo>
  <data>
    <record model="ir.ui.view" id="gestion_productos.producto">
      <field name="name">Producto</field>
      <field name="model">gestion_productos.producto</field>
      <field name="arch" type="xml">
        <tree>
          <field name="name"/>
          <field name="description"/>
          <field name="code"/>
          <field name="image"/>
          <field name="category"/>
          <field name="destacable"/>
          <field name="price"/>
          <field name="stock"/>
          <field name="creation_date"/>
          <field name="update_date"/>
          <field name="active"/>
          <field name="weight"/>
        </tree>
      </field>
    </record>
    <record model="ir.actions.act_window" id="gestion_productos.action_producto">
      <field name="name">Añadir producto</field>
      <field name="res_model">gestion_productos.producto</field>
      <field name="view_mode">tree,form</field>
    </record>
  </data>
</odoo>
```