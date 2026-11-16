:layout: book
:type: problem
:order: 1
:folio: 0057
:page: 31
:title: Notes: Linear Distance Doubling

.. _mascheroni-libro-3-sec-64-notes:

====================================
Notes: Linear Distance Doubling
====================================

.. rubric:: Symbolic Verification and Hexagonal Symmetries

.. folio:: 0057

SymPy Coordinate Verification
-----------------------------

In Cartesian coordinates, let :math:`A = (0, 0)` and :math:`B = (1, 0)`.
Then:

.. math::

   C = \left(\frac{1}{2}, \frac{\sqrt{3}}{2}\right), \quad D = \left(-\frac{1}{2}, \frac{\sqrt{3}}{2}\right), \quad E = (-1, 0).

The distance from :math:`B` to :math:`E` is :math:`2`, and the vector :math:`\vec{AE} = (-1, 0) - (0, 0) = -1 \cdot \vec{AB}`.
The library implementation in :func:`geometor.mascheroni.collinear_doubling` verifies:

.. code-block:: python

   import sympy as sp
   from geometor.mascheroni import collinear_doubling

   a = sp.Point2D(0, 0)
   b = sp.Point2D(1, 0)
   e = collinear_doubling(a, b)
   assert e == sp.Point2D(-1, 0)
   assert b.distance(e) == 2 * a.distance(b)

Significance in Compass Geometry
--------------------------------

Collinear doubling is the arithmetic engine of compass geometry. Because straight lines cannot be prolonged with a ruler, linear extension is accomplished by stepping along circumferences. By repeating § 64, any integer multiple :math:`k \cdot AB` is constructed along the ray.

Archival Witness
----------------

* **Facsimile Scan:** Folio ``0057`` (p. 31), Editio Princeps (:cite:`mascheroni-1797`).
