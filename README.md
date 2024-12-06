# 🌌 **Particle Collision in a Glass Box Simulation**

---

## 🧪 **Introduction**

This project simulates the dynamic behavior of gas particles inside a transparent glass box. It visually demonstrates principles of molecular dynamics, including collisions between particles and with walls, changes in particle speed, and energy exchanges. The simulation uses Blender for visualization and Python for scripting, making it an engaging way to explore the fundamentals of physics and computation.

---

## 🎬 **Demo Video**

![Render Video](render.gif)

---

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

---

## 🔢 **Formula Used**

To handle particle-particle collisions and ensure energy and momentum conservation, the following **elastic collision formula** is used:

**Velocity of Particle 1 after Collision**:

$$
v_1' = v_1 - \frac{2m_2}{m_1 + m_2} \frac{(v_1 - v_2) \cdot (x_1 - x_2)}{\|x_1 - x_2\|^2} (x_1 - x_2)
$$

**Velocity of Particle 2 after Collision**:

$$
v_2' = v_2 - \frac{2m_1}{m_1 + m_2} \frac{(v_2 - v_1) \cdot (x_2 - x_1)}{\|x_2 - x_1\|^2} (x_2 - x_1)
$$

Where:

- `m1, m2`: Masses of the particles (assumed equal for simplicity).
- `x1, x2`: Positions of the particles.
- `v1, v2`: Velocities of the particles.
- `⋅`: Dot product.
- `||x1 - x2||`: Distance between particle centers.

This ensures that both momentum and kinetic energy are conserved during collisions.

---

## 🌀 **Speed Ranges**

The particles are categorized based on their speed (|v|) as follows:

- **Slow (Blue)**: |v| < 0.5 × VELOCITY_SCALE
- **Medium (Green)**: 0.5 × VELOCITY_SCALE ≤ |v| < 1.5 × VELOCITY_SCALE
- **Fast (Red)**: |v| ≥ 1.5 × VELOCITY_SCALE

**Unit for Velocity**: Arbitrary units (a.u.), normalized for visualization purposes.

For example, if VELOCITY_SCALE = 2.0:

- **Slow (Blue)**: Speeds less than 1.0 a.u.
- **Medium (Green)**: Speeds between 1.0 and 3.0 a.u.
- **Fast (Red)**: Speeds greater than or equal to 3.0 a.u.

---

## 🛠️ **Tools and Technologies Used**

- **Blender**:
  - Used as the 3D visualization platform.
  - Provides particle animation and rendering.
- **Python**:
  - Scripts written in Python control the simulation logic.
  - Utilizes Blender's Python API for object manipulation and animation.

---

## 🚀 **How to Run the Script in Blender**

1. **Open Blender**:

   - Launch the Blender application on your system.

2. **Go to the Scripting Tab**:

   - In the Blender interface, switch to the **Scripting** workspace.

3. **Load the Script**:

   - Open the Python script (`ParticleCollision.py`) in the scripting editor.

4. **Run the Script**:

   - Click the **Run Script** button in the scripting editor.
   - This initializes the simulation, creates the box and particles, and sets up animation handlers.

5. **Play the Animation**:
   - In the timeline at the bottom of the interface, click the **Play** button.
   - Observe the particles moving, colliding, and dynamically changing colors based on their speeds.

---

## 📈 **Applications of This Simulation**

- **Scientific Computing**:
  - Modeling molecular dynamics and particle systems in a confined environment.
- **Physics Education**:
  - Visualizing particle motion, collisions, and energy changes to aid learning.
- **Data Visualization**:
  - Demonstrating dynamic speed categorization and its impact on system behavior.
- **Research Prototyping**:
  - Simulating small-scale systems to explore thermodynamic principles.

---

## 🎯 **Final Objective**

We aim to achieve a state where the particles in the system eventually reach a uniform distribution of speeds, representing an equilibrium state in the confined system.

---

## 👥 **Team Members**

- **Bhavya Sethi**
- **Anurag Maravi**
- **Deep Prajapati**

---

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
