:layout: book

.. _mascheroni-libro-10-summary:

Summary: Libro X — Napoleon's Problem & Minimal-Instrument Duality
==================================================================

.. rubric:: Algorithmic Duality of Center Determination

1. The Center Problem Ledger
----------------------------

.. list-table:: Center Determination: Mascheroni vs. Steiner
   :header-rows: 1
   :widths: 25 35 40

   * - Instrument Regime
     - Status of Center :math:`O`
     - Constructive Possibility
   * - **Mascheroni (Compass Alone)**
     - Circle :math:`\Gamma` given without center
     - **Solvable**: Found in 6 circles (:math:`S = 15`) via inversion
   * - **Steiner (Straightedge Alone)**
     - Circle :math:`\Omega` given without center
     - **Impossible**: Collineations fixing :math:`\Omega` move center :math:`M`
   * - **Poncelet–Steiner (Straightedge)**
     - Circle :math:`\Omega` given **with** center :math:`M`
     - **Solvable**: Restores full Euclidean quadratic closure

2. Algebraic Invariants of Napoleon's Problem
---------------------------------------------

For given circle :math:`\Gamma(O, R)` and arbitrary point :math:`A` on :math:`\Gamma`:

.. math::

   AB = AC = r, \qquad AD = \frac{r^2}{R}, \qquad \text{Inversion of } D \text{ through } A(r) \implies AO = \frac{r^2}{AD} = R.

Because :math:`D` lies on diameter :math:`AO`, the inverse of :math:`D` through circle :math:`A(r)` falls at distance :math:`R` from :math:`A` along the diameter, which is precisely the center :math:`O`!
