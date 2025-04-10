# Guía de Usuario - AnalizadorEstadisticoJudicial (Versión de Escritorio)

## Índice
1. [Introducción](#introducción)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Instalación](#instalación)
4. [Preparación de Archivos](#preparación-de-archivos)
5. [Ejecución del Programa](#ejecución-del-programa)
6. [Interpretación de Resultados](#interpretación-de-resultados)
7. [Arquitectura de Archivos Generados](#arquitectura-de-archivos-generados)
8. [Manejo de Errores](#manejo-de-errores)
9. [Solución de Problemas](#solución-de-problemas)
10. [Preguntas Frecuentes](#preguntas-frecuentes)

## Introducción

El **AnalizadorEstadisticoJudicial** en su versión de escritorio es una herramienta especializada para el procesamiento y consolidación de datos estadísticos judiciales almacenados en archivos Excel. Esta aplicación ejecutable permite procesar archivos trimestrales, generando informes estructurados que facilitan el análisis de la eficiencia judicial.

La versión de escritorio es ideal para usuarios que prefieren un procesamiento local, sin dependencia de conexión a internet, y para aquellos que necesitan procesar grandes volúmenes de datos con máxima eficiencia.

## Requisitos del Sistema

Para un funcionamiento óptimo, su sistema debe cumplir con las siguientes especificaciones mínimas:

- **Sistema Operativo**: Windows 7/8/10/11 (64 bits)
- **Procesador**: Intel Core i3 o equivalente
- **Memoria RAM**: 4 GB (recomendado 8 GB para archivos grandes)
- **Espacio en Disco**: 50 MB para la aplicación + espacio para archivos de datos
- **Resolución de Pantalla**: 1280x720 o superior
- **Software Adicional**: Microsoft Excel 2010 o superior (recomendado, no obligatorio)

## Instalación

La aplicación no requiere instalación tradicional. Siga estos pasos para preparar el ejecutable:

1. **Descarga del Ejecutable**:
   - Obtenga el archivo `AnalizadorEstadisticoJudicial v1.1.exe` desde el [repositorio oficial](https://github.com/bladealex9848/AnalizadorEstadisticoJudicial/releases)
   - Alternativamente, puede descargar el ejecutable desde la versión web de la aplicación

2. **Ubicación del Ejecutable**:
   Tiene dos opciones para ubicar el ejecutable:

   **Opción A - Misma carpeta que los archivos Excel**:
   - Coloque el archivo `.exe` en la misma carpeta que contiene sus archivos Excel trimestrales
   - Esta opción es ideal para procesamiento ad-hoc o por proyecto

   **Opción B - Carpeta PROCESAR en C:**:
   - Cree una carpeta llamada `PROCESAR` en la unidad C: de su equipo
   - Coloque sus archivos Excel trimestrales en esta carpeta
   - El ejecutable puede estar en cualquier ubicación
   - Esta opción es recomendada para procesamiento rutinario

3. **Verificación de Seguridad**:
   - Windows puede mostrar advertencias de seguridad al ejecutar por primera vez
   - Seleccione "Más información" y luego "Ejecutar de todas formas"
   - El ejecutable es seguro y no contiene malware

## Preparación de Archivos

Los archivos Excel que desea procesar deben seguir estas convenciones estrictas:

### 1. Nomenclatura de Archivos
- `Primer Trimestre.xls` o `Primer Trimestre.xlsx`
- `Segundo Trimestre.xls` o `Segundo Trimestre.xlsx`
- `Tercer Trimestre.xls` o `Tercer Trimestre.xlsx`
- `Cuarto Trimestre.xls` o `Cuarto Trimestre.xlsx`

Para múltiples archivos del mismo trimestre, use sufijos numéricos:
- `Primer Trimestre_1.xls`
- `Primer Trimestre_2.xls`

### 2. Estructura Interna
Cada archivo Excel debe contener:
- Al menos 20 filas de datos
- Una fila con la etiqueta "Total" (crucial para el procesamiento)
- Estructura consistente en todas las hojas
- La fila 20 debe contener títulos de columnas relevantes

### 3. Consideraciones Importantes
- Evite protección con contraseña en los archivos
- No deje hojas vacías o incompletas
- Asegúrese de que los totales estén correctamente calculados
- Mantenga coherencia en la estructura de todas las hojas y archivos

## Ejecución del Programa

Siga estos pasos para procesar sus archivos:

### 1. Verificación Previa
- Confirme que sus archivos Excel están en la ubicación correcta (misma carpeta que el .exe o en C:\PROCESAR)
- Asegúrese de que los archivos siguen la nomenclatura requerida
- Cierre los archivos Excel si están abiertos en Microsoft Excel

### 2. Iniciar el Programa
- Haga doble clic en el archivo `AnalizadorEstadisticoJudicial v1.1.exe`
- Se abrirá una ventana de consola mostrando información inicial del programa

### 3. Procesamiento Automático
- El programa identifica automáticamente los archivos trimestrales
- Muestra una tabla de información con la versión y descripción
- Procesa cada archivo y hoja de cálculo, mostrando el progreso en pantalla
- Al finalizar, muestra un mensaje de confirmación con la ubicación de los resultados

### 4. Finalización
- Al terminar el procesamiento, el programa muestra "Procesamiento finalizado"
- Se solicita "Presiona cualquier tecla para salir..."
- Pulse cualquier tecla para cerrar la aplicación

## Interpretación de Resultados

Después de la ejecución, el programa genera los siguientes resultados:

### 1. Estructura de Carpetas
- Se crea una carpeta `Consolidado` en el mismo directorio donde se ejecutó el programa
- Dentro de esta carpeta, se crea un subdirectorio con la fecha y hora de procesamiento (formato `YYYY-MM-DD_HH-MM-SS`)

### 2. Archivos Generados
En el subdirectorio con marca de tiempo encontrará:
- **Archivos individuales**: `Primer Trimestre_results.xlsx`, `Segundo Trimestre_results.xlsx`, etc.
- **Archivo consolidado**: `Consolidado.xlsx`

### 3. Contenido de Archivos
- Los archivos individuales contienen los datos procesados de cada trimestre
- El archivo consolidado contiene:
  - Primera sección: Datos individuales de cada trimestre (ordenados)
  - Segunda sección (si hay archivos con sufijo): Datos consolidados por trimestre

### 4. Análisis de Datos
Los datos procesados permiten:
- Comparar eficiencia entre diferentes trimestres
- Identificar tendencias y patrones temporales
- Generar informes estadísticos basados en datos consolidados
- Analizar el desempeño por áreas específicas (según las hojas existentes)

## Arquitectura de Archivos Generados

### 1. Archivo de Log
- **Ubicación**: Directorio raíz donde se ejecutó el programa
- **Nombre**: `log.txt`
- **Contenido**: Registro detallado de todas las operaciones, con marcas de tiempo
- **Utilidad**: Diagnóstico y auditoría del procesamiento

### 2. Archivos de Resultados Individuales
- **Estructura**: Cada archivo conserva las hojas originales
- **Formato**: Celdas con bordes, texto ajustado y combinación de celdas adecuada
- **Contenido**: Encabezados + datos de filas totales por cada hoja

### 3. Archivo Consolidado
- **Hojas**: Mantiene la misma estructura de hojas que los archivos originales
- **Primera tabla**: Datos individuales ordenados cronológicamente
- **Segunda tabla** (cuando aplica): Consolidación por trimestre con sumatorias
- **Formato**: Diseño profesional con bordes, alineación y ajuste de texto

## Manejo de Errores

El programa implementa un sistema robusto de manejo de errores:

### 1. Errores de Lectura de Archivo
- El programa continúa con el siguiente archivo si uno no puede ser leído
- Registra el error en el archivo log.txt con detalles específicos
- Muestra mensaje en pantalla indicando el archivo problemático

### 2. Errores de Estructura
- Si una hoja no cumple los requisitos (20 filas mínimo, texto "Total"), es omitida
- Se registra la omisión tanto en pantalla como en el archivo log
- El procesamiento continúa con las siguientes hojas

### 3. Errores de Escritura
- Si no se puede guardar algún archivo de resultados, se notifica
- El proceso intenta continuar con los siguientes archivos
- Se proporciona información detallada sobre la causa del error

## Solución de Problemas

| Problema | Posible Causa | Solución |
|----------|---------------|----------|
| El programa no inicia | Permisos de Windows | Ejecute como administrador |
| No encuentra archivos | Nomenclatura incorrecta | Verifique nombres de archivos |
| Error en archivo específico | Formato incompatible | Abra y guarde nuevamente en formato compatible |
| No procesa alguna hoja | Falta la palabra "Total" | Añada fila con "Total" en la columna A |
| Resultados incompletos | Error en procesamiento | Consulte log.txt para detalles específicos |
| Error "At least one sheet must be visible" | Sin hojas válidas | Asegúrese de que al menos una hoja cumpla requisitos |
| Programa se cierra inmediatamente | Error crítico | Ejecute desde línea de comandos para ver error |

### Diagnóstico Avanzado

Para un diagnóstico detallado en caso de errores:

1. Abra el símbolo del sistema (cmd)
2. Navegue hasta la carpeta donde está el ejecutable usando `cd ruta\a\la\carpeta`
3. Ejecute manualmente: `AnalizadorEstadisticoJudicial v1.1.exe`
4. Observe los mensajes de error completos antes de que se cierre la ventana
5. Consulte el archivo log.txt para información adicional

## Preguntas Frecuentes

**P: ¿Puedo procesar archivos de años diferentes simultáneamente?**  
R: Sí, mientras sigan la nomenclatura trimestral. Para diferenciarlos, use el sufijo numérico (ej: `Primer Trimestre_2022.xls`).

**P: ¿Qué sucede si falta algún trimestre?**  
R: El programa procesará los trimestres disponibles. El consolidado incluirá solo los trimestres presentes.

**P: ¿Se sobrescriben los resultados anteriores?**  
R: No, cada ejecución crea una carpeta con fecha y hora única, preservando resultados anteriores.

**P: ¿Puedo modificar la plantilla de los archivos Excel?**  
R: No se recomienda. El programa espera una estructura específica con al menos 20 filas y una fila "Total".

**P: ¿Es posible automatizar la ejecución periódica?**  
R: Sí, puede utilizar el Programador de tareas de Windows para ejecutar el programa automáticamente.

**P: ¿Qué formato de Excel es preferible usar?**  
R: Ambos formatos (.xls y .xlsx) son compatibles, pero .xlsx es recomendado por ser más moderno y eficiente.

**P: ¿Cómo actualizo a una nueva versión del programa?**  
R: Simplemente descargue el nuevo ejecutable y reemplace el anterior. No se requiere desinstalación.

---

Para soporte técnico o consultas adicionales, contacte al desarrollador:

Alexander Oviedo Fadul  
Profesional Universitario Grado 11  
Consejo Seccional de la Judicatura de Sucre

[GitHub](https://github.com/bladealex9848) | [Sitio Web](https://alexanderoviedofadul.dev/) | [LinkedIn](https://www.linkedin.com/in/alexander-oviedo-fadul/)