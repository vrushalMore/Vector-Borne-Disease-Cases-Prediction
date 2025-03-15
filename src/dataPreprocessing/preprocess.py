import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

def load_data(file_path):
    df = pd.read_csv(file_path, parse_dates=["Date"])
    return df

def extract_date_features(df):
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Day"] = df["Date"].dt.day
    df.drop(columns=["Date"], inplace=True)
    return df

def define_transformers():
    numeric_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])
    
    categorical_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])
    
    return numeric_transformer, categorical_transformer

def preprocess_data(df):
    numeric_features = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_features = df.select_dtypes(include=["object"]).columns.tolist()

    numeric_transformer, categorical_transformer = define_transformers()

    preprocessor = ColumnTransformer(transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ])

    processed_data = preprocessor.fit_transform(df)
    return pd.DataFrame(processed_data)

def save_data(df, output_path):
    df.to_csv(output_path, index=False)

def main():
    df = load_data("data.csv")
    df = extract_date_features(df)
    df_processed = preprocess_data(df)
    save_data(df_processed, "../../data/processed/processed_data.csv")

if __name__ == "__main__":
    main()
