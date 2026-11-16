:layout: book

.. _mascheroni-libro-1-en:

Book I: Preliminary Principles — Foundations of Compass-Only Construction
=========================================================================

.. rubric:: Lorenzo Mascheroni (*La Geometria del Compasso*, Pavia 1797, §§ 1–11, pp. 11–18)

.. contents:: In This Book
   :local:
   :depth: 2
   :backlinks: none

.. folio:: 0040
   :page: 11

§ 1. Points, Virtual Lines & Compass Postulates (§§ 1–3)
--------------------------------------------------------

In this geometry, **no instrument other than the compass is admitted**.

Because continuous straight lines cannot be drawn without a straightedge, Mascheroni establishes the principle of the :term:`virtual line <retta-virtuale>`: a straight line is regarded as completely determined whenever **two distinct points** :math:`A` and :math:`B` belonging to it are known:

1. **Constructing a straight line** means determining two points through which that line must pass.
2. **Intersecting two straight lines**, or a straight line and a circle, means finding purely by intersecting compass arcs the point or points where the loci would meet if traced with a ruler.
3. Every geometric figure—triangle, polygon, or conic locus—is resolved into a discrete network of constructible points.

.. folio:: 0043
   :page: 14

§ 2. Operational Algebra: The Three Elementary Compass Operations (§§ 4–11)
---------------------------------------------------------------------------

Mascheroni's procedures reduce to three primitive operations, codified in Lemoine's :term:`Géométrographie Mascheronienne <geometrographie-mascheronienne>` (:cite:`lemoine-1902`, pp. 66–74):

* :term:`Operation C₁ <c1>`: Placing one leg of the compass on a previously determined point :math:`A`. Taking up distance :math:`AB` requires placing both points: :math:`2C_1`.
* :term:`Operation C₂ <c2>`: Placing one leg of the compass on an arbitrary point of an already traced arc.
* :term:`Operation C₃ <c3>`: Describing a circle or circular arc once its center and radius are fixed.

When the straightedge is banished (:math:`l_1 = l_2 = 0`), every construction ledger simplifies to:

.. math::

   \mathrm{Op.}_{\text{Masch.}} : \left(m_1 C_1 + m_2 C_2 + m_3 C_3\right), \qquad S = m_1 + m_2 + m_3, \quad E = m_1 + m_2, \quad N_{\text{lines}} = 0.

§ 3. Distance Transfer and Orthogonal Symmetry (§ 11)
-----------------------------------------------------

Given points :math:`A, B` and an origin :math:`C`:

* Describing circle :math:`C(AB)` requires taking up radius :math:`AB` (:math:`2C_1`), placing the point at :math:`C` (:math:`C_1`), and drawing the arc (:math:`C_3`), totaling :math:`3C_1 + C_3` (:math:`S = 4, E = 3`).
* Two intersecting circles :math:`A(R_1)` and :math:`B(R_2)` yield two intersection points :math:`P, Q`. The segment :math:`PQ` is perpendicularly bisected by the line of centers :math:`AB`, so that :math:`P` and :math:`Q` are **mutual orthogonal reflections** across :math:`AB`. This reflection lemma forms the fundamental engine of Books III, IV, and VII.
