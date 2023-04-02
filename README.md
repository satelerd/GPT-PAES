# GPT-PAES

## ¿Que pasa si le pasas la prueba PAES a la IA mas avanzada (GPT4)?

#### ¿Que es PAES?
Prueba de Acceso a la Educación Superior (PAES) es una prueba (anteriormente conocida como PSU o PTU) que debe ser realizada por todo Chileno que quiera acceder a la universidad. En esta prueba se evalúa el nivel de conocimiento de los estudiantes en 3 áreas: Matemáticas, Lenguaje y Ciencias.
En nuestro caso, nos enfocaremos en la prueba de Lenguaje.

#### ¿Que es GPT-4?
GPT-4 es una IA desarrollada por OpenAI que fue entrenada con "practicamente todo el texto de internet" para generar texto. Es decir, si le pasas un texto de entrada, GPT-4 te generará un texto de salida que sigue con el contexto anterior. Esto lo hace capaz de entender y comunicarse en lenguaje natural.
En nuestro caso, le daremos la PAES como texto de entrada y le pediremos a GPT-4 que nos responda con las respuestas de cada una de las preguntas.

## ¿Como funciona?

GPT-4 es sorprendentemente facil de entender y usar, no es necesario tener conocimientos de IA para usarlo. Solo necesitas un poco de internet.

#### Paso 1: Descargar el texto de la PAES
Podemos encontrar la PAES en el [Demre](https://demre.cl/publicaciones/2023/pruebas-oficiales-paes), pero debido a que GPT-4 tiene un limite caracteres por request, debemos dividirlo en archivos mas pequeños de 7 preguntas cada uno. 

#### Paso 2: Diseño de Prompt
Primero debemos obtener una API Key (en [OpenAI](https://beta.openai.com/)).
El prompt es el texto de entrada que le pasaremos a GPT-4. Dependiendo de este texto es que la IA podra generar respuestas coherentes y con el formato correcto. En la carpeta `prompts` se encuentran las distintas versiones de prompts que usamos para generar las respuestas de la PAES.

### Paso 3: Logica de programacion
Usaremos python para ciclar por cada set de preguntas y hacer un request a GPT-4 para que nos responda con las respuestas y las guardaremos en un excel.

## ¿Como usarlo?
Es muy simple, simplemente hay que clonar el repositorio y ejecutar el archivo `main.py`.
Puedes cambiar las variables (desde la linea 12 a las 15), donde puedes seleccionar el prompt a usar y el numero de sets de preguntas a usar (en el caso de comprension lectora, 8 set contienen toda la prueba).

## Para futuras versiones
- Siempre podemos mejorar los prompt... sustancialmente. (Chain of thought)
