import pandas as pd

# Load dataset
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Show first 5 rows
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing Age values
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Embarked values
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned data
df.to_csv("cleaned_dataset.csv", index=False)

print("\nData Cleaning Completed Successfully!")
print(df.head())
print(df.isnull().sum())
print(df.duplicated().sum())
print("Loaded Data:")
print(df.head())

print("\nDataset Info:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())