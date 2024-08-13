
# Check-in Empresarial

Requisitos:
Para ejecutar esta aplicación, solo necesitas tener Docker instalado en tu sistema.

Instalación

1. **Clona el Repositorio**

   Clona el repositorio en tu máquina local:

   ```bash
   git clone https://github.com/edgar118/-business_check-in.git
   cd business_check-in

2. Construye la Imagen Docker

    Utiliza el siguiente comando para construir la imagen Docker:
    ```bash
    docker up --build
    ```
    
    Esto instalara las librerias requeridas y iniciará la aplicación.


3. **Endpoints**

    La aplicación expone varios endpoints que puedes utilizar:
    
    GET /api/v1/users: Obtiene una lista de usuarios con filtros opcionales.
    
    PUT /api/v1/users/{id}: Actualiza un usuario existente por ID.
    
    POST /api/v1/user/entry: Registra la entrada de un usuario.
    
    POST /api/v1/user/exit: Registra la salida de un usuario.
    
    Para una vista detalla de los diferentes endpoints puedes acceder a la documentacion de swagger 
    
    http://localhost:8000/docs
