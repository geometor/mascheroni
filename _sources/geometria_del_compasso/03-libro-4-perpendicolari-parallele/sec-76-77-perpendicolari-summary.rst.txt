:layout: book
:type: problem
:order: 1
:folio: 0067
:page: 42
:title: Summary: Perpendicular Lines with Compass Alone

.. _mascheroni-libro-4-sec-76-summary:

================================================
Summary: Perpendicular Lines with Compass Alone
================================================

.. rubric:: Structural Decomposition and Operational Complexity

.. folio:: 0067

Problem Formulation (§ 77: Perpendicular at Endpoint)
-----------------------------------------------------

**Given:**
   Two points :math:`A, B` defining baseline segment :math:`AB`.

**Construct:**
   1. Choose arbitrary radius :math:`r > \frac{1}{2} AB`. Intersect :math:`A(r) \cap B(r)` at :math:`C`.
   2. With center :math:`C` and radius :math:`CA`, draw circle :math:`C(CA)` passing through :math:`A` and :math:`B`.
   3. Double diameter from :math:`B` through center :math:`C` to obtain opposite point :math:`D` (§ 64).
   4. Ray :math:`AD` is perpendicular to :math:`AB` at point :math:`A`.

**Demonstrate:**
   Triangle :math:`\triangle BAD` is inscribed in circle :math:`C` with hypotenuse :math:`BD` as diameter. By Thales' Theorem (Euclid III.31), :math:`\angle BAD = 90^\circ`.

**Operational Complexity (Lemoine OpCount):**
   * Arcs for center :math:`C`: :math:`4C_1 + 2C_3`.
   * Circle and doubling for :math:`D`: :math:`3C_1 + 3C_3`.
   * Total: :math:`7C_1 + 5C_3` (:math:`S = 12, E = 7, \text{circles} = 4`).
