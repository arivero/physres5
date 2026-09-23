#!/usr/bin/env python3
"""Run every algebra/check script and summarize pass/fail status."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    scripts = sorted(
        path
        for path in here.glob("*.py")
        if path.name != Path(__file__).name and not path.name.startswith("_")
    )

    failures: list[tuple[str, int]] = []
    print("Signed de Broglie-de Vries algebra check suite")
    print("==============================================")
    for script in scripts:
        completed = subprocess.run(
            [sys.executable, str(script)],
            cwd=here.parents[1],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        status = "PASS" if completed.returncode == 0 else "FAIL"
        print(f"{status} {script.relative_to(here.parents[1])}")
        if completed.returncode != 0:
            failures.append((script.name, completed.returncode))
            if completed.stdout:
                print(completed.stdout)
            if completed.stderr:
                print(completed.stderr)

    print()
    if failures:
        print("Failures:")
        for name, code in failures:
            print(f"  {name}: exit code {code}")
        return 1

    print(f"All {len(scripts)} scripts completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
