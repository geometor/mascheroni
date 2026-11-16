:layout: book

.. _mascheroni-libro-4-it:

Libro IV: Perpendicolari e Parallele al Solo Compasso
=====================================================

.. rubric:: Lorenzo Mascheroni (*La Geometria del Compasso*, Pavia 1797, §§ 76–80, pp. 40–45)

.. contents:: In questo libro
   :local:
   :depth: 2
   :backlinks: none

.. folio:: 0067
   :page: 42

§ 1. Perpendicolare in un Estremo o per un Punto Dato (§§ 76–77)
----------------------------------------------------------------

.. epigraph::

   « § 76. Dati i due punti :math:`A` e :math:`B` ; trovare un punto :math:`H` tale, che la retta :math:`BH` sia perpendicolare alla :math:`AB` in :math:`B` ed eguale ad una data :math:`CD` (p. 42, Fig. 26). »

   « § 77. Dati i due punti :math:`A` e :math:`B` ; trovare un punto :math:`D` in guisa, che la :math:`DA` sia perpendicolare alla :math:`AB` (p. 42–43, Fig. 27). »

**Soluzione di Mascheroni (§ 77)**:
1. Con un raggio arbitrario :math:`r > \frac{1}{2}AB`, si descrivano due archi coi centri :math:`A` e :math:`B` che si taglino in :math:`C`.
2. Col centro :math:`C` e raggio :math:`CA`, si descriva la semicirconferenza :math:`BAD` (§ 64) prolungando il diametro :math:`BC` in :math:`D`.
3. L'angolo inscritto nel semicerchio :math:`\angle BAD` è retto per la Prop. 31 del Libro III di :person:`Euclide <euclid>`. Pertanto la congiungente virtuale :math:`DA` è perpendicolare alla :math:`AB` nel punto :math:`A`!

*Bilan géométrographique*: :math:`6C_1 + 3C_3` (:math:`S = 9, E = 6`, 3 cerchi, 0 rette).

.. folio:: 0068
   :page: 43

§ 2. Perpendicolare da un Punto Esterno e Piede della Perpendicolare (§§ 78–79)
-------------------------------------------------------------------------------

.. epigraph::

   « § 78. Dati i due estremi d'una retta :math:`AB` e un punto :math:`D` fuori di essa, trovare un altro punto :math:`E` (Fig. 28), che determini la posizione della :math:`DE` perpendicolare alla :math:`AB`, e il punto :math:`M`, dove la taglia.

   *Soluzione*: Si faccia ad :math:`AD = AE`, a :math:`BD = BE` (§ 11). Sarà :math:`E` il primo punto cercato [simmetrico ortogonale di :math:`D` rispetto ad :math:`AB`]. Si divida :math:`DE` per metà in :math:`M` (§ 66). Sarà :math:`M` il secondo [piede della perpendicolare]. »

   — :person:`Lorenzo Mascheroni <mascheroni>`, :cite:`mascheroni-1797`, § 78 (p. 43)

* Costruire il punto simmetrico :math:`E` esige :math:`4C_1 + 2C_3` (:math:`S = 6, E = 4`, 2 cerchi).
* Trovare il piede :math:`M` mediante bisezione (§ 66, Sol. V) su :math:`DE` aggiunge :math:`10C_1 + 7C_3` (:math:`S = 17`), risolvendo interamente la proiezione ortogonale.

.. folio:: 0068
   :page: 43

§ 3. Parallela per un Punto Fuori della Retta (§ 80)
----------------------------------------------------

.. epigraph::

   « § 80. Dati due punti :math:`A` e :math:`B` d'una retta, e un punto :math:`C` fuori di essa (Fig. 29), pel quale si voglia condurre una parallela alla :math:`AB` ; trovare un altro punto :math:`D`, che ne determini la posizione.

   *Soluzione*: Si faccia a :math:`CA = BD` (§ 11) ; :math:`BA = CD`. Sarà :math:`D` il punto cercato. »

   — :person:`Lorenzo Mascheroni <mascheroni>`, :cite:`mascheroni-1797`, § 80 (p. 43)

.. picture:: /_static/figures/fig_mascheroni_parallel.svg
   :alt: Costruzione della retta parallela al solo compasso in due archi

**Dimostrazione**:
Nel quadrilatero :math:`ABDC`, i lati opposti sono eguali per costruzione: :math:`AB = CD` e :math:`AC = BD`. Per la Prop. 34 del Libro I di Euclide, :math:`ABDC` è un parallelogrammo, onde la retta virtuale :math:`(C, D)` è rigorosamente parallela alla retta virtuale :math:`(A, B)`.

*Bilan géométrographique*: :math:`5C_1 + 2C_3` (:math:`S = 7, E = 5`, 2 cerchi, 0 rette).
