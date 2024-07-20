# Django Online Shop

Este es el tercer proyecto del libro *Django 5 By Example: Build powerful and reliable Python web applications from scratch (English Edition)*. Este proyecto abarca los siguientes capítulos y alcances:

## Capítulos del Libro

### Capítulo 8: Construyendo una Tienda en Línea
Explora cómo crear una tienda en línea. Construirás modelos para un catálogo de productos y crearás un carrito de compras usando sesiones de Django. Construirás un procesador de contexto para el carrito de compras y aprenderás a gestionar los pedidos de los clientes. El capítulo te enseñará cómo enviar notificaciones asincrónicas usando Celery y RabbitMQ. También aprenderás a monitorear Celery usando Flower.

### Capítulo 9: Gestionando Pagos y Pedidos
Explica cómo integrar una pasarela de pago en tu tienda. Integrarás Stripe Checkout y recibirás notificaciones de pago asincrónicas en tu aplicación. Implementarás vistas personalizadas en el sitio de administración y también personalizarás el sitio de administración para exportar pedidos a archivos CSV. Además, aprenderás a generar facturas en PDF de forma dinámica.

### Capítulo 10: Ampliando tu Tienda
Te enseñará cómo crear un sistema de cupones para aplicar descuentos al carrito de compras. Actualizarás la integración de Stripe Checkout para implementar descuentos de cupones y aplicarás cupones a los pedidos. Utilizarás Redis para almacenar productos que suelen comprarse juntos, y usarás esta información para construir un motor de recomendación de productos.

### Capítulo 11: Añadiendo Internacionalización a tu Tienda
Te mostrará cómo añadir internacionalización a tu proyecto. Aprenderás cómo generar y gestionar archivos de traducción y traducir cadenas en código Python y plantillas de Django. Utilizarás Rosetta para gestionar traducciones e implementar URLs por idioma. Aprenderás a traducir campos de modelos usando `django-parler` y cómo usar traducciones con el ORM. Finalmente, crearás un campo de formulario localizado usando `django-localflavor`.


```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13.1-management
```

```bash