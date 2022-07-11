# Model Reduction of Swing Equations with Physics Informed PDE

Dated : 15.06.2022

This manuscript reports the first step towards building a robust and efficient model reduction methodology to capture transient dynamics in a transmission level electric power system. Such dynamics is normally modeled on seconds-to-tens-of-seconds time scales by the so-called swing equations, which are ordinary differential equations defined on a spatially discrete model of the power grid. Following Seymlyen (1974) and Thorpe, Seyler, and Phadke (1999), we suggest to map the swing equations onto a linear, inhomogeneous Partial Differential Equation (PDE) of parabolic type in two space and one time dimensions with time-independent coefficients and properly defined boundary conditions. We illustrate our method on the synchronous transmission grid of continental Europe. We show that, when properly coarse- grained, i.e., with the PDE coefficients and source terms extracted from a spatial convolution procedure of the respective discrete coefficients in the swing equations, the resulting PDE reproduces faithfully and efficiently the original swing dynamics. We finally discuss future extensions of this work, where the presented PDE-based modeling will initialize a physics-informed machine learning approach for real-time modeling, n − 1 feasibility assessment and transient stability analysis of power systems.

**Authors :** Laurent Pagnier<sup>1</sup>, Julian Fritzsch<sup>2,3</sup>, Michael Chertkov<sup>1</sup>, Philippe Jacquod<sup>2,3</sup>

1) University of Arizona, Tucson, USA
2) School of Engineering, University of Applied Sciences of Western Switzerland HES-SO, CH-1951 Sion, Switzerland
3) Department of Quantum Matter Physics, University of Geneva, 1211 Geneva, Switzerland

Also available online there : [Arxiv.org] (https://arxiv.org/abs/2110.14066) 



<!-- keywords: network_stability, -->

<!-- link: -->
