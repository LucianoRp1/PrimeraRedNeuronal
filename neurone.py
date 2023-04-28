# librerias
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


#eventos pasados
# datos de entrada X (en metros)
datos_x = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]], dtype=float)

# datos de salida Y (en yardas)
datos_y = np.array([[1093.61], [2187.22], [3280.84], [4374.46], [5468.08], [6561.69], [7655.31], [8748.93], [9842.55], [10936.17]], dtype=float)

# topología de la red
capa1 = tf.keras.layers.Dense(units=1, input_shape=[1])

#creacion del tipo de red 
modelo = tf.keras.Sequential([capa1])

#optimizador y metrica de perdida
modelo.compile(
    optimizer= tf.keras.optimizers.Adam(1) ,
    loss= 'mean_squared_error',
    metrics=['mse']
)

#entrenamos la red

entrenamiento = modelo.fit(datos_x, datos_y, epochs=9000, verbose= False)

# evaluación del modelo
error = modelo.evaluate(datos_x, datos_y)
print('Error:', error)

#guardamos en entrenamiento de la red
modelo.save('first_red_neuronal.h5')
modelo.save_weights('yd.h5')

#predicciones
yd = float(input('Ingrese la cantidad de metros a convertir en yardas : '))
meters = modelo.predict([yd])[0][0]
print('{} metro equivale a {} yardas'.format(yd, meters))