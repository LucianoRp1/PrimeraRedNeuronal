<h2>En esta sección se importan las librerías necesarias para el desarrollo del programa. numpy es una librería para realizar operaciones matemáticas en Python, tensorflow es una librería de aprendizaje automático y matplotlib es una librería para graficar datos.</h2>

 import numpy as np<br/>
import tensorflow as tf <br/>
import matplotlib.pyplot as plt <br/>

--------------------------------------------------------------

<h2>Se definen los datos de entrada datos_x y los datos de salida datos_y. En este caso, los datos de entrada representan una distancia en metros y los datos de salida la misma distancia, pero en yardas.</h2>

 <h4> datos de entrada X (en metros)
datos_x = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]], dtype=float)</h4><br/>

<h4> datos de salida Y (en yardas)
datos_y = np.array([[1093.61], [2187.22], [3280.84], [4374.46], [5468.08], [6561.69], [7655.31], [8748.93], [9842.55], [10936.17]], dtype=float) </h4>
--------------------------------------------------------------

<h2>Luego se define la topología de la red neuronal con la capa Dense de tensorflow. En este caso, se define una capa con un solo neurona y una entrada.</h2>

  topología de la red
 <h4>capa1 = tf.keras.layers.Dense(units=1, input_shape=[1])</h4><br/>

creacion del tipo de red 
<h4>modelo = tf.keras.Sequential([capa1]) </h4>
--------------------------------------------------------------


<h2>En esta parte se define el optimizador, que es el algoritmo utilizado para minimizar el error de la red neuronal. Se utiliza el optimizador Adam y se define la función de pérdida mean_squared_error.</h2>

 <h4>modelo.compile(
    optimizer= tf.keras.optimizers.Adam(1) ,
    loss= 'mean_squared_error',
    metrics=['mse']
) </h4>
-------------------------------------------------------------

<h2>En este caso se entrena la red neuronal. Se utiliza la función fit de tensorflow para entrenar la red con los datos de entrada y salida definidos anteriormente. Se realizan 9000 épocas de entrenamiento y el argumento verbose=False es para que no muestre el progreso del entrenamiento</h2>

<h4> entrenamiento = modelo.fit(datos_x, datos_y, epochs=9000, verbose= False) </h4>

--------------------------------------------------------------

<h2>Se guardan los pesos de la red neuronal en dos archivos distintos. La función save se utiliza para guardar la arquitectura de la red y la función save_weights se utiliza para guardar los pesos de la red.</h2>


<h4>modelo.save('first_red_neuronal.h5')</h4><br/>
 <h4>modelo.save_weights('yd.h5') </h4>
--------------------------------------------------------------


<h2>Finalmente, se utiliza el modelo para hacer predicciones. El usuario puede ingresar la cantidad de metros a convertir en yardas.</h2>

 <h4>yd = float(input('Ingrese la cantidad de metros a convertir en yardas : '))</h4><br/>
<h4>meters = modelo.predict([yd])[0][0]</h4><br/>
<h4>print('{} metro equivale a {} yardas'.format(yd, meters)) </h4><br/><br/>
