import pandas as pd
db=pd.read_csv("employees.csv")
#Read the CSV file into a DataFrame
#print(db)
#Shape of CSV file
#print(db.shape)
#First 5 rows
#print(db.head())
#Print employees earn more than 50000
#earners=db[db["SALARY"]>50000]
#print(earners)
#Filter by specific department
marketing = db[db["DEPARTMENT"] ==  "MARKETING"]
print(marketing)
#Bonus Column
#db["raise_amount"]=db["SALARY"]*0.05
#db["new_salary"]=db["SALARY"]+db["raise_amount"]
#print(db)

#TODO 5: Group by department, get total salary per department
#dept_salary=db.groupby("DEPARTMENT")["SALARY"].sum()
#print(dept_salary)

#TODO 6: Find average salary,Find max salary,Find min salary,Print all three
#avgsalary= db["SALARY"].mean()
#maxsalary= db["SALARY"].max()
#minsalary= db["SALARY"].min()
#print(" Average Salary:"+str(avgsalary))
#print(" Highest Salary:"+str(maxsalary))
#print(" Lowest  Salary:"+str(minsalary))

#TODO 7:SORTING SALARY FROM HIGHEST TO LOWEST
#dbsorted= db.sort_values("SALARY", ascending=False)
#print(dbsorted.head(5))
