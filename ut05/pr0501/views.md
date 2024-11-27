# views/views.xml
```xml
<odoo>
  <data>
    <!-- explicit list view definition -->
    <record model="ir.ui.view" id="gestion_salas.list">
      <field name="name">gestion_salas list</field>
      <field name="model">gestion_salas.salas</field>
      <field name="arch" type="xml">
        <tree>
          <field name="nombre"/>
          <field name="capacidad"/>
          <field name="fecha_reserva"/>
          <field name="reservada" widget="boolean_toogle"/>
          <field name="comentarios"/>
        </tree>
      </field>
    </record>

    <!-- actions opening views on models -->
    <record model="ir.actions.act_window" id="gestion_salas.open_salas">
      <field name="name">gestion_salas window</field>
      <field name="res_model">gestion_salas.salas</field>
      <field name="view_mode">tree,form</field>
    </record>

    <!-- server action to the one above -->
<!--
    <record model="ir.actions.server" id="gestion_salas.action_server">
      <field name="name">gestion_salas server</field>
      <field name="model_id" ref="model_gestion_salas_gestion_salas"/>
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

    <!-- Top menu item -->
    <menuitem name="gestion_salas" id="gestion_salas.menu_root"/>
    <!-- menu categories -->
    <menuitem name="Salas" id="gestion_salas.salas" parent="gestion_salas.menu_root"/>
    <menuitem name="Reservas" id="gestion_salas.reservas" parent="gestion_salas.menu_root"/>
    <!-- actions -->
    <menuitem name="Salas" id="gestion_salas.menu_1_list" parent="gestion_salas.salas"
              action="gestion_salas.open_salas"/>
  </data>
</odoo>
```