# Calculates measures of central tendency and drawing boxplot
# to check for potential outliers

import init
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Measures of Central Tendency
data1 = init.get_cleaned_dataset1()
df = data1['seconds_after_rat_arrival']
print("Measures of central tendencies for seconds_after_rat_arrival:")
info = df.describe()

df.hist(bins=20)
plt.title('Histogram of seconds_after_rat_arrival')
plt.savefig("result/histogram.png")
plt.show()



print(info)

print("====================================")

data2 = init.get_cleaned_dataset2()
df = data2[['bat_landing_number', 'rat_arrival_number']]
print("Measures of central tendencies for bat_landing_number and rat_arrival_number:")
info = df.describe()
print(info)

# Mode check for column risk
print("====================================")

df = data1
df.loc[df['risk'] == 0, 'risk_label'] = "Avoid risk"
df.loc[df['risk'] == 1, 'risk_label'] = "Takes risk"
df = df['risk_label']
risk_count = df.value_counts()
risk_count.plot(kind='bar')
plt.title("Risk takers & risk avoiders count comparison")
plt.savefig("result/risk_taker_avoider_barchar.png")
plt.show()
plt.close()

# Outlier check
sns.set_theme(style="whitegrid")  

# outlier check for seconds_after_rat_arrival
df = data1['seconds_after_rat_arrival']
sns.boxplot(y=df)
plt.title("Outlier check for seconds_after_rat_arrival")
plt.ylabel("Seconds after rat's arrival")
plt.savefig("result/seconds_after_rat_arrival_boxplot.png")
plt.show()
plt.close()

# checking at the result manually, there isn't any outliers
print("seconds_after_rat_arrival does not have notable outlier values.")
print("====================================")

# outlier check for bat_landing_number
df = data2['bat_landing_number']
sns.boxplot(y=df)
plt.title("Outlier check for bat_landing_number")
plt.ylabel("Bat landing number in 30 mins interval")
plt.savefig("result/bat_landing_number_boxplot.png")
plt.show()
plt.close()

# the outliers can be found at value above 100
outliers = [i for i in df if i > 100]
print("Outliers for bat_landing_number are: ", outliers)
print("====================================")


# outlier check for rat_arrival_number
df = data2['rat_arrival_number']
sns.boxplot(y=df)
plt.title("Outlier check for rat_arrival_number")
plt.ylabel("Rat arrival number in 30 mins interval")
plt.savefig("result/rat_arrival_number_boxplot.png")
plt.show()
plt.close()


# the outliers can be found at value above 2
outliers = [i for i in df if i > 2]
print("Outliers for rat_arrival_number are: ", outliers)
print("====================================")
