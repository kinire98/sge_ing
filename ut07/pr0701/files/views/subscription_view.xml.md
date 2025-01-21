# views/subscription_view.xml
```xml
<odoo>
   <template id="subscription_list" name="Lista de subscripciones">
     <t t-call="web.html_container">
       <style>
         .sub-div {
          margin-block: 5vh;
         }
       </style>
       <div id="container">
        <h1>Subscripciones</h1>
        <t t-foreach="subs" t-as="sub">
          <div class="sub-div">
           <h2>Nombre de la subscripción: <t t-esc="sub.name"/></h2>
           <span>Codigo de la subscripción: <t t-esc="sub.subscription_code"/></span>
          </div> 
        </t>
       </div>
     </t>
   </template>
</odoo>
```