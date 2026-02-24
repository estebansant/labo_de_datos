import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")
# Variables que vamos a usar
features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
target = "Survived"

# Nos quedamos con esas columnas
data = df[features + [target]].copy()

# Manejo simple de valores faltantes
data["Age"] = data["Age"].fillna(data["Age"].median())
data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0])

X = data[features]
y = data[target]

# Columnas categóricas y numéricas
cat = ["Sex", "Embarked"]
num = ["Pclass", "Age", "SibSp", "Parch", "Fare"]

# One-hot encoding solo en las categóricas
prep = ColumnTransformer(
    [("cat", OneHotEncoder(), cat)],
    remainder="passthrough"
)

# Separar train / test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Transformar datos
X_train2 = prep.fit_transform(X_train)
X_test2 = prep.transform(X_test)

# Entrenar árbol
model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train2, y_train)

# Evaluación
y_pred = model.predict(X_test2)
print("Accuracy:", accuracy_score(y_test, y_pred))



plt.figure(figsize=(12,6))
plot_tree(model, filled=True)
plt.show()