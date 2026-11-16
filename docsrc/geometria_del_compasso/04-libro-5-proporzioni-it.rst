:layout: book

.. _mascheroni-libro-5-it:

Libro V: Delle Distanze Proporzionali al Solo Compasso
======================================================

.. rubric:: Lorenzo Mascheroni (*La Geometria del Compasso*, Pavia 1797, §§ 86–96, pp. 46–50)

.. contents:: In questo libro
   :local:
   :depth: 2
   :backlinks: none

.. folio:: Terza proporzionale
   :page: 46

§ 1. Terza Proporzionale a Due Distanze Date (§ 86)
---------------------------------------------------

.. epigraph::

   « § 86. Trovare una terza proporzionale alle due distanze :math:`Qp`, :math:`MN`, delle quali la prima :math:`Qp` è maggiore della seconda :math:`MN` (p. 46, Fig. 35 : cercles concentriques / corde d'arc). »

   — :person:`Lorenzo Mascheroni <mascheroni>`, :cite:`mascheroni-1797`, § 86 (p. 46)

**Costruzione mediante cerchi concentrici**:
1. Con un centro arbitrario :math:`O`, si descrivano due cerchi concentrici :math:`\Gamma_1` e :math:`\Gamma_2` coi raggi :math:`R_1 = Qp` ed :math:`R_2 = MN`.
2. Sopra la circonferenza maggiore :math:`\Gamma_1`, si prenda una corda :math:`AB` eguale alla seconda distanza :math:`MN`.
3. Dai punti :math:`A` e :math:`B` si conducano i raggi verso il centro :math:`O`, i quali intersecano la circonferenza minore :math:`\Gamma_2` nei punti :math:`a` e :math:`b`.
4. Per similitudine dei triangoli isosceli :math:`\triangle OAB \sim \triangle Oab`:

   .. math::

      \frac{OA}{Oa} = \frac{AB}{ab} \implies \frac{Qp}{MN} = \frac{MN}{ab} \implies ab = \frac{MN^2}{Qp}.

La corda :math:`ab` è la rigorosa terza proporzionale cercata!

.. folio:: Quarta proporzionale per cerchi concentrici
   :page: 48

§ 2. Quarta Proporzionale a Tre Distanze Date (§ 93)
----------------------------------------------------

.. epigraph::

   « § 93. Trovare una quarta proporzionale a tre distanze date :math:`PQ`, :math:`RS`, :math:`TV` (p. 48–49 : cercles concentriques de centre :math:`O` et rayons :math:`PQ`, :math:`RS`). »

   — :person:`Lorenzo Mascheroni <mascheroni>`, :cite:`mascheroni-1797`, § 93 (p. 48)

Siano date le tre grandezze :math:`a = PQ`, :math:`b = RS`, :math:`c = TV` con :math:`c \le 2a`:
1. Con centro comune :math:`O`, si descrivano due cerchi concentrici :math:`O(a)` di raggio :math:`a` ed :math:`O(b)` di raggio :math:`b`.
2. Sul cerchio :math:`O(a)`, si collochi la corda :math:`BC = c`.
3. Con un'apertura di compasso arbitraria o uguale, si trasportino gli archi eguali :math:`BD = CE` sul cerchio concentrico :math:`O(b)`.
4. La corda :math:`DE` sottende l'angolo al centro :math:`\angle DOE = \angle BOC`.

Per la similitudine dei triangoli :math:`\triangle ODE \sim \triangle OBC`:

.. math::

   \frac{OD}{OB} = \frac{DE}{BC} \implies \frac{b}{a} = \frac{DE}{c} \implies DE = \frac{b \cdot c}{a}.

Questa celebre costruzione compie la quarta proporzionale in appena **4 cerchi** (:math:`S = 14`), celebrata da :person:`Gaetano Fazzari <fazzari>` (1901, p. xi) come notevolmente più rapida e precisa di qualsiasi costruzione euclidea con riga e fascio di rette parallele!

.. folio:: Divisione proporzionale d'un segmento
   :page: 49

§ 3. Divisione Proporzionale delle Distanze (§ 96)
--------------------------------------------------

* **§ 96. Dividere :math:`MN` in parti proporzionali**: Data la distanza :math:`MN`, trovare su di essa il punto :math:`P` tale che :math:`MP : PN = PQ : RS`.
* Applicando la quarta proporzionale (§ 93) colla distanza totale :math:`PQ + RS`, la posizione del punto interno :math:`P` viene individuata direttamente intersecando gli archi centrati in :math:`M` ed :math:`N`.
