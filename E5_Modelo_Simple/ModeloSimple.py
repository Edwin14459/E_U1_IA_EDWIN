from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]  #va de uno en uno datos
Y = [2, 4, 6, 8, 10]           #va de dos en dos datos

# Crear y entrenar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X, Y)

# Hacer una predicción para un nuevo valor de X
nuevo_X = [[6]]
prediccion = modelo.predict(nuevo_X)

print(f"Predicción para X = {nuevo_X[0][0]}: {prediccion[0]:.2f}")