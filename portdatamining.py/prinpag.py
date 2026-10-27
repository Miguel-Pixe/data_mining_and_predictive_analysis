# Manipulacao e analise de dados

import pandas as pd
import numpy as np

# Visualizcao

import matplotlib.pyplot as plt
import seaborn as sns

# Pre-processamento e modelagem

from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.metrics import (
    average_precision_score, confusion_matrix,classification_report, accuracy_score, precision_score,
    recall_score, f1_score, roc_auc_score, roc_curve, auc
)

# Algoritmos de classificacao

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb

# Balanceamento de classes

from imblearn.over_sampling import SMOTENC


# carregando e tratando o dataset

df = pd.read_csv('diabetes_prediction_dataset.csv')

print(df.isna().sum())

print(df.head(5))


# 1. Estatísticas descritivas
print("Estatísticas descritivas:")
print(df.describe())

# 3. Distribuição das variáveis numéricas
num_cols = ['age', 'bmi', 'blood_glucose_level']  

for col in num_cols:
    plt.figure(figsize=(6, 4))
    sns.histplot(data=df, x=col, bins=30, kde=False)
    plt.title(f'Distribuição de {col}')
    plt.xlabel(col)
    plt.ylabel('Frequência')
    plt.tight_layout()
    plt.show()


plt.figure(figsize=(6, 4))
sns.countplot(x=df['hypertension'])
plt.title('Distribuição de hypertension')
plt.show()

# 4. Boxplots para identificar outliers
for col in num_cols:
    plt.figure(figsize=(6,4))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot de {col}')
    plt.show()

# 5. Matriz de correlação
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="Blues")
plt.title("Matriz de Correlação")
plt.show()

#Verificando a distribuição da variável alvo

print(df['diabetes'].value_counts())
print(df['diabetes'].value_counts(normalize=True))



X = df.drop(columns=['diabetes'])

y = df['diabetes']


colunas_categoricas = ['gender', 'smoking_history','hypertension',
    'heart_disease',]

colunas_numericas = [col for col in X.columns if col not in colunas_categoricas]

#treino e teste

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', colunas_numericas),
        ('cat', OneHotEncoder(handle_unknown='ignore'), colunas_categoricas)

]
)


# Balanceamento de classes com SMOTENC

smote_nc = SMOTENC(
    categorical_features=colunas_categoricas,
    random_state=42,
)


X_train_bal, y_train_bal = smote_nc.fit_resample(X_train, y_train)

print("Classes antes do SMOTENC:")
print(y_train.value_counts())

print("Classes após o SMOTENC:")
print(y_train_bal.value_counts())

#Pre processamento dos dados:

X_train_proc = preprocessor.fit_transform(X_train_bal)
X_test_proc = preprocessor.transform(X_test)



#Modelos de classificacao

modelos = {
    "Decision Tree": DecisionTreeClassifier(
        min_samples_leaf=10, 
        random_state=42
                                      ),
    "Random Forest": RandomForestClassifier(
        n_estimators=300,
        random_state=42,
        n_jobs=-1,

    ),
    "XGBoost": xgb.XGBClassifier(
        objective="binary:logistic",
        eval_metric="logloss",
        scale_pos_weight=1.0,
        random_state=42,
        n_jobs=1,

    ),
                    
}


#Identificando a importância das variáveis para cada modelo

resultados = []
importancias = {}

nomes_variaveis = preprocessor.get_feature_names_out()

for nome, modelo in modelos.items():
    modelo.fit(X_train_proc, y_train_bal)

    predicoes = modelo.predict(X_test_proc)
    probabilidades = modelo.predict_proba(X_test_proc)[:, 1]

    tn, fp, fn, tp = confusion_matrix(y_test, predicoes, labels=[0, 1]).ravel()

    especificidade = tn / (tn + fp) if (tn + fp) > 0 else 0

    resultados.append({
    "Modelo": nome,
    "Acurácia": accuracy_score(y_test, predicoes),
    "Precisão classe 1": precision_score(
        y_test, predicoes, pos_label=1, zero_division=0
    ),
    "Recall classe 1": recall_score(
        y_test, predicoes, pos_label=1, zero_division=0
    ),
    "F1 classe 1": f1_score(
        y_test, predicoes, pos_label=1, zero_division=0
    ),
    "Especificidade": especificidade,
    "ROC-AUC": roc_auc_score(y_test, probabilidades),
    "PR-AUC": average_precision_score(y_test, probabilidades),
    "VN": tn,
    "FP": fp,
    "FN": fn,
    "VP": tp,
    })
    
    importancias[nome] = (
    pd.DataFrame({
        "Variável": nomes_variaveis,
        "Importância": modelo.feature_importances_,
    })
    .sort_values("Importância", ascending=False)
    )

tabela_comparativa = pd.DataFrame(resultados).sort_values(
    "PR-AUC", ascending=False
)


print("\nComparação dos modelos (ordenada por PR-AUC):")
for _, resultado in tabela_comparativa.iterrows():
    print(f"\n{resultado['Modelo']}")
    print(f"  Acurácia:             {resultado['Acurácia']:.3f}")
    print(f"  Precisão classe 1:    {resultado['Precisão classe 1']:.3f}")
    print(f"  Recall classe 1:      {resultado['Recall classe 1']:.3f}")
    print(f"  F1 classe 1:          {resultado['F1 classe 1']:.3f}")
    print(f"  Especificidade:       {resultado['Especificidade']:.3f}")
    print(f"  ROC-AUC:              {resultado['ROC-AUC']:.3f}")
    print(f"  PR-AUC:               {resultado['PR-AUC']:.3f}")
    print(f"  VN (verdadeiros negativos): {resultado['VN']}")
    print(f"  FP (falsos positivos):      {resultado['FP']}")
    print(f"  FN (falsos negativos):      {resultado['FN']}")
    print(f"  VP (verdadeiros positivos): {resultado['VP']}")

melhor_modelo = tabela_comparativa.iloc[0]


print(
    f"\nMaior PR-AUC: {melhor_modelo['Modelo']} "
    f"(PR-AUC = {melhor_modelo['PR-AUC']:.3f})"
)


metricas_classificacao = [
    "Acurácia",
    "Precisão classe 1",
    "Recall classe 1",
    "F1 classe 1",
    "Especificidade",
]

metricas_auc = ["ROC-AUC", "PR-AUC"]

dados_grafico = tabela_comparativa.set_index("Modelo")

fig, eixos = plt.subplots(1, 2, figsize=(15, 6))

# Compara as métricas de classificação para cada modelo
dados_grafico[metricas_classificacao].plot(
    kind="bar",
    ax=eixos[0],
)
eixos[0].set_title("Métricas de classificação")
eixos[0].set_ylabel("Valor")
eixos[0].set_ylim(0, 1.05)
eixos[0].set_xlabel("")
eixos[0].tick_params(axis="x", rotation=0)
eixos[0].grid(axis="y", linestyle="--", alpha=0.5)

# Compara as áreas sob as curvas ROC e Precision-Recall
dados_grafico[metricas_auc].plot(
    kind="bar",
    ax=eixos[1],
)
eixos[1].set_title("Métricas AUC")
eixos[1].set_ylabel("Valor")
eixos[1].set_ylim(0, 1.05)
eixos[1].set_xlabel("")
eixos[1].tick_params(axis="x", rotation=0)
eixos[1].grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()

for nome, tabela_importancia in importancias.items():
    
    print(f"\n10 variáveis mais importantes — {nome}:")
    print(tabela_importancia.head(10).round(4).to_string(index=False))











