# Config Server ClinicaCloud

Servidor centralizado de configuración para el grupo 5. El proyecto usa Spring Boot 4.1.1, Spring Cloud 2025.1.3 y Java 25, como solicita la evaluación. Los archivos `cita-service-dev.properties` y `cita-service-prod.properties` están en la raíz de este mismo repositorio, que sirve también como backend Git de Config Server.

Las claves cifradas del repositorio son valores ficticios para la demostración. No corresponden a credenciales reales.

## Requisitos

- JDK 25 y Maven 3.6.3 o superior.
- Acceso de lectura al repositorio privado desde GitHub.

## Variables locales

El Config Server lee el repo privado a través de HTTPS. En una terminal, configura las variables sin guardarlas en archivos versionados:

```bash
export CONFIG_REPO_URI="https://github.com/guallycanazas/config-server-grupo5.git"
export GITHUB_USERNAME="guallycanazas"
export GITHUB_TOKEN="TU_TOKEN_DE_GITHUB_CON_ACCESO_DE_LECTURA"
export ENCRYPT_KEY="CLAVE_COMPARTIDA_DE_LA_PRACTICA"
```

`ENCRYPT_KEY` debe coincidir con la clave acordada para la evaluación; si no se define, el proyecto usa la clave de demostración especificada en el enunciado. Esa clave solo sirve para esta práctica y no debe reutilizarse. `GITHUB_TOKEN` es un personal access token con permiso de lectura a este repositorio. No subas el token ni credenciales reales a Git.

## Iniciar el servidor

```bash
mvn spring-boot:run
```

El Config Server queda disponible en `http://localhost:8888`. Para comprobar que GitHub sirve los perfiles dev/prod, las claves demo se desencriptan y Actuator responde, ejecuta en otra terminal: `python3 scripts/validate-config.py`. Para consultar manualmente el perfil dev:

```bash
curl http://localhost:8888/cita-service/dev
```

El endpoint `/encrypt` recibe texto plano y devuelve ciphertext. Ejemplo para generar una nueva clave de demostración:

```bash
curl --silent --request POST \
  --header 'Content-Type: text/plain' \
  --data-binary 'demo-api-key-dev-grupo5' \
  http://localhost:8888/encrypt
```

Guarda la respuesta como `{cipher}<respuesta>` en el archivo correspondiente y sube el cambio. No cifres ni publiques credenciales reales para este examen.

## Integración con cita-service-grupo5

El enunciado pide los archivos `cita-service-dev.properties` y `cita-service-prod.properties`, aunque el nombre de registro del microservicio es `cita-service-grupo5`. En el cliente Citas, conserva `spring.application.name=cita-service-grupo5` para Eureka y configura `spring.cloud.config.name=cita-service` para solicitar estos archivos. Con el perfil `dev`, la URL consultada por el cliente será `http://localhost:8888/cita-service/dev`.

La recarga dinámica se implementa en `cita-service-grupo5` (Actuator, `@RefreshScope` y `POST /actuator/refresh`), no en este servidor. Después de actualizar el archivo en GitHub, la petición de refresh debe dirigirse al puerto del servicio Citas (8081).
