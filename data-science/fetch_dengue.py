import pandas as pd

URL = (
    "https://info.dengue.mat.br/api/alertcity?geocode=4106902&disease=dengue&format=csv&ew_start=1&ew_end=50&ey_start=2017&ey_end=2017"  
)

df = pd.read_csv(URL)

df = df[
    [
        "data_iniSE",
        "casos",
        "tempmin",
        "umidmed",
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

print("Dados salvos:", len(df))