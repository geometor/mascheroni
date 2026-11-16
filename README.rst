==========
mascheroni
==========

the Italian geometer whose 1797 La Geometria del Compasso proved that every Euclidean construction can be executed with the compass alone

Edition Overview
----------------

- **Treatise**: *La Geometria del Compasso*
- **Author**: Lorenzo Mascheroni
- **Primary Edition Track**: ``docsrc/geometria_del_compasso/`` (``:layout: book``)
- **Apparatus**: ``resources/persons.json``, ``resources/citations.json``, ``resources/glossary.json``
Installation & Verification
---------------------------

Managed with ``uv`` on Python 3.13:

.. code-block:: bash

   uv run --no-sync pytest
   ruff check src tests demos
   publish build

Usage
-----

.. code-block:: bash

   mascheroni --help

Links
-----

- **Documentation**: https://geometor.github.io/mascheroni
- **Repository**: https://github.com/geometor/mascheroni
- **Issues**: https://github.com/geometor/mascheroni/issues

License
-------

Licensed under the MIT License. See ``LICENSE`` for details.
