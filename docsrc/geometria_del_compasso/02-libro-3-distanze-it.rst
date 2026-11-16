:layout: book

.. _mascheroni-libro-3-it:

Libro III: Moltiplicazione e Divisione delle Distanze in Linea Retta
====================================================================

.. rubric:: Lorenzo Mascheroni (*La Geometria del Compasso*, Pavia 1797, §§ 64–68, pp. 31–36)

.. contents:: In questo libro
   :local:
   :depth: 2
   :backlinks: none

.. folio:: Raddoppiamento della distanza
   :page: 31

§ 1. Raddoppiare la Distanza AB in Linea Retta (§ 64)
-----------------------------------------------------

.. epigraph::

   « Raddoppiare la distanza :math:`AB` in linea retta mediante la semicirconferenza :math:`BCDE` di raggio :math:`AB` (3 corde eguali a :math:`AB` : :math:`AB = BC = CD = DE`, dunque :math:`AE = 2\,AB`). »

   — :person:`Lorenzo Mascheroni <mascheroni>`, :cite:`mascheroni-1797`, § 64 (p. 31)

**Costruzione**:
1. Col centro :math:`A` e raggio :math:`AB`, si descriva un arco o cerchio :math:`A(AB)`.
2. A partire da :math:`B`, si riporti tre volte consecutivamente la corda di apertura :math:`AB` sulla circonferenza, determinando i punti :math:`C, D, E`.
3. Poiché ogni corda sottende un arco di :math:`60^\circ` nel cerchio di raggio :math:`AB`, i tre archi consecutivi :math:`BC, CD, DE` compiono un semicerchio esatto di :math:`180^\circ`. Il punto :math:`E` giace pertanto sul diametro prolungato per :math:`B` ed :math:`A`, cosicché :math:`E, A, B` sono rigorosamente allineati e la distanza :math:`EB = 2\,AB` (ovvero :math:`AE = AB` dal lato opposto).

*Bilan géométrographique*: :math:`5C_1 + 4C_3` (:math:`S = 9, E = 5`, 4 cerchi, 0 rette).

.. folio:: Bisezione d'una distanza al solo compasso
   :page: 32

§ 2. Dividere per Metà una Distanza Data AB (§ 66, Soluzione V)
---------------------------------------------------------------

.. epigraph::

   « Col raggio :math:`AB`, centro :math:`A` descritta la semicirconferenza :math:`BCDE` (§ 64) ; col centro :math:`E`, raggio :math:`EB` descritto l'arco indefinito :math:`PBp` ; col centro :math:`B`, raggio :math:`BA` tagliando quest'arco in :math:`P` e :math:`p` ; con questi centri :math:`P` e :math:`p`, e collo stesso raggio :math:`BA` si descrivano due archi, che si taglino in :math:`M`. Sarà :math:`M` il punto cercato. »

   — :person:`Lorenzo Mascheroni <mascheroni>`, :cite:`mascheroni-1797`, § 66, Sol. V (p. 33, Fig. 14)

.. picture:: /_static/figures/fig_mascheroni_midpoint.svg
   :alt: Bisezione del segmento AB al solo compasso mediante raddoppiamento in E e archi P, p

**Dimostrazione analitica**:
Posto :math:`A = (0, 0)` e :math:`B = (1, 0)` lungo l'asse delle ascisse:
* Il raddoppiamento fornisce :math:`E = (-1, 0)`, onde :math:`EB = 2`.
* L'arco :math:`E(EB)` ha equazione :math:`(x + 1)^2 + y^2 = 4`.
* Il cerchio :math:`B(BA)` ha centro :math:`(1, 0)` e raggio :math:`1`, equazione :math:`(x - 1)^2 + y^2 = 1`.
* Sottraendo le equazioni: :math:`4x = 3 \implies x = \frac{3}{4}`, onde :math:`y = \pm \frac{\sqrt{15}}{4}` per :math:`P` e :math:`p`.
* Gli archi centrati in :math:`P` e :math:`p` con raggio :math:`BA = 1` hanno equazione :math:`(x - \frac{3}{4})^2 + (y \mp \frac{\sqrt{15}}{4})^2 = 1`.
* Intersecandosi sull'asse delle ascisse (:math:`y = 0`): :math:`(x - \frac{3}{4})^2 + \frac{15}{16} = 1 \implies (x - \frac{3}{4})^2 = \frac{1}{16} \implies x = \frac{3}{4} \pm \frac{1}{4}`.
* La radice :math:`x = \frac{3}{4} - \frac{1}{4} = \frac{1}{2}` cade esattamente a metà tra :math:`A(0, 0)` e :math:`B(1, 0)`: **il punto M è il perfetto punto medio di AB**! (La seconda radice :math:`x = 1` coincide con :math:`B`).

*Bilan géométrographique*: :math:`10C_1 + 7C_3` (:math:`S = 17, E = 10`, 7 cerchi, 0 rette).

.. folio:: Suddivisione e trisezione
   :page: 34

§ 3. Suddivisione all'Infinito e Trisezione (§§ 67–68)
------------------------------------------------------

* **§ 67. Suddivisione continua**: Ripetendo la Soluzione V sulla distanza :math:`AM`, si ottiene il punto :math:`N` (quarto di :math:`AB`), indi :math:`O` (ottavo), e così via all'infinito con la più rigorosa economia di archi.
* **§ 68. Trisezione di AB**: Mediante cerchi ausiliari di raggio doppio e triplo (§ 64), si determina la terza parte della distanza :math:`AB` senza tracciare alcuna retta secante.
