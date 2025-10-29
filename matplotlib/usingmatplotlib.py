import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv')


print("Head of data:\n", df.head())
print("\nTail of data:\n", df.tail())
print("\nNull values:\n", df.isnull().sum())


if 'Marks' in df.columns and 'Age' in df.columns:
    plt.plot(df['Age'], df['Marks'], marker='o', color='orange')
    plt.title('Age vs Marks')
    plt.xlabel('Age')
    plt.ylabel('Marks')
    plt.grid(True)
    plt.show()