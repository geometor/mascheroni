:layout: book

.. _mascheroni-libro-7-en:

Book VII: Intersection of Lines and Circles by Compass Alone
============================================================

.. rubric:: Lorenzo Mascheroni (*La Geometria del Compasso*, Pavia 1797, §§ 110–112, pp. 60–63)

.. contents:: In This Book
   :local:
   :depth: 2
   :backlinks: none

.. folio:: Line-Circle Meet
   :page: 60

§ 1. Intersecting a Virtual Line with a Circle (§§ 110–111)
-----------------------------------------------------------

To find the points where a virtual line :math:`(P, Q)` intersects circle :math:`\Gamma = A(R)` without drawing the line:

1. Reflect the circle center :math:`A` across line :math:`(P, Q)` using Book IV, § 78: sweep arcs :math:`P(PA)` and :math:`Q(QA)` meeting at :math:`A'`.
2. With center :math:`A'` and the original radius :math:`R`, describe the reflected circle :math:`\Gamma' = A'(R)`.
3. Circles :math:`\Gamma` and :math:`\Gamma'` intersect at two points :math:`X` and :math:`Y`.
4. Because :math:`(P, Q)` is the perpendicular bisector (line of symmetry) between centers :math:`A` and :math:`A'`, every intersection of :math:`\Gamma` and :math:`\Gamma'` must lie on line :math:`(P, Q)`.
5. Therefore, :math:`X` and :math:`Y` are the exact intersections of the line and the circle!

*Operation Count*: :math:`7C_1 + 3C_3` (:math:`S = 10, E = 7`, 3 circles, 0 lines).

.. folio:: Line-Line Meet
   :page: 61

§ 2. Intersecting Two Virtual Lines (§ 112)
-------------------------------------------

Given two virtual lines :math:`(A, B)` and :math:`(C, D)`, determine their point of intersection :math:`S`:

1. Reflect points :math:`C` and :math:`D` across line :math:`(A, B)` to obtain :math:`c` and :math:`d`.
2. Construct the fourth vertex :math:`\delta` of parallelogram :math:`CDd\delta` using Book IV, § 80.
3. Using the concentric fourth proportional (Book V, § 93), compute radius:

   .. math::

      CS = \frac{CD \cdot Cc}{c\delta}.

4. Arcs of radius :math:`CS` centered at :math:`C` and :math:`c` intersect at point :math:`S`. Point :math:`S` lies simultaneously on :math:`(C, D)` and on the axis of symmetry :math:`(A, B)`, yielding the exact meet of the two lines!

.. folio:: Adler's Circular Inversion
   :page: 63

§ 3. August Adler's Inversion Functor (1890)
--------------------------------------------

In 1890, :person:`August Adler <adler>` (:cite:`adler-1890`) established the modern conceptual completion of the Mohr–Mascheroni theorem via circular inversion (:cite:`lemoine-1902`, Problem XXXVIII: :math:`5C_1 + 3C_3, S = 8`):

.. picture:: /_static/figures/fig_mascheroni_inversion.svg
   :alt: Circular inversion by compass alone

* Under circular inversion with respect to reference circle :math:`\Gamma(O, R)`, every straight line not passing through :math:`O` transforms into a circle passing through :math:`O`.
* Consequently, the problem of intersecting two straight lines :math:`L_1 \cap L_2` transforms into intersecting two circles passing through :math:`O`.
* The circles intersect at :math:`O` and at an inverse point :math:`S'`. Inverting :math:`S'` back through :math:`\Gamma` recovers the intersection :math:`S`!
* This unified functor provides the ultimate algebraic proof that **compass geometry is isomorphic to ruler-and-compass geometry over the Euclidean quadratic closure**.
