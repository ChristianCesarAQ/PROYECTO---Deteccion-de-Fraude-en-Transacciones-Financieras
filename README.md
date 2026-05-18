# Sistema Inteligente de Detección de Fraude en Transacciones Financieras

Consiste en un sistema de información capaz de clasificar transacciones financieras como "Legítimas" o "Fraude" utilizando algoritmos de aprendizaje supervisado, implementados tanto en Python como en RapidMiner.

## Dataset Utilizado

El proyecto utiliza el conjunto de datos **Fraud Detection Transactions Dataset**, el cual cuenta con 50000 registros de transacciones financieras simulación de operaciones bancarias.

- **Fuente del Dataset:** [Enlace a Kaggle](https://www.kaggle.com/datasets/samayashar/fraud-detection-transactions-dataset)
- _Nota: Por políticas de almacenamiento, el archivo CSV no se sube a este repositorio y debe colocarse en la carpeta `data/` en local._

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
