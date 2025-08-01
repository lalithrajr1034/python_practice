import pandas as pd

df = pd.read_csv(
    r"C:\Users\LALITH RAJ R\OneDrive\Desktop\python_practice\MACHIE_LEARNING\sharemarket\NIFTY50_60d_5min.csv",
    parse_dates=["datetime"]
)

print(df.head())
