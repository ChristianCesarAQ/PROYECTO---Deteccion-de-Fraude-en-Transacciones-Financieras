# Sistema Inteligente de Detección de Fraude en Transacciones Financieras

Este proyecto consiste en un Sistema de Información Inteligente capaz de clasificar transacciones financieras como _"Legítimas"_ o _"Fraude"_ utilizando algoritmos de aprendizaje supervisado. El desarrollo sigue un enfoque metodológico híbrido, combinando la flexibilidad y control del código en **Python** con la auditoría, análisis estructural y validación visual de **RapidMiner Studio**.

La solución no solo se limita al modelado matemático, sino que abarca todo el ciclo de vida del dato, culminando en la persistencia del modelo optimizado y su despliegue en producción mediante una plataforma web interactiva.

## Dataset Utilizado

El proyecto utiliza el conjunto de datos **Fraud Detection Transactions Dataset**, el cual cuenta con 50000 registros de transacciones financieras simulación de operaciones bancarias.

- **Fuente del Dataset:** [Enlace a Kaggle](https://www.kaggle.com/datasets/samayashar/fraud-detection-transactions-dataset)
- _Nota: Por políticas de almacenamiento, el archivo CSV no se sube a este repositorio y debe colocarse en la carpeta `data/` en local._

## Despliegue y Enlaces del Proyecto

- **Aplicación Web en Producción (Streamlit):** [Acceder a la App](https://proyecto---deteccion-de-fraude-en-transacciones-financieras-c3.streamlit.app/)
- **Repositorio del Código Fuente:** [GitHub Repository](https://github.com/ChristianCesarAQ/PROYECTO---Deteccion-de-Fraude-en-Transacciones-Financieras.git)

## Tecnologías y Librerías

- **Entorno Visual:** RapidMiner Studio
- **Lenguaje:** Python 3.12.0
- **Librerías Core:** Streamlit, Scikit-Learn, Pandas, NumPy, Joblib

## 📁 Estructura del Proyecto

- `data/` : Repositorio local para el dataset de Kaggle.
- `notebooks/` : Jupyter Notebooks con el Análisis Exploratorio (EDA) y entrenamiento.
- `rapidminer/` : Archivos de proceso `.rmp` desarrollados en la plataforma visual.
- `src/` : Código fuente de la aplicación en producción.
  - `app.py` : Interfaz de usuario web interactiva desarrollada en Streamlit.
  - `validator.py` : Módulo de reglas de validación de datos de entrada.

## Instrucciones para Ejecución Local

Si deseas clonar y ejecutar este proyecto en tu computadora, sigue estos pasos:

1. **Clonar el repositorio:**

   ```bash
   git clone [https://github.com/ChristianCesarAQ/PROYECTO---Deteccion-de-Fraude-en-Transacciones-Financieras.git](https://github.com/ChristianCesarAQ/PROYECTO---Deteccion-de-Fraude-en-Transacciones-Financieras.git)
   cd PROYECTO---Deteccion-de-Fraude-en-Transacciones-Financieras

   ```

2. **Crear y activar el entorno virtual:**

   ```bash
   python -m venv .venv
   # En Windows :
   .venv\Scripts\activate
   # En Mac/Linux:
   source .venv/bin/activate

   ```

3. **Instalar dependecias:**

   ```bash
   pip install -r requirements.txt

   ```

4. **Descargar dataset de Kaggle**
   colocar archivo descargado en data/

5. **Correr interfaz de usuario(Streamlit):**
   ```bash
   streamlit run src/app.py
   ```
