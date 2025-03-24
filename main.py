import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Define Metal Data and Equilibrium Equations
METAL_DATA = {
    "Iron": {
        "species": ["Fe2+", "Fe3+", "FeOH2", "Fe2O3", "Fe3O4"],
        "equations": lambda pH, potentials: [
            np.full_like(pH, potentials[0]),  # Fe2+ ↔ Fe
            potentials[1] - 0.059 * pH,       # Fe3+ ↔ Fe2+
            potentials[2] - 0.059 * pH,       # FeOH2 formation
            potentials[3] - 0.059 * pH,       # Fe2O3 formation
            potentials[4] - 0.059 * pH        # Fe3O4 formation
        ]
    }
}

def plot_pourbaix(metal, potentials):
    pH_range = np.linspace(0, 14, 100)

    species = METAL_DATA[metal]["species"]
    equilibrium_lines = METAL_DATA[metal]["equations"](pH_range, potentials)

    # Identify corrosion-resistant regions
    protection_potential_max = equilibrium_lines[0].min()
    passivation_potential_min = equilibrium_lines[2].max()
    
    # Display conclusion
    st.subheader("Conclusion")
    st.markdown(f"""
    **The metal {metal} is resistant to corrosion under the following conditions:**
    - **Protection Zone:** pH range 0-14, Potential ≤ {protection_potential_max:.2f} V
    - **Passivation Zone:** pH range 0-14, Potential ≥ {passivation_potential_min:.2f} V
    """)
    
    # Plot Setup
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(f"Pourbaix Diagram for {metal}")
    ax.set_xlabel("pH")
    ax.set_ylabel("Potential (V)")

    # Region Colors
    ax.axhspan(-2, protection_potential_max, color='#FFFF99', alpha=0.5, label="Protection")
    ax.axhspan(protection_potential_max, passivation_potential_min, color='#FFCCCC', alpha=0.5, label="Corrosion")
    ax.axhspan(passivation_potential_min, 2, color='#CCFFCC', alpha=0.5, label="Passivation")

    # Plot Equilibrium Lines
    line_styles = ['k--', 'k-.', 'k:', 'k-', 'k-']
    for i in range(len(equilibrium_lines)):
        ax.plot(pH_range, equilibrium_lines[i], line_styles[i], label=f"{metal} {species[i]}")

    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Streamlit UI
st.title("Pourbaix Diagram Generator")

# Metal Selection (Currently only Iron is supported)
metal = st.selectbox("Select Metal", list(METAL_DATA.keys()))

st.subheader("Enter Equilibrium Potentials (V)")

potentials = []
for species in METAL_DATA[metal]["species"]:
    potentials.append(st.number_input(f"{metal} ({species}) Potential", value=0.0, step=0.1))

if st.button("Generate Pourbaix Diagram"):
    plot_pourbaix(metal, potentials)
