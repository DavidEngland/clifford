# Useful Feynman Diagrams in Mathematical Physics

## 1. Introduction to Feynman Diagrams

Feynman diagrams, introduced by Richard Feynman in the late 1940s, provide a powerful graphical representation of mathematical expressions describing the behavior of subatomic particles. While originally developed for quantum electrodynamics (QED), they have found applications across theoretical physics and mathematics.

### Key Features:
- Visual representations of complex mathematical integrals
- Encode information about particle interactions and propagation
- Provide a systematic way to organize perturbation theory
- Simplify the calculation of scattering amplitudes and cross-sections

## 2. Basic Elements of Feynman Diagrams

### 2.1 Fundamental Components
- **External lines**: Represent incoming/outgoing particles
- **Internal lines**: Represent virtual particles/propagators
- **Vertices**: Represent interactions between particles
- **Loops**: Represent quantum corrections

### 2.2 Reading Conventions
- Time typically flows from left to right (or bottom to top)
- Arrows indicate charge flow or particle/antiparticle distinction
- Different line styles represent different particles:
  - Straight lines: Fermions (electrons, quarks)
  - Wavy lines: Gauge bosons (photons, gluons)
  - Dashed lines: Scalar particles (Higgs)

## 3. Mathematical Correspondence

Feynman diagrams aren't just pictorial aids—they correspond precisely to mathematical expressions:

| Diagram Element | Mathematical Expression |
|-----------------|-------------------------|
| External fermion line | Dirac spinor u(p) or v(p) |
| Internal fermion line | Fermion propagator: i(p̸+m)/(p²-m²+iε) |
| Photon line | Photon propagator: -ig^μν/(p²+iε) |
| Vertex | Coupling constant × gamma matrices |
| Loop | Integration over internal momentum: ∫d⁴p/(2π)⁴ |

## 4. Applications in Mathematical Physics

### 4.1 Quantum Field Theory
- Computing scattering amplitudes
- Calculating cross-sections
- Renormalization procedures
- Effective field theories

### 4.2 Statistical Physics
- Feynman diagrams in path integrals
- Wick's theorem and Green's functions
- Diagrammatic expansion of partition functions
- Phase transitions and critical phenomena

### 4.3 Condensed Matter Physics
- Many-body perturbation theory
- Feynman diagrams for phonons and electron-phonon interactions
- Superconductivity
- Topological phases

## 5. Feynman Diagrams and Geometric Algebra

The connection between Feynman diagrams and Clifford/geometric algebra offers interesting mathematical insights:

### 5.1 Spinors and Clifford Algebra
- Dirac spinors in Feynman diagrams naturally connect to the Clifford algebra Cl(1,3)
- The gamma matrices γᵅ form a representation of the Clifford algebra
- Propagators can be expressed using geometric product notation

### 5.2 Spacetime Algebra Formulation
- Feynman diagrams can be reformulated using spacetime algebra (Cl₁,₃)
- The Dirac equation becomes (∇+m)ψ=0 in geometric algebra
- Interaction terms gain geometric interpretation

### 5.3 Benefits of Geometric Approach
- Coordinate-free formulation
- Clear geometric interpretation of quantum interactions
- Unification of different mathematical objects (scalars, vectors, spinors)
- Simplification of certain calculations

## 6. Essential Feynman Diagrams to Understand

### 6.1 QED Fundamentals
![QED Vertex](placeholder-for-qed-vertex.png)
- The basic QED vertex: electron + photon → electron
- Mathematically represents the term -ieγᵅ in the Lagrangian

![Electron Propagator](placeholder-for-electron-propagator.png)
- The electron propagator
- Represents S_F(x-y) = ⟨0|T{ψ(x)ψ̄(y)}|0⟩

### 6.2 Higher-Order Processes
![Compton Scattering](placeholder-for-compton.png)
- Compton scattering: photon + electron → photon + electron
- Contains two vertices and demonstrates how to combine propagators

![Electron Self-Energy](placeholder-for-self-energy.png)
- Electron self-energy diagram (one-loop correction)
- Demonstrates renormalization necessity

### 6.3 Advanced Examples
![Vacuum Polarization](placeholder-for-vacuum-polarization.png)
- Vacuum polarization
- Shows how quantum fields modify empty space

![Box Diagram](placeholder-for-box-diagram.png)
- Box diagram for electron-electron scattering
- Demonstrates higher-order corrections

## 7. Computational Techniques

### 7.1 Feynman Rules
- Step-by-step procedures for translating diagrams to mathematical expressions
- Rules specific to different theories (QED, QCD, electroweak)
- Symmetry factors and sign conventions

### 7.2 Modern Computational Methods
- Symbolic manipulation with software (FeynCalc, LoopTools)
- Numerical evaluation techniques
- Monte Carlo methods for phase space integration

### 7.3 Geometric Algebra Computation
- Implementing Feynman rules with geometric algebra
- Computational advantages of geometric approach
- Software tools: GAViewer, Gaalop, or custom Python libraries

## 8. Pedagogical Examples

### 8.1 Worked Example: e⁺e⁻ → μ⁺μ⁻
Step-by-step calculation of electron-positron annihilation into muon pairs:
1. Draw the diagram (single photon exchange)
2. Apply Feynman rules to each element
3. Combine mathematical expressions
4. Square amplitude and calculate cross-section
5. Compare with experimental data

### 8.2 Geometric Algebra Approach
The same calculation using geometric algebra:
1. Express spinors in terms of spacetime algebra
2. Formulate propagators using geometric product
3. Calculate the geometric product expressions
4. Compare with traditional approach

## 9. Advanced Topics

### 9.1 Non-Perturbative Effects
- Limitations of Feynman diagrammatic expansion
- Instantons and topological effects
- Resummation techniques

### 9.2 Feynman Diagrams in String Theory
- World-sheet diagrams
- Relation to Riemann surfaces
- Connection to moduli spaces

### 9.3 Twistor Methods and Feynman Diagrams
- Modern amplitudes techniques
- Grassmannian formulations
- Connection to geometric algebra

## 10. Further Resources

### 10.1 Classical Textbooks
- Feynman, R.P. "QED: The Strange Theory of Light and Matter"
- Peskin, M.E. & Schroeder, D.V. "An Introduction to Quantum Field Theory"
- Zee, A. "Quantum Field Theory in a Nutshell"

### 10.2 Geometric Algebra Resources
- Doran, C. & Lasenby, A. "Geometric Algebra for Physicists"
- Hestenes, D. "Space-Time Algebra"
- Lasenby, J., Lasenby, A.N. & Doran, C.J.L. "A unified mathematical language for physics and engineering in the 21st century"

### 10.3 Software Tools
- FeynCalc: https://feyncalc.github.io/
- JaxoDraw: http://jaxodraw.sourceforge.net/
- GAViewer: http://www.geometricalgebra.net/gaviewer_download.html
