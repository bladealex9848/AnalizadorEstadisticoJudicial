# Guía de Usuario - AnalizadorEstadisticoJudicial (Versión Web)

## Índice
1. [Introducción](#introducción)
2. [Requisitos Técnicos](#requisitos-técnicos)
3. [Acceso a la Aplicación](#acceso-a-la-aplicación)
4. [Interfaz de Usuario](#interfaz-de-usuario)
5. [Procesamiento de Archivos](#procesamiento-de-archivos)
6. [Visualización de Resultados](#visualización-de-resultados)
7. [Descarga de Informes](#descarga-de-informes)
8. [Dataset de Muestra](#dataset-de-muestra)
9. [Solución de Problemas](#solución-de-problemas)
10. [Preguntas Frecuentes](#preguntas-frecuentes)

## Introducción

El **AnalizadorEstadisticoJudicial** en su versión web es una herramienta especializada para el procesamiento y consolidación de datos estadísticos judiciales almacenados en archivos Excel. Esta interfaz permite cargar, procesar y visualizar datos trimestrales, generando informes estructurados que facilitan el análisis de la eficiencia judicial.

La versión web proporciona una interfaz gráfica interactiva desarrollada con Streamlit, permitiendo acceder a las funcionalidades completas desde cualquier navegador moderno, sin necesidad de instalación local.

## Requisitos Técnicos

Para un rendimiento óptimo de la aplicación web, se recomienda:

- **Navegador**: Chrome, Firefox, Edge o Safari en sus versiones más recientes
- **Conexión a Internet**: Estable, mínimo 1 Mbps
- **Archivos Excel**: Formato .xls o .xlsx, siguiendo la nomenclatura requerida
- **Especificaciones recomendadas**: 
  - Tamaño máximo de archivo: 200 MB por archivo
  - Número máximo de archivos simultáneos: 10

## Acceso a la Aplicación

La aplicación web está disponible en:

```
https://judidata.streamlit.app
```

No se requiere registro ni autenticación para acceder a las funcionalidades básicas.

## Interfaz de Usuario

La interfaz se divide en las siguientes secciones principales:

### 1. Barra Lateral
- **Carga de Archivos**: Zona para subir los archivos Excel trimestrales
- **Instrucciones**: Guía rápida de uso
- **Recursos Adicionales**: Enlaces a documentación complementaria
- **Marco Normativo**: Documentación legal relacionada
- **Información de Contacto**: Detalles del desarrollador

### 2. Área Principal
- **Encabezado**: Título y descripción del sistema
- **Pestañas de Visualización**:
  - **Resumen**: Vista general de los datos procesados
  - **Detalles por Trimestre**: Exploración detallada por período
  - **Gráficos**: Visualizaciones interactivas
  - **Descargar Informe**: Opciones para obtener resultados
- **Método Manual**: Instrucciones alternativas para procesamiento local

## Procesamiento de Archivos

El proceso consta de los siguientes pasos:

### 1. Preparación de Archivos
Prepare sus archivos Excel siguiendo estas convenciones de nomenclatura:
- `Primer Trimestre.xls` o `Primer Trimestre.xlsx`
- `Segundo Trimestre.xls` o `Segundo Trimestre.xlsx`
- `Tercer Trimestre.xls` o `Tercer Trimestre.xlsx`
- `Cuarto Trimestre.xls` o `Cuarto Trimestre.xlsx`

Para múltiples archivos del mismo trimestre, use sufijos numéricos:
- `Primer Trimestre_1.xls`
- `Primer Trimestre_2.xls`

### 2. Carga de Archivos
1. En la barra lateral, haga clic en el botón "Browse files" dentro de la sección "Carga tus archivos Excel trimestrales"
2. Seleccione uno o más archivos Excel (.xls o .xlsx)
3. Confirme la carga de los archivos (aparecerán listados bajo el botón de carga)

### 3. Procesamiento
1. Una vez cargados los archivos, haga clic en el botón "Procesar Archivos"
2. El sistema mostrará indicadores de progreso durante el procesamiento
3. Al finalizar, se mostrará un mensaje de confirmación

### 4. Consideraciones Importantes
- Cada hoja del archivo Excel debe contener una fila con el texto "Total" para ser procesada correctamente
- La estructura de los archivos debe mantener la consistencia en todas las hojas
- Los archivos deben tener al menos 20 filas de datos
- El sistema procesa automáticamente los archivos en orden cronológico de trimestre

## Visualización de Resultados

La aplicación ofrece múltiples formas de visualizar los datos procesados:

### 1. Resumen
- Muestra tablas con los totales por cada hoja y trimestre
- Los datos se presentan en formato tabular interactivo
- Permite ordenar y filtrar información

### 2. Detalles por Trimestre
- Permite seleccionar un trimestre específico mediante un menú desplegable
- Muestra datos detallados de cada hoja para el trimestre seleccionado
- Facilita el análisis comparativo entre diferentes secciones

### 3. Gráficos
Esta sección permite:
- Seleccionar una hoja específica de datos
- Elegir el tipo de gráfico (Barras, Líneas o Combinado)
- Seleccionar la columna de valores a visualizar
- Interactuar con la visualización (zoom, descarga, filtrado)
- Ver la tabla de datos correspondiente al gráfico

## Descarga de Informes

La aplicación genera archivos consolidados que pueden descargarse:

### 1. Archivo ZIP
- Contiene todos los resultados del procesamiento
- Incluye archivos individuales por cada archivo Excel procesado
- Incorpora el archivo consolidado con todos los datos
- Incluye el archivo de log con detalles de la ejecución

### 2. Proceso de Descarga
1. Navegue a la pestaña "Descargar Informe"
2. Haga clic en el botón "📥 Descargar todos los resultados (ZIP)"
3. Seleccione la ubicación en su dispositivo para guardar el archivo
4. El archivo se guardará con el nombre "Resultados_AnalizadorEstadisticoJudicial.zip"

## Dataset de Muestra

Para familiarizarse con la aplicación sin necesidad de cargar archivos propios:

1. En la barra lateral, haga clic en el botón "Usar Dataset de Muestra"
2. El sistema cargará datos ficticios de ejemplo
3. Explore las diferentes visualizaciones y funcionalidades
4. Estos datos se pueden utilizar para practicar la generación de gráficos e informes

## Solución de Problemas

### Problemas Comunes y Soluciones

| Problema | Posible Causa | Solución |
|----------|---------------|----------|
| "Error al leer el archivo" | Formato no compatible | Asegúrese de que el archivo esté en formato .xls o .xlsx y no esté corrupto |
| "La hoja no cumple con el formato esperado" | Estructura incorrecta | Verifique que las hojas contengan la palabra "Total" y al menos 20 filas |
| "No se pudieron procesar los archivos" | Datos inválidos | Compruebe la estructura y formato de los archivos Excel |
| "Archivo consolidado no disponible" | Error en consolidación | Intente nuevamente el procesamiento o utilice la versión de escritorio |
| Errores en la visualización | Datos no numéricos | Asegúrese de que las columnas contienen valores numéricos válidos |

### Recomendaciones Avanzadas
- Limpie los datos Excel antes de cargarlos (elimine filas/columnas vacías, formato especial)
- Para archivos muy grandes, considere dividirlos en múltiples archivos más pequeños
- Mantenga la estructura consistente entre los diferentes archivos trimestrales
- Consulte el archivo log.txt en el ZIP descargado para diagnóstico detallado

## Preguntas Frecuentes

**P: ¿Puedo procesar archivos con nombres diferentes?**  
R: No, la aplicación requiere que los archivos sigan la nomenclatura específica: "Primer Trimestre.xls", "Segundo Trimestre.xls", etc.

**P: ¿Cuántos archivos puedo procesar simultáneamente?**  
R: La aplicación puede manejar múltiples archivos, pero se recomienda no exceder 10 archivos simultáneos para un rendimiento óptimo.

**P: ¿Se conservan mis datos en el servidor?**  
R: No, los datos se procesan temporalmente durante la sesión y no se almacenan permanentemente en el servidor.

**P: ¿Qué navegadores son compatibles?**  
R: Chrome, Firefox, Edge y Safari en sus versiones recientes son totalmente compatibles.

**P: ¿Qué hago si encuentro un error no documentado?**  
R: Puede contactar al desarrollador mediante los enlaces proporcionados en la parte inferior de la barra lateral.

**P: ¿Es posible automatizar el proceso para múltiples conjuntos de datos?**  
R: Para procesamiento automatizado o por lotes, se recomienda utilizar la versión de escritorio.

---

Para soporte adicional o consultas, contacte al desarrollador:

Alexander Oviedo Fadul  
Profesional Universitario Grado 11  
Consejo Seccional de la Judicatura de Sucre

[GitHub](https://github.com/bladealex9848) | [Sitio Web](https://alexanderoviedofadul.dev/) | [LinkedIn](https://www.linkedin.com/in/alexander-oviedo-fadul/)