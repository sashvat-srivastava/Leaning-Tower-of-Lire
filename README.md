# The Leaning Tower of Lire: Physical Manifestation of the Harmonic Series

This project investigates the mechanical stability of a stack of identical uniform blocks, a problem also known as the Book Stacking Problem. It explores how the physical requirements of static equilibrium force the geometry of the stack to adopt a harmonic distribution, theoretically allowing for an infinite horizontal overhang.

## Theoretical Basis
The stability of the system relies on the Center of Mass (COM) of the stack remaining vertically above the edge of the support base. Through inductive derivation using torque balance ($\sum\tau=0$), the maximum overhang $d_n$ for the $n$-th plank is found to be:

$$d_{n} = \frac{L}{2n}$$

The total horizontal distance $D_N$ spanned by $N$ planks is governed by the Harmonic Series:

$$D_{N} = \sum_{n=1}^{N} \frac{L}{2n} = \frac{L}{2} \sum_{n=1}^{N} \frac{1}{n}$$

Because the harmonic series diverges, a stack can theoretically extend to an infinite horizontal distance.



## Computational Methodology
The project features a "blind" physics simulation written in Python. Rather than using the $1/n$ formula directly, the algorithm iteratively calculates the COM of the existing stack and places the next support block to maintain equilibrium.

### Validation Results
The simulation was tested across multiple scales to verify that the physically emergent behavior tracks with theoretical predictions.

| Test Case ($N$) | Simulated Overhang | Theory ($L/2n$) | Absolute Error |
| :--- | :--- | :--- | :--- |
| 1 | 0.5000000000 | 0.5000000000 | 0.00 |
| 100 | 0.0050000000 | 0.0050000000 | $8.67 \times 10^{-19}$ |
| 1000 | 0.0005000000 | 0.0005000000 | $2.23 \times 10^{-18}$ |

## Repository Structure
* `stack_simulation.py`: The iterative physics engine and error analysis script.
* `Leaning_Tower_of_Lire_Report.pdf`: Technical report detailing the Oresme proof of divergence and inductive physical derivation.

## Dependencies
* Python 3.x
* NumPy

---
**Author:** Sashvat Srivastava  
**Course:** MAT1002: Calculus II, Shiv Nadar Institute of Eminence  
**Instructor:** Prof. Amber Habib
