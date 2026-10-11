# Config Server - Grupo 5

Proyecto del examen para compartir la configuración de Citas. Los archivos `cita-service-dev.properties` y `cita-service-prod.properties` están aquí mismo. Las claves cifradas son de prueba.

## Ejecutar

Se necesita Java 25 y Maven.

```bash
mvn spring-boot:run
```

El servidor inicia en el puerto 8888. Para comprobar los perfiles y Actuator:

```bash
python3 scripts/validate-config.py
```

También se puede consultar un perfil directamente: `http://localhost:8888/cita-service/dev`.

## Conectar Citas

En `cita-service-grupo5`, usar `spring.application.name=cita-service-grupo5` para Eureka y `spring.cloud.config.name=cita-service` para leer estos archivos. Config Server debe estar iniciado antes que Citas.

Para la sustentación, cambien el copago dev de 50 a 75 en GitHub, hagan commit y push, envíen `POST http://localhost:8081/actuator/refresh` y consulten otra vez `/api/v1/citas/configuracion` por el Gateway.
