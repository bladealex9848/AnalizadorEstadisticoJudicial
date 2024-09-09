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
   - [Versión Web (Streamlit)](#versión-web-streamlit)
   - [Versión de Escritorio](#versión-de-escritorio)
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

AnalizadorEstadisticoJudicial es una aplicación diseñada para automatizar el análisis de archivos Excel relacionados con la organización del trabajo y la eficiencia en la Judicatura. Este sistema procesa automáticamente los datos y genera un consolidado, facilitando significativamente la tarea de análisis y presentación de informes estadísticos judiciales.

La aplicación está disponible en dos versiones:
1. Una versión web desarrollada con Streamlit, que ofrece una interfaz gráfica intuitiva y accesible desde cualquier navegador.
2. Una versión de escritorio para usuarios que prefieren una aplicación local.

Ambas versiones procesan archivos Excel con nombres específicos (por ejemplo, 'Primer Trimestre.xls', 'Segundo Trimestre.xls', etc.), incluyendo aquellos con sufijos numéricos como 'Tercer Trimestre_1.xls'. Esto permite manejar múltiples archivos para un trimestre específico. Cada hoja de estos archivos es procesada y finalmente se genera un archivo consolidado con todos los resultados.

## Características Principales

- Interfaz web intuitiva desarrollada con Streamlit
- Procesamiento automático de archivos Excel trimestrales
- Generación de archivos de resultados individuales por cada archivo Excel
- Creación de un archivo consolidado con todos los resultados
- Visualización interactiva de datos con gráficos y tablas
- Manejo de múltiples archivos por trimestre
- Sistema robusto de logging para seguimiento y auditoría
- Optimización para el procesamiento eficiente de grandes volúmenes de datos
- Versión de escritorio disponible para uso local

## Estructura del Proyecto

```
AnalizadorEstadisticoJudicial/
│
├── main.py                           # Script principal de la versión web (Streamlit)
├── AnalizadorEstadisticoJudicial.py  # Script principal de la versión de escritorio
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
├── tests/                            # Directorio para pruebas unitarias
├── assets/                           # Directorio para recursos estáticos
│   ├── logo.jpg                      # Logo del proyecto
│   └── AnalizadorEstadisticoJudicial v1.1.exe  # Ejecutable de la versión de escritorio
│
└── .streamlit/                       # Configuración de Streamlit (si es necesario)
```

## Requisitos Previos

- Python 3.11+
- Bibliotecas de Python: streamlit, pandas, plotly, openpyxl, xlrd, rich
- Navegador web moderno (para la versión web)
- Archivos Excel de datos trimestrales

## Instalación

1. Clone el repositorio:
   ```
   git clone https://github.com/bladealex9848/AnalizadorEstadisticoJudicial.git
   cd AnalizadorEstadisticoJudicial
   ```

2. Instale las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Configuración

No se requiere configuración adicional para el uso básico. Para configuraciones avanzadas, consulte la sección de [Uso](#uso).

## Uso

### Versión Web (Streamlit)

1. Ejecute la aplicación Streamlit:
   ```
   streamlit run main.py
   ```
2. Abra su navegador y vaya a la dirección indicada (generalmente `http://localhost:8501`).
3. Use la interfaz web para:
   - Cargar archivos Excel trimestrales
   - Procesar los archivos
   - Visualizar resultados en gráficos interactivos
   - Descargar el informe consolidado

#### Características de la Versión Web:
- Carga de múltiples archivos Excel
- Visualización de datos en tablas interactivas
- Generación de gráficos personalizables
- Descarga de informes consolidados
- Acceso a recursos adicionales y documentación

### Versión de Escritorio

1. Descargue 'AnalizadorEstadisticoJudicial v1.1.exe' desde la carpeta 'assets' del repositorio.
2. Coloque el ejecutable en la misma carpeta que los archivos Excel a procesar, o cree una carpeta 'PROCESAR' en C:\ y coloque allí los archivos.
3. Ejecute el programa haciendo doble clic en el ejecutable.
4. Siga las instrucciones en pantalla para procesar los archivos y generar el informe consolidado.

### Notas Importantes:

- Asegúrese de que los archivos Excel sigan el formato de nomenclatura esperado (por ejemplo, 'Primer Trimestre.xls', 'Segundo Trimestre.xls', etc.).
- La aplicación maneja archivos con sufijos numéricos (ej: 'Tercer Trimestre_1.xls') para múltiples archivos del mismo trimestre.
- Los resultados se guardan en una carpeta 'Consolidado' con marca de tiempo.
- Revise el archivo 'log.txt' para detalles sobre la ejecución y posibles errores.

## Arquitectura del Sistema

AnalizadorEstadisticoJudicial utiliza una arquitectura modular:

1. Interfaz de Usuario: 
   - Web: Implementada con Streamlit para una experiencia interactiva.
   - Escritorio: Interfaz de línea de comandos.
2. Módulo de Lectura de Archivos: Lee y valida los archivos Excel de entrada.
3. Módulo de Procesamiento de Hojas: Analiza cada hoja de los archivos Excel.
4. Módulo de Generación de Resultados: Crea archivos de resultados individuales.
5. Módulo de Consolidación: Combina los resultados en un archivo consolidado.
6. Módulo de Visualización: Genera gráficos y tablas interactivas (versión web).
7. Sistema de Logging: Registra todas las operaciones y errores.

## Componentes Principales

- `main.py`: Punto de entrada para la versión web (Streamlit).
- `process_excel_files()`: Procesa los archivos Excel y genera resultados individuales.
- `create_consolidated_file()`: Crea el archivo consolidado final.
- `show_charts()`: Genera visualizaciones interactivas de los datos (versión web).
- `offer_download()`: Permite la descarga del informe consolidado (versión web).

## Flujo de Trabajo

1. El usuario carga los archivos Excel (web) o los coloca en el directorio apropiado (escritorio).
2. La aplicación valida y procesa cada archivo.
3. Se generan resultados individuales y un archivo consolidado.
4. En la versión web, se presentan visualizaciones interactivas de los datos.
5. El usuario puede descargar el informe consolidado.
6. Todas las operaciones se registran para auditoría y depuración.

## Manejo de Errores y Logging

- Sistema de logging detallado que registra operaciones en `log.txt`.
- Manejo de excepciones con mensajes de error claros para el usuario.
- En la versión web, se muestran advertencias y errores directamente en la interfaz.

## Optimización y Rendimiento

- Uso de pandas para procesamiento eficiente de datos.
- Implementación de caché en Streamlit para mejorar el rendimiento de la versión web.
- Procesamiento por lotes para manejar grandes volúmenes de datos.

## Pruebas

El proyecto incluye pruebas unitarias en el directorio `tests/`. Para ejecutarlas:

1. Asegúrese de estar en el directorio raíz del proyecto.
2. Ejecute:
   ```
   python -m unittest discover tests
   ```

Las pruebas cubren:
- Procesamiento de archivos Excel
- Generación de informes consolidados
- Funcionalidades de la interfaz web (utilizando mocks de Streamlit)

## Contribución

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio.
2. Cree una nueva rama (`git checkout -b feature/AmazingFeature`).
3. Haga sus cambios y commit (`git commit -m 'Add some AmazingFeature'`).
4. Push a la rama (`git push origin feature/AmazingFeature`).
5. Abra un Pull Request.

## Registro de Cambios

Consulte el archivo [CHANGELOG.md](CHANGELOG.md) para ver el historial detallado de cambios del proyecto.

## Roadmap

- Implementar análisis estadísticos más avanzados.
- Mejorar la personalización de gráficos en la versión web.
- Integrar directamente con el sistema SIERJU para la obtención y envío de datos.
- Desarrollar una API REST para integración con otros sistemas.
- Implementar un sistema de autenticación para la versión web.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - vea el archivo [LICENSE](LICENSE) para más detalles.

## Créditos

Desarrollado y mantenido por Alexander Oviedo Fadul, Profesional Universitario Grado 11 en el Consejo Seccional de la Judicatura de Sucre.

[GitHub](https://github.com/bladealex9848) | [Website](https://alexanderoviedofadul.dev/) | [Instagram](https://www.instagram.com/alexander.oviedo.fadul) | [Twitter](https://twitter.com/alexanderofadul) | [Facebook](https://www.facebook.com/alexanderof/) | [WhatsApp](https://api.whatsapp.com/send?phone=573015930519&text=Hola%20!Quiero%20conversar%20contigo!) | [LinkedIn](https://www.linkedin.com/in/alexander-oviedo-fadul/)