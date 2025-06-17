# Adaptive Multi-Agent Exploration in Communication-Denied Environments

## 🎯 Mission Context & Assumptions

This project models a scenario inspired by DARPA-style challenges, prioritizing concept validation over full physical realism.

- **Environment**: Unknown, likely enclosed but possibly open. Topology and terrain complexity are not known a priori.
- **Agents**: Multiple autonomous robots deployed without any communication or identification capability.
  - No RF or acoustic communication.
  - No global positioning (e.g., GPS).
  - No active peer detection (no beacons, no IDs).
  - **Optional**: Passive short-range visual detection (future extension).
- **Sensors**: Each robot possesses onboard mapping capability (e.g., visual SLAM with depth or monocular camera, IMU, wheel odometry).
- **Objective**: Maximize cumulative environment coverage across all agents while ensuring at least partial map overlap between them to enable eventual map merging.
- **Constraints**:
  - Robots do not know each other’s starting positions or paths.
  - No direct coordination or shared decision-making.
  - Redundant coverage is wasteful but partial overlap is necessary for eventual map fusion.
  - Assumes the environment may contain obstacles, corners, and structural variation.

---

## 🔍 Core Concept

### Adaptive Behavior Based on Environmental Complexity

Each agent adaptively modulates its exploration behavior in response to *perceived terrain complexity*, using local mapping data alone.

- If the **local terrain is increasingly complex**, the robot:
  - Interprets this as a feature-rich area.
  - Moves more **erratically** (higher turning rate).
  - Explores more **densely** to maximize feature acquisition.
  
- If the **terrain is becoming simpler or more open**, the robot:
  - Interprets this as a sparse region with fewer features.
  - Moves more **linearly** (lower turning rate).
  - Attempts to **cover greater distance** with fewer turns.

This balances **coverage density** in cluttered areas with **spatial reach** in simpler terrain.

---

## 🔁 Exploration Logic Summary

Each robot follows an independent loop:

1. **Biased random walk**:
   - Biased away from previously covered regions (to reduce redundancy).
   - Frontier-seeking bias if available (regions adjacent to unexplored zones).

2. **Terrain complexity trend tracking**:
   - Maintain rolling measure of feature density change.
   - Adjust movement policy dynamically (turning rate vs. straight-line speed).

3. **Map overlap encouragement (passive)**:
   - No knowledge of other agents.
   - But partial overlap with others is encouraged via **entropy-aware motion** and **coverage divergence penalty**.

4. **(Future)**: Visual sighting of another robot can trigger local merge attempt if available.

---

## ⚠️ Limitations and Refinements

- **Complexity ≠ information**:
  - High feature density may not imply high *novelty*.
  - Additional metric: *information gain rate* (new features per unit distance).

- **Subjectivity risk**:
  - Terrain may be underestimated due to sensor degradation or occlusion.

- **No topological awareness**:
  - Robots can drift indefinitely in linear paths without recognizing junctions or unexplored branches.
  - Future enhancement: maintain basic graph of decision points.

---

## 🧠 Potential Improvement Terms

- **Information Gain Rate**: New map data acquired per step.
- **Path Redundancy Penalty**: A cost added when revisiting previously covered areas.
- **Merge Pressure**: A scalar increasing over time and distance from origin to motivate convergence behavior.
- **Exploration Bias**: A composite score computed to steer motion adaptively.

---

## 🧪 Simulation Approach (Future Work)

- 2D Python-based simulation using occupancy grids or feature maps.
- Robots act as particles with directional bias influenced by internal complexity metric.
- Visualize exploration paths, redundancy, and potential overlaps.