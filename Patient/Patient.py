import pandas as pd


#loading the patientset
patient = pd.read_csv("D:/BLR10AM/Assi/30.survival analytics/Datasets_Survival Analytics/Patient.csv")

#2.	Work on each feature of the patientset to create a patient dictionary as displayed in the below image
#######feature of the patientset to create a patient dictionary

#######feature of the patientset to create a patient dictionary


patient_details =pd.DataFrame({"column name":patient.columns,
                            "patient type(in Python)": patient.dtypes})

            #3.	patient Pre-patientcessing
          #3.1 patient Cleaning, Feature Engineering, etc
          

            

#details of patient 
patient.info()
patient.describe()          


#patient types        
patient.dtypes



#checking for na value
patient.isna().sum()
patient.isnull().sum()

#checking unique value for each columns
patient.nunique()



"""	Exploratory patient Analysis (EDA):
	Summary
	Univariate analysis
	Bivariate analysis """
    

EDA ={"column ": patient.columns,
      "mean": patient.mean(),
      "median":patient.median(),
      "mode":patient.mode(),
      "standard deviation": patient.std(),
      "variance":patient.var(),
      "skewness":patient.skew(),
      "kurtosis":patient.kurt()}

EDA




# covariance for patient set 
covariance = patient.cov()
covariance

# Correlation matrix 
co = patient.corr()
co


import seaborn as sns
####### graphipatient repersentation



#boxplot for every continuous type data
patient.columns
patient.nunique()

patient.boxplot(column=['Followup'])   #no outlier
 

# Boxplot of independent variable distribution for each category of Result 
sns.boxplot(x = "Eventtype", y = "Followup", data = patient)



# Scatter plot for each categorical Result of car
sns.stripplot(x = "Eventtype", y = "Followup", jitter = True, data = patient)


"""4.	Model Building
4.1Build the model on the scaled data (try multiple options)
4.2Perform Survival analytics on the given datasets.

4.3Briefly explain the model output in the documentation. 
"""

# followup is referring to time 
f=patient.Followup

# Importing the KaplanMeierFitter model to fit the survival analysis
from lifelines import KaplanMeierFitter

# Initiating the KaplanMeierFitter model
kmf = KaplanMeierFitter()

# Fitting KaplanMeierFitter model on Time and Events for death 
kmf.fit(f, event_observed=patient.Eventtype)

# Time-line estimations plot 
kmf.plot()
