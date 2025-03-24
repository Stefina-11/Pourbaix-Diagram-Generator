# Pourbaix-Diagram-Generator
This program generates Pourbaix diagrams, which are graphical representations of the stability of a metal in different pH and electrochemical potential conditions. It helps determine corrosion, protection, and passivation zones for a given metal.
How It Works
User Input:

The user selects a metal (currently supports Iron)

The user provides equilibrium potential values for various species of the metal

Calculation:

The program uses the Nernst equation to compute equilibrium lines for metal species

It defines three zones based on potential values:

Corrosion Zone (Unstable, metal dissolves)

Protection Zone (Stable, no significant corrosion)

Passivation Zone (Forms protective oxide layer)

Visualization:

The program plots the Pourbaix diagram using Matplotlib

It shades different zones for better understanding

A conclusion section highlights safe operating conditions for the metal

Deployment:

The application is built using Streamlit, allowing it to run as a web-based interactive tool

Key Features
✅ User-friendly Streamlit UI for easy input
✅ Dynamic Pourbaix diagram generation
✅ Customizable equilibrium potential values
✅ Clear visualization of corrosion behavior
