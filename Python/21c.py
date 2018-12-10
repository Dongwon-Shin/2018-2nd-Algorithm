import pandas as pd
from scipy.stats import pearsonr
data = pd.read_csv("^GSPC.csv", index_col = "Date")
print(data["Close"].mean())
print(data["Close"].std())
print(data["Close"].skew())

print(pearsonr(data["Close"], data["Volume"]))