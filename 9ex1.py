import pandas as pd
data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print(series)
series2 = series + 10
print(series2)
# Filtering
filtered_series = series[series > 2]
print(filtered_series)
# Statistical Calculations
mean_value = series.mean()
print(mean_value)
