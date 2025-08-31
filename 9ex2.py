import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)
print(df[['Name']])
df['Salary'] = [70000, 80000, 90000]
print(df)
df = df.drop('City', axis=1)
print(df)
print(df.loc[[0]])
print(df.loc[[0, 1]])



import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)
