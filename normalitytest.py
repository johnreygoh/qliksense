import pandas as pd
from scipy import stats

# Load your CSV dataset
df = pd.read_csv('storeTransactions.csv')  # Replace 'your_dataset.csv' with the actual file path

# Select the column for which you want to perform the normality tests
column_to_test = df['Sales']  # Replace 'ColumnName' with the name of your column

# Shapiro-Wilk Test
shapiro_stat, shapiro_p = stats.shapiro(column_to_test)
print("Shapiro-Wilk Test:")
print(f"Statistic: {shapiro_stat}")
print(f"P-value: {shapiro_p}")
if shapiro_p > 0.05:
    print("Data looks normally distributed (fail to reject H0)")
else:
    print("Data does not look normally distributed (reject H0)")

# Anderson-Darling Test
anderson_stat, anderson_critical, anderson_significance = stats.anderson(column_to_test)
print("\nAnderson-Darling Test:")
print(f"Statistic: {anderson_stat}")
print(f"Critical Values: {anderson_critical}")
if anderson_stat < anderson_critical[2]:
    print("Data looks normally distributed (fail to reject H0)")
else:
    print("Data does not look normally distributed (reject H0)")

# Kolmogorov-Smirnov Test (against a normal distribution)
ks_stat, ks_p = stats.kstest(column_to_test, 'norm')
print("\nKolmogorov-Smirnov Test (against a normal distribution):")
print(f"Statistic: {ks_stat}")
print(f"P-value: {ks_p}")
if ks_p > 0.05:
    print("Data follows a normal distribution (fail to reject H0)")
else:
    print("Data does not follow a normal distribution (reject H0)")
