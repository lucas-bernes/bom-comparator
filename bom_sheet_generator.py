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


df_jlcpcb = pd.DataFrame(generate_resistor(20))
# df_jlcpcb.to_excel('template.xlsx', index=False)
print(df_jlcpcb)
