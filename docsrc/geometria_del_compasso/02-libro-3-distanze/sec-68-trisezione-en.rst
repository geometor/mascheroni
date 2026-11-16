:layout: book
:type: problem
:order: 4
:folio: 0061
:page: 36
:title: Book III § 68: Distance Trisection in a Straight Line

.. _mascheroni-libro-3-sec-68-en:

=======================================================
Book III § 68: Distance Trisection in a Straight Line
=======================================================

.. rubric:: Lorenzo Mascheroni (*The Geometry of the Compass*, Pavia 1797, § 68, pp. 36–37)

.. folio:: 0061

68. *Problem.* To divide the distance :math:`AB` into three equal parts.

*Solution.* With radius :math:`AB` and center :math:`B` (fig. 20), describe circle :math:`BCDE`, and set :math:`AB = BC = CD = DE` (§ 10). Then with center :math:`E` and radius :math:`EC`, describe the indefinite arc :math:`QCPq`. With center :math:`A` and radius :math:`AB`, cut this arc in :math:`P` and :math:`p`. With centers :math:`P` and :math:`p` and with the same radius :math:`AB`, describe two arcs intersecting in :math:`M`. The distance :math:`BM` will be one-third of :math:`AB`. If then with center :math:`M` and the same radius :math:`MB` an arc be described cutting :math:`AB` in :math:`N` toward :math:`A`, the distance :math:`AB` will be divided into three equal parts at points :math:`M` and :math:`N`.

.. picture:: /_static/figures/plates/fig_20.png
   :alt: Mascheroni Fig. 20 (Book III § 68)

*Demonstration.* The point :math:`M` will lie on line :math:`BE` (§ 13). Since :math:`BC = CD = AB`, we have :math:`BD = \sqrt{3} AB` (§ 2); and since :math:`BE = 2 AB` (§ 64), in the right triangle :math:`\triangle BCE` inscribed in the semicircle (Euclid III.31):

.. math::

   (EC)^2 = (BE)^2 - (BC)^2 = 4(AB)^2 - (AB)^2 = 3(AB)^2.

Hence :math:`EP = EC = \sqrt{3} AB`.

Now the two isosceles triangles :math:`\triangle PBE` and :math:`\triangle PBM` are similar, having their base angle at :math:`B` in common (Euclid I.5, I.32; VI.4).

Therefore:

.. math::

   BE : BP = BP : BM.

Consequently :math:`BE \cdot BM = (BP)^2`. With :math:`E` placed at distance :math:`3 AB` along the line:

.. math::

   3 AB \cdot BM = (AB)^2.

Dividing by :math:`AB`, we obtain :math:`3 BM = AB`, or :math:`BM = \frac{1}{3} AB`. Thus :math:`BM` is one-third of :math:`AB`, and :math:`N` marks the second trisection point.
