Modelo de Aprendizaje Supervisado en Python 

Estudiantes: 
Jhon Fredy Rada 

Nicolas Fabian Caceres

Modelo de aprendizaje automático supervisado usando Python. Este modelo predice la cantidad de pasajeros que puede tener una ruta de transporte masivo, 
basándose en variables como la hora, el clima, el
tráfico, entre otras. Todo esto es simulado, pero muestra cómo se puede usar la inteligencia artificial para mejorar el transporte público.

Paso 1: Importar las librerías
Importamos las librerías necesarias para manipular datos y construir el modelo. Usamos pandas,
numpy y sklearn, que es una librería de machine learning.

Paso 2: Crear un dataset simulado
Creamos 500 registros con variables como ruta, hora, día de la semana, clima y tráfico.
Representan situaciones reales en el transporte público.

Paso 3: Agregar la variable objetivo
La columna 'pasajeros' representa la cantidad de personas en un viaje. Se calcula con reglas
lógicas como aumento en hora pico y reducción con tráfico alto.

Paso 4: Convertir texto a números
Los algoritmos entienden números, por eso usamos LabelEncoder para transformar palabras como
'lunes' o 'nublado' en valores numéricos.

Paso 5: Separar variables de entrada y salida
Dividimos los datos en X (variables predictoras) e y (variable objetivo: pasajeros).

Paso 6: Dividir datos en entrenamiento y prueba
Usamos 80% de los datos para entrenar el modelo y 20% para probar qué tan bien predice en
datos nuevos.

Paso 7: Entrenar el modelo
Creamos un modelo Random Forest Regressor y lo entrenamos con los datos. Este modelo
aprende patrones para hacer predicciones numéricas.

Paso 8: Hacer predicciones y evaluar
Probamos el modelo y calculamos el error cuadrático medio (MSE). Entre menor sea este valor,
mejor es la predicción.
Conclusión
Creamos un modelo de aprendizaje supervisado que predice la cantidad de pasajeros en el
transporte masivo. Este tipo de modelos pueden ayudar a mejorar el servicio y la toma de
decisiones.
