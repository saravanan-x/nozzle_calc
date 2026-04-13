import numpy as np
import math
import pandas as pd

#   SOLIDWORKS EXCEL / TEXT EXPORT                           
def export_plot(tita_n, r1, rt, x, rx):

    # 1. Divergent Arc (Throat to N)
    t_vals_div = np.linspace(-np.pi/2, -np.pi/2 + tita_n, 100)
    x_div_arc = r1 * np.cos(t_vals_div)
    y_div_arc = r1 * np.sin(t_vals_div) + (rt + r1)

    # 2. Bell Curve (N to Exit) - Variables 'x' and 'rx' are already defined in your code

    # Combine only the post-throat coordinate arrays into a single continuous path
    X_coords = np.concatenate([x_div_arc, x])
    Y_coords = np.concatenate([y_div_arc, rx])
    Z_coords = np.zeros_like(X_coords)  # Z is 0 for a 2D sketch

    # Your plot variables are in meters, so we multiply by 1000 for standard CAD mm dimensions
    df = pd.DataFrame({
        'X_mm': X_coords * 1000,
        'Y_mm': Y_coords * 1000,
        'Z_mm': Z_coords * 1000
    })

    # Drop overlapping endpoints between the piecewise segments to ensure a clean CAD curve
    df = df.round(6).drop_duplicates().reset_index(drop=True)

    # Export as an Excel sheet
    excel_file = "Bell_Nozzle_Divergent_Profile.xlsx"
    df.to_excel(excel_file, index=False)


    # Export as a raw Text file 
    txt_file = "Bell_Nozzle_Divergent_Profile.txt"
    df.to_csv(txt_file, sep='\t', index=False, header=False)
