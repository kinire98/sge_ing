# `views/menu.xml`  
```xml
<?xml version='1.0' encoding='utf-8'?>
<odoo>
  <data>
    <menuitem name="Gestión de productos" id="gestion_productos.menu_root"/>
    <menuitem name="Producto" id="gestion_productos.menu_producto" parent="gestion_productos.menu_root"/>
    <menuitem name="Añadir" id="gestion_productos.menu_producto_anadir" parent="gestion_productos.menu_producto" 
      action="gestion_productos.action_producto"/>

  </data>
</odoo>
```