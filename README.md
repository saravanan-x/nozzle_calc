<div align="center" style="
    padding: 15px;
    border-radius: 12px;
    background: linear-gradient(135deg, #0F2027, #203A43, #2C5364);
    box-shadow: 0px 4px 20px rgba(0,0,0,0.4);">

<h1 style="
    color: #4FC3F7;
    font-size: 38px;
    margin: 0;
    font-weight: bold;">
Rocket Nozzle Design  
</h1>

<p style="
    color: #B0BEC5;
    font-size: 16px;
    margin-top: 5px;">
Flow Calculations • Simulation • Geometry
</p>

</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Aerospace-Propulsion-black?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Focus-Nozzle%20Design-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge"/>
</p>

## <span style = "color: lightgreen">Rocket Nozzle Design Calculations</span>
### Given Parameters

| Parameter | Variable | Parameter | Variable |
| :--- | :--- | :--- | :--- |
| **Thrust (N)** | $F$ | **Chamber Temp (K)** | $T_c$ |
| **Chamber Pressure (Pa)** | $P_c$ | **Specific Heat Ratio** | $\gamma$ |
| **Exit Pressure (Pa)** | $P_e$ | **Gas Constant (J/kg·K)** | $R$ |



###  Flow & Area Dynamics

| Metric | Formula | Metric | Formula |
| :--- | :--- | :--- | :--- |
| **Exit Velocity** | $\displaystyle V_e = \sqrt{\frac{2\gamma}{\gamma - 1} \cdot R T_c \cdot \left(1 - \left(\frac{P_e}{P_c}\right)^{\frac{\gamma - 1}{\gamma}}\right)}$ | **Exit Mach No.** | $\displaystyle M_e = \sqrt{\frac{2}{\gamma - 1} \left[ \left(\frac{P_c}{P_e}\right)^{\frac{\gamma - 1}{\gamma}} - 1 \right]}$ |
| **Mass Flow Rate** | $\displaystyle \dot{m} = \frac{F}{V_e}$ | **Area Ratio** | $\displaystyle \frac{A_e}{A_t} = \frac{1}{M_e} \left[ \frac{1 + \frac{\gamma - 1}{2} M_e^2}{\frac{\gamma + 1}{2}} \right]^{\frac{\gamma + 1}{2(\gamma - 1)}}$ |
| **Throat Area** | $\displaystyle A_t = \frac{\dot{m}}{P_c} \cdot \sqrt{\frac{R T_c}{\gamma} \cdot \left(\frac{\gamma + 1}{2}\right)^{\frac{\gamma + 1}{2(\gamma - 1)}}}$ | **Exit Area** | $\displaystyle A_e = A_t \cdot \frac{A_e}{A_t}$ |
| **Throat Diameter** | $\displaystyle d_t = \sqrt{\frac{4A_t}{\pi}}$ | **Exit Diameter** | $\displaystyle d_e = \sqrt{\frac{4A_e}{\pi}}$ |



###  Geometry & Structural Design

| Metric | Formula | Metric | Formula |
| :--- | :--- | :--- | :--- |
| **Chamber Diameter** | $\displaystyle d_c = 3 d_t$ | **Convergent Length** | $\displaystyle L_{conv} = \frac{d_c - d_t}{2 \tan(\alpha)}$ |
| **Chamber Area** | $\displaystyle A_c = \frac{\pi d_c^2}{4}$ | **Divergent Length** | $\displaystyle L_{div} = \frac{d_e - d_t}{2 \tan(\beta)}$ |
| **Chamber Length** | $\displaystyle L_c = \frac{L^* \cdot A_t}{A_c}$ | **Total Length** | $\displaystyle L_{total} = L_c + L_{conv} + L_{div}$ |
| **Wall Thickness** | $\displaystyle t_w = \frac{P_c \cdot d_c}{16000}$ | **Stress Check** | $\displaystyle \sigma = \frac{P_c \cdot d_c}{2 t_w}$ |
| **Design Thickness** | $\displaystyle t = \frac{P_c \cdot d_c \cdot SF}{2 \sigma_{yield}}$ | | |


## Features

- ✔ Nozzle geometry calculations  
- ✔ Atmospheric model (altitude-based)  
- ✔ Flow property analysis (Mach, thrust, ISP)  
- ✔ Conical nozzle plotting  
- ✔ Bell nozzle design (Rao method)  
- ✔ Export to Excel, TXT, and CAD formats  
- ✔ SolidWorks-compatible curve generation  

---

## Concepts Used

- Isentropic flow relations  
- Compressible flow  
- Rocket propulsion theory  
- Area–Mach relation  
- Rao bell nozzle design  

---

##  Project Structure
