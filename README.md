# The Leaning Tower of Lire: Physical Manifestation of the Harmonic Series

This project investigates the mechanical stability of a stack of identical blocks, known as the **Book Stacking Problem**. It explores how the physical requirements of static equilibrium force the geometry of the stack to adopt a harmonic distribution, theoretically allowing for an infinite horizontal overhang.

## Theoretical Basis
[cite_start]The stability of the system relies on the **Center of Mass (COM)** of the stack remaining vertically above the edge of the support base[cite: 1256]. [cite_start]Through inductive derivation using torque balance ($\sum\tau=0$), the maximum overhang $d_n$ for the $n$-th plank is found to be[cite: 1294, 1295]:

$$d_{n} = \frac{L}{2n}$$

[cite_start]The total horizontal distance $D_N$ spanned by $N$ planks is therefore governed by the **Harmonic Series**[cite: 1298]:

$$D_{N} = \sum_{n=1}^{N} \frac{L}{2n} = \frac{L}{2} \sum_{n=1}^{N} \frac{1}{n}$$

[cite_start]Because the harmonic series diverges, a stack can theoretically extend to an infinite horizontal distance[cite: 1244, 1299].

## Computational Methodology
[cite_start]The project features a **"blind" physics simulation** written in Python[cite: 1384]. [cite_start]Rather than using the $1/n$ formula directly, the algorithm iteratively calculates the COM of the existing stack and places the next support block to maintain equilibrium[cite: 1310, 1397, 1399].


### Validation Results
[cite_start]The simulation was stress-tested across multiple scales to verify that the physically emergent behavior tracks with theoretical predictions[cite: 1407]:

| Test Case ($N$) | Simulated Overhang | Theory ($L/2n$) | Absolute Error |
| :--- | :--- | :--- | :--- |
| 1 | 0.5000000000 | 0.5000000000 | [cite_start]0.00 [cite: 1431] |
| 100 | 0.0050000000 | 0.0050000000 | [cite_start]$8.67 \times 10^{-19}$ [cite: 1431] |
| 1000 | 0.0005000000 | 0.0005000000 | [cite_start]$2.23 \times 10^{-18}$ [cite: 1431] |

## Repository Structure
* [cite_start]`stack_simulation.py`: The iterative physics engine and error analysis script[cite: 1381].
* [cite_start]`Leaning_Tower_of_Lire_Report.pdf`: Technical report detailing the Oresme proof of divergence and inductive physical derivation[cite: 1188, 1199].

## Dependencies
* Python 3.x
* NumPy

---
[cite_start]**Author:** Sashvat Srivastava [cite: 1192]  
[cite_start]**Course:** MAT1002: Calculus II, Shiv Nadar Institute of Eminence [cite: 1194]  
[cite_start]**Instructor:** Prof. Amber Habib [cite: 1196]