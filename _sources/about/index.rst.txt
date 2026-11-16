:navigation: header
:order: 10

=====
About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

the Italian geometer whose 1797 La Geometria del Compasso proved that every Euclidean construction can be executed with the compass alone

Primary Digital Scriptorium codex for *La Geometria del Compasso* (Lorenzo Mascheroni), structured under :ref:`geometria_del_compasso-index` with prosopographical and bibliographic apparatus in :ref:`persons` and :ref:`bibliography`.


The GEOMETOR Mission
--------------------

The GEOMETOR project, directed by **phi ARCHITECT**, is dedicated to the systematic recovery, exact formalization, and dynamic re-expression of foundational geometric and philosophical knowledge:

- **Extracting Historical Semantic Knowledge**: Recovering the deductive structure of classical geometric, axiomatic, and philosophical treatises—elevating verbatim primary prose, primary-source folio scans (``publish folio``), and calibrated ``.euclid-graphic`` diagrams into addressable semantic graphs.
- **Exact Symbolic Grounding (``geometor.model``)**: Anchoring geometric constructions in 100% exact symbolic algebra (``SymPy``) and Rational Trigonometry invariants over closed-form radical fields.
- **Repurposing Knowledge Across Mediums**: Deploying extracted structures across multi-track **Book Codices**, EPUB 3 editions, computable canons, interactive SVG laboratories, and visual broadcasts.

Sources, Provenance & Repository Architecture
---------------------------------------------

- **Python Package**: ``src/geometor/mascheroni/`` (Python 3.13)
- **Codex Edition Track**: ``docsrc/geometria_del_compasso/`` (``:layout: book``)
- **Edition Structure Map**: ``resources/geometria_del_compasso/structure_map.json``
- **Archival PDFs & Folios**: ``resources/geometria_del_compasso/pdfs/`` (parsed via ``publish folio-ingest``)
- **Scholarly Apparatus**: ``resources/persons.json``, ``resources/citations.json``, ``resources/glossary.json``
- **Automated Verification**: ``tests/`` (``pytest`` + ``ruff``) and ``docsrc/`` (``publish build``)
