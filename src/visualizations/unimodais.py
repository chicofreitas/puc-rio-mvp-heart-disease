import pandas as pd
import matplotlib.pyplot as plt

labels_attributes = [
    'id',
    'ccf',
    'age',
    'sex',
    'painloc',
    'painexer',
    'relrest',
    'pncaden',
    'cp',
    'trestbps',
    'htn',
    'chol',
    'smoke',
    'cigs',
    'years',
    'fbs',
    'dm',
    'famhist',
    'restecg',
    'ekgmo',
    'ekgday',
    'ekgyr',
    'dig',
    'prop',
    'nitr',
    'pro',
    'diuretic',
    'proto',
    'thaldur',
    'thaltime', 
    'met',
    'thalach',
    'thalrest',
    'tpeakbps',
    'tpeakbpd',
    'dummy',
    'trestbpd',
    'exang',
    'xhypo',
    'oldpeak',
    'slope',
    'rldv5',
    'rldv5e',
    'ca',
    'restckm',
    'exerckm',
    'restef',
    'restwm',
    'exeref',
    'exerwm',
    'thal',
    'thalsev',
    'thalpul',
    'earlobe',
    'cmo',
    'cday',
    'cyr',
    'num',
    'lmt',
    'ladprox',
    'laddist',
    'diag',
    'cxmain',
    'ramus',
    'om1',
    'om2',
    'rcaprox',
    'rcadist',
    'lvx1',
    'lvx2',
    'lvx3',
    'lvx4',
    'lvf',
    'cathef',
    'junk',
    'name'
    ]

heart_disease = pd.read_csv('resources/datasets/heart-disease/csv/heart-disease.csv', names=labels_attributes)

fig, ax = plt.subplots(5, 3, figsize=(15, 10))

heart_disease['age'] = pd.to_numeric(heart_disease['age'], errors='coerce')
print(heart_disease['age'])

ax[0, 0].hist(heart_disease['age'], bins=7,edgecolor='black')
ax[0, 0].set_title('Age')

heart_disease['sex'] = pd.to_numeric(heart_disease['sex'], errors='coerce')
ax[0, 1].hist(heart_disease['sex'], bins=7,edgecolor='black')
ax[0, 1].set_title('Sex')

heart_disease['cp'] = pd.to_numeric(heart_disease['cp'], errors='coerce')
ax[0, 2].hist(heart_disease['cp'], bins=7,edgecolor='black')
ax[0, 2].set_title('Chest Pain')

heart_disease['trestbps'] = pd.to_numeric(heart_disease['trestbps'], errors='coerce')
ax[1, 0].hist(heart_disease['trestbps'], bins=7,edgecolor='black')
ax[1, 0].set_title('Resting Blood Pressure mmHg')

heart_disease['chol'] = pd.to_numeric(heart_disease['chol'], errors='coerce')
ax[1, 1].hist(heart_disease['chol'], bins=7,edgecolor='black')
ax[1, 1].set_title('Serum Cholestoral (mg/dl)')

heart_disease['fbs'] = pd.to_numeric(heart_disease['fbs'], errors='coerce')
ax[1, 2].hist(heart_disease['fbs'], bins=7,edgecolor='black')
ax[1, 2].set_title('fasting blood sugar')

heart_disease['restecg'] = pd.to_numeric(heart_disease['restecg'], errors='coerce')
ax[2, 0].hist(heart_disease['restecg'], bins=7,edgecolor='black')
ax[2, 0].set_title('Resting Electrocardiographic Results')

heart_disease['thalach'] = pd.to_numeric(heart_disease['thalach'], errors='coerce')
ax[2, 1].hist(heart_disease['thalach'], bins=7,edgecolor='black')
ax[2, 1].set_title('Maximum Heart Rate Achieved')

heart_disease['exang'] = pd.to_numeric(heart_disease['exang'], errors='coerce')
ax[2, 2].hist(heart_disease['exang'], bins=7,edgecolor='black')
ax[2, 2].set_title('Exercise Induced Angina')

heart_disease['oldpeak'] = pd.to_numeric(heart_disease['oldpeak'], errors='coerce')
ax[3, 0].hist(heart_disease['oldpeak'], bins=7,edgecolor='black')
ax[3, 0].set_title('ST Depression Induced by Exercise Relative to Rest')

heart_disease['slope'] = pd.to_numeric(heart_disease['slope'], errors='coerce')
ax[3, 1].hist(heart_disease['slope'], bins=7,edgecolor='black')
ax[3, 1].set_title('Slope of the Peak Exercise ST Segment')

heart_disease['ca'] = pd.to_numeric(heart_disease['ca'], errors='coerce')
ax[3, 2].hist(heart_disease['ca'], bins=7,edgecolor='black')
ax[3, 2].set_title('Number of Major Vessels (0-3) Colored by Flourosopy')

heart_disease['thal'] = pd.to_numeric(heart_disease['thal'], errors='coerce')
ax[4, 0].hist(heart_disease['thal'], bins=7,edgecolor='black')
ax[4, 0].set_title('Thal')

heart_disease['num'] = pd.to_numeric(heart_disease['num'], errors='coerce')
ax[4, 1].hist(heart_disease['num'], bins=7,edgecolor='black')
ax[4, 1].set_title('Diagnosis of Heart Disease')


fig.tight_layout()

plt.show()