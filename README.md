![Logo de AnalizadorEstadisticoJudicial](https://raw.githubusercontent.com/bladealex9848/AnalizadorEstadisticoJudicial/main/assets/logo.jpg)

# AnalizadorEstadisticoJudicial

## Tabla de Contenidos
1. [Descripción](#descripción)
2. [Características Principales](#características-principales)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Requisitos Previos](#requisitos-previos)
5. [Instalación](#instalación)
6. [Configuración](#configuración)
7. [Uso](#uso)
8. [Arquitectura del Sistema](#arquitectura-del-sistema)
9. [Componentes Principales](#componentes-principales)
10. [Flujo de Trabajo](#flujo-de-trabajo)
11. [Manejo de Errores y Logging](#manejo-de-errores-y-logging)
12. [Optimización y Rendimiento](#optimización-y-rendimiento)
13. [Pruebas](#pruebas)
14. [Contribución](#contribución)
15. [Registro de Cambios](#registro-de-cambios)
16. [Roadmap](#roadmap)
17. [Licencia](#licencia)
18. [Créditos](#créditos)

## Descripción

AnalizadorEstadisticoJudicial es un programa diseñado para automatizar el análisis de archivos Excel relacionados con la organización del trabajo y la eficiencia en la Judicatura. Este sistema procesa automáticamente los datos y genera un consolidado, facilitando significativamente la tarea de análisis y presentación de informes estadísticos judiciales.

El programa busca y procesa archivos Excel con nombres específicos (por ejemplo, 'Primer Trimestre.xls', 'Segundo Trimestre.xls', etc.), incluyendo aquellos con sufijos numéricos como 'Tercer Trimestre_1.xls'. Esto permite manejar múltiples archivos para un trimestre específico. Cada hoja de estos archivos es procesada y finalmente se genera un archivo consolidado con todos los resultados.

## Características Principales

- Procesamiento automático de archivos Excel trimestrales
- Generación de archivos de resultados individuales por cada archivo Excel
- Creación de un archivo consolidado con todos los resultados
- Manejo de múltiples archivos por trimestre
- Sistema robusto de logging para seguimiento y auditoría
- Interfaz de línea de comandos intuitiva
- Optimización para el procesamiento eficiente de grandes volúmenes de datos

## Estructura del Proyecto

```
AnalizadorEstadisticoJudicial/
│
├── AnalizadorEstadisticoJudicial.py  # Script principal
├── README.md                         # Este archivo
├── requirements.txt                  # Dependencias del proyecto
├── log.txt                           # Archivo de registro
│
├── Consolidado/                      # Directorio para resultados
│   └── YYYY-MM-DD_HH-MM-SS/          # Subdirectorio con marca de tiempo
│       ├── Primer Trimestre_results.xlsx
│       ├── Segundo Trimestre_results.xlsx
│       ├── Tercer Trimestre_results.xlsx
│       ├── Cuarto Trimestre_results.xlsx
│       └── Consolidado.xlsx
│
└── tests/                            # Directorio para pruebas unitarias
└── assets/                           # Directorio para recursos estáticos
```

## Requisitos Previos

- Python 3.8+
- Bibliotecas de Python: pandas, openpyxl, rich
- Archivos Excel de datos trimestrales en el mismo directorio que el script

## Instalación

1. Clone el repositorio:
   ```
   git clone https://github.com/bladalex9848/AnalizadorEstadisticoJudicial.git
   cd AnalizadorEstadisticoJudicial
   ```

2. Instale las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Configuración

No se requiere configuración adicional. Asegúrese de que los archivos Excel que desea analizar estén en el mismo directorio que el script principal.

## Uso

Hay dos formas principales de utilizar el AnalizadorEstadisticoJudicial:

### 1. Ejecución del script Python

Si tiene Python instalado y prefiere ejecutar el script directamente:

1. Asegúrese de que los archivos Excel trimestrales estén en el mismo directorio que el script.
2. Abra una terminal o línea de comandos.
3. Navegue hasta el directorio donde se encuentra el script.
4. Ejecute el siguiente comando:
   ```
   python AnalizadorEstadisticoJudicial.py
   ```
5. El programa procesará automáticamente los archivos y creará una carpeta 'Consolidado' con los resultados en el mismo directorio.

### 2. Uso del archivo ejecutable

Para usuarios que prefieren no trabajar con Python directamente, ofrecemos un archivo ejecutable:

1. Descargue 'AnalizadorEstadisticoJudicial v1.1.exe' desde la carpeta 'assets' del repositorio.
2. Tiene dos opciones para la ubicación de los archivos Excel a procesar:
   a) Coloque el ejecutable en la misma carpeta donde están los archivos Excel trimestrales.
   b) Cree una carpeta llamada 'PROCESAR' en la raíz de la unidad C (C:\PROCESAR) y coloque allí los archivos Excel.
3. Haga doble clic en 'AnalizadorEstadisticoJudicial v1.1.exe' para ejecutarlo.
4. El programa buscará automáticamente los archivos Excel en la carpeta actual o en C:\PROCESAR, los procesará y creará una carpeta 'Consolidado' con los resultados.

### Notas importantes:

- Asegúrese de que los archivos Excel sigan el formato de nomenclatura esperado (por ejemplo, 'Primer Trimestre.xls', 'Segundo Trimestre.xls', etc.).
- El programa también maneja archivos con sufijos numéricos como 'Tercer Trimestre_1.xls' para múltiples archivos del mismo trimestre.
- Después de la ejecución, revise la carpeta 'Consolidado' para encontrar:
  - Archivos de resultados individuales para cada archivo Excel procesado.
  - Un archivo 'Consolidado.xlsx' que combina todos los resultados.
- Se generará un archivo 'log.txt' en la misma ubicación que el ejecutable o script, que contiene detalles sobre el proceso de ejecución y cualquier error encontrado.

### Recomendaciones:

- Antes de procesar los archivos reales, realice una prueba con copias de sus archivos Excel para familiarizarse con el proceso y los resultados.
- Revise el archivo 'log.txt' después de cada ejecución para verificar que no haya habido errores o advertencias importantes.
- Mantenga una copia de seguridad de sus archivos Excel originales antes de procesarlos.

## Arquitectura del Sistema

AnalizadorEstadisticoJudicial utiliza una arquitectura modular para procesar los datos:

1. Módulo de Lectura de Archivos: Lee y valida los archivos Excel de entrada.
2. Módulo de Procesamiento de Hojas: Analiza cada hoja de los archivos Excel.
3. Módulo de Generación de Resultados: Crea archivos de resultados individuales.
4. Módulo de Consolidación: Combina los resultados en un archivo consolidado.
5. Sistema de Logging: Registra todas las operaciones y errores.

## Componentes Principales

- `create_info_table()`: Genera una tabla informativa sobre el programa.
- `process_excel_files()`: Procesa los archivos Excel y genera resultados individuales.
- `create_consolidated_file()`: Crea el archivo consolidado final.
- `sort_key_func()` y `sorted_files()`: Funciones para ordenar los archivos de manera lógica.

## Flujo de Trabajo

1. El programa inicia y muestra información sobre su versión y propósito.
2. Se crea la estructura de carpetas para los resultados.
3. Se buscan y ordenan los archivos Excel en el directorio.
4. Cada archivo se procesa, generando un archivo de resultados individual.
5. Se consolidan todos los resultados en un archivo final.
6. Se registran todas las operaciones en el archivo de log.

## Manejo de Errores y Logging

- Se utiliza un sistema de logging detallado que registra cada operación en `log.txt`.
- Los errores se manejan con bloques try-except y se registran tanto en el log como en la consola.
- Se utilizan advertencias para notificar sobre problemas no críticos durante el procesamiento.

## Optimización y Rendimiento

- El programa utiliza pandas para el procesamiento eficiente de datos.
- Se implementa un sistema de caché para evitar el reprocesamiento de datos ya analizados.
- La consolidación de datos se realiza de manera eficiente, minimizando el uso de memoria.

## Pruebas

El proyecto incluye un conjunto completo de pruebas unitarias para asegurar la calidad y el correcto funcionamiento del AnalizadorEstadisticoJudicial. Estas pruebas se encuentran en el directorio `tests/` y cubren las principales funcionalidades del sistema.

### Ejecutar las pruebas

Para ejecutar las pruebas unitarias:

1. Asegúrese de estar en el directorio raíz del proyecto.
2. Ejecute el siguiente comando:

   ```
   python -m unittest discover tests
   ```

   Este comando ejecutará todas las pruebas encontradas en el directorio `tests/`.

### Cobertura de las pruebas

Las pruebas unitarias cubren las siguientes funcionalidades principales:

- Ordenamiento de archivos
- Procesamiento de archivos Excel
- Procesamiento de hojas y filas de datos
- Consolidación de datos
- Creación de archivos consolidados

### Mantenimiento de las pruebas

A medida que se agreguen nuevas características o se modifiquen las existentes, asegúrese de actualizar o agregar pruebas correspondientes para mantener una alta cobertura de pruebas.

### Contribución a las pruebas

Si contribuye al proyecto, por favor incluya pruebas unitarias para cualquier nueva funcionalidad o modificación que realice. Esto ayudará a mantener la calidad y confiabilidad del código a largo plazo.

## Contribución

Las contribuciones son bienvenidas. Por favor, siga estos pasos:

1. Fork el repositorio.
2. Cree una nueva rama (`git checkout -b feature/AmazingFeature`).
3. Haga sus cambios y commit (`git commit -m 'Add some AmazingFeature'`).
4. Push a la rama (`git push origin feature/AmazingFeature`).
5. Abra un Pull Request.

## Registro de Cambios

Consulte el archivo [CHANGELOG.md](CHANGELOG.md) para ver el historial detallado de cambios del proyecto.

## Roadmap

- Implementar análisis estadísticos más avanzados.
- Desarrollar una interfaz gráfica de usuario.
- Integrar directamente con el sistema SIERJU para la obtención y envío de datos.
- Añadir capacidades de visualización de datos y generación de gráficos.
- Implementar un sistema de pruebas automatizadas.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - vea el archivo [LICENSE](LICENSE) para más detalles.

## Créditos

Desarrollado y mantenido por Alexander Oviedo Fadul, Profesional Universitario Grado 11 en el Consejo Seccional de la Judicatura de Sucre.

[GitHub](https://github.com/bladealex9848) | [Website](https://alexanderoviedofadul.dev/) | [Instagram](https://www.instagram.com/alexander.oviedo.fadul) | [Twitter](https://twitter.com/alexanderofadul) | [Facebook](https://www.facebook.com/alexanderof/) | [WhatsApp](https://api.whatsapp.com/send?phone=573015930519&text=Hola%20!Quiero%20conversar%20contigo!) | [LinkedIn](https://www.linkedin.com/in/alexander-oviedo-fadul/)
    