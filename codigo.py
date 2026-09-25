# ==========================================
# 1. IMPORTAÇÃO DE BIBLIOTECAS
# ==========================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, precision_recall_curve, confusion_matrix

import shap

# Configuração para ignorar avisos visuais
import warnings
warnings.filterwarnings('ignore')

print("Bibliotecas importadas com sucesso!")


# ==========================================
# 2. CARREGAR E EXPLORAR OS DADOS
# ==========================================
# Substitua 'creditcard.csv' pelo caminho real do seu arquivo
df = pd.read_csv('creditcard.csv')

print(f"Dimensões do dataset: {df.shape}")
print("\nDistribuição das Classes (%):")
print(df['Class'].value_counts(normalize=True) * 100)

# Verificando valores nulos
print(f"\nTotal de valores nulos no dataset: {df.isnull().sum().max()}")


# ==========================================
# 3. PREPARAÇÃO E ENGENHARIA DE ATRIBUTOS
# ==========================================
# Criando log do valor para suavizar a assimetria da coluna Amount
df['Log_Amount'] = np.log1p(df['Amount'])

# Padronizando Time e Amount originais
scaler = StandardScaler()
df['Scaled_Amount'] = scaler.fit_transform(df[['Amount']])
df['Scaled_Time'] = scaler.fit_transform(df[['Time']])

# Removendo colunas originais substituídas
df_model = df.drop(['Time', 'Amount'], axis=1)

# Separando variáveis preditoras (X) e a classe alvo (y)
X = df_model.drop('Class', axis=1)
y = df_model['Class']

# Divisão treino/teste com estratificação para manter a proporção de fraudes
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Formato do conjunto de treino: {X_train.shape}")
print(f"Formato do conjunto de teste: {X_test.shape}")


# ==========================================
# 4. TREINAMENTO DOS MODELOS
# ==========================================

# 1. Baseline: Regressão Logística com class_weight balanceado
print("\nTreinando Regressão Logística...")
lr_model = LogisticRegression(class_weight='balanced', random_state=42, max_iter=1000)
lr_model.fit(X_train, y_train)

# 2. Random Forest
print("Treinando Random Forest...")
rf_model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42, n_jobs=-1)
rf_model.fit(X_train, y_train)

# 3. XGBoost (calculando a proporção para o scale_pos_weight)
print("Treinando XGBoost...")
scale_pos = (len(y_train) - sum(y_train)) / sum(y_train)
xgb_model = XGBClassifier(scale_pos_weight=scale_pos, random_state=42, eval_metric='logloss')
xgb_model.fit(X_train, y_train)

print("Treinamento concluído!")


# ==========================================
# 5. AVALIAÇÃO E AJUSTE DE LIMIAR (THRESHOLD)
# ==========================================
# Vamos usar o XGBoost como exemplo principal de otimização
y_pred_proba = xgb_model.predict_proba(X_test)[:, 1]

# Curva Precision-Recall para encontrar o limiar ideal focado em F1-Score
precision, recall, thresholds = precision_recall_curve(y_test, y_pred_proba)

# Evitando divisão por zero
f1_scores = 2 * (precision * recall) / (precision + recall + 1e-10)
best_threshold = thresholds[np.argmax(f1_scores)]

print(f"\nMelhor limiar (threshold) calculado: {best_threshold:.4f}")

# Aplicando o limiar personalizado no conjunto de teste
y_pred_custom = (y_pred_proba >= best_threshold).astype(int)

print("\nRelatório de Classificação (XGBoost com Limiar Otimizado):")
print(classification_report(y_test, y_pred_custom))


# ==========================================
# 6. EXPLICABILIDADE COM SHAP
# ==========================================
print("\nCalculando valores SHAP para explicabilidade...")

# Amostrando uma parte do teste para agilizar a computação do SHAP
X_test_sample = X_test.sample(1000, random_state=42)

explainer = shap.TreeExplainer(xgb_model)
shap_values = explainer.shap_values(X_test_sample)

# Gráfico de Importância Global das Variáveis
plt.figure(figsize=(10, 6))
shap.summary_plot(shap_values, X_test_sample, plot_type="bar", show=False)
plt.title("Importância das Variáveis (SHAP)")
plt.tight_layout()
plt.show()
