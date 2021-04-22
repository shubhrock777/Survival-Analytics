
library(survminer)
library(survival)

library(readr)

patient <- read.csv(file.choose())

attach(patient)
str(patient)

# Define variables 
time <- Followup
event <- Eventtype
 

# Descriptive statistics
summary(time)
table(event)


# Kaplan-Meier non-parametric analysis
kmsurvival <- survfit(Surv(time, event) ~ 1)

summary(kmsurvival)

plot(kmsurvival, xlab="Time", ylab="Survival Probability")

ggsurvplot(kmsurvival, data=patient, risk.table = TRUE)
