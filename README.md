# Variable-Stiffness-Pendulum-SysID
2026.04.21started

# Variable-Stiffness-Pendulum-SysID

## Data-Driven System Identification for a Variable Stiffness Pendulum

---

## 1. Overview

This project presents a **data-driven system identification framework** for a variable stiffness pendulum, combining **physics-based modeling**, **experimental data acquisition**, and **numerical optimization**.

A physical pendulum system with adjustable stiffness is constructed, and its dynamic behavior is captured using an IMU sensor. Unknown system parameters (damping and equivalent stiffness) are identified by minimizing the discrepancy between real-world data and simulated responses.

Beyond parameter identification, the project further explores the **mapping between structural parameters and dynamic performance**, forming a basis for future **multi-constraint optimization** in variable stiffness systems.

---

## 2. Motivation

In many engineering systems (e.g., robotics, compliant mechanisms), dynamic performance is governed by:

* Structural parameters (geometry, stiffness)
* Physical properties (mass, damping)
* External constraints

However, these parameters are often difficult to estimate directly.

This project aims to:

* Bridge **physical systems and data-driven modeling**
* Enable **accurate parameter identification**
* Lay the foundation for **design optimization**

---

## 3. System Description

### 3.1 Mechanical Structure

* Single pendulum with adjustable spring attachment point
* Lever arm length (r) controls equivalent stiffness
* Moment of inertia (J) computed from CAD (SolidWorks)

### 3.2 Sensors and Hardware

* IMU: MPU6050 (pitch angle measurement)
* Controller: Raspberry Pi / ESP32 / Arduino
* Sampling rate: **100 Hz**

### 3.3 Experimental Setup

* Initial condition: (\theta(0) = 30^\circ), (\dot{\theta}(0) = 0)
* Release method: non-contact (string burn / quick release)
* Data recorded until full decay

---

## 4. Mathematical Model

The system is modeled as a second-order linear dynamical system:

J \ddot{\theta} + c \dot{\theta} + K_{eq} \theta = 0

Where:

* (J): moment of inertia (known)
* (c): damping coefficient (unknown)
* (K_{eq}): equivalent stiffness (unknown)

---

## 5. System Identification

### 5.1 Simulation

The dynamic system is numerically solved using:

* `scipy.integrate.odeint`

Given a parameter set ((c, K_{eq})), a simulated trajectory is generated.

---

### 5.2 Optimization

We estimate parameters by minimizing the mean squared error (MSE):

$$
\min_{c, K_{eq}} ; \text{MSE}(\theta_{\text{real}}, \theta_{\text{sim}})
$$

* Optimization method: `scipy.optimize.minimize`
* Output: optimal (c^*, K_{eq}^*)

---

## 6. Parameter–Performance Mapping

To extend beyond identification, we investigate how structural parameters influence system behavior:

* Vary lever arm length (r)
* Identify corresponding (K_{eq})
* Analyze system response characteristics:

  * settling time
  * damping ratio
  * oscillation frequency

Theoretical relation:

$$
K_{eq} = k_s r^2
$$

Experimental validation confirms this relationship.

---

## 7. Digital Twin Validation

A virtual model is built in Unity:

* CAD model imported
* Hinge joint configured
* Identified parameters applied:

  * stiffness → spring
  * damping → damper

The simulated motion closely matches real-world behavior, forming a **basic digital twin loop**:

> Physical System → Data → Model → Simulation → Validation

---

## 8. Results

* Accurate estimation of damping and stiffness parameters
* Strong agreement between simulation and experiment
* Linear relationship observed between (r^2) and (K_{eq})
* Demonstration of physics-consistent data-driven modeling

---

## 9. Project Structure

```
.
├── data/                # raw and processed CSV data
├── hardware/            # sensor code (Arduino / ESP32 / Pi)
├── simulation/          # ODE simulation scripts
├── optimization/        # parameter identification
├── visualization/       # plotting and analysis
├── unity/               # digital twin setup
└── README.md
```

---

## 10. Future Work

This project can be extended toward:

* Multi-constraint optimization (stability vs speed vs energy)
* Real-time parameter updating (online system identification)
* Integration with control algorithms
* Extension to multi-DOF systems (robotic joints)

---

## 11. Key Takeaways

* Combines **physics modeling + data-driven identification**
* Demonstrates **closed-loop validation**
* Provides a foundation for **design space exploration and optimization**

---

## 12. Keywords

Digital Twin, System Identification, Variable Stiffness, Optimization, Dynamic Systems, Robotics

---
