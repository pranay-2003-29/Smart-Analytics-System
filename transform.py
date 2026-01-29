import pandas as pd

def transform_data(df):
    # Drop customer ID (not useful for ML)
    df = df.drop(columns=["customerID"])

    # Convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Handle missing values
    df = df.dropna()

    # Encode target variable
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    # One-hot encoding
    df = pd.get_dummies(df, drop_first=True)

    print("Data transformed successfully")
    return df

if __name__ == "__main__":
    raw_df = pd.read_csv("D://college//projects//Smart Analytics System (Data Engineering + AI)//data//raw//WA_Fn-UseC_-Telco-Customer-Churn.csv")
    clean_df = transform_data(raw_df)
    clean_df.to_csv("D://college//projects//Smart Analytics System (Data Engineering + AI)//data//processed//clean_churn.csv", index=False)
