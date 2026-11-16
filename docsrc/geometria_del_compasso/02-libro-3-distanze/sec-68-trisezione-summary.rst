:layout: book
:type: problem
:order: 4
:folio: 0061
:page: 36
:title: Summary: Distance Trisection in a Straight Line

.. _mascheroni-libro-3-sec-68-summary:

==================================================
Summary: Distance Trisection in a Straight Line
==================================================

.. rubric:: Structural Decomposition and Operational Complexity

.. folio:: 0061

Problem Formulation (§ 68)
--------------------------

**Given:**
   Segment :math:`AB`.

**Construct:**
   1. Collinear tripling: Produce ray :math:`AB` to :math:`E` such that :math:`BE = 3 AB`.
   2. Arc with radius :math:`\sqrt{3} AB`: With center :math:`E` and radius :math:`EC = \sqrt{3} AB`, draw arc :math:`\Gamma`.
   3. Circle at :math:`A`: With center :math:`A` and radius :math:`AB`, cut arc :math:`\Gamma` at :math:`P` and :math:`p`.
   4. Arcs from :math:`P, p`: With radius :math:`AB`, describe arcs meeting at :math:`M`.
   5. Step :math:`M(MB)` cutting :math:`AB` in :math:`N`.
   6. Points :math:`M` and :math:`N` divide :math:`AB` into three equal parts: :math:`BM = MN = NA = \frac{1}{3} AB`.

**Demonstrate:**
   By similar isosceles triangles :math:`\triangle PBE \sim \triangle PBM`:

   .. math::

      \frac{BE}{BP} = \frac{BP}{BM} \implies BM = \frac{BP^2}{BE} = \frac{AB^2}{3 AB} = \frac{1}{3} AB.

**Operational Complexity (Lemoine OpCount):**
   * Formula: :math:`12C_1 + 8C_3`
   * Simplicity: :math:`S = 20`
   * Exactitude: :math:`E = 12`
   * Circles: :math:`6`
