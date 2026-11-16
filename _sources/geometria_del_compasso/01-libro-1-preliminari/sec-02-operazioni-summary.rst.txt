:layout: book
:type: problem
:order: 2
:folio: 0043
:page: 14
:title: Summary: Notation & Fundamental Collinearity Lemma

.. _mascheroni-libro-1-sec-2-summary:

=======================================================
Summary: Notation & Fundamental Collinearity Lemma
=======================================================

.. rubric:: Structural Decomposition of Orthogonal Reflection

.. folio:: 0043

Problem Formulation: The Fundamental Lemma (§ 13)
-------------------------------------------------

**Given:**
   Two fixed points :math:`A, B` defining baseline :math:`AB`. Two radii :math:`r_1 = AP` and :math:`r_2 = AQ`.

**Construct:**
   1. Intersect :math:`A(r_1) \cap B(BP)` to determine point pair :math:`(P, p)`.
   2. Intersect :math:`A(r_2) \cap B(BQ)` to determine point pair :math:`(Q, q)`.

**Demonstrate:**
   1. Triangles :math:`\triangle APB \cong \triangle ApB` by SSS. Hence :math:`\angle PAB = \angle pAB` and :math:`\angle PBA = \angle pBA`.
   2. Segment :math:`Pp` is the orthogonal reflection axis: the line of centers :math:`AB` is the perpendicular bisector of :math:`Pp`.
   3. The points :math:`Q, P, p, q` all lie on the perpendicular bisector of :math:`AB`.
   4. Hence, collinearity of four points is established purely through concentric circular symmetry without drawing any lines.

**Operational Complexity (Lemoine OpCount):**
   * Intersection of two circles with centers :math:`A, B`:
     :math:`3C_1 + C_3` (first circle) :math:`+ 2C_1 + C_3` (second circle) = :math:`5C_1 + 2C_3`.
   * Simplicity :math:`S = 7`, Exactitude :math:`E = 5`, Circles :math:`= 2`.
