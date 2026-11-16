:layout: book

.. _mascheroni-libro-10-en:

Book X: Determination of Centers & Napoleon's Problem
=====================================================

.. rubric:: Lorenzo Mascheroni (*La Geometria del Compasso*, Pavia 1797, §§ 143–147, pp. 82–85)

.. contents:: In This Book
   :local:
   :depth: 2
   :backlinks: none

.. folio:: 0107
   :page: 82

§ 1. Finding the Center of a Given Circle: Napoleon's Problem (§ 143)
---------------------------------------------------------------------

A circle :math:`\Gamma` is drawn on paper, but its center :math:`O` is unmarked. Find :math:`O` using only the compass:

1. Select an arbitrary point :math:`A` on circumference :math:`\Gamma`.
2. With an arbitrary radius :math:`r`, sweep an arc from :math:`A` cutting :math:`\Gamma` at two points :math:`B` and :math:`C`.
3. With centers :math:`B` and :math:`C` and radius :math:`r = AB`, sweep arcs intersecting at point :math:`D` (opposite to :math:`A`).
4. Segment :math:`AD` lies along the diameter of :math:`\Gamma` through :math:`A`.
5. Construct the inverse of point :math:`D` with respect to circle :math:`A(r)` using compass inversion (Book VII, § 3).
6. The inverse point is **the exact center O of circle Γ**!

*Operation Count*: :math:`9C_1 + 6C_3` (:math:`S = 15, E = 9`, 6 circles, 0 lines).

.. folio:: 0108
   :page: 83

§ 2. Finding the Center of a Circle Passing Through Three Points (§ 144)
------------------------------------------------------------------------

Given three non-collinear points :math:`M, A, B`:

1. Find the orthogonal reflection lines of :math:`MA` and :math:`AB` using Book IV, § 78.
2. Intersecting the two perpendicular bisectors via Book VII, § 112 yields the circumcenter :math:`O = X(3)` of triangle :math:`\triangle MAB` using compass alone.

.. folio:: 0109
   :page: 84

§ 3. Foundational Duality Between Mascheroni and Poncelet–Steiner
-----------------------------------------------------------------

.. picture:: /_static/figures/fig_mascheroni_steiner_duality.svg
   :alt: Duality between Mascheroni compass-only and Steiner fixed-circle straightedge

This problem illustrates the profound epistemological duality between minimal instruments:

1. **Mascheroni (1797)**: A drawn circle :math:`\Gamma` is given *without* its center; the compass **can find center O** directly (§ 143) because circular arcs generate quadratic metric distances.
2. **Poncelet–Steiner (1833)**: In :person:`Jakob Steiner <steiner>`'s regime (:cite:`steiner-1833`), a straightedge can solve all Euclidean problems *only if the center M of the fixed circle is permanently given*. If :math:`M` were omitted, the straightedge **can never find it**, because hyperbolic projective transformations preserving the circular boundary move the Euclidean center while preserving all straight lines!
