:layout: book
:type: problem
:order: 3
:folio: 0060
:page: 34
:title: Summary: Repeated Binary Distance Subdivision

.. _mascheroni-libro-3-sec-67-summary:

==================================================
Summary: Repeated Binary Distance Subdivision
==================================================

.. rubric:: Structural Decomposition and Operational Complexity

.. folio:: 0060

Problem Formulation (§ 67)
--------------------------

**Given:**
   Segment :math:`AB` with midpoint :math:`M` already located (:math:`AM = \frac{1}{2} AB`).

**Construct:**
   1. Using the existing construction scaffolding of § 66, determine point :math:`Q'` on arc :math:`B(2 AB)` at distance :math:`BQ' = AP' = \sqrt{\frac{3}{2}} AB`.
   2. Intersect arcs from :math:`Q'` and :math:`q'` with radius :math:`BQ'` to locate point :math:`N`.
   3. :math:`N` is the midpoint of :math:`AM` (:math:`AN = \frac{1}{4} AB`).
   4. Iterate the step by setting :math:`BR' = AQ'` to determine :math:`O` (:math:`AO = \frac{1}{8} AB`).

**Demonstrate:**
   * Apollonius' median theorem applied to :math:`\triangle P'BE` gives the exact algebraic radius :math:`BQ' = \sqrt{3/2} AB`.
   * Similarity of triangles :math:`\triangle Q'BN \sim \triangle Q'BE` yields :math:`BN = \frac{BQ'^2}{BE} = \frac{(3/2) AB^2}{2 AB} = \frac{3}{4} AB`.
   * Consequently :math:`AN = AB - BN = \frac{1}{4} AB = \frac{1}{2} AM`.

**Operational Complexity:**
   * Each subsequent subdivision step reuses the established center :math:`B` and axis :math:`BE`.
   * Requires :math:`4C_1 + 2C_3` per dyadic step.
