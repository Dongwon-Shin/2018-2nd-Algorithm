import pandas as pd
import numpy as np
alco = pd.read_csv("niaaa-report.csv", index_col=["State", "Year"])
alco["Total"] = alco.Wine + alco.Spirits + alco.Beer
alco.head()
print(alco.head())
np.log10(alco.Total).head()
print(np.log10(alco.Total).head())

dna = "AGTCCGCGAATACAGGCTCGGT"
dna1 = dna.replace("C", "")
dna2 = dna.replace("T", "")
dna_as_series1 = pd.Series(list(dna1), name="genes")
dna_as_series2 = pd.Series(list(dna2), name="genes")
dna_as_series1.value_counts() + dna_as_series2.value_counts()

print(dna_as_series1.value_counts() + dna_as_series2.value_counts())
