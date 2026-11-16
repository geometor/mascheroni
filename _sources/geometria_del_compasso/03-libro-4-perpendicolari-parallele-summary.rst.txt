:layout: book

.. _mascheroni-libro-4-summary:

Summary: Libro IV — Perpendiculars, Reflections, and Parallels
==============================================================

.. rubric:: Operational Comparison: Mascheroni Compass vs. Classical Straightedge

1. Benchmark Comparison Table
-----------------------------

.. list-table:: Perpendicular & Parallel Benchmarks
   :header-rows: 1
   :widths: 22 28 25 25

   * - Problem
     - Method
     - Operation Symbol
     - Complexity
   * - **Perpendicular Foot**
     - Mascheroni Libro IV, § 78
     - :math:`14C_1 + 9C_3`
     - :math:`S = 23, E = 14`, 9 circles
   * - **Perpendicular Foot**
     - Euclid I.12 (Ruler+Compass)
     - :math:`2R_1 + R_2 + 6C_1 + 3C_3`
     - :math:`S = 12, E = 8`, 1 line, 3 circles
   * - **Parallel Point**
     - Mascheroni Libro IV, § 80
     - :math:`5C_1 + 2C_3`
     - :math:`S = 7, E = 5`, 2 circles, 0 lines
   * - **Parallel Line**
     - Euclid I.31 (Classical)
     - :math:`4R_1 + 2R_2 + 8C_1 + 4C_3`
     - :math:`S = 18, E = 12`, 2 lines, 4 circles
   * - **Parallel Line**
     - Tarry Rhombus (:cite:`lemoine-1892`)
     - :math:`2R_1 + R_2 + 4C_1 + 2C_3`
     - :math:`S = 9, E = 6`, 1 line, 2 circles

2. Key Algorithmic Insight
--------------------------

On parallel construction, **Mascheroni (:math:`S = 7`) strictly beats both classical Euclid (:math:`S = 18`) and Tarry's optimized ruler-and-compass method (:math:`S = 9`)**, because constructing a parallelogram requires only two circular arcs when the straightedge is omitted!
