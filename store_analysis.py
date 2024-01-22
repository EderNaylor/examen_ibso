from functions.data_ops import read_file
import pandas as pd


def analyze_store_sales(df):
    """
    filter data to show only one store (Código tienda) during year 2022 
    and month 12 (fecha de venta). Group sales (pieces) by 
    clothing category (Descriptor artículo 3) and calculate 
    the percentage of the total sales of each category.
    """
    # Convert 'Fecha de venta' to datetime and filter for December 2022


    df['Fecha de venta'] = pd.to_datetime(df['Fecha de venta'], format="%Y-%m-%d", errors='coerce')
    df['Código Tienda'] = df['Código Tienda'].astype(int)
    df = df[(df['Fecha de venta'].dt.month == 12) & (df['Fecha de venta'].dt.year == 2022)]  

    id_tienda = df["Código Tienda"].drop_duplicates().tolist()
    print(f"Codigos de tienda disponibles {id_tienda}")  

    store_code = input("Inserta código de Tienda: ")
    # Convertimos la cadena a un entero usando int()
    try:
        store_code = int(store_code)
        print("El número entero que ingresaste es:", store_code)
        store_code = int(store_code)
        df = df[df['Código Tienda'] == store_code]
        # Agrupar por 'producto' y sumar la cantidad vendida
        ventas_por_producto = df.groupby('Descriptor de artículo 3')['Cantidad vendida'].sum().reset_index()

        # Calcular el porcentaje de ventas para cada producto
        total_ventas = ventas_por_producto['Cantidad vendida'].sum()
        ventas_por_producto['porcentaje_ventas'] = (ventas_por_producto['Cantidad vendida'] / total_ventas) * 100
        # Formatear la columna 'porcentaje_ventas' con dos decimales y símbolo '%'
        ventas_por_producto['porcentaje_ventas'] = ventas_por_producto['porcentaje_ventas'].apply(lambda x: f'{x:.2f}%')

        # Imprimir el resultado
        print(ventas_por_producto)
    
    except ValueError:
        print("Error: No ingresaste un número entero válido.")




dir = "files"
file_name = "2020_12_10 - BD Ventas (Ligero).xlsx"
df_ventas = read_file(dir, file_name, sheet='Base de datos')


analyze_store_sales(df_ventas)
