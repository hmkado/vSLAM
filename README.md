# Simulated MAS-vSLAM

Project using Raspberry Pi 5 and Intel D435 to create an indoor Differential Drive Visual-SLAM Robot on ROS2 platform.

Ultimately use one robot multiple times to simulate multiple robots mapping different areas. We will attempt to find a (hopefully novel) approach.

## Assumptions
Based on my thesis, Anti-cohesion swarming. Similar to Boids.

## What we have now
- Raspberry Pi 5 + active fan
- Intel Realsense D435

## Parts list (not yet purchased)
- 2 * 310 Encoder Motors, Rated Voltage 7.4V, Rated Power 4.8W, Gear 1:20, 9000 RPM (~450 RPM after reduction) , Rated Torque 0.4 kg*cm, AB phase Hall Encoder
- 1 * Raspberry Pi 5 power extension board from Yahboom
- 1 * STM32F103C8T6 - For encoder offloading
- 1 * 3S 5000 mah 100C T-connector LiPo
- 1 * 12/24V to 5V 10A step down buck converter
- 1 * 1 Male to 2 Female T-connector splitter
- 2 * TB6612FNG Motor Driver
- 2 * MPU-6050 IMU

- 1 * 1 inch generic caster wheel
- 2 * motor bracket
- 2 * rubber tires
- 1 * bracket for chassis 
