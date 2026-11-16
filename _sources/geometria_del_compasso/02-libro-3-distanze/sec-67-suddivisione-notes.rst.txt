:layout: book
:type: problem
:order: 3
:folio: 0060
:page: 34
:title: Notes: Repeated Binary Distance Subdivision

.. _mascheroni-libro-3-sec-67-notes:

================================================
Notes: Repeated Binary Distance Subdivision
================================================

.. rubric:: Dyadic Rationals and Algorithmic Succession

.. folio:: 0060

Dyadic Point Generation
-----------------------

Mascheroni's § 67 establishes the constructibility with compass alone of the complete ring of dyadic rationals:

.. math::

   \mathbb{Z}\left[\frac{1}{2}\right] = \left\{ \frac{k}{2^n} \cdot AB \;\middle|\; k, n \in \mathbb{Z}_{\ge 0} \right\}.

Because any real number in :math:`[0, 1]` possesses a binary expansion :math:`\sum_{i=1}^\infty b_i 2^{-i}`, this provides the theoretical basis for Libro XII's arbitrary-precision approximations of transcendental and algebraic quantities.

Apollonius' Theorem Application
-------------------------------

Mascheroni's demonstration relies on Apollonius' theorem for the median of a triangle: for any triangle with sides :math:`a, b`, base :math:`c`, and median :math:`m`:

.. math::

   a^2 + b^2 = 2 m^2 + \frac{1}{2} c^2.

Here :math:`c = BE = 2 AB`, :math:`a = BP' = AB`, :math:`b = P'E = 2 AB`, and the median is :math:`m = AP'`. Hence:

.. math::

   AB^2 + 4 AB^2 = 2 (AP')^2 + 2 AB^2 \implies 2 (AP')^2 = 3 AB^2 \implies AP' = \sqrt{\frac{3}{2}} AB.

Archival Witness
----------------

* **Facsimile Scan:** Folio ``0060`` (p. 35), Fig. 19 crop embedded (:cite:`mascheroni-1797`).
