# Config Server ClinicaCloud

Servidor centralizado de configuración para los servicios de ClinicaCloud. Usa Spring Boot 4.1.1, Spring Cloud 2025.1.3 y Java 25, según la evaluación.

## Configuración local

Define las variables de entorno antes de iniciar la aplicación:

```bash
export CONFIG_REPO_URI="https://github.com/USUARIO/REPOSITORIO-CONFIG.git"
export ENCRYPT_KEY="ClaveSecretaSalud2026"
```

La clave se lee desde el entorno y no se guarda en este repositorio. Para la evaluación, coordina que los microservicios usen la misma clave.

## Iniciar

```bash
mvn spring-boot:run
```

El servidor escucha en `http://localhost:8888`. La configuración del repositorio Git se consulta en `/{application}/{profile}`; por ejemplo:

```text
http://localhost:8888/cita-service-grupo5/dev
```

## Encriptar valores

Con el servidor iniciado, se puede enviar un secreto al endpoint `/encrypt` y guardar el resultado en el repositorio de configuración con el prefijo `{cipher}`. No subas credenciales reales en texto plano.
