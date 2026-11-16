:layout: book
:type: problem
:order: 1
:folio: 0057
:page: 31
:title: Summary: Linear Distance Doubling

.. _mascheroni-libro-3-sec-64-summary:

======================================
Summary: Linear Distance Doubling
======================================

.. rubric:: Structured Decomposition and Operational Complexity

.. folio:: 0057

Problem Formulation (§ 64)
--------------------------

**Given:**
   Two distinct points :math:`A, B` defining distance :math:`AB`.

**Construct:**
   1. Describe circle :math:`B(AB)`.
   2. Using the unchanged span :math:`AB`, step off three successive chords on the circumference:
      * :math:`C = B(AB) \cap A(AB)`
      * :math:`D = B(AB) \cap C(AB)`
      * :math:`E = B(AB) \cap D(AB)`
   3. The point :math:`E` is the required collinear doubled endpoint.

**Demonstrate:**
   * Central angles: :math:`\angle ABC = \angle CBD = \angle DBE = 60^\circ`.
   * Total angle: :math:`\angle ABE = 180^\circ`, ensuring collinearity of :math:`A, B, E`.
   * Segment addition: :math:`AE = AB + BE = AB + AB = 2AB`.

**Operational Complexity (Lemoine OpCount):**
   * Compass operations: :math:`3C_1 + 3C_3` (one initial circle plus two chord-marking arcs with same aperture).
   * Simplicity: :math:`S = 6`.
   * Exactitude: :math:`E = 3`.
   * Circles: :math:`3`.
   * Distinct compass apertures: :math:`1` (constant radius :math:`AB`).
