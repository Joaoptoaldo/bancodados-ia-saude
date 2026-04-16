import pandas as pd

URL = (
    "https://info.dengue.mat.br/api/alertcity"
    "?geocode=4316907"  # Código IBGE correto
    "&disease=dengue"
    "&format=csv"
    "&ew_start=1"
    "&ew_end=52"
    "&ey_start=2022"
    "&ey_end=2023"
)

df = pd.read_csv(URL)

df = df[
    [
       "data_iniSE",
        "casos",
        # "temp_min", 
        # "umid_med", 
        "Rt"
    ]
].dropna()

df["media_movel"] = df["casos"].rolling(4).mean()

df = df.dropna()

df.to_json(
    "../backend/data.json",
    orient="records",
    date_format="iso"
)

print("Dados epidemiológicos salvos:", len(df))