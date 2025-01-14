```xml
<?xml version='1.0' encoding='utf-8'?>
<odoo>
    <data>

    <!-- Top menu item -->
    <menuitem name="Subscripciones" id="subscription.menu_root"/>
    <!-- menu categories -->
    <menuitem name="Subscripción" id="subscription.menu_subscription" parent="subscription.menu_root"/>
    <!-- actions -->
    <menuitem name="Básico" id="subscription.menu_subscription_basic_list" parent="subscription.menu_subscription"
              action="subscription.action_basic_list"/>
    <menuitem name="Uso" id="subscription.menu_subscription_usage_list" parent="subscription.menu_subscription"
              action="subscription.action_usage_list"/>
      
    </data>
</odoo>
```