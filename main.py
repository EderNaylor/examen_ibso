from display_fav_number import display_favorite_number
from save_fav_number import save_favorite_number
from store_analysis import analyze_store_sales
from two_favorite_numbers import add_two_numbers

from functions.data_ops import read_file


if __name__ == "__main__":
    dir = "files"
    file_name = "2020_12_10 - BD Ventas (Ligero).xlsx"
    df_ventas = read_file(dir, file_name, sheet='Base de datos')

    analyze_store_sales(df_ventas)
    save_favorite_number()
    display_favorite_number()
    add_two_numbers()
