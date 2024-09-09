import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path
import tempfile
import os
import openpyxl
from openpyxl.styles import Alignment, Border, Side
import base64
from io import BytesIO
import re
import requests
import glob
from datetime import datetime
from openpyxl.utils.dataframe import dataframe_to_rows
import warnings


# Configuración de la página
st.set_page_config(page_title="AnalizadorEstadisticoJudicial", page_icon="📊", layout="wide")

def create_download_link(url, label):
    return f'<a href="{url}" target="_blank" class="btn-download">{label}</a>'

def show_sidebar_resources():
    st.sidebar.title("Recursos Adicionales")
    with st.sidebar.expander("Ver Recursos Adicionales", expanded=False):        
        st.markdown(create_download_link("https://enki.care/AnalizadorEstadisticoJudicialGuiaUsuario", 'Guía de Usuario'), unsafe_allow_html=True)

    st.sidebar.title("Marco Normativo")
    with st.sidebar.expander("Ver Marco Normativo", expanded=False):
        st.markdown(create_download_link("https://enki.care/PSAA16-10618", 'ACUERDO PSAA16-10618'), unsafe_allow_html=True)
        st.markdown(create_download_link("https://enki.care/SIERJU-Formularios-e-Instructivos", 'SIERJU Formularios e Instructivos'), unsafe_allow_html=True)
        
    st.sidebar.title("Descargar Versión Portable")
    with st.sidebar.expander("Ver Versión Portable", expanded=False):
        st.markdown(create_download_link("https://enki.care/AnalizadorEstadisticoJudicial_v1.1.zip", 'Versión 1.1'), unsafe_allow_html=True)

    st.sidebar.markdown("""
    <style>
    .btn-download {
        display: inline-block;
        padding: 0.5em 1em;
        color: #ffffff !important;
        background-color: #0066cc;
        border-radius: 5px;
        text-decoration: none;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }
    .btn-download:hover {
        background-color: #0056b3;
        color: #ffffff !important;
        text-decoration: none;
    }
    </style>
    """, unsafe_allow_html=True)

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}" class="btn-download">Descargar {file_label}</a>'
    return href

def sort_key_func(file_name):
    order = ["Primer", "Segundo", "Tercer", "Cuarto"]
    match = re.match(r"(\w+ Trimestre)(_?(\d)?)", file_name)
    if match:
        name, _, number = match.groups()
        return (order.index(name.split(' ')[0]), int(number) if number else 0)
    return (0, 0)

def sorted_files(files):
    return sorted(files, key=lambda x: sort_key_func(Path(x).name))

def log_message(message, add_space=False):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] {message}"
    with open("log.txt", "a") as log_file:
        if add_space:
            log_file.write("\n")
        log_file.write(log_entry + "\n")

def process_excel_files(excel_files, subfolder):
    all_sheets_data = {}
    for file in excel_files:
        file_path = Path(file)
        st.info(f"Procesando archivo: {file_path.name}")
        try:
            if file_path.suffix.lower() == '.xls':
                xls = pd.ExcelFile(file, engine='xlrd')
            else:
                xls = pd.ExcelFile(file, engine='openpyxl')
            
            process_file(xls, file_path, all_sheets_data)
        except Exception as e:
            st.warning(f"Error al procesar {file_path.name}: {str(e)}")
            log_message(f"Error al procesar {file_path.name}: {str(e)}")
    return all_sheets_data

def process_file(xls, file_path, all_sheets_data):
    for sheet_name in xls.sheet_names:
        try:
            data = pd.read_excel(xls, sheet_name=sheet_name, header=None)
            if len(data) >= 20 and 'Total' in data[0].values:
                if sheet_name not in all_sheets_data:
                    all_sheets_data[sheet_name] = []
                
                # Reemplazar NaN con None para evitar problemas de conversión
                data = data.replace({np.nan: None})
                
                header_rows = data.iloc[:19].values.tolist()
                row_20_titles = [''] + data.iloc[19, 1:].tolist()
                total_row_index = data[data[0] == 'Total'].index[0]
                total_row_values = ['Total'] + data.iloc[total_row_index, 1:].tolist()
                
                all_sheets_data[sheet_name].append(header_rows + [row_20_titles, total_row_values + [file_path.name]])
                
                st.text(f"Datos procesados para la hoja '{sheet_name}':")
                st.dataframe(data.head())
        except Exception as e:
            st.warning(f"Error al procesar la hoja '{sheet_name}' en {file_path.name}: {str(e)}")
            log_message(f"Error al procesar la hoja '{sheet_name}' en {file_path.name}: {str(e)}")

    st.success(f"Archivo {file_path.name} procesado con éxito.")

def create_consolidated_file(all_sheets_data, subfolder):
    consolidated_writer = openpyxl.Workbook()
    consolidated_writer.remove(consolidated_writer.active)

    for sheet, data in all_sheets_data.items():
        ws = consolidated_writer.create_sheet(title=sheet)
        
        for row_data in data:
            for row in row_data:
                # Convertir elementos a string para evitar problemas con NaN
                ws.append([str(cell) if cell is not None else '' for cell in row])

    consolidated_file = os.path.join(subfolder, 'Consolidado.xlsx')
    try:
        consolidated_writer.save(consolidated_file)
        st.success(f"Archivo consolidado creado exitosamente en {consolidated_file}.")
        return consolidated_file
    except Exception as e:
        st.error(f"Error al guardar el archivo consolidado: {str(e)}")
        log_message(f"Error al guardar el archivo consolidado: {str(e)}")
        return None

def consolidate_data(data):
    consolidated_data = [data[0]]
    trimesters = ["Primer Trimestre", "Segundo Trimestre", "Tercer Trimestre", "Cuarto Trimestre"]

    for trimester in trimesters:
        rows = [row for row in data[1:] if trimester in row[-1]]
        if rows:
            consolidated_row = ['Total'] + [sum(row[i] for row in rows) for i in range(1, len(rows[0]) - 1)] + [trimester]
            consolidated_data.append(consolidated_row)

    return consolidated_data

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

    if 'all_sheets_data' not in st.session_state:
        st.session_state.all_sheets_data = None
    if 'consolidated_file' not in st.session_state:
        st.session_state.consolidated_file = None
    if 'files_processed' not in st.session_state:
        st.session_state.files_processed = False    
    
    show_sidebar_resources()
    
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

        if st.button("Usar Dataset de Muestra"):
            st.session_state.all_sheets_data = load_sample_dataset()
            st.session_state.files_processed = True
            st.success("Dataset de muestra cargado con éxito!")

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

                            st.write("Datos procesados:")
                            st.json(st.session_state.all_sheets_data)

                            st.session_state.consolidated_file = create_consolidated_file(st.session_state.all_sheets_data, temp_dir)

                            if st.session_state.consolidated_file is None:
                                st.warning("No se pudo crear el archivo consolidado, pero los datos están disponibles para visualización.")
                            else:
                                st.success('Archivos procesados y consolidados con éxito!')

                        st.session_state.files_processed = True
                    except Exception as e:
                        st.error(f"Error al procesar los archivos: {str(e)}")
                        log_message(f"Error al procesar los archivos: {str(e)}")
                        st.info("Intente usar el método manual descargando el ejecutable o use el dataset de muestra.")
                        st.session_state.all_sheets_data = None
                        st.session_state.consolidated_file = None
                        st.session_state.files_processed = False
            else:
                st.warning("Por favor, carga archivos antes de procesar.")

    st.sidebar.markdown("---")
    st.sidebar.image("assets/logo_CSJ_Sucre.png", width=200)
    st.sidebar.write("<div style='text-align: center;'>Desarrollado por Alexander Oviedo Fadul</div>", unsafe_allow_html=True)
    st.sidebar.write("<div style='text-align: center;'>v.1.1.1</div>", unsafe_allow_html=True)
    st.sidebar.write("<div style='text-align: center;'><a href='https://github.com/bladealex9848'>GitHub</a> | <a href='https://alexanderoviedofadul.dev/'>Website</a> | <a href='https://www.linkedin.com/in/alexander-oviedo-fadul/'>LinkedIn</a></div>", unsafe_allow_html=True)

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

    st.markdown("""
    ### Método Manual
    Si experimenta problemas al cargar los archivos, puede descargar el ejecutable y procesar los archivos localmente.
    
    Instrucciones:
    1. Descargue el ejecutable 'AnalizadorEstadisticoJudicial v1.1.exe'.
    2. Coloque el ejecutable en la misma carpeta que sus archivos Excel trimestrales, o
       cree una carpeta 'PROCESAR' en C: y coloque allí los archivos Excel.
    3. Ejecute el programa haciendo doble clic en el ejecutable.
    4. Los resultados se guardarán en una nueva carpeta 'Consolidado'.
    """)
    
    ejecutable_path = Path('assets/AnalizadorEstadisticoJudicial v1.1.exe')
    if ejecutable_path.exists():
        st.markdown(get_binary_file_downloader_html(ejecutable_path, 'Ejecutable'), unsafe_allow_html=True)
    else:
        st.warning("El ejecutable no está disponible en este momento. Por favor, contacte al administrador del sistema.")

def show_summary(all_sheets_data):
    st.header("Resumen de Datos")
    if not all_sheets_data:
        st.warning("No hay datos para mostrar. Por favor, carga y procesa los archivos Excel.")
        return
    for sheet, data_list in all_sheets_data.items():
        st.subheader(f"Hoja: {sheet}")
        for data in data_list:
            try:
                df = pd.DataFrame(data[1:], columns=data[0])
                st.dataframe(df)
            except Exception as e:
                st.error(f"Error al mostrar datos de la hoja {sheet}: {str(e)}")
                st.write("Datos en bruto:", data)

def show_details(all_sheets_data):
    st.header("Detalles por Trimestre")
    if not all_sheets_data:
        st.warning("No hay datos para mostrar. Por favor, carga y procesa los archivos Excel.")
        return
    trimester = st.selectbox("Selecciona un trimestre", 
                             ["Primer Trimestre", "Segundo Trimestre", "Tercer Trimestre", "Cuarto Trimestre"])
    
    for sheet, data_list in all_sheets_data.items():
        for data in data_list:
            try:
                df = pd.DataFrame(data[1:], columns=data[0])
                trimester_data = df[df.iloc[:, -1].str.contains(trimester)]
                if not trimester_data.empty:
                    st.subheader(f"{sheet} - {trimester}")
                    st.dataframe(trimester_data)
            except Exception as e:
                st.error(f"Error al mostrar detalles de la hoja {sheet} para {trimester}: {str(e)}")
                st.write("Datos en bruto:", data)

def show_charts(all_sheets_data):
    st.header("Visualización de Datos")
    if not all_sheets_data:
        st.warning("No hay datos para visualizar. Por favor, carga y procesa los archivos Excel.")
        return
    
    sheet = st.selectbox("Selecciona una hoja", list(all_sheets_data.keys()))
    
    if all_sheets_data[sheet]:
        try:
            df = pd.DataFrame(all_sheets_data[sheet][0][1:], columns=all_sheets_data[sheet][0][0])
            numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
            
            if numeric_columns.empty:
                st.warning("No se encontraron columnas numéricas para graficar.")
                return

            chart_type = st.radio("Tipo de gráfico", ["Barras", "Líneas", "Dispersión"])
            x_axis = st.selectbox("Eje X", df.columns)
            y_axis = st.selectbox("Eje Y", numeric_columns)

            if chart_type == "Barras":
                fig = px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} por {x_axis}")
            elif chart_type == "Líneas":
                fig = px.line(df, x=x_axis, y=y_axis, title=f"{y_axis} a lo largo de {x_axis}")
            else:
                fig = px.scatter(df, x=x_axis, y=y_axis, title=f"Relación entre {x_axis} y {y_axis}")

            st.plotly_chart(fig)
        except Exception as e:
            st.error(f"Error al crear el gráfico: {str(e)}")
            st.write("Datos en bruto:", all_sheets_data[sheet])
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

def load_sample_dataset():
    # Dataset de muestra para casos de derecho de familia en Colombia
    sample_data = {
        "Casos de Familia": [
            [
                ["Tipo de Proceso", "Ingresados", "Egresados", "Pendientes", "Tiempo Promedio (días)", "Trimestre"],
                ["Divorcio", 150, 130, 20, 90, "Primer Trimestre"],
                ["Custodia", 80, 70, 10, 60, "Primer Trimestre"],
                ["Alimentos", 200, 180, 20, 45, "Primer Trimestre"],
                ["Adopción", 30, 25, 5, 120, "Primer Trimestre"],
                ["Violencia Intrafamiliar", 100, 95, 5, 30, "Primer Trimestre"],
                ["Total", 560, 500, 60, 69, "Primer Trimestre"],
                ["Divorcio", 140, 145, 15, 85, "Segundo Trimestre"],
                ["Custodia", 85, 80, 15, 65, "Segundo Trimestre"],
                ["Alimentos", 190, 185, 25, 50, "Segundo Trimestre"],
                ["Adopción", 35, 30, 10, 115, "Segundo Trimestre"],
                ["Violencia Intrafamiliar", 110, 105, 10, 35, "Segundo Trimestre"],
                ["Total", 560, 545, 75, 70, "Segundo Trimestre"],
                ["Divorcio", 160, 150, 25, 88, "Tercer Trimestre"],
                ["Custodia", 90, 85, 20, 62, "Tercer Trimestre"],
                ["Alimentos", 210, 200, 35, 48, "Tercer Trimestre"],
                ["Adopción", 40, 35, 15, 118, "Tercer Trimestre"],
                ["Violencia Intrafamiliar", 120, 115, 15, 32, "Tercer Trimestre"],
                ["Total", 620, 585, 110, 69.6, "Tercer Trimestre"],
                ["Divorcio", 155, 160, 20, 87, "Cuarto Trimestre"],
                ["Custodia", 95, 90, 25, 63, "Cuarto Trimestre"],
                ["Alimentos", 205, 215, 25, 47, "Cuarto Trimestre"],
                ["Adopción", 45, 40, 20, 116, "Cuarto Trimestre"],
                ["Violencia Intrafamiliar", 115, 120, 10, 31, "Cuarto Trimestre"],
                ["Total", 615, 625, 100, 68.8, "Cuarto Trimestre"]
            ]
        ],
        "Eficiencia Judicial": [
            [
                ["Indicador", "Valor", "Trimestre"],
                ["Tasa de Resolución", 0.89, "Primer Trimestre"],
                ["Tasa de Congestión", 1.12, "Primer Trimestre"],
                ["Tasa de Pendencia", 0.12, "Primer Trimestre"],
                ["Tasa de Resolución", 0.97, "Segundo Trimestre"],
                ["Tasa de Congestión", 1.14, "Segundo Trimestre"],
                ["Tasa de Pendencia", 0.14, "Segundo Trimestre"],
                ["Tasa de Resolución", 0.94, "Tercer Trimestre"],
                ["Tasa de Congestión", 1.19, "Tercer Trimestre"],
                ["Tasa de Pendencia", 0.19, "Tercer Trimestre"],
                ["Tasa de Resolución", 1.02, "Cuarto Trimestre"],
                ["Tasa de Congestión", 1.16, "Cuarto Trimestre"],
                ["Tasa de Pendencia", 0.16, "Cuarto Trimestre"]
            ]
        ]
    }
    return sample_data

if __name__ == "__main__":
    main()