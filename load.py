import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:root@localhost/smart_analytics")

df = pd.read_csv("D://college//projects//Smart Analytics System (Data Engineering + AI)//data//processed//clean_churn.csv")
df.to_sql("churn_data", engine, if_exists="replace", index=False)

print("Data loaded into warehouse")
