import pandas as pd
import io
hospital_data = """gender,disease,age,bill_amount,doctor
Male,Viral,35,1200,Dr.Sharma
Female,Dengue,42,4500,Dr Verma
Female,Viral, 28,1500,Dr Sharma
Male,Malaria,61,8000,Dr.Khan
Male,Dengue,61,8000,Dr Verma
Female,Viral,45,2000,Dr Sharma"""
df=pd.read_csv(io.StringIO(hospital_data))
df["doctor"]=df["doctor"].str.replace("."," ",regex=False).str.strip()
                                      
print("---hospital patient_ data---")
print(df)

print("\ntotal patients:",len(df)) 

print("\ngender count")
print(df["gender"].value_counts())

print("\ndisease-wise Patients")
print(df["disease"].value_counts())

print("\naverage age:",df["age"].mean())

print("\ntotal revenue:",df["bill_amount"].sum())
 

print("\ndoctor_wise revenue:")
print(df.groupby("doctor")["bill_amount"].sum())

highest=df.loc[df["bill_amount"].idxmax()]
print("\nhighest bill patient:")
print(highest)
       
 
 
 
