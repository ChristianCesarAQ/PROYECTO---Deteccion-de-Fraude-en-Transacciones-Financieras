import os
import joblib
import pandas as pd


def evaluar_transaccion(cant_fallidas, risk_score):
    """
    Carga el modelo serializado del Árbol de Decisión y evalúa 
    los parámetros de una transacción para determinar si es fraude.
    """
    try:
        # Resolución de rutas para localizar el modelo .pkl
        base_dir = os.path.dirname(__file__) if __file__ else os.getcwd()

        posibles_rutas = [
            os.path.join(base_dir, 'notebooks', 'modelo_arbol_decision.pkl'),
            os.path.join(os.path.dirname(base_dir), 'notebooks',
                         'modelo_arbol_decision.pkl'),  # Si validator está en /src
            # Caída de respaldo
            os.path.join(base_dir, 'modelo_arbol_decision.pkl')
        ]

        model_path = None
        for ruta in posibles_rutas:
            if os.path.exists(ruta):
                model_path = ruta
                break

        if not model_path:
            return {
                "codigo": -1,
                "estado": "ERROR",
                "motivo": f"No se encontró 'modelo_arbol_decision.pkl'. Buscado en: {posibles_rutas}"
            }

        # Cargar modelo persistido
        model = joblib.load(model_path)

        # Reconstruir el DataFrame
        if hasattr(model, 'feature_names_in_'):
            columnas_originales = model.feature_names_in_
            # Inicializar todas las variables decorativas del dataset original en 0.0
            datos = {col: [0.0] for col in columnas_originales}
            # Inyectar las variables analíticas que el árbol realmente evalúa
            datos['Failed_Transaction_Count_7d'] = [float(cant_fallidas)]
            datos['Risk_Score'] = [float(risk_score)]
            # Reordenamos las columnas
            df_input = pd.DataFrame(datos)[columnas_originales]
        else:
            # Respaldo simple por si el modelo no guardó los nombres de las columnas
            df_input = pd.DataFrame({
                'Failed_Transaction_Count_7d': [float(cant_fallidas)],
                'Risk_Score': [float(risk_score)]
            })

        # Ejecutar la predicción del modelo
        prediccion = model.predict(df_input)[0]

        # Estructurar y retornar la respuesta
        if prediccion == 1:
            return {
                "codigo": 1,
                "estado": "RECHAZADA",
                "motivo": "Alerta de fraude: La operación quiebra los umbrales seguros del Árbol de Decisión."
            }
        else:
            return {
                "codigo": 0,
                "estado": "APROBADA",
                "motivo": "Transacción legítima: Los parámetros se encuentran dentro de los rangos normales."
            }

    except ValueError:
        return {"codigo": -1, "estado": "ERROR", "motivo": "Los datos de entrada deben ser estrictamente numéricos."}
    except Exception as e:
        return {"codigo": -1, "estado": "ERROR", "motivo": f"Falla inesperada en el motor de reglas: {str(e)}"}
