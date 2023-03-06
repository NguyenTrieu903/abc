import pandas as pd
from unidecode import unidecode
df = pd.read_csv('diemthi2022.csv')

df['Province/City'] = df['Province/City'].apply(lambda x: unidecode(x))
print(df)
df.to_csv('data2.csv', index=False)
