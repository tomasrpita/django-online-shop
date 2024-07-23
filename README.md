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

## Puesta en Marcha

### Prerrequisitos

Asegúrate de tener Docker y Docker Compose instalados en tu sistema.

### Instalación de Dependencias

1. **Clonar el repositorio:**

    ```sh
    git clone https://github.com/tomasrpita/django-online-shop.git
    cd django-online-shop
    ```

2. **Crear un entorno virtual e instalar las dependencias de Python:**

    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Crear el archivo `.env` a partir del archivo de plantilla `.env.template`:**

    ```sh
    cp .env.template .env
    ```

4. **Rellenar las variables de entorno en el archivo `.env`:**

    ```plaintext
    # Email
    EMAIL_HOST=smtp.example.com
    EMAIL_HOST_USER=your-email@example.com
    EMAIL_HOST_PASSWORD=your-email-password
    EMAIL_PORT=587
    DEFAULT_FROM_EMAIL=your-email@example.com

    # RabbitMQ
    RABBITMQ_USER=your_rabbitmq_user
    RABBITMQ_PASSWORD=your_rabbitmq_password

    # Stripe
    STRIPE_PUBLISHABLE_KEY=pk_test_XXXX
    STRIPE_SECRET_KEY=sk_test_XXXX
    STRIPE_WEBHOOK_SECRET=whsec_XXXX
    ```

### Configuración de Docker

1. **Iniciar los servicios con Docker Compose:**

    ```sh
    docker-compose up -d
    ```

### Configuración de la Aplicación Django

1. **Ejecutar las migraciones de la base de datos:**

    ```sh
    python ./myshop/manage.py migrate
    ```

2. **Crear un superusuario:**

    ```sh
    python ./myshop/manage.py createsuperuser
    ```

3. **Cargar datos iniciales (si aplica):**

    ```sh
    python ./myshop/manage.py loaddata initial_data.json
    ```

### Ejecutar Celery y Flower

1. **Iniciar el worker de Celery:**

    ```sh
    celery -A myshop worker -l info
    ```

2. **Iniciar Flower para monitorear Celery:**

    ```sh
    celery -A myshop flower --basic-auth=your_user:your_password
    ```

### Iniciar el Servidor de Desarrollo

1. **Iniciar el servidor de desarrollo de Django:**

    ```sh
    python ./myshop/manage.py runserver 0.0.0.0:8000
    ```

### Acceso a la Aplicación

- La aplicación estará disponible en `http://localhost:8000`.
- La interfaz de administración de Django estará en `http://localhost:8000/admin`.

