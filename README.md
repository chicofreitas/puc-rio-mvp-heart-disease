# MVP Sprint I - Heart Disease

Fonte dos dados: [ UC Irvine Machine Learning Repository - Heart Disease ]( https://archive-beta.ics.uci.edu/dataset/45/heart+disease )

Este banco de dados contém 76 atributos, mas todos os experimentos publicados referem-se ao uso de um subconjunto de 14 deles. Em particular, o banco de dados de Cleveland é o único que foi usado por pesquisadores de ML até hoje. O campo "objetivo" refere-se à presença de cardiopatia no paciente. É um valor inteiro de 0 (sem presença) a 4. Os experimentos com o banco de dados Cleveland se concentraram em simplesmente tentar distinguir a presença (valores 1,2,3,4) da ausência (valor 0).
   
Os nomes e números de segurança social dos pacientes foram recentemente removidos do banco de dados, substituídos por valores fictícios.

Um arquivo foi "processado", aquele que contém o banco de dados de Cleveland. Todos os quatro arquivos não processados também existem neste diretório.

Para ver os Custos dos Testes (doados por Peter Turney), consulte a pasta "Custos". <sup>1</sup>

## Definição do Problema

...

## Informações sobre os atributos

...

## Download dos dados

...

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

Visualizando as 5 últimas linhas do arquivo *heart-disease.csv*:

        $ heart_disease.tail()

                0  1     2    3    4    5    6     7    8      9    10   11    12    13    14  ...   61   62   63   64   65   66   67   68   69   70   71   72    73    74     75
        897  4070.0  0  54.0  1.0  1.0  1.0  1.0  -9.0  4.0  180.0  0.0  0.0  -9.0  -9.0  -9.0  ...  1.0  1.0  1.0  1.0  1.0  1.0  1.0  1.0  1.0  1.0  1.0  1.0  71.0  -9.0   name
        898  4071.0  0  56.0  1.0  1.0  1.0  1.0  -9.0  4.0  125.0  0.0  0.0   1.0  -9.0  -9.0  ...  1.0  2.0  1.0  1.0  1.0  2.0  1.0  5.0  1.0  1.0  1.0  2.0  68.0  -9.0   name
        899  4072.0  0  56.0  1.0  0.0  1.0  1.0  -9.0  3.0  125.0  0.0  0.0  -9.0  -9.0  -9.0  ...  1.0  1.0  2.0  1.0  1.0  1.0  1.0  1.0  1.0  5.0  3.0  2.0  61.0  -9.0   name
        900  4073.0  0  54.0  1.0  1.0  1.0  1.0  -9.0  4.0  130.0  0.0  0.0  -9.0  -9.0  -9.0  ...  1.0  2.0  1.0  1.0  1.0  2.0  1.0  1.0  1.0  1.0  1.0  1.0  -9.0  -9.0   name
        901  4074.0  0  66.0  0.0  1.0  1.0  1.0  -9.0  4.0  155.0  0.0  0.0  -9.0  -9.0  -9.0  ...  1.0  1.0  1.0  1.0  1.0  2.0  1.0  1.0  1.0  1.0  1.0  1.0  70.0  -9.0   name

### Visualizações
...

#### Visualizações Unimodais
...

#### Visualizações Multimodais
...

1. Tradução livre do README.md original, disponível em: https://archive-beta.ics.uci.edu/ml/datasets/Heart+Disease