# Pasos
1. Instalamos y activamos el módulo de facturación en Odoo. Para ello en la pantalla de `Aplicaciones` buscamos `Facturación` y pinchamos en `Activar`. Una vez presionado este botón se cargará el módulo. Tardará un poco en instalar.  
2. Después de este paso, se nos abrirá el módulo de `Conversaciones` (cuyo propósito es la comunicación entre los usuarios), el cual se instaló con el módulo de facturación. Para ir a la aplicación de facturación, pinchamos en el icono de cuadrícula 3x3 de la esquina superior izquierda. Se abrirá un menú. Pincha en `Facturación/Contabilidad`.  
3. Cómo no hay ninguna empresa creada, Odoo nos dará un pequeño tutorial de cómo crear la empresa. Habrá una pequeña flecha moviéndose debajo de un botón que pone `¡Empecemos!` en el recuadro `Información de compañía`. Pincha en el bóton.  
4. Se abrirá una ventana emergente dónde nos preguntará por:
	- `Contacto`: Nombre de la compañía
	- `Dirección`: Dirección de facturación de la compañía
	- `Tax ID`: NIF de la empresa
	- `ID de la compañía`: El número de registro de la empresa. Solo se debe utilizar si es distinto del NIF
	- `Moneda`: La moneda principal en la que opera la empresa
	- `Phone`: Número de teléfono fijo de la empresa
	- `Móvil`: Número de teléfono móvil de la empresa
	- `Email`: Correo electrónico de la empresa
	- `Sitio web`: Página web de la empresa
	- `Favicon de la Compañía`: Logo de la compañía.
	Una vez rellenados estos datos (para el campo `Contacto` si pinchas en él te llevará a otra ventana. Llena ahí los datos, pincha en `Nuevo`, vuelve a la pantalla principal de `Facturación/Contabilidad` y vuelve a darle a `¡Empecemos!`. Estarán todos los datos rellenados, excepto el `Favicon de la Compañía`), pinchamos en `Aplicar`.  
5. Ahora vamos a Personalizar el diseño de la factura. Ahora la flecha que antes estaba en `Información de compañía` ahora estará en el apartado `Diseño de Factura` debajo del botón `Personalizar`. Pincha en ese botón.  
   Se abre un cuadro dónde nos dejará personalizar la factura (aparecerá una vista previa a la derecha de las opciones de personalización):  
   - `Diseño`: Tenemos cuatro distintos para elegir:
	   - `Light`: sencillo y sobrio
	   - `Boxed`: cuadriculado y partes fácilmente distinguibles
	   - `Bold`: más sobrio que el anterior y con letra en negrita
	   - `Striped`: distintos productos de la factura más fácilmente distinguibles
   -  `Fuente`: La fuente que se va a utilizar en la factura. Hay 7 disponibles: `Lato`, `Roboto`, `Open Sans`, `Montserrat`,  `Oswald`, `Raleway` y `Tajawal`.
   - `Logotipo de la empresa`: El logo de la empresa. Se pondrá en la factura. El que escogiste a la hora de crear la empresa.
   - `Colores`: Los colores a utilizar en la factura. Se escogerán automáticamente teniendo en cuenta el logo utilizado. Sin embargo, puedes personalizarlos al gusto.
   - `Fondo de diseño`: El fondo de la factura:
	  - `Vacío`: sin fondo
	  - `Geométrica`: formas geométricas suaves de fondo
	  - `Personalizado`: escoge tu propia imagen para el fondo de las facturas
   -  `Lema de la compañía`
   - `Detalles de la compañía`: Ya vendrán rellenados con los datos de la empresa escritos en el paso anterior.
   - `Pie de página`: Aquí se pondrán los datos de contacto de la compañía de forma automática según lo que pusiéramos cuando creamos la empresa
   - `Formato de papel`: Formato para la impresión. `A4`, `US Letter` o `US Batch Deposit`.
   
   Selecciona las opciones que quieras y pincha en `Guardar`.  
6. Ahora vamos a crear la primera factura. La flecha se habrá cambiado al apartado `Crear factura`, debajo del botón `Crear`. Si pinchamos en ese botón de primeras nos saldrá el siguiente mensaje:  
      `No se pudo encontrar ningun diario en la empresa ING Computers para ninguno de esos tipos: sale`  
    Para poder crear una factura primero tendremos que añadir un paquete de localización fiscal. Para ellos pinchamos en el cuadro 3x3 y vamos a `Ajustes` > `Facturación/Contabilidad`>`Localización fiscal`>`Instalar más paquetes`. (Este último paso es por si no tenemos el paquete para España instalado. Si así es sáltate esa parte). En esta sección selecciona el paquete de tu país, en mi caso España. Una vez instalado seleccionaré la opción `PGCE PYMEs 2008`.  
 7. Para importar algunos clientes de prueba antes de generar la factura vamos a la sección `Clientes` > `Clientes`. Pincha en `Favoritos` > `Importar resgistros`.  Arriba a la izquierda encontrarás un botón que pone `Subir archivo`. Pincha en él y selecciona un archivo csv o xslx válidos para importar los clientes. Si está bien hecho te saltarán varias filas con unos desplegables. La opción de la izquierda es la columna del archivo es inmutable. Justo al lado tenemos que seleccionar uno de los campos de Odoo. Si están repetidos se concatenarán. Puedes poner un comentario al lado. Pincha en `Importar` para importar los clientes.  
 8. Ahora volvemos a `Facturación/Contabilidad` y pinchamos el botón `Crear` en `Crear factura`. Nos llevará a una nueva ventana dónde podremos llenar los datos de la factura:  
	 - `Factura de cliente`: Identificador único de la factura
	 - `Cliente`: Cliente que abonará la factura
	 - `Fecha de factura`
	 - `Referencia de pago`
	 - `Condiciones de pago`: Condiciones en las que se realizará el pago, es decir, en 3 días, 4, a final de mes, al final del siguiente mes, etc. 
	 - `Líneas de factura`: Añade distintos productos a la factura:
		 - `Producto`: Nombre del producto
		 - `Etiqueta`: Sección o grupo al que pertenece el producto
		 - `Cantidad`
		 - `Precio`: Precio unitario del producto
		 - `Impuestos`: Tipo de impuestos a los que está sujeto.
		 - `Subtotal`: Total de ese producto en concreto multiplicado por la cantidad
	
    Una vez añadidos los productos pincha el botón `Confirmar` al lado del cual se habrá movido la flecha morada.  
    Para poder descargarla pincha en `Enviar e Imprimir`. Saltará una ventana en la que te dirá que registres al cliente en el ERP, si no has seleccionado uno de los importados, añade el correo y guárdalo.  
    Saltará una ventana, dónde nos dará la posibilidad de imprimir la factura, enviarla por correo postal o por correo electrónico. Yo solo seleccionaré la opción de `Imprimir`, ya que solo quiero descargarla.  
    Una vez hecho esto se abrirá una ventana nueva con la factura y, si no se ha descargado automáticamente, la descargamos y ya tendremos nuestra factura de prueba.  
[Enlace a la factura](./INV_2024_00001-1.pdf)