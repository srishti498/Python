import numpy as np
import pandas as pd
data = np.array([["", "Col1", "Col2"],
                 ["Row1", 1, 2],
                 ["Row2", 3, 4]])
df1 = pd.DataFrame(data[1:, 1:], index=data[1:, 0], columns=data[0, 1:])
print(df1)

my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
df2 = pd.DataFrame(my_2darray)
print(df2)

my_dict = {"A": ['1', '3'], "B": ['1', '2'], "C": ['2', '4']}
df3 = pd.DataFrame(my_dict)
print(df3)

my_df = pd.DataFrame(data=[[4], [5], [6], [7]], index=range(0, 4), columns=['A'])
df4 = pd.DataFrame(my_df)
print(df4)

my_series = pd.Series({"United Kingdom": "London", "India": "New Delhi",
                       "United States": "Washington", "Belgium": "Brussels"})
df5 = pd.DataFrame(my_series, columns=["Capital"])
print(df5)

df6 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]))
print(df6.shape)
print(len(df6.index))
