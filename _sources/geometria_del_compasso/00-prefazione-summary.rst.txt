:layout: book

.. _mascheroni-prefazione-summary:

Summary: The Scope and Axiomatic Foundation of Compass-Only Geometry
====================================================================

.. rubric:: Structural Overview of Mascheroni's 1797 Treatise and Operational Principles

1. The Postulate of the Single Instrument
-----------------------------------------

In classical Euclidean geometry (:cite:`euclid-heath`), constructive power rests upon three postulates:

* **Postulate 1**: To draw a straight line from any point to any point.
* **Postulate 2**: To produce a finite straight line continuously in a straight line.
* **Postulate 3**: To describe a circle with any center and radius.

:person:`Lorenzo Mascheroni <mascheroni>` proved that **Postulates 1 and 2 can be entirely eliminated** for all point-determination problems in plane geometry. The geometer requires only Postulate 3.

2. The Virtual Line Principle
-----------------------------

Because a continuous straight line cannot be traced without a straightedge, Mascheroni introduces the fundamental concept of the :term:`virtual line <retta-virtuale>`:

* Any straight line :math:`L` is determined and represented by **two distinct points** :math:`(A, B)`.
* A third point :math:`C` is said to lie on line :math:`(A, B)` if its distance from :math:`A` and :math:`B` satisfies the collinear triangle-inequality degenerate limit :math:`AB + BC = AC` or :math:`AC + CB = AB`.
* All operations on straight lines—drawing parallels, erecting perpendiculars, reflecting across lines, and intersecting lines with circles or with other lines—are executed purely by intersecting circular arcs.

3. Systematic Codex Division
----------------------------

.. list-table:: Mascheroni's Twelve Books and Primary Constructive Invariants
   :header-rows: 1
   :widths: 15 35 25 25

   * - Book
     - Canonical Title
     - Key Problem Solved
     - Operation Count
   * - **Libro I**
     - Preliminari (§§ 1–11)
     - Virtual line representation & arc meets
     - :math:`2C_1 + C_3`
   * - **Libro II**
     - Divisione della circonferenza (§§ 12–63)
     - Circle quadrisection, golden ratio
     - 4 auxiliary arcs
   * - **Libro III**
     - Moltiplicazione e divisione (§§ 64–75)
     - Linear doubling § 64, bisection § 66
     - :math:`10C_1 + 7C_3` (:math:`S = 17`)
   * - **Libro IV**
     - Perpendicolari e parallele (§§ 76–85)
     - Perpendiculars § 76, parallels § 80
     - :math:`5C_1 + 2C_3` (:math:`S = 7`)
   * - **Libro V**
     - Distanze proporzionali (§§ 86–101)
     - Fourth proportional via concentric circles
     - 4 circles (:math:`S = 14`)
   * - **Libro VII**
     - Intersezioni rette-cerchi (§§ 110–112)
     - Line–circle and line–line meets
     - Inversion :math:`5C_1 + 3C_3`
   * - **Libro X**
     - Determinazione dei centri (§§ 143–155)
     - Finding circle center (Napoleon)
     - Pure compass sweep
