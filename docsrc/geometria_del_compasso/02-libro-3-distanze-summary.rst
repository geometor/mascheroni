:layout: book

.. _mascheroni-libro-3-summary:

Summary: Libro III — Linear Doubling and the S = 17 Midpoint Construction
=========================================================================

.. rubric:: Algorithmic Complexity of Segment Multiplication and Division

1. Invariant Ledger for Libro III
---------------------------------

.. list-table:: Mascheroni Book III Benchmarks
   :header-rows: 1
   :widths: 20 20 30 30

   * - Benchmark
     - Locus
     - Operation Symbol
     - Invariants
   * - **Collinear Doubling**
     - Libro III, § 64
     - :math:`5C_1 + 4C_3`
     - :math:`S = 9, E = 5`, 4 circles, 0 lines
   * - **Midpoint Bisection**
     - Libro III, § 66 (Sol. V)
     - :math:`10C_1 + 7C_3`
     - :math:`S = 17, E = 10`, 7 circles, 0 lines
   * - **Euclidean Midpoint**
     - Euclid I.10 (:cite:`lemoine-1892`)
     - :math:`2R_1 + R_2 + 4C_1 + 2C_3`
     - :math:`S = 9, E = 6`, 1 line, 2 circles

2. Algebraic Invariants of Solution V
-------------------------------------

For unit segment :math:`AB = 1`:

.. math::

   x_E = -1, \quad x_P = x_p = \frac{3}{4}, \quad y_P = -y_p = \frac{\sqrt{15}}{4}, \quad x_M = \frac{1}{2}.

The radical axis of circles :math:`E(2)` and :math:`B(1)` passes through :math:`x = \frac{3}{4}`, and the reflection chords of length :math:`1` from :math:`P` and :math:`p` meet at :math:`M = \frac{1}{2}`, proving constructive stability.
