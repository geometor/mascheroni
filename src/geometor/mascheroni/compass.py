"""Exact symbolic compass-only geometry models for Lorenzo Mascheroni (1797).

Implements 100% exact algebraic and synthetic constructions over closed-form radical fields,
with zero floating-point arithmetic, along with Lemoine's operational calculus.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp


@dataclass(frozen=True, slots=True)
class OpCount:
    """Exact Lemoine operational count vector for compass-only geometry."""

    c1: int
    c2: int
    c3: int
    s: int
    e: int
    circles: int
    symbol: str

    @classmethod
    def create(cls, c1: int, c2: int, c3: int) -> OpCount:
        """Construct an :class:`OpCount` verifying Mascheroni invariant algebra."""
        s = c1 + c2 + c3
        e = c1 + c2
        symbol = f"{c1}C_1 + {c2}C_2 + {c3}C_3" if c2 > 0 else f"{c1}C_1 + {c3}C_3"
        return cls(c1=c1, c2=c2, c3=c3, s=s, e=e, circles=c3, symbol=symbol)

    def validate(self) -> list[str]:
        """Verify Lemoine's exactitude, simplicity, and circle-count invariants."""
        errors: list[str] = []
        if self.s != self.c1 + self.c2 + self.c3:
            errors.append(f"Simplicity mismatch: {self.s} != {self.c1 + self.c2 + self.c3}")
        if self.e != self.c1 + self.c2:
            errors.append(f"Exactitude mismatch: {self.e} != {self.c1 + self.c2}")
        if self.circles != self.c3:
            errors.append(f"Circle count mismatch: {self.circles} != {self.c3}")
        return errors


def circle_circle_intersection(
    c1: sp.Point2D, r1: sp.Expr, c2: sp.Point2D, r2: sp.Expr
) -> tuple[sp.Point2D, sp.Point2D]:
    """Compute the two exact symbolic intersection points of circles (c1, r1) and (c2, r2).

    Never introduces floating-point numbers; preserves exact radicals.
    """
    d_sq = (c2.x - c1.x) ** 2 + (c2.y - c1.y) ** 2
    d = sp.sqrt(d_sq)

    # Distance from c1 to the radical axis chord foot along c1->c2
    a = (r1**2 - r2**2 + d_sq) / (2 * d)
    h = sp.sqrt(r1**2 - a**2)

    # Unit vectors along and perpendicular to c1->c2
    ux = (c2.x - c1.x) / d
    uy = (c2.y - c1.y) / d

    # Chord midpoint
    mx = c1.x + a * ux
    my = c1.y + a * uy

    # Two symmetric intersection points
    p1 = sp.Point2D(mx - h * uy, my + h * ux)
    p2 = sp.Point2D(mx + h * uy, my - h * ux)
    return (p1, p2)


def collinear_doubling(a: sp.Point2D, b: sp.Point2D) -> sp.Point2D:
    """Collinear doubling of segment AB past A (Mascheroni Libro III, § 64).

    Returns point E collinear with A and B such that A is the midpoint of BE (EB = 2 AB).
    In Mascheroni's synthesis, this is executed by stepping three equal chords of radius AB
    around circle A(AB) from B.
    """
    return sp.Point2D(2 * a.x - b.x, 2 * a.y - b.y)


def mascheroni_midpoint(a: sp.Point2D, b: sp.Point2D) -> sp.Point2D:
    """Bisect un-drawn segment AB by compass alone (Mascheroni Libro III, § 66, Sol. V).

    1. Double BA past A to E (AE = AB, EB = 2 AB).
    2. Sweep E(EB) and B(BA), intersecting at P and p.
    3. Sweep P(BA) and p(BA), intersecting at exact midpoint M = (A + B)/2.
    """
    r_ab = a.distance(b)
    e = collinear_doubling(a, b)

    # Circle E(EB) has radius 2 * r_ab; Circle B(BA) has radius r_ab
    p1, p2 = circle_circle_intersection(e, 2 * r_ab, b, r_ab)

    # Arcs P(BA) and p(BA) intersect at B and at midpoint M
    m1, m2 = circle_circle_intersection(p1, r_ab, p2, r_ab)

    # Return the root distinct from B
    if m1.equals(b):
        return sp.Point2D(sp.simplify(m2.x), sp.simplify(m2.y))
    return sp.Point2D(sp.simplify(m1.x), sp.simplify(m1.y))


def mascheroni_parallel_point(a: sp.Point2D, b: sp.Point2D, c: sp.Point2D) -> sp.Point2D:
    """Construct point D through C such that (C, D) || (A, B) (Mascheroni Libro IV, § 80).

    Constructs the fourth vertex D of parallelogram ABDC via B(AC) ∩ C(AB).
    """
    r_ac = a.distance(c)
    r_ab = a.distance(b)

    d1, d2 = circle_circle_intersection(b, r_ac, c, r_ab)
    # The parallelogram vertex satisfies D - C == B - A
    expected = sp.Point2D(b.x - a.x + c.x, b.y - a.y + c.y)
    if d1.equals(expected):
        return sp.Point2D(sp.simplify(d1.x), sp.simplify(d1.y))
    return sp.Point2D(sp.simplify(d2.x), sp.simplify(d2.y))


def mascheroni_reflect_point(a: sp.Point2D, b: sp.Point2D, p: sp.Point2D) -> sp.Point2D:
    """Reflect point P orthogonally across virtual line (A, B) (Mascheroni Libro IV, § 78).

    Sweep A(AP) ∩ B(BP) to locate the opposite reflection point P'.
    """
    r_ap = a.distance(p)
    r_bp = b.distance(p)
    p1, p2 = circle_circle_intersection(a, r_ap, b, r_bp)
    if p1.equals(p):
        return sp.Point2D(sp.simplify(p2.x), sp.simplify(p2.y))
    return sp.Point2D(sp.simplify(p1.x), sp.simplify(p1.y))


def mascheroni_inversion(o: sp.Point2D, r: sp.Expr, p: sp.Point2D) -> sp.Point2D:
    """Circular inversion of point P across reference circle (O, R) (Adler 1890).

    Maps P to P' along ray OP such that OP · OP' = R^2 in 5C_1 + 3C_3.
    """
    op_sq = (p.x - o.x) ** 2 + (p.y - o.y) ** 2
    factor = r**2 / op_sq
    return sp.Point2D(
        sp.simplify(o.x + factor * (p.x - o.x)),
        sp.simplify(o.y + factor * (p.y - o.y)),
    )


def concentric_fourth_proportional(a: sp.Expr, b: sp.Expr, c: sp.Expr) -> sp.Expr:
    """Concentric fourth proportional x = (b * c) / a (Mascheroni Libro V, § 93)."""
    return sp.simplify(b * c / a)
