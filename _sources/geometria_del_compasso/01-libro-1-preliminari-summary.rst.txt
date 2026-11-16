:layout: book

.. _mascheroni-libro-1-summary:

Summary: Libro I — Elementary Invariants and the Virtual Line
=============================================================

.. rubric:: Formal Grammar of the Compass Alone and Exact Invariants

1. Operation Ledger
-------------------

.. list-table:: Mascheroni Elementary Operations & Complexity Measures
   :header-rows: 1
   :widths: 25 35 40

   * - Symbol
     - Name
     - Description
   * - :math:`C_1`
     - Determined Point Coincidence
     - Placing compass leg on an already determined point :math:`A`
   * - :math:`C_2`
     - Indeterminate Point Coincidence
     - Placing compass leg on an arbitrary point of a traced arc
   * - :math:`C_3`
     - Arc Tracing
     - Describing a circle or circular arc
   * - :math:`S = m_1 + m_2 + m_3`
     - Simplicity
     - Total number of physical operations
   * - :math:`E = m_1 + m_2`
     - Exactitude
     - Sum of preparatory point alignments (error opportunities)

2. Core Invariant Identities
----------------------------

For any compass-only construction:

.. math::

   S = m_1 + m_2 + m_3, \qquad E = m_1 + m_2, \qquad N_{\text{circles}} = m_3, \qquad N_{\text{lines}} = 0.

3. The Four Fundamental Primitives of Book I
--------------------------------------------

1. **Taking up an interval**: :math:`2C_1` (setting legs on :math:`A` and :math:`B`).
2. **Transferring a radius**: :math:`3C_1 + C_3` (:math:`S = 4`, drawing :math:`C(AB)`).
3. **Intersecting two circles**: :math:`A(R_1) \cap B(R_2)` yields points :math:`P, Q`.
4. **Orthogonal reflection**: Points :math:`P` and :math:`Q` are reflection partners across line :math:`AB`.
