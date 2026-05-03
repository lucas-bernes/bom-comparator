import pandas as pd
import numpy as np


def generate_designator(prefix, count):
    return [f"{prefix}{i}" for i in range(1, count+1)]


def generate_resistor(count):
    values = ['1K', '10K', '100K', '470', '4K7', '5K', '500']
    footprint = ['0603', '0805']

    designators = generate_designator('R', count)

    topCount = np.random.randint(0, count+1)

    shuffled_designators = np.random.permutation(designators)

    top_list = shuffled_designators[:topCount]
    bottom_list = shuffled_designators[topCount:]

    component_list = []

    for i in top_list:
        component_list.append({
            'Comment': np.random.choice(values),
            'topDesignator': i,
            'bottomDesignator': None,
            'Footprint': np.random.choice(footprint)
        })

    for i in bottom_list:
        component_list.append({
            'Comment': np.random.choice(values),
            'topDesignator': None,
            'bottomDesignator': i,
            'Footprint': np.random.choice(footprint)
        })

    return component_list


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
        'topDesignator': lambda x: ', '.join(sorted(x.dropna(), key=lambda d: int(d[1:]))),
        'bottomDesignator': lambda x: ', '.join(sorted(x.dropna(), key=lambda d: int(d[1:])))
    })

    return df_grouped.reset_index()


df_jlcpcb = pd.DataFrame()
df_jlcpcb = pd.concat([
    df_jlcpcb,
    pd.DataFrame(generate_resistor(30)),
    # pd.DataFrame(generate_capacitor(30)),
    # pd.DataFrame(generate_inductor(5)),
    # pd.DataFrame(generate_power_source(3))
], ignore_index=True)

print(join_components(df_jlcpcb))
