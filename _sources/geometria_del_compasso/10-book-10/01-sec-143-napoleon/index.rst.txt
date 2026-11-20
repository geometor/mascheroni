:order: 1
:layout: book
:title: §§ 143–145: Center of a Given Circle (Napoleon's Problem)
:nav_title: §§ 143–145: Napoleon's Problem
:breadcrumb_title: §§ 143–145: Napoleon's Problem
:folio: 0107
:page: 82
:tracks: English: index | Italian: it | Summary: summary | Notes: notes

.. _mascheroni-10-book-10-01-sec-143-napoleon-en:

=========================================================
§§ 143–145: Center of a Given Circle (Napoleon's Problem)
=========================================================

.. folio:: 0107
   :page: 82

**§ 143. Problem (Fig. 71, folio 0107–folio 0108, pp. 82–83).** Find the center :g:`O` of a given circle :g:`( O A )` using the compass alone — celebrated across Europe as :term:`Napoleon's Problem <problema-di-napoleone>`.

*Authentic Mascheroni Construction (direct from folio 0107):*

1. Choose any point :g:`A` on the given circle and an arbitrary compass radius :math:`AB` (greater than a quarter of the diameter and less than the full diameter, with :g:`B` on the given circle). Sweep the semicircle :g:`( A B )` stepping :math:`AB = BC = CD = DE` (:g:`C`, :g:`D`, :g:`E`), and let :g:`M` be the other intersection of semicircle :math:`BCDE` with the given circle.
2. Take chord :math:`EM` as radius and from centers :g:`E` and :g:`A` sweep arcs :g:`( E M )` and :g:`( A L )` intersecting at :g:`L` (:math:`LA = LE = EM`).
3. With the **same radius** :math:`LA = EM` and center :g:`L`, sweep arc :g:`( L Q )` cutting semicircle :math:`BCDE` at :g:`Q`.
4. Then chord :g:`/ B Q /` equals the exact radius :math:`R` of the given circle! Finally, with radius :g:`/ B Q /` and centers :g:`B` and :g:`A`, sweep arcs :g:`( B O )` and :g:`( A O )` intersecting at the exact center :g:`O` (:eq:`/ O A / = / O B / = / B Q /`).

*Proof:* Congruent isosceles triangles :math:`\triangle LAE \cong \triangle LAQ` force :math:`\angle QAB = \angle QLA`, so :math:`\triangle LAQ \sim \triangle ABQ`, giving :math:`EM : EA :: AB : BQ`. Meanwhile in the given circle, :math:`\triangle MAE \sim \triangle OAB` gives :math:`EM : EA :: AB : OB`, hence :math:`BQ = OB = OA = OM = R` identically!

**§§ 144–145 (p. 83, folio 0108).** Once radius :math:`BQ` is found, any two points on the circumference intersect at :math:`O`; in practice, choosing :math:`AB` close to :math:`R` keeps all arc intersections near :math:`90^\circ`.

.. picture:: 0107.g1.svg
   :alt: Calibrated 5-layer vector diagram of Book X § 143 (Fig. 71): Mascheroni's exact third-proportional construction of center O

.. picture:: 0107.g1.png
   :alt: Archival Fig. 71 (folio 0107, p. 82): Mascheroni's authentic compass-only center of a given circle


.. toctree::
   :hidden:

   it
   summary
   notes
