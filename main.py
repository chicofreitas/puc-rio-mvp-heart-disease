import pandas as pd

cleveland_dataset = 'resources/datasets/heart-disease/csv/cleveland.csv'
hungarian_dataset = 'resources/datasets/heart-disease/csv/hungarian.csv'
long_beach_dataset = 'resources/datasets/heart-disease/csv/long-beach-va.csv'
switzerland_dataset = 'resources/datasets/heart-disease/csv/switzerland.csv'

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

hd_cleveland = pd.read_csv(cleveland_dataset, names=labels_attributes, nrows=282)
hd_hungarian = pd.read_csv(hungarian_dataset, names=labels_attributes)
hd_long_beach = pd.read_csv(long_beach_dataset, names=labels_attributes)
hd_switzerland = pd.read_csv(switzerland_dataset, names=labels_attributes)

data_frames = [hd_cleveland, hd_hungarian, hd_long_beach, hd_switzerland]

data_frame = pd.concat(data_frames)

data_frame.to_csv('resources/datasets/heart-disease/csv/heart-disease.csv', index=False)