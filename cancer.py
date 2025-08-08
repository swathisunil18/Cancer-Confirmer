import pandas as pd
import sklearn.linear_model as lm
from sklearn.preprocessing import LabelEncoder
mydata = pd.read_csv("cancer.csv")

le=LabelEncoder()
mydata["diagnosis_encoded"]= le.fit_transform(mydata[["diagnosis"]])
x= mydata[["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"]]
y= mydata[["diagnosis_encoded"]]

model=lm.LinearRegression()
model.fit(x,y)


rm = float(input("Enter radius_mean: "))
tm = float(input("Enter texture_mean: "))
pm = float(input("Enter perimeter_mean: "))
am = float(input("Enter area_mean: "))
sm = float(input("Enter smoothness_mean: "))
cm = float(input("Enter compactness_mean: "))
cvm = float(input("Enter concavity_mean: "))
cpm = float(input("Enter concave points_mean: "))
symm = float(input("Enter symmetry_mean: "))
fdm = float(input("Enter fractal_dimension_mean: "))
rse = float(input("Enter radius_se: "))
tse = float(input("Enter texture_se: "))
pse = float(input("Enter perimeter_se: "))
ase = float(input("Enter area_se: "))
sse = float(input("Enter smoothness_se: "))
cse = float(input("Enter compactness_se: "))
cvse = float(input("Enter concavity_se: "))
cpse = float(input("Enter concave points_se: "))
symse = float(input("Enter symmetry_se: "))
fdse = float(input("Enter fractal_dimension_se: "))
rw = float(input("Enter radius_worst: "))
tw = float(input("Enter texture_worst: "))
pw = float(input("Enter perimeter_worst: "))
aw = float(input("Enter area_worst: "))
sw = float(input("Enter smoothness_worst: "))
cw = float(input("Enter compactness_worst: "))
cvw = float(input("Enter concavity_worst: "))
cpw = float(input("Enter concave points_worst: "))
symw = float(input("Enter symmetry_worst: "))
fdw = float(input("Enter fractal_dimension_worst: "))

result = model.predict([[rm,tm,pm,am,sm,cm,cvm,cpm,symm,fdm,rse,tse,pse,ase,sse,cse,cvse,cpse,symse,fdse,rw,tw,pw,aw,sw,cw,cvw,cpw,symw,fdw]])

if result>=0.5:
    print("Cancerous")
else :
    print("Non Cancerous")

