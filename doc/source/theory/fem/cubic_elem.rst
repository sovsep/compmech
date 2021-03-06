Cubic element of the Serendipity family
.......................................

Zienkiewicz and Taylor (2000) [zienkiewicz2000v1]_ present a rectangular
cubic element of the Serendipity family (in Chapter 8) which will be described
here, focusing on its implementation using an isoparametric approach, i.e.
the same approximation used for the geometry will be used to approximate
the displacement field vector `\{u\}`.

The element and the 12 nodes are shown in the figure below.

.. _figure_quadcubics:
.. plot:: ../pyplots/theory/fem/fsdt_donnell_quad12.py

The variables of `\{u\}` are interpolated using:

.. math::
    \{u\} = \sum_{i=1}^{i=12}{h_i \{u_i\}}

where `h_i` and `\{u_i\}` represent the interpolation and the displacement
vector at node `n_i`. The interpolation function for the corner nodes are:

.. math::
    h_{1,\cdots,4} = \frac{1}{32}(1 + \xi\cdot\xi_{1,\cdots,4})
             (1 + \eta\cdot\eta_{1,\cdots,4})[-10 + 9\cdot(\xi^2 + \eta^2)]

and for the middle nodes are:

.. math::
    h_{5,\cdots,12}  = \frac{9}{32}(1 + \xi\cdot\xi_{5,\cdots,12})
                           (1-\eta^2)(1+9\cdot\eta\cdot\eta_{5,\cdots,12})

The coordinates for each node




