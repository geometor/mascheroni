:layout: book

.. _mascheroni-libro-4-en:

Book IV: Perpendiculars & Parallels by Compass Alone
====================================================

.. rubric:: Lorenzo Mascheroni (*La Geometria del Compasso*, Pavia 1797, §§ 76–80, pp. 40–45)

.. contents:: In This Book
   :local:
   :depth: 2
   :backlinks: none

.. folio:: Perpendicular Lines
   :page: 42

§ 1. Erecting a Perpendicular at a Given Point (§§ 76–77)
---------------------------------------------------------

To erect a perpendicular :math:`DA` to line :math:`(A, B)` at point :math:`A`:

1. Choose an arbitrary radius :math:`r > \frac{1}{2}AB`. Sweep arcs from :math:`A` and :math:`B` intersecting at an auxiliary vertex :math:`C`.
2. With center :math:`C` and radius :math:`CA`, double diameter :math:`BC` across :math:`C` to point :math:`D` via collinear doubling (Book III, § 64).
3. By :person:`Euclid <euclid>` III.31 (an angle inscribed in a semicircle is a right angle), :math:`\angle BAD = 90^\circ`. The virtual line :math:`(D, A)` is strictly perpendicular to :math:`(A, B)`.

*Operation Count*: :math:`6C_1 + 3C_3` (:math:`S = 9, E = 6`, 3 circles, 0 lines).

.. folio:: Perpendicular Foot from an External Point
   :page: 43

§ 2. Dropping a Perpendicular & Finding its Foot (§§ 78–79)
-----------------------------------------------------------

Given line :math:`(A, B)` and an external point :math:`D`:

1. Sweep arc :math:`A(AD)` and arc :math:`B(BD)`. Their opposite intersection :math:`E` is the exact orthogonal reflection of :math:`D` across line :math:`(A, B)`.
2. The virtual line :math:`(D, E)` represents the perpendicular dropped from :math:`D` onto :math:`(A, B)` (:math:`4C_1 + 2C_3, S = 6`).
3. Bisecting the vertical segment :math:`DE` via Book III, § 66 (Solution V) yields point :math:`M`, the exact orthogonal projection (foot of the perpendicular) of :math:`D` onto :math:`(A, B)`!

.. folio:: Parallel Point Construction
   :page: 43

§ 3. Constructing a Parallel Through an External Point (§ 80)
-------------------------------------------------------------

Given line :math:`(A, B)` and an external point :math:`C`, determine a point :math:`D` such that :math:`(C, D) \parallel (A, B)`:

1. With center :math:`B` and radius equal to distance :math:`AC`, sweep arc :math:`B(AC)`.
2. With center :math:`C` and radius equal to distance :math:`AB`, sweep arc :math:`C(AB)`.
3. Let :math:`D` be their intersection on the appropriate side of :math:`C`.

.. picture:: /_static/figures/fig_mascheroni_parallel.svg
   :alt: Mascheroni parallel line construction by compass alone

**Geometric Proof**:
In quadrilateral :math:`ABDC`, the opposite sides are equal by construction: :math:`AB = CD` and :math:`AC = BD`. By Euclid I.34, :math:`ABDC` is a parallelogram. Therefore, the virtual line :math:`(C, D)` is parallel to :math:`(A, B)`.

*Operation Count*: :math:`5C_1 + 2C_3` (:math:`S = 7, E = 5`, 2 circles, 0 lines).

This matches or beats the best ruler-and-compass parallel constructions (such as Tarry's :math:`S = 9`), completely dispensing with straightedge alignment!
