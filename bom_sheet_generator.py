import pandas as pd
import numpy as np
import re


def generate_designator(prefix, count):
    return [f"{prefix}{i}" for i in range(1, count+1)]


def generate_component_base(prefix, count, values, footprints=('0603', '0805')):
    return [
        {
            'Comment': np.random.choice(values),
            'Designator': designator,
            'Footprint': np.random.choice(footprints)
        }
        for designator in generate_designator(prefix, count)
    ]


def make_altium_bom(df_base):
    return df_base.copy()


def make_jlcpcb_bom(df_base):
    df_jlc = df_base.copy()

    is_top = np.random.choice([True, False], size=len(df_jlc))

    df_jlc['topDesignator'] = df_jlc['Designator'].where(is_top, None)
    df_jlc['bottomDesignator'] = df_jlc['Designator'].where(~is_top, None)

    df_jlc = df_jlc.drop(columns='Designator')

    return df_jlc


def designator_number(designator):
    return int(re.search(r'\d+', designator).group())


def join_components_jlcpcb(df):
    df_grouped = df.groupby(['Comment', 'Footprint']).agg({
        'topDesignator': lambda x: ', '.join(sorted(x.dropna(), key=designator_number)),
        'bottomDesignator': lambda x: ', '.join(sorted(x.dropna(), key=designator_number))
    })

    return df_grouped.reset_index()


def join_components_altium(df):
    df_grouped = df.groupby(['Comment', 'Footprint']).agg({
        'Designator': lambda x: ', '.join(sorted(x, key=designator_number))
    })

    return df_grouped.reset_index()


def drop_component(df):
    quantity = np.random.randint(0, len(df)+1)
    df.drop(np.random.choice(df.index, quantity, replace=False), inplace=True)
    df.reset_index(drop=True, inplace=True)


df_base = pd.concat([
    pd.DataFrame(generate_component_base(
        'R', 30, ['1K', '10K', '100K', '470', '4K7', '5K', '500'])),

    pd.DataFrame(generate_component_base(
        'C', 30, ['1u', '10p', '100p', '220n', '100n', '10n', '2200n'])),

    pd.DataFrame(generate_component_base(
        'L', 5, ['1uH', '10uH', '100uH'])),

    pd.DataFrame(generate_component_base(
        'PS', 3, ['12V', '5V', '-12V', '-5V', '6V', '9V']))
], ignore_index=True)


df_altium_base = make_altium_bom(df_base)
df_jlcpcb_base = make_jlcpcb_bom(df_base)

drop_component(df_altium_base)
drop_component(df_jlcpcb_base)

df_altium = join_components_altium(df_altium_base)
df_jlcpcb = join_components_jlcpcb(df_jlcpcb_base)

df_altium.index = df_altium.index + 1


df_altium.to_excel(
    'data/altium_bom.xlsx', index=True, startrow=np.random.randint(3, 12)
)

df_jlcpcb.to_excel(
    'data/jlcpcb_bom.xlsx', index=False
)
