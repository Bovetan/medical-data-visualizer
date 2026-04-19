from medical_data_visualizer import draw_cat_plot, draw_heat_map

if __name__ == "__main__":
    # Generar y guardar gráfico categórico
    draw_cat_plot().savefig("catplot.png")

    # Generar y guardar heatmap
    draw_heat_map().savefig("heatmap.png")

    print("Plots created successfully.")