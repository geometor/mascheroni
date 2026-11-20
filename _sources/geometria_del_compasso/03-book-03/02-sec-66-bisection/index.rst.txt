:order: 2
:layout: book
:title: § 66: Segment Bisection Without Straightedge
:nav_title: § 66: Segment Bisection
:breadcrumb_title: § 66: Segment Bisection
:folio: 0057
:page: 32
:tracks: English: index | Italian: it | Summary: summary | Notes: notes

.. _mascheroni-03-book-03-02-sec-66-bisection-en:
.. _mascheroni-libro-3-sec-66-en:

============================================
§ 66: Segment Bisection Without Straightedge
============================================

.. folio:: 0057
   :page: 32

**§ 66. Problem (Fig. 17).** Bisect a given distance :math:`AB` (find exact midpoint :g:`M` collinear with :g:`A` and :g:`B`) using the compass alone.

Mascheroni presents five distinct compass-only solutions (pp. 32–34, folio 0057–folio 0059), of which **Solution V** is the enduring canonical benchmark of :term:`Mascheroni midpoint bisection <bisezione-mascheroni>`:

1. Double :math:`BA` past :g:`A` to collinear point :g:`E` via § 64 (:math:`EA = AB`, :math:`EB = 2\,AB`).
2. Sweep circle :g:`( B A )` of radius :math:`AB` and arc :g:`( E B )` of radius :math:`EB = 2\,AB`, intersecting at symmetric points :g:`P` and :g:`p`.
3. With centers :g:`P` and :g:`p` and radius :math:`PB = AB`, sweep arcs :g:`( P B )` and :g:`( p B )`. They intersect at :g:`B` and at the exact midpoint :g:`M` of segment :math:`AB` (:eq:`/ A M / = / M B /`).

*Exact Verification:* With :math:`A = (0,0)`, :math:`B = (1,0)`, and :math:`E = (-1,0)`, intersecting :math:`(x+1)^2 + y^2 = 4` with :math:`(x-1)^2 + y^2 = 1` gives :math:`4x = 3 \implies x_P = \frac{3}{4}` and :math:`y_P = \pm\frac{\sqrt{15}}{4}`. Reflecting :math:`B(1,0)` across :math:`x = \frac{3}{4}` yields :math:`x_M = 2(\frac{3}{4}) - 1 = \frac{1}{2}`, so :math:`M = (\frac{1}{2}, 0)` identically!

.. picture:: 0058.g1.svg
   :alt: Calibrated 5-layer vector diagram of Book III § 66 (Sol. V): midpoint M of AB in 7 circles (10C₁ + 7C₃)

.. picture:: 0058.g1.png
   :alt: Archival Fig. 17 (folio 0058, p. 33): Mascheroni's classic compass-only midpoint construction


.. toctree::
   :hidden:

   it
   summary
   notes
