"""Comprehensive test suite for ``geometor.mascheroni`` (1797)."""

from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

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
CODEX_DIR = REPO_ROOT / "docsrc" / "geometria_del_compasso"
FOLIOS_DIR = REPO_ROOT / "resources" / "geometria_del_compasso" / "folios"


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


def test_circle_circle_intersection_exact() -> None:
    """Verify Book I § 1 exact symbolic circle–circle intersection."""
    p1, p2 = circle_circle_intersection(
        sp.Point2D(0, 0), sp.Integer(1), sp.Point2D(1, 0), sp.Integer(1)
    )
    assert p1 == sp.Point2D(sp.Rational(1, 2), sp.sqrt(3) / 2)
    assert p2 == sp.Point2D(sp.Rational(1, 2), -sp.sqrt(3) / 2)


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


def test_mascheroni_trisection_exact() -> None:
    """Verify Libro III § 68 authentic compass-only trisection (Fig. 20)."""
    e = sp.Point2D(-1, 0)
    v = sp.Point2D(2, 0)
    f1, f2 = circle_circle_intersection(v, sp.Integer(3), e, sp.Integer(2))
    t1, t2 = circle_circle_intersection(f1, sp.Integer(2), f2, sp.Integer(2))
    t_pt = t2 if t1.equals(e) else t1
    assert sp.simplify(t_pt.x - sp.Rational(1, 3)) == 0
    assert sp.simplify(t_pt.y) == 0


def test_mascheroni_parallel_point_exact() -> None:
    """Verify Libro IV § 80 parallel point construction."""
    a = sp.Point2D(0, 0)
    b = sp.Point2D(3, 0)
    c = sp.Point2D(1, 2)
    d = mascheroni_parallel_point(a, b, c)
    assert d == sp.Point2D(4, 2)
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
    assert len(structure["sections"]) == 14
    assert structure["leaves_count"] == 55


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


def test_codex_leaf_partitioning_and_folio_coverage() -> None:
    """Verify 14 books, 55 atomic 4-track leaves, 100% folio coverage, and monotonicity."""
    structure = json.loads(
        (REPO_ROOT / "resources" / "geometria_del_compasso" / "structure_map.json").read_text(
            encoding="utf-8"
        )
    )
    leaf_start_folios: list[int] = []
    for section in structure["sections"]:
        sec_index = REPO_ROOT / "docsrc" / f"{section['path']}.rst"
        assert sec_index.is_file(), f"Missing book container {sec_index}"
        for leaf in section["leaves"]:
            leaf_dir = (REPO_ROOT / "docsrc" / f"{leaf['path']}.rst").parent
            for track in ("index.rst", "it.rst", "summary.rst", "notes.rst"):
                tf = leaf_dir / track
                assert tf.is_file(), f"Missing track file {tf}"
            idx_text = (leaf_dir / "index.rst").read_text(encoding="utf-8")
            m = re.search(r"^:folio:\s*(\d{4})\s*$", idx_text, re.MULTILINE)
            assert m, f"Missing frontmatter :folio: badge in {leaf_dir / 'index.rst'}"
            assert ".. folio::" in idx_text, f"Missing .. folio:: directive in {leaf_dir}"
            leaf_start_folios.append(int(m.group(1)))

    assert len(leaf_start_folios) == 55
    for i in range(1, len(leaf_start_folios)):
        assert leaf_start_folios[i] >= leaf_start_folios[i - 1], (
            f"Non-monotonic folio order at leaf {i}: "
            f"{leaf_start_folios[i - 1]} -> {leaf_start_folios[i]}"
        )

    all_codex_text = "\n".join(p.read_text(encoding="utf-8") for p in CODEX_DIR.rglob("*.rst"))
    linked_folios = set(re.findall(r"\.\.\s+folio::\s+(\d{4})", all_codex_text))
    tracked_scans = {p.stem for p in FOLIOS_DIR.glob("*.png")}
    assert len(tracked_scans) == 181
    assert tracked_scans.issubset(linked_folios), (
        f"Unlinked folios: {sorted(tracked_scans - linked_folios)}"
    )


def test_zero_orphaned_plates_and_clean_directives() -> None:
    """Verify zero orphaned plates and zero forbidden directives/options across the codex."""
    pngs = list(CODEX_DIR.rglob("*.png"))
    svgs = list(CODEX_DIR.rglob("*.svg"))
    assert len(pngs) >= 85
    assert len(svgs) >= 16

    for asset in pngs + svgs:
        en_idx = (asset.parent / "index.rst").read_text(encoding="utf-8")
        it_idx = (asset.parent / "it.rst").read_text(encoding="utf-8")
        assert asset.name in en_idx, f"Orphaned plate in English track: {asset}"
        assert asset.name in it_idx, f"Orphaned plate in Italian track: {asset}"

    for rst in CODEX_DIR.rglob("*.rst"):
        text = rst.read_text(encoding="utf-8")
        assert ".. py_file::" not in text, f"Forbidden .. py_file:: in {rst}"
        assert ":align:" not in text, f"Forbidden :align: option in {rst}"
        assert ":width:" not in text, f"Forbidden :width: option in {rst}"


def test_svg_diagrams_valid() -> None:
    """Verify all SVGs follow strict 5-layer .euclid-graphic standard with tick markers."""
    static_svgs = list((REPO_ROOT / "docsrc" / "_static" / "figures").glob("*.svg"))
    leaf_svgs = list(CODEX_DIR.rglob("*.svg"))
    assert len(static_svgs) >= 4
    assert len(leaf_svgs) >= 16

    ns = "{http://www.w3.org/2000/svg}"
    expected_layers = ["elements", "graphics", "highlights", "points", "labels"]

    for svg in static_svgs + leaf_svgs:
        content = svg.read_text(encoding="utf-8")
        root = ET.fromstring(content)
        assert "euclid-graphic" in root.attrib.get("class", ""), f"Missing class in {svg}"
        assert "--geom-fg" in content, f"Missing theme variable --geom-fg in {svg}"
        for tick_id in ("geom-tick-1", "geom-tick-2", "geom-tick-3"):
            assert f'id="{tick_id}"' in content, f"Missing marker {tick_id} in {svg}"

        g_ids = [
            child.attrib.get("id")
            for child in root
            if child.tag in ("g", f"{ns}g") and child.attrib.get("id")
        ]
        assert g_ids == expected_layers, f"Layer order mismatch in {svg}: {g_ids}"
        lines = [el for el in root.iter() if el.tag in ("line", f"{ns}line")]
        assert not lines, f"Raw <line> found in {svg}; use 3-vertex midpoint <path>"
