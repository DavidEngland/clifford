# Variational Formulation for a Two-Velocity Medium with Entropy Transport

## Problem Statement

Consider a continuous medium consisting of two interpenetrating constituents, each characterized by its own velocity field. This system is used to model phenomena such as:
- Multi-phase flows
- Superfluid helium
- Plasma dynamics
- Suspensions and mixtures

The medium occupies a region Ω ⊂ ℝ³, and its dynamics is to be determined from a variational principle without introducing Lagrange multipliers for constraints.

### Key Characteristics:
1. Two distinct constituents (labeled 1 and 2) with separate velocity fields v₁ and v₂
2. Each constituent carries its own mass and entropy
3. No creation or destruction of mass or entropy (conservation)
4. Constituents interact through momentum exchange and other coupling mechanisms
5. The formulation should yield a self-consistent set of partial differential equations governing the evolution of the system

The goal is to derive the equations of motion from a single quadratic Lagrangian using Hamilton's principle of least action, while preserving the essential conservation laws and constituent interactions.

## Lagrangian Framework

In the Lagrangian (material) description, we track the motion of material particles from their reference configurations.

### Reference Configuration and Motion

Let $\mathbf{X}_i$ represent material coordinates in the reference configuration for constituent $i$ (where $i = 1, 2$). The motion of each constituent is described by two surjective mappings:

$$\mathbf{x}_1 = \boldsymbol{\varphi}_1(\mathbf{X}_1, t)$$
$$\mathbf{x}_2 = \boldsymbol{\varphi}_2(\mathbf{X}_2, t)$$

where $\mathbf{x}_i$ represents the spatial (Eulerian) position of a material particle of constituent $i$ at time $t$.

### Deformation Gradients and Jacobians

The deformation gradients for each constituent are:

$$\mathbf{F}_i = \frac{\partial \boldsymbol{\varphi}_i}{\partial \mathbf{X}_i}$$

with Jacobians $J_i = \det(\mathbf{F}_i)$ representing the local volume change.

### Material Velocities

The material velocities of each constituent are defined as:

$$\mathbf{V}_i = \frac{\partial \boldsymbol{\varphi}_i}{\partial t}$$

### Specific Entropy

Let $S_i(\mathbf{X}_i)$ represent the specific entropy (per unit mass) in the reference configuration for constituent $i$. The transport of entropy is governed by:

$$s_i(\mathbf{x}_i, t) = S_i(\mathbf{X}_i)$$

where $s_i$ is the specific entropy in the current configuration.

### Lagrangian Density

A quadratic Lagrangian density $\mathcal{L}$ in the reference configuration has the form:

$$\mathcal{L} = \mathcal{T} - \mathcal{U}$$

where $\mathcal{T}$ represents the kinetic energy density and $\mathcal{U}$ the internal energy density, which may depend on:

- Deformation gradients $\mathbf{F}_i$
- Specific entropies $S_i$
- Relative motion between constituents
- Coupling terms between constituents

### Action Integral

The action integral in the Lagrangian framework is:

$$\mathcal{A} = \int_{t_1}^{t_2} \int_{\Omega_0} \mathcal{L}(\mathbf{F}_1, \mathbf{F}_2, \mathbf{V}_1, \mathbf{V}_2, S_1, S_2) \, dV_0 \, dt$$

where $\Omega_0$ is the reference domain.

## Eulerian Framework

In the Eulerian (spatial) description, we focus on fields at fixed spatial points rather than following material particles.

### Eulerian Variables

The primary Eulerian variables are:
- Mass densities $\rho_i(\mathbf{x}, t)$
- Velocity fields $\mathbf{v}_i(\mathbf{x}, t)$
- Specific entropy fields $s_i(\mathbf{x}, t)$

These relate to their Lagrangian counterparts through:

$$\rho_i(\boldsymbol{\varphi}_i(\mathbf{X}_i, t), t) \, J_i = \rho_{0i}(\mathbf{X}_i)$$
$$\mathbf{v}_i(\boldsymbol{\varphi}_i(\mathbf{X}_i, t), t) = \mathbf{V}_i(\mathbf{X}_i, t)$$

where $\rho_{0i}$ is the reference mass density.

### Conservation Laws in Eulerian Form

The conservation of mass for each constituent takes the form:

$$\frac{\partial \rho_i}{\partial t} + \nabla \cdot (\rho_i \mathbf{v}_i) = 0$$

The transport of entropy is governed by:

$$\frac{\partial (\rho_i s_i)}{\partial t} + \nabla \cdot (\rho_i s_i \mathbf{v}_i) = 0$$

### Eulerian Lagrangian Density

The Eulerian Lagrangian density $\mathcal{L}_E$ is expressed in terms of Eulerian variables:

$$\mathcal{L}_E = \sum_{i=1}^{2} \frac{1}{2} \rho_i |\mathbf{v}_i|^2 - e(\rho_1, \rho_2, s_1, s_2, \mathbf{v}_1 - \mathbf{v}_2)$$

where $e$ is the internal energy density that may depend on densities, entropies, and the relative velocity.

### Eulerian Action Integral

The action integral in the Eulerian framework is:

$$\mathcal{A}_E = \int_{t_1}^{t_2} \int_{\Omega_t} \mathcal{L}_E(\rho_1, \rho_2, \mathbf{v}_1, \mathbf{v}_2, s_1, s_2) \, dV \, dt$$

where $\Omega_t$ is the current spatial domain.

## Variations and Resulting Equations

To derive the equations of motion, variations are taken with respect to the mappings $\boldsymbol{\varphi}_i$ in the Lagrangian framework, or with respect to appropriate potentials in the Eulerian framework. The resulting Euler-Lagrange equations provide the complete set of governing equations for the two-velocity medium with entropy transport.

---

The challenge lies in:
1. Properly accounting for the coupling between constituents
2. Ensuring all conservation laws are satisfied without explicit constraints
3. Choosing appropriate variations that respect the physical structure of the problem
4. Deriving a self-consistent set of equations that properly describe the dynamics of the two-velocity medium