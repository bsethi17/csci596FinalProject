# 🌌 **Gas Particles in a Glass Box Simulation**

## 🧪 **Introduction**
This project simulates the dynamic behavior of gas particles inside a transparent glass box. It visually demonstrates principles of molecular dynamics, including collisions between particles and with walls, changes in particle speed, and energy exchanges. The simulation uses Blender for visualization and Python for scripting, making it an engaging way to explore the fundamentals of physics and computation.

## 🎯 **Key Applications Demonstrated**
1. **Particle Collision Physics**:
   - Elastic collisions between particles and with the walls of the box.
   - Speed changes and energy redistribution during collisions.

2. **Dynamic Speed-Based Behavior**:
   - Particles are categorized as:
     - **Blue (Slow)**: Low speed.
     - **Green (Medium)**: Moderate speed.
     - **Red (Fast)**: High speed.
   - Colors dynamically update based on speed after collisions.

3. **Interactive Visualization**:
   - Real-time updates to particle positions, velocities, and colors.
   - Transparent box provides a clear view of particle behavior.

4. **Applications**:
   - Understanding principles of thermodynamics and molecular motion.
   - Educational tool for teaching collision physics and energy conservation.
   - Visualizing speed distributions and kinetic energy exchanges in a confined system.

## 🌀 **Speed Ranges**

The particles are categorized based on their speed (|v|):

- **Slow (Blue)**: |v| < 0.5 × VELOCITY_SCALE
- **Medium (Green)**: 0.5 × VELOCITY_SCALE ≤ |v| < 1.5 × VELOCITY_SCALE
- **Fast (Red)**: |v| ≥ 1.5 × VELOCITY_SCALE

For example, if VELOCITY_SCALE = 2.0:
- **Slow (Blue)**: Speeds less than 1.0.
- **Medium (Green)**: Speeds between 1.0 and 3.0.
- **Fast (Red)**: Speeds greater than or equal to 3.0.

## 🛠️ **Tools and Technologies Used**
- **Blender**:
  - Used as the 3D visualization platform.
  - Provides particle animation and rendering.
- **Python**:
  - Scripts written in Python control the simulation logic.
  - Utilizes Blender's Python API for object manipulation and animation.

## 📈 **Applications of This Simulation**
- **Scientific Computing**:
  - Modeling molecular dynamics and particle systems in a confined environment.
- **Physics Education**:
  - Visualizing particle motion, collisions, and energy changes to aid learning.
- **Data Visualization**:
  - Demonstrating dynamic speed categorization and its impact on system behavior.
- **Research Prototyping**:
  - Simulating small-scale systems to explore thermodynamic principles.

## 🎯 **Final Objective**
We aim to achieve a state where the particles in the system eventually reach a uniform distribution of speeds, representing an equilibrium state in the confined system.

## 👥 **Team Members**
- **Bhavya Sethi**
- **Anurag Maravi**
- **Deep Prajapati**

## 📚 **References**
1. **Blender Documentation**:
   - Official Blender Documentation: [https://docs.blender.org/](https://docs.blender.org/)
   - Blender Python API Reference: [https://docs.blender.org/api/current/](https://docs.blender.org/api/current/)

2. **Physics Resources**:
   - Elastic Collision Theory: [https://en.wikipedia.org/wiki/Elastic_collision](https://en.wikipedia.org/wiki/Elastic_collision)
   - Principles of Molecular Dynamics: [https://en.wikipedia.org/wiki/Molecular_dynamics](https://en.wikipedia.org/wiki/Molecular_dynamics)

3. **Python Resources**:
   - Python Official Documentation: [https://www.python.org/doc/](https://www.python.org/doc/)

4. **Tutorials and Examples**:
   - Blender Guru Tutorials: [https://www.blenderguru.com/](https://www.blenderguru.com/)
   - Stack Overflow (Blender & Python discussions): [https://stackoverflow.com/](https://stackoverflow.com/)
