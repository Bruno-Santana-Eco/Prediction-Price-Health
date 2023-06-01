pwd

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')
# Verificar
Base_Dados = pd.read_csv("d:/Repositório GIT/Projetos/Prediction-Price-Health/Datasets/Base_Dados_Plano_Saude.csv")
Base_Dados.head()




# Grid de gráficos
Quantidade_Graficos = 4
Colunas = 4
Loop_Repeticao = 1

# Ajuste do relatorio
Figura = plt.figure( figsize=(20, 15) )
Cor_Fundo = "#14171a"
Figura.set_facecolor(Cor_Fundo)

# Estilo
plt.style.use('dark_background')

# Titulo principal
plt.suptitle(f'Análise das variáveis quantitativas', fontsize=18, color='#ffffff', fontweight=600 )

# Loop usando o Index e Nome da coluna
for Index, Coluna in zip( Base_Dados.dtypes.index, Base_Dados.dtypes.values ):

  # Apenas se for numerico
  if Coluna != object:

    # Boxplot
    plt.subplot( Quantidade_Graficos, Colunas, Loop_Repeticao )
    plt.title(f'Distribuição de dados - {Index.upper()}')
    sns.boxplot( x=Base_Dados[Index], width=0.45, notch=True, showmeans=True )
    Loop_Repeticao += 1

    # Distplot
    plt.subplot( Quantidade_Graficos, Colunas, Loop_Repeticao )
    sns.distplot( Base_Dados[Index] )
    plt.title(f'Histograma de dados - {Index.upper()}')
    plt.xlabel('Valor')
    plt.ylabel('Frequência')
    Loop_Repeticao += 1

    # Serie
    plt.subplot( Quantidade_Graficos, Colunas, Loop_Repeticao )
    plt.title(f'Serie Temporal - {Index.upper()}')
    plt.plot( Base_Dados[Index].values, linewidth=0.5 )
    Loop_Repeticao += 1

    # Estatística
    plt.subplot( Quantidade_Graficos, Colunas, Loop_Repeticao )
    plt.title(f'Estatística Descritiva - {Index.upper()}')
    sns.heatmap( pd.DataFrame( Base_Dados[Index].describe() ), annot=True, cmap="GnBu" )
    Loop_Repeticao += 1
    
plt.subplots_adjust( left=0.1, bottom=0.1, right=0.9, top=0.915, wspace=0.3, hspace=0.55 );
       