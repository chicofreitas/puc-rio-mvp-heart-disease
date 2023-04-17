# MVP Sprint I - Heart Disease

## Francisco das Chagas Alves Freitas

**Fonte dos dados:** [ UC Irvine Machine Learning Repository - Heart Disease ]( https://archive-beta.ics.uci.edu/dataset/45/heart+disease )

## Definição do Problema

Este banco de dados contém 76 atributos, mas todos os experimentos publicados referem-se ao uso de um subconjunto de 14 deles. Em particular, o banco de dados de Cleveland é o único que foi usado por pesquisadores de ML até hoje. O campo "objetivo" refere-se à presença de cardiopatia no paciente. É um valor inteiro de 0 (sem presença) a 4. Os experimentos com o banco de dados Cleveland se concentraram em simplesmente tentar distinguir a presença (valores 1,2,3,4) da ausência (valor 0).
   
Os nomes e números de segurança social dos pacientes foram recentemente removidos do banco de dados, substituídos por valores fictícios.

Um arquivo foi "processado", aquele que contém o banco de dados de Cleveland. Todos os quatro arquivos não processados também existem neste diretório.

Para ver os Custos dos Testes (doados por Peter Turney), consulte a pasta "Custos". <sup>1</sup>

## Informações sobre os atributos
        -- Only 14 used
            -- 1. #3  (age)       
            -- 2. #4  (sex)       
            -- 3. #9  (cp)        
            -- 4. #10 (trestbps)  
            -- 5. #12 (chol)      
            -- 6. #16 (fbs)       
            -- 7. #19 (restecg)   
            -- 8. #32 (thalach)   
            -- 9. #38 (exang)     
            -- 10. #40 (oldpeak)   
            -- 11. #41 (slope)     
            -- 12. #44 (ca)        
            -- 13. #51 (thal)      
            -- 14. #58 (num)       (the predicted attribute)


        num: diagnosis of heart disease (angiographic disease status)
        -- Value 0: < 50% diameter narrowing
        -- Value 1: > 50% diameter narrowing
        (in any major vessel: attributes 59 through 68 are vessels)

## Download dos dados

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

            ...

            'lvx4',
            'lvf',
            'cathef',
            'junk',
            'name'
            ]

Realizando a leitura dos arquivos:

        hd_cleveland = pd.read_csv(cleveland_dataset, names=labels_attributes, nrows=282)
        hd_hungarian = pd.read_csv(hungarian_dataset, names=labels_attributes)
        hd_long_beach = pd.read_csv(long_beach_dataset, names=labels_attributes)
        hd_switzerland = pd.read_csv(switzerland_dataset, names=labels_attributes)

Concatenando os arquivos:
        data_frames = [hd_cleveland, hd_hungarian, hd_long_beach, hd_switzerland]

        data_frame = pd.concat(data_frames)

Armazenando o arquivo concatenado em um novo arquivo *csv*:

        data_frame.to_csv('resources/datasets/heart-disease/csv/heart-disease.csv', index=False)

## Análise Exploratória dos Dados

...

### Estatísticas descritivas

Visualizando as 5 primeiras linhas do arquivo *heart-disease.csv*:

        $ heart_disease.head()

            0    1     2    3        4         5        6        7    8         9    10     11  ...   64    65       66       67    68    69    70    71   72      73    74     75
        0   id  ccf   age  sex  painloc  painexer  relrest  pncaden   cp  trestbps  htn   chol  ...  om1   om2  rcaprox  rcadist  lvx1  lvx2  lvx3  lvx4  lvf  cathef  junk   name
        1  1.0    0  63.0  1.0     -9.0      -9.0     -9.0     -9.0  1.0     145.0  1.0  233.0  ...  1.0  -9.0      1.0      1.0   1.0   1.0   1.0   1.0  1.0    -9.0  -9.0   name
        2  2.0    0  67.0  1.0     -9.0      -9.0     -9.0     -9.0  4.0     160.0  1.0  286.0  ...  1.0  -9.0      1.0      1.0   1.0   1.0   1.0   1.0  1.0    -9.0  -9.0   name
        3  3.0    0  67.0  1.0     -9.0      -9.0     -9.0     -9.0  4.0     120.0  1.0  229.0  ...  1.0  -9.0      2.0      2.0   1.0   1.0   1.0   7.0  3.0    -9.0  -9.0   name
        4  4.0    0  37.0  1.0     -9.0      -9.0     -9.0     -9.0  3.0     130.0  0.0  250.0  ...  1.0  -9.0      1.0      1.0   1.0   1.0   1.0   1.0  1.0    -9.0  -9.0   name

        [5 rows x 76 columns]

Visualizando as 5 últimas linhas do arquivo *heart-disease.csv*:

        $ heart_disease.tail()

                0  1     2    3    4    5    6     7    8      9    10   11    12    13    14  ...   61   62   63   64   65   66   67   68   69   70   71   72    73    74     75
        897  4070.0  0  54.0  1.0  1.0  1.0  1.0  -9.0  4.0  180.0  0.0  0.0  -9.0  -9.0  -9.0  ...  1.0  1.0  1.0  1.0  1.0  1.0  1.0  1.0  1.0  1.0  1.0  1.0  71.0  -9.0   name
        898  4071.0  0  56.0  1.0  1.0  1.0  1.0  -9.0  4.0  125.0  0.0  0.0   1.0  -9.0  -9.0  ...  1.0  2.0  1.0  1.0  1.0  2.0  1.0  5.0  1.0  1.0  1.0  2.0  68.0  -9.0   name
        899  4072.0  0  56.0  1.0  0.0  1.0  1.0  -9.0  3.0  125.0  0.0  0.0  -9.0  -9.0  -9.0  ...  1.0  1.0  2.0  1.0  1.0  1.0  1.0  1.0  1.0  5.0  3.0  2.0  61.0  -9.0   name
        900  4073.0  0  54.0  1.0  1.0  1.0  1.0  -9.0  4.0  130.0  0.0  0.0  -9.0  -9.0  -9.0  ...  1.0  2.0  1.0  1.0  1.0  2.0  1.0  1.0  1.0  1.0  1.0  1.0  -9.0  -9.0   name
        901  4074.0  0  66.0  0.0  1.0  1.0  1.0  -9.0  4.0  155.0  0.0  0.0  -9.0  -9.0  -9.0  ...  1.0  1.0  1.0  1.0  1.0  2.0  1.0  1.0  1.0  1.0  1.0  1.0  70.0  -9.0   name

        [5 rows x 76 columns]

Verificando o tipo de dataset de cada atributo:

        $ heart_disease.dtypes

        id         object
        ccf        object
        age        object
        sex        object
        painloc    object
                    ...  
        lvx4       object
        lvf        object
        cathef     object
        junk       object
        name       object
        Length: 76, dtype: object


Resumo estatístico 

                0    1     2    3    4    5    6     7    8      9    10   11    12    13  ...   62    63   64    65   66   67   68   69   70   71   72    73    74     75
        count     900  902   900  900  900  900  900   900  900    900  900  900   900   900  ...  900   900  900   900  900  900  900  900  900  900  900   900   900    900
        unique    715    4    51    3    4    4    4     2    5     62    4  215     4    27  ...    4     4    4     4    4    4    6    9   10   10    8    90    54      2
        top     172.0    0  54.0  1.0  1.0  1.0  1.0  -9.0  4.0  120.0  0.0  0.0  -9.0  -9.0  ...  1.0  -9.0  1.0  -9.0  1.0  1.0  1.0  1.0  1.0  1.0  1.0  -9.0  -9.0   name
        freq        2  494    51  711  568  366  412   899  485    128  453  172   669   420  ...  467   567  517   572  430  521  874  871  843  769  759   588   780    899
            
        [4 rows x 76 columns]
Dimensões do dataset

        $ heart_disease.shape

        (902, 76)

Informaçõse sobre o dataset

        $ heart_disease.info()

        <class 'pandas.core.frame.DataFrame'>
        RangeIndex: 902 entries, 0 to 901
        Data columns (total 76 columns):
        #   Column    Non-Null Count  Dtype 
        ---  ------    --------------  ----- 
        0   id        900 non-null    object
        1   ccf       902 non-null    object
        2   age       900 non-null    object
        3   sex       900 non-null    object
        4   painloc   900 non-null    object
        5   painexer  900 non-null    object

        ...

        65  om2       900 non-null    object
        66  rcaprox   900 non-null    object
        67  rcadist   900 non-null    object
        68  lvx1      900 non-null    object
        69  lvx2      900 non-null    object
        70  lvx3      900 non-null    object
        71  lvx4      900 non-null    object
        72  lvf       900 non-null    object
        73  cathef    900 non-null    object
        74  junk      900 non-null    object
        75  name      900 non-null    object
        dtypes: object(76)
        memory usage: 535.7+ KB
        None


Visualizando as colunas do dataset

        $ heart_disease.columns

        Index(['id', 'ccf', 'age', 'sex', 'painloc', 'painexer', 'relrest', 'pncaden',
            'cp', 'trestbps', 'htn', 'chol', 'smoke', 'cigs', 'years', 'fbs', 'dm',
            'famhist', 'restecg', 'ekgmo', 'ekgday', 'ekgyr', 'dig', 'prop', 'nitr',
            'pro', 'diuretic', 'proto', 'thaldur', 'thaltime', 'met', 'thalach',
            'thalrest', 'tpeakbps', 'tpeakbpd', 'dummy', 'trestbpd', 'exang',
            'xhypo', 'oldpeak', 'slope', 'rldv5', 'rldv5e', 'ca', 'restckm',
            'exerckm', 'restef', 'restwm', 'exeref', 'exerwm', 'thal', 'thalsev',
            'thalpul', 'earlobe', 'cmo', 'cday', 'cyr', 'num', 'lmt', 'ladprox',
            'laddist', 'diag', 'cxmain', 'ramus', 'om1', 'om2', 'rcaprox',
            'rcadist', 'lvx1', 'lvx2', 'lvx3', 'lvx4', 'lvf', 'cathef', 'junk',
            'name'],
            dtype='object')


### Visualizações
...

#### Visualizações Unimodais
...

#### Visualizações Multimodais
...

1. Tradução livre do README.md original, disponível em: https://archive-beta.ics.uci.edu/ml/datasets/Heart+Disease