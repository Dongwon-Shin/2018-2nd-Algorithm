import pandas as pd 
alco2009 = pd.read_csv("niaaa-report2009.csv", index_col="State")
alco2009.max()

print(alco2009.max())