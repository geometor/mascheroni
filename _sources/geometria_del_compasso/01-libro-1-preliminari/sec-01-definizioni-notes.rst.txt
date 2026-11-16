:layout: book
:type: problem
:order: 1
:folio: 0040
:page: 11
:title: Notes: Definitions & Fundamental Principles

.. _mascheroni-libro-1-sec-1-notes:

============================================
Notes: Definitions & Fundamental Principles
============================================

.. rubric:: Axiomatic Foundations and Historical Precedents

.. folio:: 0040

The Virtual Line as an Ordered Pair
-----------------------------------

Mascheroni establishes the ontological status of the line in compass geometry:
A line is defined and given by an ordered pair of distinct points :math:`(A, B)`. Tracing a continuous graphite or ink stroke is discarded as an unnecessary physical artifact. The intersection of two lines :math:`(A, B)` and :math:`(C, D)` is defined strictly as locating the unique point :math:`S` that would lie on both lines if drawn.

Compass Rigidity vs. Collapsing Compass
---------------------------------------

In Euclid's *Elements* (Book I, Prop. 2 and 3), the compass is historically interpreted as a "collapsing compass" that closes when lifted from the page, requiring Euclid's elaborate auxiliary construction to transfer distances. Mascheroni explicitly adopts the modern rigid divider (*compasso fedele*), where a measured distance :math:`AB` is preserved unchanged across the plane.

Conditioning of Arc Intersections (§ 9)
---------------------------------------

Mascheroni's insistence on near-orthogonal arc crossings anticipates modern numerical condition numbers:
If two circular arcs intersect at angle :math:`\theta`, an uncertainty :math:`\delta r` in the radius produces a positional uncertainty in the intersection point of magnitude:

.. math::

   \delta P \approx \frac{\delta r}{\sin \theta}.

When :math:`\theta \to 0` (tangential glancing intersection), :math:`\delta P \to \infty` and precision collapses. When :math:`\theta = 90^\circ`, :math:`\delta P = \delta r`, yielding maximal stability.

Archival Witness
----------------

* **Facsimile Scan:** Folio ``0040`` (p. 11), Fig. 1 crop embedded (:cite:`mascheroni-1797`).
