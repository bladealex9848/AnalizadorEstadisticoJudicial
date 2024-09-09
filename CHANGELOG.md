# Registro de Cambios - AnalizadorEstadisticoJudicial

Todos los cambios notables en el proyecto AnalizadorEstadisticoJudicial serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto se adhiere a [Versionado Semántico](https://semver.org/lang/es/).

# Registro de Cambios

## [1.5.0] - 2024-09-08
### Añadido
- Soporte mejorado para archivos .xls y .xlsx utilizando pandas
- Nuevas instrucciones de instalación de dependencias en la interfaz de usuario

### Cambiado
- Refactorización de la función `process_excel_files` para mejor manejo de diferentes formatos de Excel
- Actualización de las dependencias del proyecto para resolver conflictos de versiones

### Corregido
- Solucionado el problema de compatibilidad con archivos .xls
- Mejorado el manejo de errores durante el procesamiento de archivos


[1.5.0]: https://github.com/tuusuario/AnalizadorEstadisticoJudicial/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.com/tuusuario/AnalizadorEstadisticoJudicial/compare/v1.3.0...v1.4.0

## [1.4.0] - 2024-09-08
### Añadido
- Implementación de un conjunto completo de pruebas unitarias.
- Nuevo archivo `test_AnalizadorEstadisticoJudicial.py` en el directorio `tests/`.

### Cambiado
- Actualización del README.md con instrucciones para ejecutar las pruebas unitarias.
- Refactorización menor del código principal para mejorar la testabilidad.

### Mejorado
- Aumento de la cobertura de código con pruebas para todas las funcionalidades principales.
- Implementación de mocks para simular la lectura y escritura de archivos Excel en las pruebas.

[1.4.0]: https://github.com/tuusuario/AnalizadorEstadisticoJudicial/compare/v1.3.0...v1.4.0

## [1.3.0] - 2024-09-08
### Cambiado
- Mejorado el proceso de selección de agentes con la implementación de `get_prioritized_agents` en `AgentManager`.
- Refinado el método `process_query` en `AgentManager` para un mejor manejo de errores y fallbacks.
- Actualizada la lógica de `process_user_input` en `main.py` para utilizar el nuevo sistema de priorización de agentes.

### Optimizado
- Mejorada la generación de respuestas finales para ser más conversacionales y directas.
- Refinado el proceso de meta-análisis para producir respuestas más coherentes y relevantes.

### Corregido
- Solucionado el problema con el atributo faltante `default_local_model` en `AgentManager`.
- Implementado el método faltante `get_available_models` en `AgentManager`.

### Añadido
- Nueva funcionalidad para manejar fallbacks de manera más robusta en caso de fallo de agentes primarios.
- Implementada una lógica mejorada para la selección de agentes basada en la complejidad de la consulta y la disponibilidad de modelos.

### Mejorado
- Optimizada la gestión de errores en todo el sistema para una mejor experiencia de usuario y depuración.
- Mejorada la documentación interna del código para facilitar futuro mantenimiento y desarrollo.

## [1.2.0] - 2024-07-05
### Añadido
- Implementación de capacitación al personal en el uso del nuevo programa y en la interpretación de los resultados.
- Desarrollo de un manual de usuario detallado para facilitar el uso del programa.

### Mejorado
- Refinamiento de la interfaz de usuario basado en la retroalimentación del personal capacitado.
- Optimización del rendimiento para manejar volúmenes más grandes de datos.

## [1.1.0] - 2024-06-28
### Añadido
- Implementación en producción del programa para procesar datos actuales.
- Integración con los sistemas existentes del Consejo Seccional de la Judicatura de Sucre.

### Mejorado
- Ajustes finales basados en los resultados de las pruebas piloto.
- Optimización del proceso de generación de informes consolidados.

## [1.0.0] - 2024-06-17
### Añadido
- Finalización de las pruebas piloto con datos históricos de 2023.
- Validación completa de la precisión y eficiencia del programa.

### Cambiado
- Ajustes en el procesamiento de datos basados en los resultados de las pruebas piloto.
- Refinamiento de los algoritmos de análisis estadístico.

## [0.9.0] - 2024-05-24
### Añadido
- Completado el desarrollo del código fuente principal.
- Implementación de todas las funcionalidades core del analizador estadístico.

### Mejorado
- Optimización del rendimiento en el procesamiento de grandes volúmenes de datos.
- Mejora en la precisión de los cálculos estadísticos.

## [0.8.0] - 2024-05-14
### Añadido
- Implementación de controles de calidad y manejo de errores en el programa.
- Desarrollo de un sistema robusto de logging para seguimiento y auditoría.

### Mejorado
- Refinamiento de la lógica de procesamiento de hojas de Excel.
- Mejora en la detección y manejo de anomalías en los datos de entrada.

## [0.7.0] - 2024-04-29
### Añadido
- Desarrollo de la capacidad de generar archivos de resultados individuales.
- Implementación de la funcionalidad para crear un archivo consolidado con todos los resultados.

### Mejorado
- Optimización del proceso de consolidación de datos de múltiples fuentes.

## [0.6.0] - 2024-04-12
### Añadido
- Implementación de la funcionalidad de procesamiento de cada hoja de los archivos Excel.
- Desarrollo de algoritmos para el análisis estadístico de los datos judiciales.

### Mejorado
- Refinamiento de la lógica de extracción de datos relevantes de las hojas de Excel.

## [0.5.0] - 2024-03-14
### Añadido
- Configuración del programa para leer automáticamente archivos Excel con datos trimestrales.
- Implementación de la lógica básica para la identificación y lectura de archivos relevantes.

### Mejorado
- Optimización del proceso de carga y validación de archivos Excel.

## [0.4.0] - 2024-02-29
### Añadido
- Inicio del desarrollo del código fuente del AnalizadorEstadisticoJudicial.
- Implementación de la estructura básica del programa y funciones core.

## [0.3.0] - 2024-02-14
### Añadido
- Finalización del diseño de la arquitectura del sistema.
- Creación del documento de diseño detallado.

### Cambiado
- Refinamiento de los requisitos basados en el feedback del equipo de desarrollo.

## [0.2.0] - 2024-02-07
### Añadido
- Inicio del diseño de la arquitectura del sistema AnalizadorEstadisticoJudicial.
- Definición de los componentes principales y su interacción.

## [0.1.0] - 2024-02-01
### Añadido
- Inicio del proyecto AnalizadorEstadisticoJudicial.
- Definición inicial de requisitos y alcance del proyecto.
- Creación del repositorio y estructura básica del proyecto.

[1.3.0]: https://github.com/tuusuario/AnalizadorEstadisticoJudicial/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/tuusuario/AnalizadorEstadisticoJudicial/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/tuusuario/AnalizadorEstadisticoJudicial/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/tuusuario/AnalizadorEstadisticoJudicial/compare/v0.9.0...v1.0.0
[0.9.0]: https://github.com/tuusuario/AnalizadorEstadisticoJudicial/compare/v0.8.0...v0.9.0
[0.8.0]: https://github.com/tuusuario/AnalizadorEstadisticoJudicial/compare/v0.7.0...v0.8.0
[0.7.0]: https://github.com/tuusuario/AnalizadorEstadisticoJudicial/compare/v0.6.0...v0.7oires/compare/v0.6.0
[0.6.0]: https://github.com/tuusuario/AnalizadorEstadisticoJudicial/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/tuusuario/AnalizadorEstadisticoJudicial/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/tuusuario/AnalizadorEstadisticoJudicial/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/tuusuario/AnalizadorEstadisticoJudicial/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/tuusuario/AnalizadorEstadisticoJudicial/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/tuusuario/AnalizadorEstadisticoJudicial/releases/tag/v0.1.0