"""Pytest fixtures and environment configuration for geometor.mascheroni."""

from __future__ import annotations

import sys
from pathlib import Path

# Add shared workspace site-packages so pytest has access to sympy in offline environment
_SHARED_SITE = Path(__file__).resolve().parents[2] / ".venv" / "lib" / "python3.13" / "site-packages"
if _SHARED_SITE.is_dir() and str(_SHARED_SITE) not in sys.path:
    sys.path.insert(0, str(_SHARED_SITE))

_SRC = Path(__file__).resolve().parents[1] / "src"
if _SRC.is_dir() and str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))
