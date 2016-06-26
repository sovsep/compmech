r"""
=====================================================
Panel Connections (:mod:`compmech.panel.connections`)
=====================================================

.. currentmodule:: compmech.panel.connections

Connection between panel domains. Each panel domain is currently using its own
set of Bardell approximation functions.

kCBFycte
---------

Connection of type::

                          _
                           |
       || --> Flange       |
       ||                  |-> Can be used to model a stiffener
     ======  --> Base      |
                          _|

``ycte`` indicates the connection is made a constant `y_1` for panel 1 (base)
and `y_2` for panel 2 (flange).

kCSB
---------

Connection of type::

               ======        ==> base
               ------        --> skin

Takes into account the offset between the two mid-surfaces.


kCSSxcte
---------

Connection of type::

      __________
      |        |
      |        |      /^\ x2
      |   S2   |       |
      |        |   y2  |
      |        |   <----
      |________| (connection at x2=xcte2)
      __________ (connection at x1=xcte1)
      |        |
      |        |      /^\ x1
      |   S1   |       |
      |        |   y1  |
      |________|   <----

kCSSycte
---------

Connection of type::

                 /-> (connection at y1=ycte1)
                /
               /  /->(connection at y2=ycte2)
      _________| |_________
      |        | |        |
      |        | |        |
      |   S1   | |   S2   |
      |        | |        |
      |________| |________|

          /^\ x1       /^\ x2
           |            |
       y1  |        y2  |
       <----        <----

"""
from . kCBFycte import *
from . kCSB import *
from . kCSSxcte import *
from . kCSSycte import *
