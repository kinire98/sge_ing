# `views/menu.xml`

```xml
<?xml version='1.0' encoding='utf-8'?>
<odoo>
    <data>
      
    <!-- Top menu item -->
    <menuitem name="Administración de stock" id="stock_management.menu_root"/>
    <!-- menu categories -->
    <menuitem name="Producto" id="stock_management.menu_product" parent="stock_management.menu_root"/>
    <!-- actions -->
    <menuitem name="Añadir producto" id="stock_management.menu_action_producto" parent="stock_management.menu_product"
              action="stock_management.product_action_window"/>
    </data>
</odoo>
```
