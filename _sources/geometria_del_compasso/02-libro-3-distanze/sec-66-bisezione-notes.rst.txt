:layout: book
:type: problem
:order: 2
:folio: 0058
:page: 32
:title: Notes: Segment Bisection (Solution V)

.. _mascheroni-libro-3-sec-66-notes:

==============================================
Notes: Segment Bisection (Solution V)
==============================================

.. rubric:: Algebraic Verification, Inversion Geometry, and Archival History

.. folio:: 0058

SymPy Exact Verification
------------------------

In Cartesian coordinates, let :math:`A = (0, 0)` and :math:`B = (1, 0)`.
1. Collinear doubling gives :math:`E = (-1, 0)`.
2. Arc :math:`\Gamma = E(2)` has equation :math:`(x + 1)^2 + y^2 = 4`.
3. Circle :math:`B(1)` has equation :math:`(x - 1)^2 + y^2 = 1`.
4. Subtracting equations: :math:`4x = 3 \implies x = \frac{3}{4}, y = \pm \frac{\sqrt{7}}{4}`. Thus :math:`P = \left(\frac{3}{4}, \frac{\sqrt{7}}{4}\right)` and :math:`p = \left(\frac{3}{4}, -\frac{\sqrt{7}}{4}\right)`.
5. Arcs from :math:`P, p` of radius :math:`1` meet on the :math:`x`-axis:

   .. math::

      \left(x - \frac{3}{4}\right)^2 + \frac{7}{16} = 1 \implies \left(x - \frac{3}{4}\right)^2 = \frac{9}{16} \implies x - \frac{3}{4} = \pm \frac{3}{4}.

   The positive root yields :math:`x = \frac{3}{2}` (external), and the negative root yields :math:`x = \frac{1}{2}`, which is the exact midpoint :math:`M = \left(\frac{1}{2}, 0\right)`.

Verified in :func:`geometor.mascheroni.mascheroni_midpoint`:

.. code-block:: python

   import sympy as sp
   from geometor.mascheroni import mascheroni_midpoint

   a = sp.Point2D(0, 0)
   b = sp.Point2D(1, 0)
   m = mascheroni_midpoint(a, b)
   assert m == sp.Point2D(sp.Rational(1, 2), 0)

Comparison with Georg Mohr (1672)
---------------------------------

Georg Mohr in *Euclides Danicus* (Part I, Prob. 2) solved segment bisection using an 8-circle construction based on an equilateral triangle and orthogonal projection. Mascheroni's Solution V is distinctly more efficient, requiring only 5 circles and achieving an optimal Lemoine simplicity score.

Archival Witness
----------------

* **Facsimile Scan:** Folio ``0058`` (p. 33), Editio Princeps (:cite:`mascheroni-1797`).
* **Companion SVG:** :file:`/_static/figures/fig_mascheroni_midpoint.svg`.
