# `views/menu.xml`

```xml
<?xml version='1.0' encoding='utf-8'?>
<odoo>
  <data>
    <!-- Top menu item -->
    <menuitem name="modulo_biblioteca" id="modulo_biblioteca.menu_root"/>
    <!-- menu categories -->
    <menuitem name="Biblioteca" id="modulo_biblioteca.biblioteca" parent="modulo_biblioteca.menu_root"/>
    <menuitem id="modulo_biblioteca.autor_menu" name="autor" parent="modulo_biblioteca.biblioteca"/>
    <menuitem id="modulo_biblioteca.libro_menu" name="Libro" parent="modulo_biblioteca.biblioteca"/>

    <menuitem name="Añadir" id="modulo_biblioteca.anadir_autor" parent="modulo_biblioteca.autor_menu" action="modulo_biblioteca.action_autor"/>
    <menuitem name="Añadir" id="modulo_biblioteca.anadir_libro" parent="modulo_biblioteca.libro_menu" action="modulo_biblioteca.action_libro"/>
  </data>
</odoo>
```