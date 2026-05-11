from pathlib import Path
import pandas as pd


DATA_DIR = Path('data')
OUTPUT_DIR = Path('outputs')


def normalize_footprint(df):
    df['Footprint'] = df['Footprint'].astype(str).str.zfill(4)
    return df


def find_header_row_altium(df):

    for index, row in df.iterrows():
        if 'Designator' in row.astype(str).values:
            print(f'Altium BOM Header Index: {index} \n')
            return index

    return None


def read_altium_bom(file_path):

    # 1. Read the file skipping the first index column from Excel
    df = pd.read_excel(file_path).iloc[:, 1:]

    # 2. Find the row where the actual header is located
    head_index = find_header_row_altium(df)

    # 3. Slice the dataframe to remove everything above the header
    df = df.iloc[head_index:].reset_index(drop=True)

    # 4. Set the first row as the column names
    df.columns = df.iloc[0]

    # 5. Remove the row used as header and reset the index
    df = df.iloc[1:].reset_index(drop=True)

    df = split_designators(df)
    df = normalize_footprint(df)
    return df


def read_jlcpcb_bom(file_path):

    df = pd.read_excel(file_path)
    df['Designator'] = (
        df['topDesignator'].fillna('') +
        ', ' +
        df['bottomDesignator'].fillna('')
    )

    # clear remaining commas
    df['Designator'] = (
        df['Designator']
        .str.strip(', ')
        .str.replace(r',\s*,', ',', regex=True)
    )
    df = df.drop(columns=['topDesignator', 'bottomDesignator'],)

    df = split_designators(df)
    df = normalize_footprint(df)
    return df


def split_designators(df):
    df['Designator'] = df['Designator'].apply(lambda x: x.split(', '))
    return df.explode('Designator').reset_index(drop=True)


def compare_boms(df_altium, df_jlcpcb):

    df_compare = df_altium.merge(
        df_jlcpcb,
        on=['Comment', 'Footprint', 'Designator'],
        how='left',
        indicator=True
    )

    missing_components = df_compare[df_compare['_merge'] == 'left_only']

    return missing_components.drop(columns=['_merge']).reset_index(drop=True)


def export_results(df_result, file_name='missing_components.xlsx'):

    OUTPUT_DIR.mkdir(exist_ok=True)

    output_path = OUTPUT_DIR / file_name

    df_result.to_excel(output_path, index=False)

    print(f'Results exported to: {output_path}')


def main():
    altium_path = DATA_DIR / 'altium_bom.xlsx'
    jlcpcb_path = DATA_DIR / 'jlcpcb_bom.xlsx'

    df_altium = read_altium_bom(altium_path)
    df_jlcpcb = read_jlcpcb_bom(jlcpcb_path)

    df_result = compare_boms(df_altium, df_jlcpcb)

    export_results(df_result)


if __name__ == '__main__':
    main()
