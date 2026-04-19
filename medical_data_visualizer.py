import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Importar el dataset en un DataFrame
df = pd.read_csv("medical_examination.csv")

# 2. Crear columna 'overweight'
# Se calcula el BMI: weight / (height en metros)^2
# Si BMI > 25 → overweight = 1, si no → 0
df["overweight"] = (
    df["weight"] / ((df["height"] / 100) ** 2) > 25
).astype(int)

# 3. Normalizar cholesterol y gluc
# 1 = bueno → 0
# 2 o 3 = malo → 1
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)


def draw_cat_plot():
    # 4. Convertir datos a formato largo (long format)
    # Esto permite analizar múltiples variables categóricas en un solo gráfico
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]
    )

    # 5. Agrupar los datos por:
    # cardio (enfermedad), variable y valor (0 o 1)
    # Se cuentan las ocurrencias de cada combinación
    df_cat = (
        df_cat.groupby(["cardio", "variable", "value"])
        .size()
        .reset_index(name="total")
    )

    # 6. Crear gráfico categórico
    # Se separa por cardio (0 y 1)
    # Se muestran las cantidades de cada variable (good vs bad)
    fig = sns.catplot(
        data=df_cat,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar"
    )

    # 7. Obtener figura final
    fig = fig.fig
    return fig


def draw_heat_map():
    # 8. Limpiar datos incorrectos
    # - presión diastólica > sistólica
    # - altura y peso fuera de percentiles 2.5% y 97.5%
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"]) &
        (df["height"] >= df["height"].quantile(0.025)) &
        (df["height"] <= df["height"].quantile(0.975)) &
        (df["weight"] >= df["weight"].quantile(0.025)) &
        (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # 9. Calcular matriz de correlación
    corr = df_heat.corr()

    # 10. Crear máscara para ocultar triángulo superior
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 11. Configurar figura
    fig, ax = plt.subplots(figsize=(12, 10))

    # 12. Dibujar heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
        ax=ax
    )

    return fig