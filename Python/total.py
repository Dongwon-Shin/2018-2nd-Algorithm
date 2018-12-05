import pandas as pd
alco = pd.read_csv("niaaa-report.csv", index_col=["State", "Year"])
alco_nodix = alco.reset_index()
sum_alco = alco_nodix.groupby("Year").sum()
sum_alco.tail()
print(sum_alco.tail())