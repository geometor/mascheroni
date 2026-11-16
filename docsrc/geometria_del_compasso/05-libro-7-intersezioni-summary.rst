:layout: book

.. _mascheroni-libro-7-summary:

Summary: Libro VII — Intersections, Inversion, and Euclidean Completeness
==========================================================================

.. rubric:: The Four Canonical Intersection Types in Compass Geometry

1. Intersection Type Matrix
---------------------------

In Euclidean plane geometry, all constructive problems reduce to three fundamental intersection types:

.. list-table:: The Three Fundamental Intersections Under Compass Alone
   :header-rows: 1
   :widths: 25 35 40

   * - Classical Intersection
     - Mascheroni Compass Procedure
     - Complexity
   * - **Circle ∩ Circle**
     - Direct compass sweep :math:`A(R_1) \cap B(R_2)`
     - :math:`2C_1 + 2C_3` (:math:`S = 4`)
   * - **Line ∩ Circle**
     - Reflect center across line; intersect with reflected circle (§§ 110–111)
     - :math:`7C_1 + 3C_3` (:math:`S = 10`)
   * - **Line ∩ Line**
     - Reflect lines, fourth proportional (§ 112) or Adler inversion
     - :math:`12C_1 + 6C_3` (:math:`S = 18`)

2. Adler's Inversion Invariants
-------------------------------

For inversion of point :math:`A` through circle :math:`\Gamma(O, R)` (with :math:`OA > R/2`):

.. math::

   A(AO) \cap \Gamma(O, R) \to P, Q, \qquad P(PO) \cap Q(QO) \to A', \qquad OA \cdot OA' = R^2.

The construction uses exactly **3 circles**: :math:`5C_1 + 3C_3` (:math:`S = 8, E = 5`), proving that inversion is an elementary compass primitive.
