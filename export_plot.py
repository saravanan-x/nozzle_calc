import os
import numpy as np
import pandas as pd

def export_plot(tita_n, r1, rt, x, rx):

    # ------------------ CREATE DIRECTORY ------------------
    save_path = "/home/saravanan/Music/nozzle.py/plot"
    os.makedirs(save_path, exist_ok=True)   # create folder if not exists

    # 1. Divergent Arc
    t_vals_div = np.linspace(-np.pi/2, -np.pi/2 + tita_n, 100)
    x_div_arc = r1 * np.cos(t_vals_div)
    y_div_arc = r1 * np.sin(t_vals_div) + (rt + r1)

    # 2. Combine
    X_coords = np.concatenate([x_div_arc, x])
    Y_coords = np.concatenate([y_div_arc, rx])
    Z_coords = np.zeros_like(X_coords)

    df = pd.DataFrame({
        'X_mm': X_coords * 1000,
        'Y_mm': Y_coords * 1000,
        'Z_mm': Z_coords * 1000
    })

    df = df.round(6).drop_duplicates().reset_index(drop=True)

    # ------------------ FULL FILE PATH ------------------
    excel_file = os.path.join(save_path, "Bell_Nozzle_Divergent_Profile.xlsx")
    txt_file   = os.path.join(save_path, "Bell_Nozzle_Divergent_Profile.txt")

    # ------------------ SAVE ------------------
    df.to_excel(excel_file, index=False)
    df.to_csv(txt_file, sep='\t', index=False, header=False)

 