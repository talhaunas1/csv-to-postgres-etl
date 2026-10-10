import pandas as pd
from sqlalchemy import create_engine


#extract
df = pd.read_csv("data/superstore.csv", encoding="latin-1")


print(df.shape)
print(df.head())


print(df.info)



