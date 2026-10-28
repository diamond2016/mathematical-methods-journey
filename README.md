# Mathematical Methods: A Journey

This is a mathematical journey about complex numbers from the view of an CS professional.

I'll use this repo to better use python linters, notebooks, lintes and so on.

Take a look at guidelines.

## Repository Structure

```text
mathematical-methods-journey/
├── .venv/                  <-- virtual env centralized
├── requirements.txt 
|  
├── week01-complex-numbers/
├── week02-euler/
├── week03-mappings/
├── week04-analytic-functions/
├── week05-contours/
├── week06-cauchy/
├── week07-laurent/
├── week08-residues/
├── week09-fourier-series/
├── week10-frequency-domain/
├── week11-fourier-transform/
├── week12-fft/
├── week13-laplace/
├── week14-poles-zeros/
├── week15-transfer-functions/
└── week16-final-project/
└── integrals/
```

## Main Source
[Calculus Revisited: Complex Variables (MIT OCW)](https://ocw.mit.edu/courses/res-18-008-calculus-revisited-complex-variables-differential-equations-and-linear-algebra-fall-2011/video_galleries/part-i/)

---

## Phase 1: Complex Numbers & Mappings (Weeks 1–4)

### Week 1: Review
*   **Topics:** Complex numbers, Cartesian form, Polar form, Modulus, and Phase.
*   **Python Exercise:** 
    *   Represent complex numbers in the complex plane.
    *   Implement addition and multiplication as geometric operations.
*   **Deliverable:** A Jupyter Notebook featuring geometric plots.

### Week 2: Euler's Formula
*   **Topics:** Complex exponential, Euler's formula, $n$-th roots.
*   **Goal:** Deeply understand why $e^{i\theta}$ generates the unit circle.
*   **Deliverable:** An animation or notebook demonstrating rotation in the complex plane.

### Week 3: Complex Functions & Mappings
*   **Topics:** Functions of a complex variable, geometric mapping.
*   **Task:** Visualize the geometric transformations of:
    *   $z^2$
    *   $1/z$
    *   $e^z$

### Week 4: Series & Analyticity
*   **Topics:** Series, convergence, and analyticity.
*   **Deliverable:** A personal assessment/test.

---

## Phase 2: Complex Analysis (Weeks 5–8)
**Material:** *Complex Variables with Applications*

### Week 5: Complex Integration
*   **Topics:** Complex integration and paths.
*   **Goal:** Understand the fundamental differences between complex and real integration.

### Week 6: Cauchy's Theorem
*   **Topics:** Cauchy's Theorem.
*   **Approach:** Focus on the intuition ("why it feels like magic") rather than a purely rigorous proof.

### Week 7: Taylor & Laurent Series
*   **Topics:** Taylor series and Laurent series.
*   **Deliverable:** A Python script that approximates various functions using series.

### Week 8: Residues
*   **Topics:** Residue theory.
*   **Goal:** Understand how to solve seemingly impossible real integrals using residues.

---

## Phase 3: Fourier Analysis (Weeks 9–12)
**Material:** MIT Differential Equations (Fourier Section)

### Week 9: Fourier Series
*   **Topics:** Constructing periodic signals.
*   **Task:** Build square waves and triangle waves using sums of sine waves.

### Week 10: Frequency Domain
*   **Topics:** Frequency domain interpretation.
*   **Tools:** `numpy`, `matplotlib`.
*   **Goal:** Visualize the relationship between a signal and its spectrum.

### Week 11: Fourier Transform
*   **Topics:** The Fourier Transform.
*   **Goal:** Understand why it exists and what it physically represents.

### Week 12: Fast Fourier Transform (FFT)
*   **Topics:** Practical implementation of FFT.
*   **Deliverable:** An analysis of a `.wav` audio file.

---

## Phase 4: Laplace & Systems (Weeks 13–16)
**Material:** MIT Signals and Systems & Laplace section of Differential Equations.

### Week 13: Laplace Transform
*   **Topics:** The Laplace Transform and its connection to the Fourier Transform.

### Week 14: Poles and Zeros
*   **Topics:** Poles and zeros in the complex plane (a fundamental concept).

### Week 15: Transfer Functions
*   **Topics:** Transfer functions, control systems, and stability.
*   **Goal:** Understand stability and control intuitively.

### Week 16: Final Project
*   **Option A:** Implement a Python pipeline for signal generation, FFT, filtering, and inverse transform.
*   **Option B:** Simulate a dynamic system using Laplace transforms.

---

## Bonus: Computational Science (Month 5)
**Material:** *Computational Science and Engineering I* (Gilbert Strang)

*   **Topics:** 
    *   Newton-Raphson method
    *   Interpolation
    *   Numerical integration
    *   FFT (Numerical approach)
    *   Finite differences
    *   Numerical Linear Algebra

### Bonus Integrals: Recap about integrals (During the course)
---

## Project Guidelines & Philosophy

### Folder Structure
Every week's folder must contain:
*   `README.md`: Overview of the week.
*   `notes.md`: Theoretical notes and derivations.
*   `exercise.ipynb`: Executable Python notebook.

### The Iron Rule
**No week is considered complete until an executable notebook exists.**

### Learning Philosophy
This repository follows an **incremental project-based approach**. Instead of "passive video consumption," the goal is to transform study into an active engineering project. This method is highly effective for experienced developers as it bridges the gap between abstract theory and practical implementation.

### Key Focus Areas
*   Intuitive explanations of theorems.
*   Guided exercises.
*   Complete Python notebooks.
*   Visualizations of Fourier and Laplace transforms.
*   Connections to dynamic systems, control theory, AI, DSP, and numerical simulation.
