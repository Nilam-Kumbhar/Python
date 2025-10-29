import pandas as pd
data = {
    'Name': ['Amit', 'Priya', 'Raj', 'Meena'],
    'Age': [21, 22, 20, 23],
    'Marks': [85, 90, 78, 84],
    'City': ['Pune', 'Mumbai', 'Delhi', 'Chennai']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

print("\nSelect 'Name' column:")
print(df['Name'])
print("\nSelect first 2 rows:")
print(df.head(2))
print("\nselect last 2 rows:")
print(df.tail(2))

df['Result'] = ['Pass', 'Pass', 'Fail', 'Pass']
print("\After adding new column:")
print(df)

print("\nStudents with Marks > 80:")
print(df[df['Marks'] > 80])

print("\nSorted by Marks:")
print(df.sort_values('Marks', ascending=False))

print("\nAverage Marks by Result:")
print(df.groupby('Result')['Marks'].mean())

print("\nAverage Marks:", df['Marks'].mean())
print("Maximum Marks:", df['Marks'].max())
