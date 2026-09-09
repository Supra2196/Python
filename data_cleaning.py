import pandas as pd
df=pd.read_csv(r"C:\Users\supra\OneDrive\Documents\CMC_Internshipweek2\Messy_Employee_dataset.csv")
#1-Identify missing values
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.dtypes)
#2-Remove Duplicates
df=df.drop_duplicates(subset=["Email"])
print("Rows after removing duplicates", df.shape[0])
print("Duplicate emails:", df.duplicated(subset=["Email"]).sum())
#3-Handle missing values
print("Missing before:")
print(df.isnull().sum())
df["Age"]=df["Age"].fillna(df["Age"].median())
df["Salary"]=df["Salary"].fillna(df["Salary"].median())
print("Missing after:")
print(df.isnull().sum())
#4-Standardize text columns
df["First_Name"]=df["First_Name"].str.strip().str.lower()
df["Last_Name"]=df["Last_Name"].str.strip().str.lower()
df["Department_Region"]=df["Department_Region"].str.strip().str.lower()
df["Status"]=df["Status"].str.strip().str.lower()
df["Performance_Score"]=df["Performance_Score"].str.strip().str.lower()
print(df[["First_Name","Last_Name","Department_Region", "Status"]].head())
#5-Convert Datatypes
print("Data types Before")
print(df.dtypes)
df["Join_Date"]=pd.to_datetime(df["Join_Date"], errors = "coerce")
print("Data types After")
print(df.dtypes)
#6-Make a  new file with the data
df.to_csv("Cleaned_Employee_dataset.csv",index=False)
print("And its saved!")
#7-Summary
original=pd.read_csv(r"C:\Users\supra\OneDrive\Documents\CMC_Internshipweek2\Messy_Employee_dataset.csv")
original_shape=original.shape
cleaned_shape=df.shape
print("Original Shape"+str(original_shape))
print("Cleaned Shape"+str(cleaned_shape))
