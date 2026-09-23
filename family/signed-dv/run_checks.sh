#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 algebra/verify_signed_roots.py
echo
echo "=========================================================="
python3 algebra/explore_deformations.py
echo
echo "=========================================================="
python3 algebra/oneloop_gauge_higgs.py
echo
echo "=========================================================="
python3 algebra/scalar_scale_identification.py
echo
echo "=========================================================="
python3 algebra/precision_decomposition.py
echo
echo "=========================================================="
python3 algebra/oneloop_top_higgs.py
echo
echo "=========================================================="
python3 algebra/higher_spin_slots.py
echo
echo "=========================================================="
python3 algebra/closed_form_predictions.py
echo
echo "=========================================================="
python3 algebra/smeft_nogo.py
echo
echo "=========================================================="
python3 algebra/mw_tension_and_anchors.py
echo
echo "=========================================================="
python3 algebra/running_mass_scheme.py
echo
echo "=========================================================="
python3 algebra/look_elsewhere.py
