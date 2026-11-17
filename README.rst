GEOMETOR • mascheroni
=====================

**Visit the Online Archive:** https://geometor.github.io/mascheroni/

.. image:: docsrc/_static/figures/fig_mascheroni_inversion.svg
   :alt: GEOMETOR • mascheroni featured geometric construction
   :target: https://geometor.github.io/mascheroni/
   :align: center

**Lorenzo Mascheroni • La Geometria del Compasso • semantic digital archive**

Mission
-------

``geometor/mascheroni`` is part of the interconnected `GEOMETOR <https://geometor.com>`_ semantic digital archive. It preserves Lorenzo Mascheroni's landmark 1797 treatise *La Geometria del Compasso*, which proved the remarkable Mohr–Mascheroni theorem establishing that every planar geometric construction possible with straightedge and compass can be performed using the compass alone. Through addressable semantic units, calibrated theme-adaptive vector diagrams, primary-source folio provenance, and exact symbolic models, Mascheroni's compass-only geometry is integrated into the wider GEOMETOR corpus.

Books in This Archive
---------------------

- **`The Geometry of the Compass <https://geometor.github.io/mascheroni/geometria_del_compasso/>`_** — *La Geometria del Compasso*, demonstrating that all Euclidean planar straightedge-and-compass constructions can be executed with compass alone (Pavia, 1797).

Repository Contents
-------------------

- ``docsrc/`` — RST documentation source, book codex, and Sphinx docs compiled by `PHOTON publish <https://github.com/photon-platform/publish>`_.
- ``resources/`` — Primary-source folios, facsimile page images, and archival apparatus registries.
- ``src/geometor/mascheroni/`` — Python CLI, apparatus tools, and compass-only construction validators.

Local Build & Verification
--------------------------

.. code-block:: bash

   publish build
   uv run --no-sync pytest

Part of the GEOMETOR Knowledge Archive
--------------------------------------

Explore all **74 Book Codices** and **11 Mathematical Catalogs** at https://geometor.com/books/.
