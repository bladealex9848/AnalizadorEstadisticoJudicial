import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import tempfile
import os
import openpyxl
from openpyxl.styles import Alignment, Border, Side
import base64
from io import BytesIO
import re

# Configuración de la página
st.set_page_config(page_title="AnalizadorEstadisticoJudicial", page_icon="📊", layout="wide")

# Función para ordenar los archivos
def sort_key_func(file_name):
    order = ["Primer", "Segundo", "Tercer", "Cuarto"]
    match = re.match(r"(\w+ Trimestre)(_?(\d)?)", file_name)
    if match:
        name, _, number = match.groups()
        return (order.index(name.split(' ')[0]), int(number) if number else 0)
    return (0, 0)

def sorted_files(files):
    return sorted(files, key=lambda x: sort_key_func(Path(x).name))

# Función para procesar los archivos Excel
def process_excel_files(excel_files, subfolder):
    all_sheets_data = {}
    for file in excel_files:
        try:
            # Usar pandas para leer tanto .xls como .xlsx
            xls = pd.ExcelFile(file)
            for sheet_name in xls.sheet_names:
                data = pd.read_excel(file, sheet_name=sheet_name, header=None)
                if len(data) >= 20 and 'Total' in data[0].values:
                    if sheet_name not in all_sheets_data:
                        all_sheets_data[sheet_name] = []
                    header_rows = data.iloc[:19].values.tolist()
                    row_20_titles = [''] + data.iloc[19, 1:].tolist()
                    total_row_index = data[data[0] == 'Total'].index[0]
                    total_row_values = ['Total'] + data.iloc[total_row_index, 1:].tolist()
                    all_sheets_data[sheet_name].append(header_rows + [row_20_titles, total_row_values + [Path(file).name]])
        except Exception as e:
            st.error(f"Error al procesar el archivo {file}: {str(e)}")
    return all_sheets_data

# Función para crear el archivo consolidado
def create_consolidated_file(all_sheets_data, subfolder):
    consolidated_writer = openpyxl.Workbook()
    consolidated_writer.remove(consolidated_writer.active)

    border = Border(left=Side(style='thin'), right=Side(style='thin'), 
                    top=Side(style='thin'), bottom=Side(style='thin'))

    sheets_created = 0

    for sheet, data_list in all_sheets_data.items():
        if not data_list:
            continue

        ws = consolidated_writer.create_sheet(title=sheet)
        sheets_created += 1

        for data in data_list:
            for row in data:
                ws.append(row)

        for row in ws.rows:
            for cell in row:
                cell.alignment = Alignment(wrap_text=True)
                cell.border = border

    if sheets_created == 0:
        st.warning("No se crearon hojas en el archivo consolidado.")
        return None

    consolidated_file = os.path.join(subfolder, 'Consolidado.xlsx')
    try:
        consolidated_writer.save(consolidated_file)
        st.success(f"Archivo consolidado creado exitosamente en {consolidated_file}.")
        return consolidated_file
    except Exception as e:
        st.error(f"Error al guardar el archivo consolidado: {str(e)}")
        return None

# Función principal
def main():
    st.title("AnalizadorEstadisticoJudicial 📊")

    st.write("""
        [![ver código fuente](https://img.shields.io/badge/Repositorio%20GitHub-gris?logo=github)](https://github.com/bladealex9848/AnalizadorEstadisticoJudicial)
        ![Visitantes](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fjudidata.streamlit.app&label=Visitantes&labelColor=%235d5d5d&countColor=%231e7ebf&style=flat)
        """)

    st.markdown("""
    Esta aplicación analiza archivos Excel trimestrales y genera informes consolidados 
    para el Consejo Seccional de la Judicatura de Sucre.
    """)

    # Inicializar variables de estado
    if 'all_sheets_data' not in st.session_state:
        st.session_state.all_sheets_data = None
    if 'consolidated_file' not in st.session_state:
        st.session_state.consolidated_file = None
    if 'files_processed' not in st.session_state:
        st.session_state.files_processed = False

    # Sidebar para cargar archivos y mostrar instrucciones
    with st.sidebar:
        st.header("Carga de Archivos")
        uploaded_files = st.file_uploader("Carga tus archivos Excel trimestrales", 
                                          accept_multiple_files=True, type=['xls', 'xlsx'])
        
        st.markdown("### Instrucciones")
        st.info("""
        1. Carga tus archivos Excel trimestrales.
        2. Haz clic en 'Procesar Archivos' para analizar los datos.
        3. Visualiza los resultados en las pestañas correspondientes.
        4. Descarga el informe consolidado al final.
        """)

        if st.button("Procesar Archivos"):
            if uploaded_files:
                with st.spinner('Procesando archivos...'):
                    try:
                        with tempfile.TemporaryDirectory() as temp_dir:
                            file_paths = []
                            for file in uploaded_files:
                                temp_file = Path(temp_dir) / file.name
                                temp_file.write_bytes(file.getvalue())
                                file_paths.append(str(temp_file))

                            st.session_state.all_sheets_data = process_excel_files(sorted_files(file_paths), temp_dir)
                            
                            if not st.session_state.all_sheets_data:
                                st.error("No se pudieron procesar los archivos. Verifica que contengan datos válidos.")
                                st.session_state.files_processed = False
                                return

                            st.session_state.consolidated_file = create_consolidated_file(st.session_state.all_sheets_data, temp_dir)

                            if st.session_state.consolidated_file is None:
                                st.warning("No se pudo crear el archivo consolidado, pero los datos están disponibles para visualización.")
                            else:
                                st.success('Archivos procesados y consolidados con éxito!')

                        st.session_state.files_processed = True
                    except Exception as e:
                        st.error(f"""Error al procesar los archivos: {str(e)}
                        
                        Si el error persiste, asegúrate de tener instaladas las siguientes dependencias:
                        pip install pandas==1.2.4 xlrd==1.2.0 openpyxl
                        
                        Luego, reinicia la aplicación.""")
                        st.session_state.all_sheets_data = None
                        st.session_state.consolidated_file = None
                        st.session_state.files_processed = False
            else:
                st.warning("Por favor, carga archivos antes de procesar.")

    # Mostrar resultados en pestañas
    if st.session_state.files_processed and st.session_state.all_sheets_data:
        tabs = st.tabs(["Resumen", "Detalles por Trimestre", "Gráficos", "Descargar Informe"])

        with tabs[0]:
            show_summary(st.session_state.all_sheets_data)

        with tabs[1]:
            show_details(st.session_state.all_sheets_data)

        with tabs[2]:
            show_charts(st.session_state.all_sheets_data)

        with tabs[3]:
            offer_download(st.session_state.consolidated_file)
    elif not st.session_state.files_processed:
        st.info("Carga tus archivos Excel y haz clic en 'Procesar Archivos' para comenzar.")
    else:
        st.warning("No se encontraron datos procesados. Por favor, asegúrate de cargar y procesar los archivos correctamente.")

    # Logs para depuración
    st.write("Debug: Estado de files_processed:", st.session_state.files_processed)
    st.write("Debug: all_sheets_data es None?:", st.session_state.all_sheets_data is None)
    if st.session_state.all_sheets_data:
        st.write("Debug: Número de hojas en all_sheets_data:", len(st.session_state.all_sheets_data))
        for sheet, data in st.session_state.all_sheets_data.items():
            st.write(f"Debug: Hoja '{sheet}' tiene {len(data)} entradas")

def show_summary(all_sheets_data):
    st.header("Resumen de Datos")
    if not all_sheets_data:
        st.warning("No hay datos para mostrar. Por favor, carga y procesa los archivos Excel.")
        return
    for sheet, data_list in all_sheets_data.items():
        st.subheader(f"Hoja: {sheet}")
        for data in data_list:
            df = pd.DataFrame(data[1:], columns=data[0])
            st.dataframe(df)

def show_details(all_sheets_data):
    st.header("Detalles por Trimestre")
    if not all_sheets_data:
        st.warning("No hay datos para mostrar. Por favor, carga y procesa los archivos Excel.")
        return
    trimester = st.selectbox("Selecciona un trimestre", 
                             ["Primer Trimestre", "Segundo Trimestre", "Tercer Trimestre", "Cuarto Trimestre"])
    
    for sheet, data_list in all_sheets_data.items():
        for data in data_list:
            df = pd.DataFrame(data[1:], columns=data[0])
            trimester_data = df[df.iloc[:, -1].str.contains(trimester)]
            if not trimester_data.empty:
                st.subheader(f"{sheet} - {trimester}")
                st.dataframe(trimester_data)

def show_charts(all_sheets_data):
    st.header("Visualización de Datos")
    if not all_sheets_data:
        st.warning("No hay datos para visualizar. Por favor, carga y procesa los archivos Excel.")
        return
    
    sheet = st.selectbox("Selecciona una hoja", list(all_sheets_data.keys()))
    
    if all_sheets_data[sheet]:
        df = pd.DataFrame(all_sheets_data[sheet][0][1:], columns=all_sheets_data[sheet][0][0])
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        
        if numeric_columns.empty:
            st.warning("No se encontraron columnas numéricas para graficar.")
            return

        chart_type = st.radio("Tipo de gráfico", ["Barras", "Líneas", "Dispersión"])
        x_axis = st.selectbox("Eje X", df.columns)
        y_axis = st.selectbox("Eje Y", numeric_columns)

        try:
            if chart_type == "Barras":
                fig = px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} por {x_axis}")
            elif chart_type == "Líneas":
                fig = px.line(df, x=x_axis, y=y_axis, title=f"{y_axis} a lo largo de {x_axis}")
            else:
                fig = px.scatter(df, x=x_axis, y=y_axis, title=f"Relación entre {x_axis} y {y_axis}")

            st.plotly_chart(fig)
        except Exception as e:
            st.error(f"Error al crear el gráfico: {str(e)}")
    else:
        st.warning(f"No hay datos disponibles para la hoja {sheet}")

def offer_download(file_path):
    st.header("Descargar Informe Consolidado")
    if file_path and os.path.exists(file_path):
        with open(file_path, "rb") as file:
            btn = st.download_button(
                label="Descargar informe consolidado",
                data=file,
                file_name="informe_consolidado.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.warning("El archivo consolidado aún no está disponible. Por favor, procesa los archivos primero.")

if __name__ == "__main__":
    main()