import init
import pandas as pd

data1_original = pd.read_csv("dataset1.csv")
data2_original = pd.read_csv("dataset2.csv")
data1_cleaned = init.get_cleaned_dataset1()
data2_cleaned = init.get_cleaned_dataset2()

print("Row count for dataset1 before cleanup:", len(data1_original))
print("Row count for dataset1 after cleanup:", len(data1_cleaned))
print("====================================")
print("Row count for dataset2 before cleanup:", len(data2_original))
print("Row count for dataset2 after cleanup:", len(data2_cleaned))
