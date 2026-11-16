:layout: book
:type: problem
:order: 3
:folio: 0060
:page: 34
:title: Book III § 67: Repeated Binary Distance Subdivision

.. _mascheroni-libro-3-sec-67-en:

=======================================================
Book III § 67: Repeated Binary Distance Subdivision
=======================================================

.. rubric:: Lorenzo Mascheroni (*The Geometry of the Compass*, Pavia 1797, § 67, pp. 34–35)

.. folio:: 0060

67. *Problem.* To continue to subdivide into two equal parts with the simplest construction (fig. 18 and 19), :math:`AM` into :math:`N`, :math:`AN` into :math:`O`, and so on to infinity.

.. picture:: /_static/figures/plates/fig_19.png
   :alt: Mascheroni Fig. 19 (Book III § 67)

*Solution.* Semicircle :math:`BCDE` having been described with radius :math:`AB` (§ 64), and with the same radius and center :math:`B` the indefinite arc :math:`P'CAp'`; with centers :math:`E` and :math:`B` and radius :math:`BE` the two arcs :math:`R'Q'P'Bp'q'r'`, :math:`PQRERqp`; with center :math:`E` and radius :math:`EC` the arc :math:`PCp`; if with centers :math:`P'` and :math:`p'` and radius :math:`AB` two arcs be described, they will intersect in :math:`M` at the midpoint of :math:`AB` (Sol. V, § 66).

Now set :math:`AP' = BQ' = Bq' = q'N = Q'N` (§ 11). The point :math:`N` will be at the midpoint of :math:`AM`.

Set :math:`AQ' = BR' = Br' = r'O = R'O`. The point :math:`O` will be at the midpoint of :math:`AN`.

Continuing by the same method, one would divide :math:`AO` into two equal parts, and so forth to infinity.

*Demonstration.* Imagine a line :math:`P'A` bisecting the base :math:`BE` of triangle :math:`\triangle P'BE` (§ 12). By Apollonius' median theorem (§ 26):

.. math::

   (BP')^2 + (P'E)^2 = 2(AB)^2 + 2(AP')^2.

Substituting the known values :math:`BP' = AB` and :math:`P'E = 2AB`, and subtracting :math:`2(AB)^2`, we obtain :math:`3(AB)^2 = 2(AP')^2`, whence:

.. math::

   (AP')^2 = (BQ')^2 = \frac{3}{2}(AB)^2.

Furthermore, point :math:`N` lies on line :math:`BE` (§ 13). The isosceles triangle :math:`\triangle Q'BN` is similar to the isosceles triangle :math:`\triangle Q'BE` by virtue of their common angle at :math:`B` (Euclid I.5, I.32; VI.4). Comparing the two expressions for :math:`(BQ')^2`:

.. math::

   \frac{3}{2}(AB)^2 = BN \cdot BE = 2 BN \cdot AB.

Dividing by :math:`2 AB` yields :math:`BN = \frac{3}{4} AB`, so that :math:`AN = \frac{1}{4} AB`. This proves that :math:`N` is the exact midpoint of :math:`AM`.
