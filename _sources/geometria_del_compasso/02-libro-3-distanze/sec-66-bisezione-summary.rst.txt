:layout: book
:type: problem
:order: 2
:folio: 0058
:page: 32
:title: Summary: Segment Bisection (Solution V)

.. _mascheroni-libro-3-sec-66-summary:

================================================
Summary: Segment Bisection (Solution V)
================================================

.. rubric:: Structured Decomposition and Operational Complexity

.. folio:: 0058

Problem Formulation (§ 66, Sol. V)
----------------------------------

**Given:**
   Two distinct points :math:`A, B` defining baseline segment :math:`AB`.

**Construct:**
   1. Collinear doubling: With center :math:`A` and radius :math:`AB`, construct collinear point :math:`E` such that :math:`AE = AB` and :math:`E, A, B` are collinear (:math:`BE = 2 AB`, § 64).
   2. Large arc: With center :math:`E` and radius :math:`EB = 2 AB`, describe arc :math:`\Gamma = E(2 AB)`.
   3. Circle at :math:`B`: With center :math:`B` and radius :math:`BA = AB`, cut arc :math:`\Gamma` at points :math:`P` and :math:`p`.
   4. Final intersection: With centers :math:`P` and :math:`p` and radius :math:`BA = AB`, describe arcs intersecting at :math:`M`.
   5. The point :math:`M` is the exact midpoint of :math:`AB`.

**Demonstrate:**
   * Triangle :math:`\triangle PBE` is isosceles with :math:`EP = EB = 2 AB` and :math:`BP = AB`.
   * Triangle :math:`\triangle PBM` is isosceles with :math:`BP = MP = AB` and base :math:`PM`.
   * They share the base angle :math:`\angle PBE = \angle PBM`.
   * By similarity of isosceles triangles sharing a base angle:

     .. math::

        \frac{BE}{BP} = \frac{BP}{BM} \implies BM = \frac{BP^2}{BE} = \frac{AB^2}{2 AB} = \frac{1}{2} AB.

**Operational Complexity (Lemoine OpCount):**
   * Formula: :math:`10C_1 + 7C_3`
   * Simplicity: :math:`S = 17`
   * Exactitude: :math:`E = 10`
   * Total circles: :math:`5`
   * Distinct radii: :math:`2` (:math:`R_1 = AB`, :math:`R_2 = 2 AB`).
