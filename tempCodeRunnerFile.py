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

    if metal not in METAL_DATA:
        print("Error: Metal not supported!")
        return

    species = METAL_DATA[metal]["species"]
    equilibrium_lines = METAL_DATA[metal]["equations"](pH_range, potentials)

    # --- Conclusion: Identify Corrosion-Resistant Region ---
    protection_potential_max = equilibrium_lines[0].min()
    passivation_potential_min = equilibrium_lines[2].max()
    
    conclusion_text = f"""
    --- Conclusion ---
    The metal {metal} is resistant to corrosion under the following conditions:
    🔹 **Protection Zone:** pH range 0-14, Potential ≤ {protection_potential_max:.2f} V
    🔹 **Passivation Zone:** pH range 0-14, Potential ≥ {passivation_potential_min:.2f} V
    """
    print(conclusion_text)  # Print before plotting to ensure visibility

    # Plot Setup
    plt.figure(figsize=(8, 6))
    plt.title(f"Pourbaix Diagram for {metal}")
    plt.xlabel("pH")
    plt.ylabel("Potential (V)")

    # Region Colors
    plt.axhspan(-2, protection_potential_max, color='#FFFF99', alpha=0.5, label="Protection")
    plt.axhspan(protection_potential_max, passivation_potential_min, color='#FFCCCC', alpha=0.5, label="Corrosion")
    plt.axhspan(passivation_potential_min, 2, color='#CCFFCC', alpha=0.5, label="Passivation")

    # Plot Equilibrium Lines
    line_styles = ['k--', 'k-.', 'k:', 'k-', 'k-']
    for i in range(len(equilibrium_lines)):
        plt.plot(pH_range, equilibrium_lines[i], line_styles[i], label=f"{metal} {species[i]}")

    plt.legend()
    plt.grid(True)
    plt.show()

# --- User Input ---
metal = input("Enter metal name (Iron): ").capitalize()

if metal not in METAL_DATA:
    print("Error: Unsupported metal!")
else:
    potentials = []
    print("Enter the following potential values:")
    for species in METAL_DATA[metal]["species"]:
        potentials.append(float(input(f"Enter {metal} ({species}) potential: ")))

    # Generate and Display Pourbaix Diagram
    plot_pourbaix(metal, potentials)

