import pandas as pd
import numpy as np


def generate_designator(prefix, count):
    return [f"{prefix}{i}" for i in range(1, count+1)]


def generate_resistor(count):
    values = ['1K', '10K', '100K', '470', '4K7', '5K', '500']
    footprint = ['0603', '0805']

    designators = generate_designator('R', count)

    return [
        {
            'Comment': np.random.choice(values),
            'Designators': i,
            'Footprint': np.random.choice(footprint)
        }
        for i in designators
    ]


def generate_capacitor(count):
    values = ['1u', '10p', '100p', '220n', '100n', '10n', '2200n']
    footprint = ['0603', '0805']

    designators = generate_designator('C', count)

    return [
        {
            'Comment': np.random.choice(values),
            'Designators': i,
            'Footprint': np.random.choice(footprint)
        }
        for i in designators
    ]


def generate_inductor(count):
    values = ['1uH', '10uH', '100uH']
    footprint = ['0603', '0805']

    designators = generate_designator('L', count)

    return [
        {
            'Comment': np.random.choice(values),
            'Designators': i,
            'Footprint': np.random.choice(footprint)
        }
        for i in designators
    ]


def generate_power_source(count):
    values = ['12V', '5V', '-12V', '-5V', '6V', '9V']
    footprint = ['0603', '0805']

    designators = generate_designator('PS', count)

    return [
        {
            'Comment': np.random.choice(values),
            'Designators': i,
            'Footprint': np.random.choice(footprint)
        }
        for i in designators
    ]


def join_components(df):

    df_grouped = df.groupby(['Comment', 'Footprint']).agg({
        'topDesignator': lambda x: ', '.join(x.dropna()),
        'bottomDesignator': lambda x: ', '.join(x.dropna())
    })

    return df_grouped


df_jlcpcb = pd.DataFrame()
df_jlcpcb = pd.concat([
    df_jlcpcb,
    pd.DataFrame(generate_resistor(30)),
    pd.DataFrame(generate_capacitor(30)),
    pd.DataFrame(generate_inductor(5)),
    pd.DataFrame(generate_power_source(3))
], ignore_index=True)

print(df_jlcpcb)
