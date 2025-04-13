import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Crear un dataset simulado para transporte masivo
np.random.seed(42)  # para resultados reproducibles

n = 100  # número de registros
horas = np.random.choice(['06:00', '07:00', '08:00', '09:00', '17:00', '18:00'], n)
dias = np.random.choice(['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo'], n)
climas = np.random.choice(['soleado', 'nublado', 'lluvioso'], n)
trafico = np.random.choice(['bajo', 'medio', 'alto'], n)

# Crear variable objetivo: número de pasajeros (simulado)
def calcular_pasajeros(hora, dia, clima, trafico):
    base = np.random.randint(20, 60)
    if hora in ['07:00', '08:00', '17:00', '18:00']:
        base += np.random.randint(15, 25)
    if dia in ['sábado', 'domingo']:
        base -= np.random.randint(10, 20)
    if clima == 'lluvioso':
        base += np.random.randint(5, 15)
    if trafico == 'alto':
        base -= np.random.randint(5, 10)
    return max(base, 0)

pasajeros = [calcular_pasajeros(h, d, c, t) for h, d, c, t in zip(horas, dias, climas, trafico)]

# Crear dataframe
datos = pd.DataFrame({
    "hora": horas,
    "dia": dias,
    "clima": climas,
    "trafico": trafico,
    "pasajeros": pasajeros
})

# Convertir variables categóricas en variables dummy (one-hot encoding)
datos_dummy = pd.get_dummies(datos.drop("pasajeros", axis=1))

# Variables de entrada (X) y variable objetivo (y)
X = datos_dummy
y = datos["pasajeros"]

# Dividir en datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Predecir
y_pred = modelo.predict(X_test)

# Medir desempeño
mse = mean_squared_error(y_test, y_pred)
print("Error cuadrático medio (MSE):", round(mse, 2))

# 👉 AGREGADO: Predecir para todo el conjunto original y exportar CSV
datos["prediccion_pasajeros"] = modelo.predict(X)

# Exportar a CSV
datos.to_csv("predicciones_rutas.csv", index=False)
