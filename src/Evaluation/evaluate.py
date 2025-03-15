import pandas as pd
from pycaret.regression import setup, compare_models, pull, save_model

def load_data(file_path):
    return pd.read_csv(file_path)

def train_models(df, target):
    setup(data=df, target=target, session_id=42, verbose=False) 
    best_model = compare_models(n_select=1)
    return best_model

def save_best_model(model, model_path):
    save_model(model, model_path)

def main():
    df = load_data("../../data/raw/data.csv")

    targets = ["Malaria_Cases", "Chikungunya_Cases", "Dengue_Cases"]
    names = ["Malaria", "Chikungunya", "Dengue"]

    for target, name in zip(targets, names):
        best_model = train_models(df, target)
        save_best_model(best_model, f"../Models/{name}Model.pkl")

if __name__ == "__main__":
    main()