# 🩺 Modelo Preditivo para Identificação de Diabetes

## 📌 Sobre o Projeto

Este projeto tem como objetivo desenvolver modelos de Machine Learning capazes de identificar padrões associados à ocorrência de diabetes, utilizando informações clínicas e características dos pacientes.

A proposta é explorar os dados, realizar uma análise exploratória, treinar diferentes algoritmos de classificação e comparar seus resultados para identificar o modelo com melhor desempenho na previsão de diabetes.

O projeto foi desenvolvido em Python, utilizando técnicas de análise de dados, visualização e aprendizado de máquina.

## 🎯 Objetivos

- Realizar uma análise exploratória dos dados.
- Identificar padrões e possíveis relações entre as variáveis.
- Preparar os dados para aplicação dos algoritmos.
- Tratar o desbalanceamento entre as classes.
- Desenvolver e comparar diferentes modelos de classificação.
- Avaliar o desempenho dos modelos por meio de métricas estatísticas.
- Identificar as variáveis mais importantes para as previsões.

## 📂 Base de Dados

**Fonte:** [Diabetes Prediction Dataset – Kaggle](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset)

O conjunto de dados contém **100.000 registros e 9 variáveis**, incluindo informações clínicas e características dos pacientes.

### Variáveis utilizadas

| Variável | Descrição |
|---|---|
| gender | Gênero do paciente |
| age | Idade |
| hypertension | Presença de hipertensão |
| heart_disease | Presença de doença cardíaca |
| smoking_history | Histórico de tabagismo |
| bmi | Índice de Massa Corporal (IMC) |
| HbA1c_level | Nível de hemoglobina glicada |
| blood_glucose_level | Nível de glicose no sangue |
| diabetes | Variável-alvo: presença ou ausência de diabetes |

A variável `diabetes` é utilizada como alvo da classificação:

- **0:** Não possui diabetes.
- **1:** Possui diabetes.

## 🛠️ Tecnologias e Bibliotecas

As principais ferramentas utilizadas no desenvolvimento foram:

- **Python:** linguagem de programação.
- **Pandas e NumPy:** manipulação e análise dos dados.
- **Matplotlib e Seaborn:** criação de gráficos e visualizações.
- **Scikit-learn:** pré-processamento, treinamento e avaliação dos modelos.
- **XGBoost:** implementação de algoritmo de classificação.
- **Imbalanced-learn:** balanceamento das classes utilizando SMOTENC.

## 🔎 Etapas do Projeto

### 1. Análise Exploratória dos Dados (EDA)

Inicialmente, foi realizada uma análise exploratória para compreender a estrutura da base de dados.

Foram realizadas:
- Verificação de valores ausentes.
- Análise das primeiras linhas do dataset.
- Estatísticas descritivas.
- Análise da distribuição das variáveis numéricas.
- Identificação de possíveis valores discrepantes (outliers).
- Análise da matriz de correlação.
- Verificação da distribuição da variável-alvo.

### 2. Visualização dos Dados

Foram desenvolvidos gráficos para facilitar a compreensão dos dados e identificar possíveis padrões.

As visualizações incluem:
- Histogramas das variáveis idade, IMC e glicose.
- Gráfico de distribuição de hipertensão.
- Boxplots para identificação de possíveis outliers.
- Mapa de calor da matriz de correlação.

### 3. Pré-processamento dos Dados

Nesta etapa, os dados foram preparados para o treinamento dos algoritmos.

Foram utilizadas as seguintes técnicas:

- Separação entre variáveis preditoras (X) e variável-alvo (y).
- Divisão da base em treinamento e teste, utilizando 70% para treinamento e 30% para teste.
- Separação das variáveis numéricas e categóricas.
- Codificação das variáveis categóricas utilizando One-Hot Encoding.
- Balanceamento das classes utilizando SMOTENC.

A divisão dos dados foi realizada com estratificação, preservando a proporção das classes entre treinamento e teste.

### 4. Balanceamento das Classes

Como a base apresenta uma quantidade significativamente maior de registros sem diabetes do que com diabetes, foi utilizado o **SMOTENC** para reduzir o desequilíbrio durante o treinamento.

Essa técnica permite gerar amostras sintéticas considerando a presença de variáveis categóricas e numéricas.

O balanceamento foi aplicado somente aos dados de treinamento, mantendo os dados de teste separados para avaliação dos modelos.

### 5. Modelagem

Foram desenvolvidos e comparados três algoritmos de classificação:

| Modelo | Descrição |
|---|---|
| Decision Tree | Árvore de Decisão |
| Random Forest | Conjunto de árvores de decisão |
| XGBoost | Algoritmo de boosting baseado em árvores |

Os três modelos foram treinados utilizando os dados preparados e balanceados.

### 6. Avaliação dos Modelos

Para avaliar e comparar os resultados, foram utilizadas diferentes métricas de classificação:

- **Acurácia (Accuracy):** proporção total de previsões corretas.
- **Precisão (Precision):** proporção de previsões positivas que realmente são positivas.
- **Recall:** capacidade de identificar corretamente os casos positivos.
- **F1-Score:** equilíbrio entre precisão e recall.
- **Especificidade:** capacidade de identificar corretamente os casos negativos.
- **ROC-AUC:** capacidade de discriminação entre as classes.
- **PR-AUC:** avalia o desempenho considerando a relação entre precisão e recall.

Também foram analisados os seguintes resultados da matriz de confusão:

- VN: Verdadeiros Negativos.
- FP: Falsos Positivos.
- FN: Falsos Negativos.
- VP: Verdadeiros Positivos.

A comparação dos modelos foi organizada considerando principalmente a métrica PR-AUC.

### 7. Importância das Variáveis

Por fim, foi realizada uma análise da importância das variáveis para cada algoritmo.

Essa etapa permite identificar quais características tiveram maior contribuição nas previsões realizadas pelos modelos.

## 📊 Resultados e Visualizações

Os gráficos abaixo representam as visualizações geradas pelo código durante a análise exploratória e a comparação dos modelos.

**Para exibir as imagens no GitHub:** crie uma pasta chamada `graficos` no repositório e salve nela as imagens geradas pelo Python com os nomes indicados.

### Análise Exploratória

**Distribuição das variáveis numéricas**

<!-- Inserir os histogramas de idade, IMC e glicose -->
![Distribuição das variáveis numéricas](graficos/distribuicao_variaveis.png)

**Distribuição de hipertensão**

![Distribuição de hipertensão](graficos/distribuicao_hipertensao.png)

**Identificação de outliers**

![Boxplots das variáveis numéricas](graficos/boxplots.png)

**Matriz de correlação**

![Matriz de correlação](graficos/matriz_correlacao.png)

### Comparação dos Modelos

O projeto também gera dois gráficos comparativos:

- Métricas de classificação: Acurácia, Precisão, Recall, F1-Score e Especificidade.
- Métricas AUC: ROC-AUC e PR-AUC.

![Comparação dos modelos](graficos/comparacao_modelos.png)

### Importância das Variáveis

O código também apresenta as 10 variáveis mais importantes de cada modelo, organizadas em tabelas no terminal.

## 💻 Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 2. Acesse a pasta do projeto

```bash
cd NOME_DO_REPOSITORIO
```

### 3. Instale as dependências

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost imbalanced-learn
```

### 4. Organize os arquivos

Mantenha os arquivos na seguinte estrutura:

```text
projeto-diabetes/
│
├── diabetes_prediction_dataset.csv
├── prinpag.py
├── README.md
│
└── graficos/
    ├── distribuicao_variaveis.png
    ├── distribuicao_hipertensao.png
    ├── boxplots.png
    ├── matriz_correlacao.png
    └── comparacao_modelos.png
```

### 5. Execute o código

```bash
python prinpag.py
```

Após a execução, os resultados das análises, métricas de avaliação e importância das variáveis serão apresentados.

**Observação:** as imagens precisam ser salvas na pasta `graficos` para aparecerem neste README. O código original exibe os gráficos, mas ainda precisa receber os comandos de salvamento (`plt.savefig`) para gerar esses arquivos automaticamente.

## 🏁 Considerações Finais

O projeto permite explorar a aplicação de algoritmos de Machine Learning na identificação de padrões associados ao diabetes.

A comparação entre Decision Tree, Random Forest e XGBoost possibilita avaliar diferentes abordagens de classificação, considerando métricas que ajudam a compreender tanto a identificação dos casos positivos quanto dos negativos.

Além disso, a análise da importância das variáveis contribui para uma melhor interpretação dos resultados obtidos.

**Importante:** este projeto possui finalidade acadêmica e exploratória. Os modelos não substituem avaliação médica, diagnóstico ou acompanhamento profissional.

---

**Desenvolvido em Python | Machine Learning | Análise de Dados**
