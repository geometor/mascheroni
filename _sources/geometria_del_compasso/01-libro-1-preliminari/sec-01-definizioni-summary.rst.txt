:layout: book
:type: problem
:order: 1
:folio: 0040
:page: 11
:title: Summary: Definitions & Fundamental Principles

.. _mascheroni-libro-1-sec-1-summary:

================================================
Summary: Definitions & Fundamental Principles
================================================

.. rubric:: Structured Decomposition and Operational Complexity

.. folio:: 0040

Problem 1 (§ 1): Equilateral Point Construction
------------------------------------------------

**Given:**
   Two distinct points :math:`A, E` defining base segment :math:`AE`.

**Construct:**
   1. Describe circle :math:`C_1 = A(AE)`.
   2. Describe circle :math:`C_2 = E(AE)`.
   3. Let :math:`D = C_1 \cap C_2` be an intersection point.

**Demonstrate:**
   By definition of circle radii, :math:`AD = AE` and :math:`ED = AE`. Hence :math:`AD = ED = AE`, forming equilateral triangle :math:`\triangle ADE` (Euclid I.1).

**Lemoine OpCount:**
   * Circle 1: :math:`2C_1` (measure :math:`AE`) :math:`+ C_1` (place at :math:`A`) :math:`+ C_3` (draw arc) = :math:`3C_1 + C_3`.
   * Circle 2: :math:`C_1` (place at :math:`E`, keeping same opening) :math:`+ C_3` = :math:`C_1 + C_3`.
   * Total: :math:`4C_1 + 2C_3` (:math:`S = 6, E = 4, \text{circles} = 2`).

Problem 2 (§ 2): Square Root of Three (:math:`\sqrt{3}`) Construction
----------------------------------------------------------------------

**Given:**
   Two points :math:`A, B` with :math:`AB = 1`.

**Construct:**
   1. Describe circle :math:`A(AB)`.
   2. Step off chord :math:`BC = AB` on the circumference.
   3. Step off chord :math:`CD = AB` on the circumference.
   4. The distance :math:`BD` equals :math:`\sqrt{3}`.

**Demonstrate:**
   In circle :math:`A(1)`, chords :math:`BC = CD = DE = 1` subtend central angles of :math:`60^\circ`. The diameter :math:`BE = 2`. In right triangle :math:`\triangle BDE` inscribed in the semicircle (Euclid III.31):

   .. math::

      BD^2 = BE^2 - DE^2 = 2^2 - 1^2 = 3 \implies BD = \sqrt{3}.

**Instrumental Principles (§§ 8–9):**
   * **Minimum Openings:** Minimize changing compass span to avoid mechanical calibration error.
   * **Orthogonal Intersections:** Maximize intersection angle toward :math:`90^\circ` to minimize positional blur.
