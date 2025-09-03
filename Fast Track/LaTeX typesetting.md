# LaTeX Guide for Students

## Table of Contents
1. [Getting Started with LaTeX](#getting-started-with-latex)
2. [Basic Document Structure](#basic-document-structure)
3. [Mathematical Typesetting](#mathematical-typesetting)
4. [Figures and Tables](#figures-and-tables)
5. [References and Citations](#references-and-citations)
6. [Advanced Mathematics](#advanced-mathematics)
7. [Document Classes and Templates](#document-classes-and-templates)
8. [Advanced LaTeX Techniques](#advanced-latex-techniques)
9. [Useful Templates](#useful-templates)

---

## Getting Started with LaTeX

### What is LaTeX?
LaTeX is a document preparation system especially suited for scientific and mathematical content. Unlike word processors, LaTeX uses plain text with markup commands that specify document structure and formatting.

### Setting Up LaTeX

#### Online Options (Easiest to Start)
- **Overleaf** (https://www.overleaf.com): Online LaTeX editor with built-in collaboration features
- **CoCalc** (https://cocalc.com): Collaborative calculation and LaTeX environment

#### Desktop Installation
- **Windows**: Install MiKTeX or TeX Live + TeXstudio
- **macOS**: Install MacTeX + TeXShop
- **Linux**: Install TeX Live + TeXmaker

### Your First LaTeX Document

```latex
\documentclass{article}

\title{My First LaTeX Document}
\author{Your Name}
\date{\today}

\begin{document}

\maketitle

\section{Introduction}
Hello, world! This is my first \LaTeX{} document.

\section{Mathematics}
LaTeX is great for equations: $E = mc^2$

\end{document}
```

**Key Commands:**
- `\documentclass{article}`: Sets the type of document
- `\begin{document}` and `\end{document}`: Contains all visible content
- `\section{Title}`: Creates a numbered section
- `$...$`: For inline math

---

## Basic Document Structure

### Document Classes
```latex
\documentclass[12pt, letterpaper]{article} % For articles
\documentclass{report} % For longer reports with chapters
\documentclass{book} % For books
\documentclass{beamer} % For presentations
```

### Packages
```latex
\usepackage{amsmath} % Advanced math
\usepackage{graphicx} % For images
\usepackage{hyperref} % For hyperlinks
\usepackage{geometry} % For page margins
```

### Document Structure
```latex
\documentclass{article}
\usepackage{amsmath}

\title{Sample Document}
\author{Student Name}
\date{\today}

\begin{document}

\maketitle
\tableofcontents

\section{First Section}
Text goes here...

\subsection{A Subsection}
More text...

\section{Second Section}
Even more text...

\end{document}
```

### Basic Formatting
```latex
\textbf{Bold text}
\textit{Italic text}
\underline{Underlined text}
\texttt{Monospaced text}

% Lists
\begin{itemize}
    \item Item 1
    \item Item 2
\end{itemize}

\begin{enumerate}
    \item First item
    \item Second item
\end{enumerate}
```

---

## Mathematical Typesetting

### Inline vs. Display Math
```latex
% Inline math
This formula $E = mc^2$ appears within text.

% Display math
$$E = mc^2$$

% Numbered equation
\begin{equation}
    E = mc^2
    \label{eq:einstein}
\end{equation}

% Multi-line equations
\begin{align}
    a &= b + c \\
    &= d + e
\end{align}
```

### Mathematical Symbols

#### Basic Operators
```latex
$a + b - c \times d \div e = f$
$a \cdot b$ % Dot product
$a \times b$ % Cross product
$\frac{a}{b}$ % Fraction
$\sqrt{x}$ % Square root
$\sqrt[n]{x}$ % nth root
```

#### Greek Letters
```latex
$\alpha, \beta, \gamma, \delta, \epsilon, \varepsilon$
$\zeta, \eta, \theta, \vartheta, \iota, \kappa$
$\lambda, \mu, \nu, \xi, o, \pi, \varpi$
$\rho, \varrho, \sigma, \varsigma, \tau$
$\upsilon, \phi, \varphi, \chi, \psi, \omega$

% Uppercase Greek letters
$\Gamma, \Delta, \Theta, \Lambda, \Xi, \Pi, \Sigma, \Upsilon, \Phi, \Psi, \Omega$
```

#### Subscripts and Superscripts
```latex
$x^2$ % Superscript
$x_i$ % Subscript
$x_i^j$ % Both
$x^{y^z}$ % Nested superscripts
```

#### Matrices
```latex
\begin{matrix}
    a & b \\
    c & d
\end{matrix}

\begin{pmatrix}
    a & b \\
    c & d
\end{pmatrix}

\begin{bmatrix}
    a & b \\
    c & d
\end{bmatrix}

\begin{vmatrix}
    a & b \\
    c & d
\end{vmatrix}
```

#### Special Functions
```latex
$\sin x, \cos x, \tan x, \log x, \ln x, \exp x, \lim_{x \to \infty} f(x)$
```

---

## Figures and Tables

### Including Figures
```latex
\usepackage{graphicx}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{image-filename.png}
    \caption{Description of the figure.}
    \label{fig:example}
\end{figure}
```

### Creating Tables
```latex
\begin{table}[htbp]
    \centering
    \begin{tabular}{|l|c|r|}
        \hline
        Left & Center & Right \\
        \hline
        Value 1 & Value 2 & Value 3 \\
        Value 4 & Value 5 & Value 6 \\
        \hline
    \end{tabular}
    \caption{Example table.}
    \label{tab:example}
\end{table}
```

---

## References and Citations

### Cross-References
```latex
See Figure~\ref{fig:example} and Equation~\ref{eq:einstein}.
```

### Bibliography with BibTeX
```latex
% In your main.tex file
\bibliographystyle{plain}
\bibliography{references}

% In references.bib file
@article{einstein1905,
    author = {Albert Einstein},
    title = {On the Electrodynamics of Moving Bodies},
    journal = {Annalen der Physik},
    year = {1905},
    volume = {17},
    pages = {891--921}
}
```

### Citations
```latex
Einstein's theory of relativity \cite{einstein1905} revolutionized physics.
```

---

## Advanced Mathematics

### Clifford Algebra Notation
```latex
\usepackage{amsmath}
\usepackage{amssymb}

% Define geometric product
\newcommand{\gp}{\cdot}

% Bivectors and multivectors
\begin{align}
    \mathbf{e}_i \wedge \mathbf{e}_j &= \mathbf{e}_i \mathbf{e}_j - \mathbf{e}_i \cdot \mathbf{e}_j \\
    \mathbf{a} \gp \mathbf{b} &= \mathbf{a} \cdot \mathbf{b} + \mathbf{a} \wedge \mathbf{b}
\end{align}
```

### Vector Calculus
```latex
\begin{align}
    \nabla \times \mathbf{F} &= 
    \begin{vmatrix} 
        \mathbf{i} & \mathbf{j} & \mathbf{k} \\
        \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
        F_x & F_y & F_z
    \end{vmatrix} \\
    \nabla \cdot \mathbf{F} &= \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}
\end{align}
```

### Commutative Diagrams
```latex
\usepackage{tikz-cd}

\begin{tikzcd}
    A \arrow[r, "f"] \arrow[d, "g"'] & B \arrow[d, "h"] \\
    C \arrow[r, "j"'] & D
\end{tikzcd}
```

### Tensor Notation
```latex
% Einstein summation convention
$T^{ij}_k = \sum_{l=1}^n A^i_l B^{jl}_k$

% With implicit summation
$T^{ij}_k = A^i_l B^{jl}_k$
```

---

## Document Classes and Templates

### Article Template
```latex
\documentclass[12pt]{article}
\usepackage{amsmath, amssymb, graphicx}
\usepackage[margin=1in]{geometry}

\title{Article Title}
\author{Author Name}
\date{\today}

\begin{document}
\maketitle
\abstract{
    This is the abstract of the article.
}

\section{Introduction}
% Content here...

\section{Methods}
% Content here...

\section{Results}
% Content here...

\section{Discussion}
% Content here...

\section{Conclusion}
% Content here...

\bibliographystyle{plain}
\bibliography{references}
\end{document}
```

### Lab Report Template
```latex
\documentclass[12pt]{article}
\usepackage{amsmath, amssymb, graphicx, siunitx}
\usepackage[margin=1in]{geometry}

\title{Lab Report: Experiment Title}
\author{Student Name}
\date{\today}

\begin{document}
\maketitle

\section{Objective}
% State the purpose of the experiment

\section{Theoretical Background}
% Explain relevant theories and equations

\section{Experimental Setup}
% Describe equipment and procedures

\section{Results}
% Present data, calculations, and uncertainties

\section{Discussion}
% Analyze results and discuss sources of error

\section{Conclusion}
% Summarize findings

\section{References}
% List references

\end{document}
```

### Beamer Presentation
```latex
\documentclass{beamer}
\usetheme{Madrid}
\usecolortheme{beaver}

\title{Presentation Title}
\author{Presenter Name}
\date{\today}

\begin{document}

\begin{frame}
    \titlepage
\end{frame}

\begin{frame}{Outline}
    \tableofcontents
\end{frame}

\section{First Section}

\begin{frame}{First Topic}
    \begin{itemize}
        \item Point 1
        \item Point 2
        \item Point 3
    \end{itemize}
\end{frame}

\begin{frame}{Mathematical Content}
    \begin{align}
        E &= mc^2\\
        F &= ma
    \end{align}
\end{frame}

\end{document}
```

---

## Advanced LaTeX Techniques

### Custom Commands
```latex
% Simple replacement
\newcommand{\vect}[1]{\boldsymbol{#1}}

% Command with optional parameter
\newcommand{\norm}[1][\infty]{\|#1\|}

% Usage
$\vect{a} \cdot \vect{b} = |\vect{a}||\vect{b}|\cos\theta$
$\norm{f} = \sup_{x \in X} |f(x)|$
```

### Environments
```latex
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}

\begin{theorem}
    For any right triangle, the square of the length of the hypotenuse equals
    the sum of squares of the lengths of the other two sides.
\end{theorem}

\begin{proof}
    This follows from the Pythagorean identity.
\end{proof}
```

### Advanced Page Layout
```latex
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhead[L]{Course Name}
\fancyhead[R]{Student Name}
\fancyfoot[C]{\thepage}
```

### Multi-file Projects
```latex
% main.tex
\documentclass{book}
\usepackage{amsmath, graphicx}

\begin{document}

\include{chapters/chapter1}
\include{chapters/chapter2}
\include{chapters/chapter3}

\end{document}

% chapters/chapter1.tex
\chapter{Introduction}
This is the first chapter...
```

---

## Useful Templates

### Physics Problem Set Template
```latex
\documentclass[12pt]{article}
\usepackage{amsmath, amssymb, physics, siunitx}
\usepackage[margin=1in]{geometry}

\title{Physics 401: Problem Set 3}
\author{Student Name}
\date{\today}

\newcommand{\problem}[1]{\section{Problem #1}}
\newcommand{\subproblem}[1]{\subsection{(#1)}}

\begin{document}
\maketitle

\problem{1}
\textbf{Given:} A particle moves in a potential $V(x) = \frac{1}{2}kx^2$.

\subproblem{a}
Find the equation of motion.

\textbf{Solution:} 
The Lagrangian is $L = T - V = \frac{1}{2}m\dot{x}^2 - \frac{1}{2}kx^2$.

Using the Euler-Lagrange equation:
\begin{align}
\frac{d}{dt}\frac{\partial L}{\partial \dot{x}} - \frac{\partial L}{\partial x} &= 0\\
\frac{d}{dt}(m\dot{x}) - (-kx) &= 0\\
m\ddot{x} + kx &= 0
\end{align}

Therefore, $\ddot{x} = -\frac{k}{m}x$, which is the equation for simple harmonic motion.

\end{document}
```

### Clifford Algebra Research Paper Template
```latex
\documentclass[12pt]{article}
\usepackage{amsmath, amssymb, amsthm, mathtools}
\usepackage{graphicx, hyperref}
\usepackage[margin=1in]{geometry}

% Custom commands for Clifford Algebra
\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\Cl}{\mathrm{Cl}}
\newcommand{\clifford}[1]{\Cl_{#1}}
\newcommand{\gp}{\bullet}  % geometric product
\newcommand{\ip}[2]{#1 \cdot #2}  % inner product
\newcommand{\op}[2]{#1 \wedge #2}  % outer product
\newcommand{\bivector}[2]{#1 \wedge #2}
\newcommand{\rotor}[1]{\mathcal{R}_{#1}}
\newcommand{\grade}[2]{\langle #1 \rangle_{#2}}

\title{Applications of Clifford Algebra to Quantum Mechanics}
\author{Student Name}
\date{\today}

\begin{document}
\maketitle

\begin{abstract}
This paper explores the applications of Clifford algebra to quantum mechanical systems...
\end{abstract}

\section{Introduction}
Clifford algebra, also known as geometric algebra, provides a unified mathematical language for physics...

\section{Theoretical Framework}
We begin with the Clifford algebra $\clifford{3,0}$ of Euclidean 3-space...

The geometric product of vectors $\mathbf{a}$ and $\mathbf{b}$ is defined as:
\begin{align}
\mathbf{a}\gp\mathbf{b} = \ip{\mathbf{a}}{\mathbf{b}} + \op{\mathbf{a}}{\mathbf{b}}
\end{align}

\section{Applications to Quantum Mechanics}
The Pauli matrices can be represented using the basis elements of $\clifford{3,0}$...

\section{Conclusion}
Clifford algebra provides a powerful geometric interpretation of quantum phenomena...

\bibliographystyle{plain}
\bibliography{references}
\end{document}
```

### Dispersion Model Documentation Template
```latex
\documentclass[12pt]{article}
\usepackage{amsmath, amssymb, graphicx, algorithmic, algorithm}
\usepackage{siunitx, listings, hyperref, color}
\usepackage[margin=1in]{geometry}

\lstset{
  basicstyle=\small\ttfamily,
  keywordstyle=\color{blue},
  commentstyle=\color{green!60!black},
  frame=single,
  breaklines=true
}

\title{Atmospheric Dispersion Model Documentation}
\author{Student Name}
\date{\today}

\begin{document}
\maketitle

\section{Model Overview}
This document describes the implementation of a Lagrangian particle dispersion model...

\section{Mathematical Framework}
The model solves the following stochastic differential equation for particle motion:

\begin{align}
d\mathbf{X}_p &= \mathbf{U}(\mathbf{X}_p, t)dt + \mathbf{dW} \\
\mathbf{dW} &\sim \mathcal{N}(0, 2\mathbf{K}dt)
\end{align}

where $\mathbf{X}_p$ is the particle position, $\mathbf{U}$ is the mean wind field, and $\mathbf{dW}$ is a Wiener process...

\section{Implementation}
\begin{algorithm}
\caption{Particle Tracking Algorithm}
\begin{algorithmic}[1]
\STATE Initialize particle positions $\mathbf{X}_p(t=0)$
\FOR{each time step $\Delta t$}
  \STATE Update meteorological fields
  \FOR{each particle $p$}
    \STATE Interpolate wind velocity $\mathbf{U}$ at $\mathbf{X}_p$
    \STATE Generate random displacement $\mathbf{dW}$
    \STATE Update position: $\mathbf{X}_p(t+\Delta t) = \mathbf{X}_p(t) + \mathbf{U}\Delta t + \mathbf{dW}$
    \STATE Apply boundary conditions
  \ENDFOR
  \STATE Output particle positions and concentrations
\ENDFOR
\end{algorithmic}
\end{algorithm}

\section{Code Example}
\begin{lstlisting}[language=Python]
def update_particle_position(particle, wind_field, dt, stability):
    """Update particle position based on wind and diffusion"""
    # Advection (deterministic part)
    u, v = interpolate_wind(wind_field, particle.x, particle.y)
    dx_advection = u * dt
    dy_advection = v * dt
    
    # Diffusion (stochastic part)
    sigma = calculate_diffusion_parameter(stability)
    dx_diffusion = np.random.normal(0, sigma)
    dy_diffusion = np.random.normal(0, sigma)
    
    # Update position
    particle.x += dx_advection + dx_diffusion
    particle.y += dy_advection + dy_diffusion
\end{lstlisting}

\section{Validation}
The model has been validated against analytical solutions and observational data...

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{dispersion_validation.png}
    \caption{Comparison of model results (solid line) with analytical solution (dashed line).}
    \label{fig:validation}
\end{figure}

\end{document}
```

## Resources for Further Learning

1. **Documentation**
   - [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX)
   - [Overleaf Documentation](https://www.overleaf.com/learn)
   - [LaTeX for Physicists](https://physics.oregonstate.edu/~roundyd/LaTex/)

2. **Online Communities**
   - [TeX Stack Exchange](https://tex.stackexchange.com/)
   - [LaTeX Community](https://latex.org/forum/)

3. **Editors**
   - [Overleaf](https://www.overleaf.com) (Online)
   - [TeXstudio](https://www.texstudio.org/) (Desktop)
   - [Visual Studio Code with LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) (Desktop)

4. **Books**
   - "LaTeX: A Document Preparation System" by Leslie Lamport
   - "The LaTeX Companion" by Frank Mittelbach et al.
   - "Guide to LaTeX" by Helmut Kopka and Patrick W. Daly