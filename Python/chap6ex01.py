import pandas as pd
a = pd.read_csv("lynx.csv")
a["time"] = round(a.time / 10)

a.time =  a["time"]* 10

sum_a.time = a.time.groupby("value").sum()
sum_a.time.sort_values("sum_a.time").head()



