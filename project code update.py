#libraries 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import seaborn as sns
import csv

file = pd.read_csv('ocd_patient_dataset.csv')
df = pd.DataFrame(file)
df.columns = ['Patient ID','Age','Gender','Ethnicity', 'Marital Status','Education Level','OCD Diagnosis Date','Duration of Symptoms (months)','Family History of OCD','Obsession type','Compulsion type','Previous diagnoses','Y-BOCS(Obsessions)','Y-BOCS(Compulsions)','Depression Diagnosis', 'Anxiety Diagnosis', 'Medications']
print(df)
print(file.describe())

#MATPLOTLIB histograms

#Gender 
X = []
Y = []
with open('ocd_patient_dataset.csv', 'r') as data:
    graph = csv.reader(data, delimiter=',')

    for ROWS in graph:
        X.append(ROWS[2])
        Y.append(ROWS[2])

plt.hist(X, bins = 30)
plt.xlabel('Gender')
plt.ylabel('People')
plt.title('Gender')
plt.show()

#Ethnicity
X = []
Y = []
with open('ocd_patient_dataset.csv', 'r') as data:
    graph = csv.reader(data, delimiter=',')

    for ROWS in graph:
        X.append(ROWS[3])
        Y.append(ROWS[3])

plt.hist(X, bins = 30)
plt.xlabel('Ethnicity')
plt.ylabel('People')
plt.title('Ethnicity')
plt.show()

#Family history
X = []
Y = []
with open('ocd_patient_dataset.csv', 'r') as data:
    graph = csv.reader(data, delimiter=',')

    for ROWS in graph:
        X.append(ROWS[9])
        Y.append(ROWS[9])

plt.hist(X, bins = 30)
plt.xlabel('Family History of OCD')
plt.ylabel('People')
plt.title('Family History')
plt.show()

#Previous diagnoses
X = []
Y = []
with open('ocd_patient_dataset.csv', 'r') as data:
    graph = csv.reader(data, delimiter=',')

    for ROWS in graph:
        X.append(ROWS[8])
        Y.append(ROWS[8])

plt.hist(X, bins = 30)
plt.xlabel('Previous Diagnoses')
plt.ylabel('People')
plt.title('Previous Diagnoses')
plt.show()

#Obsession type
X = []
Y = []
with open('ocd_patient_dataset.csv', 'r') as data:
    graph = csv.reader(data, delimiter=',')

    for ROWS in graph:
        X.append(ROWS[10])
        Y.append(ROWS[10])

plt.hist(X, bins = 30)
plt.xlabel('Obsession Type')
plt.ylabel('People')
plt.title('Obsession Types')
plt.show()

#Compulsion type correlation
X = []
Y = []
with open('ocd_patient_dataset.csv', 'r') as data:
    graph = csv.reader(data, delimiter=',')

    for ROWS in graph:
        X.append(ROWS[11])
        Y.append(ROWS[11])

plt.hist(X, bins = 30)
plt.xlabel('Compulsion Type')
plt.ylabel('People')
plt.title('Compulsion Types')
plt.show()

#linegraph
#Depression and anxiety diagnosis 
X = []
Y = []
with open('ocd_patient_dataset.csv', 'r') as data:
    graph = csv.reader(data, delimiter=',')
     
    for ROWS in graph:
        X.append(ROWS[14])
        Y.append(ROWS[15])
 
plt.plot(X, Y)
plt.title('Depression/Anxiety Diagnoses Correlation')
plt.xlabel('Depression Diagnosis')
plt.ylabel('Anxiety Diagnosis')
plt.show()

#SEABORN
#Heatmap 
data = pd.read_csv('ocd_patient_dataset.csv')
plt.figure(figsize=(10, 10))
sns.heatmap(data.corr(), annot=True, cmap='cool', linewidths=0.5)
plt.title('Heatmap')
plt.show()


