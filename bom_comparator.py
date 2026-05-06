from pathlib import Path
import pandas as pd


DATA_DIR = Path('data')
OUTPUT_DIR = Path('outputs')


def find_header_row_altium(df):

    for index, row in df.iterrows():
        if 'Designator' in row.astype(str).values:
            print(f' BOM Header Index: {index} \n')
            return index

    return None
    # procurar linha onde aparece Comment, Footprint, Designator


def read_altium_bom(file_path):
    df = pd.read_excel(file_path)
    head_index = find_header_row_altium(df)
    print(df)
    return df
    # usar find_header_row_altium
    # retornar df normalizado com Comment, Footprint, Designator


def read_jlcpcb_bom(file_path):
    df = pd.read_excel(file_path)
    return df
    # ler direto
    # juntar topDesignator e bottomDesignator em uma coluna Designator
    # retornar df normalizado


def split_designators(df):
    # transformar "R1, R2, R3" em linhas separadas
    pass


def compare_boms(df_altium, df_jlcpcb):
    # comparar designators
    # gerar faltantes no JLCPCB e faltantes no Altium
    pass


def export_results(df_result):
    OUTPUT_DIR.mkdir(exist_ok=True)
    df_result.to_excel(OUTPUT_DIR / 'missing_components.xlsx', index=False)


def main():
    altium_path = DATA_DIR / 'altium_bom.xlsx'
    jlcpcb_path = DATA_DIR / 'jlcpcb_bom.xlsx'

    df_altium = read_altium_bom(altium_path)
    df_jlcpcb = read_jlcpcb_bom(jlcpcb_path)

    # df_result = compare_boms(df_altium, df_jlcpcb)

    # export_results(df_result)


if __name__ == '__main__':
    main()
