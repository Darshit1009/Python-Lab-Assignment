import pandas as pd
series1 = pd.Series(['a', 'b', 'c', 'd'])
series2 = pd.Series([1, 2, 3, 4])
vertical_stack = pd.concat([series1, series2], axis=0)
print("Vertical stack:")
print(vertical_stack)
horizontal_stack = pd.concat([series1, series2], axis=1)
print("\nHorizontal stack:")
print(horizontal_stack)
