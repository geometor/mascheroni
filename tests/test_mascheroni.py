"""Comprehensive test suite for ``geometor.mascheroni`` (1797)."""

from __future__ import annotations

import json
from pathlib import Path
import xml.etree.ElementTree as ET
import pytest
import sympy as sp

from geometor.mascheroni import (
    OpCount,
    __version__,
    circle_circle_intersection,
    collinear_doubling,
    concentric_fourth_proportional,
    mascheroni_inversion,
    mascheroni_midpoint,
    mascheroni_parallel_point,
    mascheroni_reflect_point,
    run,
)

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_version_and_cli() -> None:
    """Verify initial semantic version and clean zero-argument CLI execution."""
    assert __version__ == "0.1.0"
    assert run([]) == 0


def test_cli_help_exits_cleanly() -> None:
    """Verify ``--help`` exits cleanly with code ``0``."""
    with pytest.raises(SystemExit) as exc_info:
        run(["--help"])
    assert exc_info.value.code == 0


def test_opcount_algebra_validation() -> None:
    """Test OpCount creation, validation, and error detection."""
    valid = OpCount.create(c1=10, c2=0, c3=7)
    assert valid.s == 17
    assert valid.e == 10
    assert valid.circles == 7
    assert valid.validate() == []

    bad_s = OpCount(c1=10, c2=0, c3=7, s=20, e=10, circles=7, symbol="10C_1 + 7C_3")
    assert any("Simplicity mismatch" in msg for msg in bad_s.validate())

    bad_e = OpCount(c1=10, c2=0, c3=7, s=17, e=12, circles=7, symbol="10C_1 + 7C_3")
    assert any("Exactitude mismatch" in msg for msg in bad_e.validate())

    bad_c = OpCount(c1=10, c2=0, c3=7, s=17, e=10, circles=6, symbol="10C_1 + 7C_3")
    assert any("Circle count mismatch" in msg for msg in bad_c.validate())


def test_collinear_doubling_exact() -> None:
    """Verify Libro III § 64 collinear doubling."""
    a = sp.Point2D(0, 0)
    b = sp.Point2D(1, 0)
    e = collinear_doubling(a, b)
    assert e == sp.Point2D(-1, 0)
    assert b.distance(e) == 2 * a.distance(b)


def test_mascheroni_midpoint_exact() -> None:
    """Verify Libro III § 66 Solution V bisection without straightedge."""
    a = sp.Point2D(0, 0)
    b = sp.Point2D(1, 0)
    m = mascheroni_midpoint(a, b)
    assert m == sp.Point2D(sp.Rational(1, 2), 0)
    assert a.distance(m) == b.distance(m)

    # General position points with exact radicals
    a2 = sp.Point2D(2, 4)
    b2 = sp.Point2D(6, 8)
    m2 = mascheroni_midpoint(a2, b2)
    assert m2 == sp.Point2D(4, 6)


def test_mascheroni_parallel_point_exact() -> None:
    """Verify Libro IV § 80 parallel point construction."""
    a = sp.Point2D(0, 0)
    b = sp.Point2D(3, 0)
    c = sp.Point2D(1, 2)
    d = mascheroni_parallel_point(a, b, c)
    assert d == sp.Point2D(4, 2)
    # Vectors AB and CD must be equal
    assert (b.x - a.x, b.y - a.y) == (d.x - c.x, d.y - c.y)


def test_mascheroni_reflect_point_exact() -> None:
    """Verify Libro IV § 78 orthogonal reflection across virtual line."""
    a = sp.Point2D(0, 0)
    b = sp.Point2D(2, 0)
    p = sp.Point2D(1, 3)
    p_refl = mascheroni_reflect_point(a, b, p)
    assert p_refl == sp.Point2D(1, -3)


def test_mascheroni_inversion_exact() -> None:
    """Verify Libro VII circular inversion (Adler 1890)."""
    o = sp.Point2D(0, 0)
    r = sp.Integer(3)
    p = sp.Point2D(9, 0)
    p_inv = mascheroni_inversion(o, r, p)
    assert p_inv == sp.Point2D(1, 0)
    # OP * OP' = R^2
    assert o.distance(p) * o.distance(p_inv) == r**2


def test_concentric_fourth_proportional_exact() -> None:
    """Verify Libro V § 93 fourth proportional."""
    a = sp.Integer(4)
    b = sp.Integer(12)
    c = sp.Integer(7)
    x = concentric_fourth_proportional(a, b, c)
    assert x == sp.Integer(21)


def test_apparatus_json_validity() -> None:
    """Verify JSON structure and required keys for apparatus files."""
    res_dir = REPO_ROOT / "resources"

    persons = json.loads((res_dir / "persons.json").read_text(encoding="utf-8"))
    assert "mascheroni" in persons
    assert "bonaparte" in persons
    assert "mohr" in persons
    assert "adler" in persons

    citations = json.loads((res_dir / "citations.json").read_text(encoding="utf-8"))
    assert "mascheroni-1797" in citations
    assert "mohr-1672" in citations
    assert "fazzari-1901" in citations

    glossary = json.loads((res_dir / "glossary.json").read_text(encoding="utf-8"))
    assert "geometria-del-compasso" in glossary
    assert "c1" in glossary
    assert "c2" in glossary
    assert "c3" in glossary

    structure = json.loads(
        (res_dir / "geometria_del_compasso" / "structure_map.json").read_text(encoding="utf-8")
    )
    assert structure["edition"] == "geometria_del_compasso"
    assert len(structure["sections"]) >= 6


def test_witness_files_exist() -> None:
    """Verify archival PDF and Italian transcription exist and are non-empty."""
    pdf_path = (
        REPO_ROOT
        / "resources"
        / "geometria_del_compasso"
        / "pdfs"
        / "mascheroni_1797_geometria_del_compasso.pdf"
    )
    assert pdf_path.is_file()
    assert pdf_path.stat().st_size > 1_000_000

    txt_path = (
        REPO_ROOT
        / "resources"
        / "geometria_del_compasso"
        / "sources"
        / "mascheroni_1797_compasso_it.txt"
    )
    assert txt_path.is_file()
    assert txt_path.stat().st_size > 1_000


def test_svg_diagrams_valid() -> None:
    """Verify SVG figures exist and follow .euclid-graphic structure."""
    fig_dir = REPO_ROOT / "docsrc" / "_static" / "figures"
    svgs = list(fig_dir.glob("*.svg"))
    assert len(svgs) >= 4

    for svg in svgs:
        content = svg.read_text(encoding="utf-8")
        root = ET.fromstring(content)
        assert "euclid-graphic" in root.attrib.get("class", "")
