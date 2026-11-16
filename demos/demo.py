"""Symbolic demonstration script for ``geometor.mascheroni`` (1797)."""

from __future__ import annotations

import sys
from pathlib import Path

_SRC = Path(__file__).resolve().parents[1] / "src"
if _SRC.is_dir() and str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

import sympy as sp
from geometor.mascheroni import (
    OpCount,
    __version__,
    collinear_doubling,
    concentric_fourth_proportional,
    mascheroni_inversion,
    mascheroni_midpoint,
    mascheroni_parallel_point,
    mascheroni_reflect_point,
    run,
)


def main() -> int:
    """Run the package demonstration and verify exact symbolic compass constructions."""
    print(f"geometor.mascheroni v{__version__} — Lorenzo Mascheroni (1797)\n")

    # 1. Collinear Doubling (Libro III, § 64)
    a = sp.Point2D(0, 0)
    b = sp.Point2D(1, 0)
    e = collinear_doubling(a, b)
    print(f"1. Collinear Doubling: A={a}, B={b} -> E={e} (EB = 2 AB)")
    assert e == sp.Point2D(-1, 0)

    # 2. Midpoint Bisection (Libro III, § 66, Sol. V)
    m = mascheroni_midpoint(a, b)
    print(f"2. Midpoint Bisection (Sol. V): A={a}, B={b} -> M={m}")
    assert m == sp.Point2D(sp.Rational(1, 2), 0)

    # 3. Parallel Point (Libro IV, § 80)
    c = sp.Point2D(0, 1)
    d = mascheroni_parallel_point(a, b, c)
    print(f"3. Parallel Point: A={a}, B={b}, C={c} -> D={d} ((C, D) || (A, B))")
    assert d == sp.Point2D(1, 1)

    # 4. Orthogonal Reflection (Libro IV, § 78)
    p = sp.Point2D(sp.Rational(1, 2), 2)
    p_refl = mascheroni_reflect_point(a, b, p)
    print(f"4. Orthogonal Reflection: across AB, P={p} -> P'={p_refl}")
    assert p_refl == sp.Point2D(sp.Rational(1, 2), -2)

    # 5. Circular Inversion (Libro VII / Adler 1890)
    o = sp.Point2D(0, 0)
    r = sp.Integer(2)
    pt = sp.Point2D(4, 0)
    pt_inv = mascheroni_inversion(o, r, pt)
    print(f"5. Circular Inversion: O={o}, R={r}, Pt={pt} -> Pt'={pt_inv}")
    assert pt_inv == sp.Point2D(1, 0)

    # 6. Concentric Fourth Proportional (Libro V, § 93)
    fourth = concentric_fourth_proportional(sp.Integer(3), sp.Integer(6), sp.Integer(5))
    print(f"6. Fourth Proportional: a=3, b=6, c=5 -> x={fourth}")
    assert fourth == sp.Integer(10)

    # 7. OpCount Algebra
    op = OpCount.create(c1=10, c2=0, c3=7)
    print(f"7. OpCount: {op.symbol} (S={op.s}, E={op.e}, circles={op.circles})")
    assert op.validate() == []

    print("\nAll 100% exact symbolic compass constructions verified successfully!")
    return run([])


if __name__ == "__main__":
    raise SystemExit(main())
