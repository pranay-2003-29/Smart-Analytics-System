import pandas as pd

def extract_data():
    df = pd.read_csv("D://college//projects//Smart Analytics System (Data Engineering + AI)//data//raw//WA_Fn-UseC_-Telco-Customer-Churn.csv")
    print("Data extracted successfully")
    return df

if __name__ == "__main__":
    extract_data()
