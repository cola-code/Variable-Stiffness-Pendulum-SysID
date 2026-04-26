# Variable-Stiffness-Pendulum-SysID  
**A Physics-Guided System Identification and Design Exploration Project**

---

## Abstract

This project explores a simple pipeline for understanding how structural parameters affect system dynamics.

Using a controllable variable-stiffness pendulum, the goal is to:

- collect real-world dynamic data  
- estimate system parameters  
- study the relationship between design and performance  

The project is currently in progress and focuses on system construction and data acquisition.

---

## 1. Background & Motivation

In many mechanical systems, performance is not only determined by control algorithms, but also by physical structure.

A key question is:

> How do structural parameters influence dynamic behavior?

This project combines:

- basic physics modeling  
- experimental data  
- simple optimization ideas  

---

## 2. System Description

The system is a pendulum with adjustable stiffness.

- A spring is attached to the pendulum arm  
- The attachment position $r$ can be changed  
- This changes the equivalent stiffness $K_{eq}$  

So the system can be described as:

$$
r \rightarrow K_{eq} \rightarrow \text{dynamic response}
$$

---

## 3. Modeling Idea

The pendulum is modeled as a second-order dynamic system:

$$
J \ddot{\theta} + c \dot{\theta} + K_{eq} \theta = 0
$$

where:

- $J$: moment of inertia (estimated from CAD)  
- $c$: damping coefficient (unknown)  
- $K_{eq}$: equivalent stiffness (unknown)  

The goal is to:

1. measure motion data  
2. estimate unknown parameters  
3. compare model response with real data  

---

## 4. Method Overview

The overall workflow is:

### (1) Physical System Construction
- CAD modeling (SolidWorks)  
- inertia estimation  
- adjustable stiffness mechanism  

### (2) Data Acquisition (in progress)
- microcontroller-based sampling  
- timestamped angle data  
- target frequency: $100\ \text{Hz}$  

### (3) System Identification (planned)
- simulate system dynamics  
- fit parameters using optimization  
- minimize error between real data and simulation  

### (4) Design Exploration (planned)

We aim to analyze:

$$
r \rightarrow K_{eq} \rightarrow T_s
$$

where $T_s$ is the settling time.

---

## 5. Current Progress

- [x] CAD model and mechanical design  
- [x] inertia estimation from SolidWorks  
- [x] system architecture design  
- [ ] data acquisition implementation (in progress)  
- [ ] experimental data collection  
- [ ] parameter identification  
- [ ] performance analysis  

---

## 6. Project Goal

This project is not only about building a pendulum, but about learning how to:

- connect physics, data, and modeling  
- move from observation $\rightarrow$ model $\rightarrow$ design insight  

---

## 7. Tech Stack

- SolidWorks (CAD & inertia estimation)  
- Arduino / ESP32 (data acquisition)  
- Python (NumPy, SciPy, Matplotlib)  
- MATLAB / Simscape (planned validation)  

---

## 8. Repository Structure
- data # experimental data (planned)
- src # modeling and identification code
- hardware # CAD files and setup
- docs # figures and notes


---

## 9. Status

🚧 Early-stage (system setup & data acquisition in progress)

---

## 10. Author

Zhang Chenming  
Xi'an Jiaotong University  

---

## Notes

This is an ongoing learning-oriented project.  
The focus is on building a clear and reproducible workflow rather than achieving perfect results.