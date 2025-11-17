# Stabilizer Tableau — CNOT sign-bit update (homework / worked example)

Problem statement (homework form).
In the stabilizer tableau formalism each stabilizer row is represented by binary indicator vectors for the \(X\) and \(Z\) parts and a sign bit \(\sigma\in\{0,1\}\) encoding overall sign (0 ↦ \(+1\), 1 ↦ \(-1\)). Consider applying a CNOT gate with control (source) qubit \(m\) and target (sink) qubit \(n\). For a given stabilizer row let
\[
\alpha_m,\beta_m,\alpha_n,\beta_n\in\{0,1\}
\]
be the row bits for \(X_m,Z_m,X_n,Z_n\) respectively, and let \(\sigma_{\text{in}}\) be the initial sign bit. Give the updated sign bit \(\sigma_{\text{out}}\) (binary, modulo 2) after conjugation by the CNOT. Show your steps (or use the hint below).

Hint (how to proceed).

- Use the single-qubit CNOT conjugation rules on Pauli generators:
  \[
  \mathrm{CNOT}:\quad X_m\mapsto X_m X_n,\quad X_n\mapsto X_n,\quad Z_m\mapsto Z_m,\quad Z_n\mapsto Z_m Z_n.
  \]
- Apply these images to the factors on qubits \(m,n\) in the row, then collect factors per qubit.
- Reorder factors into the chosen canonical form (e.g. \(X^\alpha Z^\beta\) per qubit). Each time you swap a non-commuting \(X\) and \(Z\) on the same qubit you introduce a sign \(-1\).
- Count parity of all such swaps (and any implicit \(i\)-factors if your convention tracks them) to obtain the change in the sign bit.

Worked solution (concise).

1. Start with the factors on qubits \(m\) and \(n\) for the row:
   \[
   \cdots (X_m)^{\alpha_m}(Z_m)^{\beta_m}\,(X_n)^{\alpha_n}(Z_n)^{\beta_n}\cdots .
   \]
2. Conjugate each factor using the CNOT rules:
   \[
   (X_m)^{\alpha_m}\mapsto (X_m X_n)^{\alpha_m},\qquad
   (Z_n)^{\beta_n}\mapsto (Z_m Z_n)^{\beta_n},
   \]
   while \((Z_m)^{\beta_m},(X_n)^{\alpha_n}\) are unchanged.
3. Multiply the images and group per qubit (exponents in \(\mathbb{F}_2\)):
   \[
   \begin{aligned}
   \text{qubit }m &: \; X_m^{\alpha_m}\,Z_m^{\beta_m+\beta_n},\\
   \text{qubit }n &: \; X_n^{\alpha_m+\alpha_n}\,Z_n^{\beta_n}.
   \end{aligned}
   \]
   (other qubits unaffected)
4. To put each qubit's factor in canonical order \(X^\alpha Z^\beta\) we may have to commute \(X\) and \(Z\) on the same qubit. For a single qubit the basic commutation is \(XZ = -ZX\), so every time an \(X\) and \(Z\) are swapped on the same qubit a factor \(-1\) is produced.
5. The parity (mod 2) of the total sign change produced during the reordering is obtained by counting the occurrences where both an \(X\) and a \(Z\) were present on the same qubit and needed to be swapped relative to the chosen canonical ordering as the images were multiplied. Working this out (see references below for the compact tableau algebra) yields the following binary update rule.

Final answer (binary formula).
Using addition and multiplication modulo 2, the updated sign bit is
\[
\boxed{\ \sigma_{\text{out}} \;=\; \sigma_{\text{in}} \;\oplus\; \big(\alpha_{m}\,\beta_{n}\,(\alpha_{n}\oplus\beta_{m}\oplus 1)\big)\ }.
\]

Remarks and sanity checks.

- The formula is modulo 2: \(\oplus\) denotes XOR (addition mod 2), and products are logical AND (multiplication mod 2).
- If \(\alpha_m=\beta_n=1\) and \(\alpha_n=\beta_m=0\) (i.e.\ the row contains \(X_m\) and \(Z_n\) but not the other factors) the factor in parentheses equals 1 and the sign flips: \(\sigma_{\text{out}}=\sigma_{\text{in}}\oplus 1\), consistent with direct matrix checks.
- If either \(\alpha_m=0\) or \(\beta_n=0\), no sign flip occurs.

Extensions for homework / exam:

1. Derive the complete update (bitwise) rules for the entire row (all \(\alpha,\beta\) entries) under CNOT: the familiar tableau update:
   \[
   \begin{aligned}
   \alpha_m' &= \alpha_m,\\
   \alpha_n' &= \alpha_n\oplus\alpha_m,\\
   \beta_m' &= \beta_m\oplus\beta_n,\\
   \beta_n' &= \beta_n.
   \end{aligned}
   \]
   and the sign update as above.
2. Repeat the derivation for Hadamard and Phase (S) gates and compare with Aaronson–Gottesman tableau rules.
3. Implement the update in a short Python routine that maintains a stabilizer tableau and test on small examples.

References.

- S. Aaronson and D. Gottesman, "Improved simulation of stabilizer circuits", Phys. Rev. A 70, 052328 (2004). See their Appendix for the tableau update rules and sign-bit formulas.
- Nielsen & Chuang, textbook discussion of conjugation of Pauli operators by Clifford gates.

Answer key (concise).

- Updated sign-bit (mod 2): \(\displaystyle \sigma_{\text{out}}=\sigma_{\text{in}}\oplus \big(\alpha_m\beta_n(\alpha_n\oplus\beta_m\oplus 1)\big)\).
