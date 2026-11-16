:layout: book

.. _mascheroni-libro-3-en:

Book III: Collinear Multiplication & Division of Distances
==========================================================

.. rubric:: Lorenzo Mascheroni (*La Geometria del Compasso*, Pavia 1797, §§ 64–68, pp. 31–36)

.. contents:: In This Book
   :local:
   :depth: 2
   :backlinks: none

.. folio:: 0057
   :page: 31

§ 1. Collinear Doubling of Distance AB (§ 64)
---------------------------------------------

To produce a point :math:`E` collinear with two given points :math:`A` and :math:`B` such that :math:`AE = 2\,AB` without a ruler:

1. With center :math:`A` and radius :math:`AB`, sweep the circle :math:`A(AB)`.
2. Stepping the radius :math:`AB` three consecutive times around the circumference from :math:`B` generates points :math:`C, D, E`.
3. Because each equilateral chord subtends :math:`60^\circ`, the three chords span an exact semicircle of :math:`180^\circ`. Hence :math:`E` lies on the diameter opposite :math:`B`, placing :math:`E, A, B` in strict collinearity with :math:`EB = 2\,AB`.

*Operation Count*: :math:`5C_1 + 4C_3` (:math:`S = 9, E = 5`, 4 circles, 0 lines).

.. folio:: 0058
   :page: 32

§ 2. Bisecting an Un-Drawn Segment AB (§ 66, Solution V)
--------------------------------------------------------

Mascheroni provides five solutions for segment bisection. Solution V is celebrated as the most elegant:

1. Double segment :math:`BA` past :math:`A` to point :math:`E` via § 64 (:math:`BE = 2\,BA`).
2. With center :math:`E` and radius :math:`EB = 2\,AB`, describe arc :math:`PBp`.
3. With center :math:`B` and radius :math:`BA`, sweep circle :math:`B(BA)` cutting the previous arc at :math:`P` and :math:`p`.
4. With centers :math:`P` and :math:`p` and radius :math:`BA`, sweep two arcs intersecting at point :math:`M`.
5. Point :math:`M` is the exact midpoint of segment :math:`AB`!

.. picture:: /_static/figures/fig_mascheroni_midpoint.svg
   :alt: Mascheroni midpoint bisection by compass alone

**Exact Algebraic Verification**:
Taking :math:`A = (0, 0)` and :math:`B = (1, 0)`:
* :math:`E = (-1, 0)`, so :math:`EB = 2`.
* Circle :math:`E(EB)`: :math:`(x + 1)^2 + y^2 = 4`.
* Circle :math:`B(BA)`: :math:`(x - 1)^2 + y^2 = 1`.
* Radicall-plane intersection: :math:`4x = 3 \implies x = \frac{3}{4}`, yielding :math:`P, p = \left(\frac{3}{4}, \pm \frac{\sqrt{15}}{4}\right)`.
* Circles centered at :math:`P, p` of radius :math:`1`: :math:`\left(x - \frac{3}{4}\right)^2 + \frac{15}{16} = 1 \implies \left(x - \frac{3}{4}\right)^2 = \frac{1}{16}`.
* Roots: :math:`x = \frac{3}{4} \pm \frac{1}{4} \implies x_1 = \frac{1}{2}, x_2 = 1`.
* The root :math:`x = \frac{1}{2}` lies precisely midway between :math:`A(0, 0)` and :math:`B(1, 0)`.

*Operation Count*: :math:`10C_1 + 7C_3` (:math:`S = 17, E = 10`, 7 circles, 0 lines).

.. folio:: 0060
   :page: 34

§ 3. Repeated Subdivision and Trisection (§§ 67–68)
---------------------------------------------------

* **§ 67. Repeated Bisection**: Applying Solution V recursively to :math:`AM` yields the quarter point :math:`N`, eighth point :math:`O`, and any dyadic fraction :math:`k/2^n \cdot AB`.
* **§ 68. Trisection**: Combining collinear doubling (§ 64) with proportional distance transfer determines the exact third :math:`\frac{1}{3} AB` with compass alone.
