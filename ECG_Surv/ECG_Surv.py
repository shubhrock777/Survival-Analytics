import pandas as pd


#loading the ecgset
ecg = pd.read_excel("D:/BLR10AM/Assi/30.survival analytics/Datasets_Survival Analytics/ECG_Surv.xlsx")

#2.	Work on each feature of the ecgset to create a ecg dictionary as displayed in the below image
#######feature of the ecgset to create a ecg dictionary

#######feature of the ecgset to create a ecg dictionary


ecg_details =pd.DataFrame({"column name":ecg.columns,
                            "ecg type(in Python)": ecg.dtypes})

            #3.	ecg Pre-ecgcessing
          #3.1 ecg Cleaning, Feature Engineering, etc
          

            

#details of ecg 
ecg.info()
ecg.describe()          


ecg.drop(columns=["name"],inplace = True) # dropind row num 1


#ecg types        
ecg.dtypes



#checking for na value
ecg.isna().sum()
ecg.isnull().sum()

#checking unique value for each columns
ecg.nunique()



"""	Exploratory ecg Analysis (EDA):
	Summary
	Univariate analysis
	Bivariate analysis """
    

EDA ={"column ": ecg.columns,
      "mean": ecg.mean(),
      "median":ecg.median(),
      "mode":ecg.mode(),
      "standard deviation": ecg.std(),
      "variance":ecg.var(),
      "skewness":ecg.skew(),
      "kurtosis":ecg.kurt()}

EDA




# covariance for ecg set 
covariance = ecg.cov()
covariance

# Correlation matrix 
co = ecg.corr()
co


import seaborn as sns
####### graphiecg repersentation



#boxplot for every continuous type data
ecg.columns
ecg.nunique()

ecg.boxplot(column=["survival_time_hr"])   #no outlier
 

sns.pairplot(ecg.iloc[:, :],hue="alive")
sns.pairplot(ecg.iloc[:, :],hue="group")

# Boxplot of independent variable distribution for each category of Result 
sns.boxplot(x = "alive", y = "survival_time_hr", data = ecg)
sns.boxplot(x = "group", y = "survival_time_hr", data = ecg)



# Scatter plot for each categorical Result of car
sns.stripplot(x = "alive", y = "survival_time_hr", jitter = True, data = ecg)
sns.stripplot(x = "group", y = "survival_time_hr", jitter = True, data = ecg)




"""4.	Model Bgrouplding
4.1Bgroup ld the model on the scaled data (try multiple options)
4.2Perform Survival analytics on the given datasets.

4.3Briefly explain the model output in the documentation. 
"""
S=ecg.survival_time_hr

# Importing the KaplanMeierFitter model to fit the survival analysis
from lifelines import KaplanMeierFitter

# Initiating the KaplanMeierFitter model
kmf = KaplanMeierFitter()

# Fitting KaplanMeierFitter model on Time and groups for death 
kmf.fit(S, group_observed=ecg.alive)

# Time-line estimations plot 
kmf.plot()




# Over Multiple groups 
# For each group, here group is group
ecg.group.value_counts()

# Applying KaplanMeierFitter model on Time and groups for the group "1"
kmf.fit(S[ecg.group==1], ecg.group[ecg.group==1], label='group-1')
ax = kmf.plot()

# Applying KaplanMeierFitter model on Time and groups for the group "2"
kmf.fit(S[ecg.group==2], ecg.group[ecg.group==2], label='group-2')
kmf.plot(ax=ax)

# Applying KaplanMeierFitter model on Time and groups for the group "3"
kmf.fit(S[ecg.group==3], ecg.group[ecg.group==3], label='group-3')
kmf.plot(ax=ax)
