#!/usr/bin/env python3
"""Scan simple SU(5) tensor-product hypercharge weights for Y=3/8."""

from __future__ import annotations

from itertools import combinations_with_replacement, product
import sympy as sp


FUND_WEIGHTS = [
    -sp.Rational(1, 3),
    -sp.Rational(1, 3),
    -sp.Rational(1, 3),
    sp.Rational(1, 2),
    sp.Rational(1, 2),
]


def tensor_sums(rank: int) -> set[sp.Rational]:
    return {sum(choice, sp.Rational(0)) for choice in product(FUND_WEIGHTS, repeat=rank)}


def antisymmetric_sums(rank: int) -> set[sp.Rational]:
    return {
        sum((FUND_WEIGHTS[i] for i in combo), sp.Rational(0))
        for combo in combinations_with_replacement(range(len(FUND_WEIGHTS)), rank)
    }


def main() -> None:
    target = sp.Rational(3, 8)
    unit = sp.Rational(1, 6)
    print("SU(5) tensor hypercharge lattice scan")
    print("-------------------------------------")
    print("Fundamental hypercharge weights: -1/3,-1/3,-1/3,1/2,1/2")
    print(f"Target Y = {sp.sstr(target)}")
    print(f"Target/(1/6) = {sp.sstr(target / unit)}")
    print()

    for rank in range(1, 9):
        values = sorted(tensor_sums(rank))
        contains = target in values or -target in values
        print(
            f"rank {rank} tensor sums: count={len(values):2d}, "
            f"contains +/-3/8={contains}, "
            f"min={sp.sstr(values[0])}, max={sp.sstr(values[-1])}"
        )

    print()
    print("All displayed weights are integer multiples of 1/6.")
    print("This is because each fundamental weight is itself on the 1/6 lattice.")
    print("Therefore no ordinary tensor representation built from these weights")
    print("contains Y=3/8.")


if __name__ == "__main__":
    main()
