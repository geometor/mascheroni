:layout: book
:type: problem
:order: 2
:folio: 0058
:page: 32
:title: Book III § 66: Distance Bisection Without Straightedge (Solution V)

.. _mascheroni-libro-3-sec-66-en:

===================================================================
Book III § 66: Distance Bisection Without Straightedge (Solution V)
===================================================================

.. rubric:: Lorenzo Mascheroni (*The Geometry of the Compass*, Pavia 1797, § 66, pp. 33–34)

.. folio:: 0058

§ 66. *Problem.* To bisect a given distance :math:`AB`.

*Solution V.* With radius :math:`AB` and center :math:`A` (fig. 14), describe the semicircle :math:`BCDE` (§ 64). With center :math:`E` and radius :math:`EB`, describe the indefinite arc :math:`PBp`. With center :math:`B` and radius :math:`BA`, cut this arc in :math:`P` and :math:`p`. With these centers :math:`P` and :math:`p` and with the same radius :math:`BA`, describe two arcs intersecting in :math:`M`. The point :math:`M` will be the sought point.

.. picture:: /_static/figures/plates/fig_17.png
   :alt: Mascheroni Fig. 17 (Book III § 66)

.. picture:: /_static/figures/fig_mascheroni_midpoint.svg
   :alt: Mascheroni segment bisection without straightedge (5 circles)

*Demonstration.* The point :math:`M` will lie on line :math:`BE` (§ 13). The two isosceles triangles :math:`\triangle PBM` and :math:`\triangle PBE` are similar on account of their common base angle at :math:`B` (Euclid I.5, I.32; VI.4). Therefore:

.. math::

   BE : BP = BP : BM

whence (Euclid VI.17):

.. math::

   BE \cdot BM = (BP)^2 = (AB)^2

that is:

.. math::

   2AB \cdot BM = (AB)^2

Dividing by :math:`AB`, we obtain:

.. math::

   2BM = AB

or :math:`BM = \frac{1}{2}AB`. Consequently, the point :math:`M` bisects the given distance :math:`AB`.
