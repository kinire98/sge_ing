# `views/library_menu_views.xml`

```xml
<?xml version='1.0' encoding='utf-8'?>
<odoo>
  <data>
<!-- Top menu item -->
    <menuitem name="library_ing" id="library_ing.menu_root"/>
    <!-- menu categories -->
    <menuitem id="library_ing.menu_autores" name="Autores" parent="library_ing.menu_root"/>
    <menuitem id="library_ing.menu_libros" name="Libros" parent="library_ing.menu_root"/>
    <menuitem id="library_ing.menu_socios" name="Socios" parent="library_ing.menu_root"/>
    <menuitem id="library_ing.menu_generos" name="Géneros" parent="library_ing.menu_root"/>
    <!-- actions -->
    <menuitem id="library_ing.add_autor_menuitem" name="Añadir autor" parent="library_ing.menu_autores" action="library_ing.add_autor_action"/>
    <menuitem id="library_ing.add_genero_menuitem" name="Añadir género" parent="library_ing.menu_generos" action="library_ing.add_genero_action"/>
    <menuitem id="library_ing.add_libro_menuitem" name="Añadir libro" parent="library_ing.menu_libros" action="library_ing.add_libro_action"/>
    <menuitem id="library_ing.add_socio_menuitem" name="Añadir socio" parent="library_ing.menu_socios" action="library_ing.add_socio_action"/>

  </data>
</odoo>
```