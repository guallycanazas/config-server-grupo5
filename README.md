# Config Server ClinicaCloud

Servidor centralizado de configuración para los servicios de ClinicaCloud. Usa Spring Boot 4.1.1, Spring Cloud 2025.1.3 y Java 25, según la evaluación.

## Configuración local

Este repositorio privado también puede actuar como repositorio Git de propiedades para Config Server. Define estas variables antes de iniciar la aplicación:

```bash
export CONFIG_REPO_URI="https://github.com/guallycanazas/config-server-grupo5.git"
export GITHUB_USERNAME="guallycanazas"
export GITHUB_TOKEN="TU_TOKEN_DE_GITHUB"
export ENCRYPT_KEY="ClaveSecretaSalud2026"
```

`GITHUB_TOKEN` debe tener acceso de lectura al repositorio. No guardes el token ni la clave en archivos versionados. Para la evaluación, todos los microservicios que lean secretos cifrados deben usar la misma `ENCRYPT_KEY`.

## Iniciar

```bash
mvn spring-boot:run
```

El servidor escucha en `http://localhost:8888`. La configuración se consulta en `/{application}/{profile}`; por ejemplo, `http://localhost:8888/cita-service-grupo5/dev`.

## Encriptar valores

Con el servidor iniciado, envía el valor al endpoint `/encrypt` y guarda la respuesta en el archivo de propiedades con el prefijo `{cipher}`. No subas credenciales reales en texto plano.
