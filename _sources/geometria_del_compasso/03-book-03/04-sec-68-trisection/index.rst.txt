:order: 4
:layout: book
:title: § 68: Exact Distance Trisection
:nav_title: § 68: Distance Trisection
:breadcrumb_title: § 68: Distance Trisection
:folio: 0061
:page: 36
:tracks: English: index | Italian: it | Summary: summary | Notes: notes

.. _mascheroni-03-book-03-04-sec-68-trisection-en:
.. _mascheroni-libro-3-sec-68-en:

===============================
§ 68: Exact Distance Trisection
===============================

.. folio:: 0061
   :page: 36

**§ 68. Problem (Fig. 20).** Divide a given straight distance :math:`AB` into three equal parts using the compass alone.

*Authentic Mascheroni Construction (folio 0061–folio 0062, pp. 36–37):*

1. Using § 64, extend :math:`AB` collinearly by :math:`AB` on **both sides** to :g:`E` (:math:`EA = AB`) and :g:`V` (:math:`BV = AB`), producing the triple span :math:`EV = 3\,AB`.
2. With center :g:`V` and radius :math:`VE = 3\,AB`, sweep arc :g:`( V E )`; with center :g:`E` and radius :math:`EB = 2\,AB`, sweep arc :g:`( E B )`. Let them intersect at :g:`F` and :g:`f`.
3. With centers :g:`F` and :g:`f` and radius :math:`FE = 2\,AB`, sweep arcs :g:`( F E )` and :g:`( f E )`, intersecting at :g:`E` and at the trisection point :g:`T`.

*Exact Proof:* Set :math:`E = (-1,0)`, :math:`A = (0,0)`, :math:`B = (1,0)`, :math:`V = (2,0)`. Intersecting :math:`(x-2)^2 + y^2 = 9` with :math:`(x+1)^2 + y^2 = 4` gives :math:`-6x + 3 = 5 \implies x_F = -\frac{1}{3}` and :math:`y_F = \pm\frac{4\sqrt{2}}{3}`. Because :math:`F` and :math:`f` reflect :math:`E(-1,0)` across :math:`x = -\frac{1}{3}`, :math:`x_T = 2(-\frac{1}{3}) - (-1) = +\frac{1}{3}`! Thus :g:`/ A T /` :math:`= \frac{1}{3}AB`, and the symmetric reflection from :g:`V` locates :g:`t` (:math:`x_t = \frac{2}{3}`), yielding :eq:`/ A T / = / T t / = / t B /`.

.. picture:: 0061.g1.svg
   :alt: Calibrated 5-layer vector diagram of Book III § 68 (Fig. 20): authentic compass trisection AT = Tt = tB = AB/3

.. picture:: 0061.g1.png
   :alt: Archival Fig. 20 (folio 0061, p. 36): Mascheroni's exact compass-only trisection of AB


.. toctree::
   :hidden:

   it
   summary
   notes
