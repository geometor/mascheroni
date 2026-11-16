:layout: book

.. _mascheroni-libro-5-en:

Book V: Proportional Distances by Compass Alone
===============================================

.. rubric:: Lorenzo Mascheroni (*La Geometria del Compasso*, Pavia 1797, §§ 86–96, pp. 46–50)

.. contents:: In This Book
   :local:
   :depth: 2
   :backlinks: none

.. folio:: 0071
   :page: 46

§ 1. Third Proportional via Concentric Circles (§ 86)
-----------------------------------------------------

To construct the third proportional :math:`x` to two given distances :math:`a` and :math:`b` (:math:`a : b = b : x \implies x = b^2/a`):

1. Choose an arbitrary point :math:`O` as center and describe two concentric circles :math:`\Gamma_a = O(a)` and :math:`\Gamma_b = O(b)`.
2. On circle :math:`\Gamma_a`, lay off chord :math:`AB = b`.
3. Rays from center :math:`O` through :math:`A` and :math:`B` meet the smaller circle :math:`\Gamma_b` at points :math:`a` and :math:`b`.
4. By similarity of isosceles triangles :math:`\triangle OAB \sim \triangle Oab`:

   .. math::

      \frac{OA}{Oa} = \frac{AB}{ab} \implies \frac{a}{b} = \frac{b}{ab} \implies ab = \frac{b^2}{a}.

The chord :math:`ab` is the required third proportional.

.. folio:: 0073
   :page: 48

§ 2. The Concentric Fourth Proportional (§ 93)
----------------------------------------------

Given three segments :math:`a, b, c` (with :math:`c \le 2a`):

1. From a common center :math:`O`, sweep concentric circles :math:`O(a)` and :math:`O(b)`.
2. In circle :math:`O(a)`, place chord :math:`BC = c`.
3. Transfer equal subtended arcs :math:`BD = CE` onto circle :math:`O(b)`.
4. Chord :math:`DE` subtends the exact central angle :math:`\angle DOE = \angle BOC`.

.. math::

   \frac{OD}{OB} = \frac{DE}{BC} \implies \frac{b}{a} = \frac{DE}{c} \implies DE = \frac{b \cdot c}{a}.

As :person:`Gaetano Fazzari <fazzari>` emphasized in his 1901 centenary preface (p. xi), this 4-circle construction (:math:`S = 14`) is dramatically more compact than standard ruler-and-compass Thales configurations, which require drawing multiple secants and parallel lines with high alignment overhead.

.. folio:: 0074
   :page: 49

§ 3. Dividing a Segment in Given Proportions (§ 96)
---------------------------------------------------

To divide segment :math:`MN` internally at point :math:`P` such that :math:`MP : PN = p : q`:

1. Find the fourth proportional :math:`x = \frac{p \cdot MN}{p + q}` using § 93.
2. With center :math:`M` and radius :math:`x`, sweep an arc.
3. With center :math:`N` and radius :math:`MN - x`, sweep an arc meeting the previous arc at :math:`P`.
4. Point :math:`P` partitions the virtual line :math:`(M, N)` in the exact requested ratio.
