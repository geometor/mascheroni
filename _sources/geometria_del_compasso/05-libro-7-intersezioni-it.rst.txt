:layout: book

.. _mascheroni-libro-7-it:

Libro VII: Intersezione delle Rette cogli Archi di Cerchio e tra Loro
=====================================================================

.. rubric:: Lorenzo Mascheroni (*La Geometria del Compasso*, Pavia 1797, §§ 110–112, pp. 60–63)

.. contents:: In questo libro
   :local:
   :depth: 2
   :backlinks: none

.. folio:: 0085
   :page: 60

§ 1. Intersezione di una Retta con un Cerchio (§§ 110–111)
----------------------------------------------------------

.. epigraph::

   « § 110–111. Dato un arco :math:`BCD` descritto col centro :math:`A`, trovare i due punti dove taglia la circonferenza una retta data per due punti (p. 60–61, Fig. 46–48). »

   — :person:`Lorenzo Mascheroni <mascheroni>`, :cite:`mascheroni-1797`, § 110 (p. 60)

**Caso generale (la retta non passa pel centro A)**:
1. Siano dati il cerchio :math:`\Gamma = A(R)` e la retta virtuale :math:`(P, Q)`.
2. Si trovi il punto :math:`A'`, simmetrico ortogonale del centro :math:`A` rispetto alla retta :math:`(P, Q)` (§ 78), mediante gli archi :math:`P(PA)` e :math:`Q(QA)` che si tagliano in :math:`A'`.
3. Col centro :math:`A'` e lo stesso raggio :math:`R = A B`, si descriva il cerchio :math:`\Gamma' = A'(R)`.
4. Poiché :math:`(P, Q)` è l'asse di simmetria ortogonale tra i centri :math:`A` ed :math:`A'`, i punti d'intersezione :math:`X, Y` tra il cerchio dato :math:`\Gamma` e il cerchio riflesso :math:`\Gamma'` giacciono rigorosamente sulla retta :math:`(P, Q)`!
5. Pertanto :math:`X` e :math:`Y` sono i due punti esatti in cui la retta :math:`(P, Q)` taglia il cerchio :math:`\Gamma`, trovati con soli archi di cerchio!

.. folio:: 0086
   :page: 61

§ 2. Intersezione di Due Rette tra Loro (§ 112)
-----------------------------------------------

.. epigraph::

   « § 112. Dati due punti :math:`A, B` d'una retta (Fig. 49 e 50), e due punti :math:`C, D` d'una altra ; trovare il punto :math:`S` dove si tagliano (p. 61–63 : symétriques :math:`c, d` de :math:`C, D` par rapport à :math:`AB`, quarto vertice :math:`\delta` del parallelogrammo :math:`CDd\delta`, quarta proporzionale a :math:`c\delta, CD, Cc` dando il raggio :math:`CS = cS`). »

   — :person:`Lorenzo Mascheroni <mascheroni>`, :cite:`mascheroni-1797`, § 112 (p. 61)

**Metodo di Mascheroni**:
1. Si riflettono i punti :math:`C` e :math:`D` rispetto alla retta :math:`(A, B)` (§ 78), ottenendo i punti simmetrici :math:`c` e :math:`d`.
2. Si costruisce il quarto vertice :math:`\delta` del parallelogrammo :math:`CDd\delta` (§ 80).
3. Mediante la quarta proporzionale (Libro V, § 93), si determina la distanza :math:`CS = cS`:

   .. math::

      CS = \frac{CD \cdot Cc}{c\delta}.

4. Gli archi centrati in :math:`C` e :math:`c` col raggio :math:`CS` si tagliano nel punto :math:`S`. Il punto :math:`S` giace contemporaneamente su :math:`(C, D)` e sull'asse di simmetria :math:`(A, B)`, essendo dunque l'esatta intersezione delle due rette!

.. folio:: 0088
   :page: 63

§ 3. Il Functor di Inversione di August Adler (1890)
----------------------------------------------------

Nel 1890, il geometra :person:`August Adler <adler>` (:cite:`adler-1890`) unificò l'intero Libro VII mediante l':term:`inversione circolare <inversione>` (:math:`5C_1 + 3C_3, S = 8`, Problème XXXVIII di :person:`Lemoine <lemoine>`):

.. picture:: /_static/figures/fig_mascheroni_inversion.svg
   :alt: Inversione circolare al solo compasso (Adler 1890)

* L'inversione rispetto a un polo :math:`O` trasforma ogni retta non passante per :math:`O` in un cerchio passante per :math:`O`.
* L'intersezione di due rette si trasforma nell'intersezione di due cerchi passanti per :math:`O` (che si tagliano in :math:`O` e nel punto inverso :math:`S'`).
* Invertendo nuovamente :math:`S'`, si ottiene il punto d'intersezione :math:`S` al solo compasso con la più sublime concisione concettuale!
