import pandas as pd
import json
import os


def read_file(directorio, nombre, sheet=None):
    """
    Lee un archivo CSV o Excel y devuelve un DataFrame de pandas.
    archivo: la ruta del archivo CSV o Excel a leer.
    sheet: el nombre de la hoja en el archivo Excel. Ignorado si el archivo es CSV.
    columnas: una lista con los nombres de las columnas a leer. Si es None, se leen todas las columnas.
    :return: DataFrame de pandas con los datos del archivo.
    """
    print(f"Leyendo {nombre} del {directorio}")
    source = os.path.join(directorio, nombre)
    # busca el archivo si existe
    if os.path.exists(source):
        if source.endswith('.csv'):
            df = pd.read_csv(source, low_memory=False, encoding='ISO-8859-1')
        else:
            df = pd.read_excel(source, sheet_name=sheet)
        
        print(f"Archivo {nombre} extraido de {directorio}")
        return df
    else:
        print(f"{nombre} no encontrado en {directorio}")  


def create_file(df, path, nombre, codificacion="ISO-8859-1"):
    """
    Guarda un DataFrame de pandas como archivo CSV o Excel.
    df: el DataFrame de pandas a guardar.
    path: la ruta de la carpeta donde se guardará el archivo.
    nombre: el nombre del archivo a guardar.
    """
    if not os.path.exists(path):
        os.makedirs(path)

    if nombre.endswith('.csv'):
        # Guarda el DataFrame como un archivo CSV
        df.to_csv(os.path.join(path, nombre), index=False, encoding=codificacion)
    else:
        # Guarda el DataFrame como un archivo Excel
        df.to_excel(os.path.join(path, nombre), index=False)
    
    print(df)
    print(f"Reporte {nombre}, generado con éxito en {path}")
    

def left_join(df_list, llave, duplicates=None):
    """
    Realiza un join left de múltiples DataFrames en una lista, en base a las columnas especificadas.
    df_list: una lista de DataFrames de pandas.
    llave: una lista de nombres de columnas para unir los DataFrames.
    df_fucinado: un nuevo DataFrame que resulta de unir todos los DataFrames en la lista.
    """
    # Verifica que la lista tenga al menos dos DataFrames
    if len(df_list) < 2:
        raise ValueError("La lista debe contener al menos dos DataFrames para hacer un join.")

    # Realiza el join iterativamente
    df_fucionado = df_list[0]
    for df in df_list[1:]:
        df_fucionado = pd.merge(df_fucionado, df, how='left', on = llave)

    if duplicates == None:
        df_fucionado = df_fucionado.drop_duplicates(subset=llave).reset_index(drop=True)
    else:
        df_fucionado = df_fucionado.drop_duplicates(subset=duplicates).reset_index(drop=True)
        
    return df_fucionado


def join_files(directorio):
    """
    Uso de la función
    directorio = "ruta/del/directorio"
    df_combinado = join_files(directorio)
    print(df_combinado)
    """

    print(f"Unificando los archivos del directorio: {directorio}")
    # Crear un DataFrame vacío para almacenar los datos combinados
    df_total = pd.DataFrame()

    # Iterar sobre todos los archivos en el directorio
    for archivo in os.listdir(directorio):
        # Obtener la extensión del archivo
        _, extension = os.path.splitext(archivo)

        # Verificar si la extensión es .xlsx, .xls o .csv
        if extension in ['.xlsx', '.xls', '.csv']:
            # Construir la ruta completa del archivo
            ruta_completa = os.path.join(directorio, archivo)

            # Leer el archivo dependiendo de su extensión
            if extension in ['.xlsx', '.xls']:
                df = pd.read_excel(ruta_completa)
            elif extension == '.csv':
                df = pd.read_csv(ruta_completa)

            # Combinar los DataFrames por columnas (unión horizontal)
            df_total = pd.concat([df_total, df])
    print("Archivos Unificados")
    return df_total

def json_file(carpeta, archivo):
    source = os.path.join(carpeta, archivo)
    with open(source, encoding='utf-8') as file:
        return json.load(file)


def merge_columns(df, col_list, new_column):
    # Verificar si el número de encabezados a unificar es válido
    num_cols = len(col_list)
    
    if num_cols < 1:
        return df  # No se realiza ninguna acción si no se proporcionan encabezados para unificar
    
    # Crear la nueva columna de destino con los valores unificados
    df[new_column] = ""
    
    # Unificar los valores de las columnas especificadas en col_list
    for i in range(0, num_cols):
        try:
            df[col_list[i]].fillna("")
            df[new_column] = df[new_column] + df[col_list[i]].astype(str).replace("nan","")
        except KeyError:
            print(f"Warning: La columna '{col_list[i]}' no esta en el index")
            continue  # Continuar con la siguiente iteración del bucle en caso de no se encuentr el index
    
    # Eliminar las columnas originales si es necesario
    if new_column in col_list:
        col_list.remove(new_column)
        columns_to_drop = [col for col in col_list if col in df.columns]
        df = df.drop(columns=columns_to_drop)
    else:
        columns_to_drop = [col for col in col_list if col in df.columns]
        df = df.drop(columns=columns_to_drop)
        
    return df