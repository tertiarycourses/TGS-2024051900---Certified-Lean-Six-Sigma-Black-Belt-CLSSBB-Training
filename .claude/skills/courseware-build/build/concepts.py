#!/usr/bin/env python3
"""Lean Six Sigma BLACK BELT teaching content — the concept slides, in DMAIC order.

This module is a thin facade. The actual teaching content lives in one module per
phase so each stays readable and independently editable:

    concepts_foundations.py  -> foundations(d)
    concepts_define.py       -> define_phase(d)
    concepts_measure.py      -> measure_phase(d)
    concepts_analyze.py      -> analyze_phase(d)
    concepts_improve.py      -> improve_phase(d)
    concepts_control.py      -> control_phase(d)
    concepts_capstone.py     -> capstone_phase(d)

Every key concept is explained VISUALLY (diagram, chart, matrix, timeline) rather
than as a wall of bullets, per the house design standard.

Content is grounded in the CSSC "Six Sigma: A Complete Step-by-Step Guide", the
original v21 trainer deck, and is deliberately built as the STEP UP from the
Green Belt course (TGS-2025055775): ~45% DMAIC recap taught in depth (a Black
Belt must be able to MENTOR Green Belts through these tools) plus ~55%
Black-Belt-only advanced material.
"""

from concepts_foundations import foundations
from concepts_define import define_phase
from concepts_measure import measure_phase
from concepts_analyze import analyze_phase
from concepts_improve import improve_phase
from concepts_control import control_phase
from concepts_capstone import capstone_phase

__all__ = [
    "foundations",
    "define_phase",
    "measure_phase",
    "analyze_phase",
    "improve_phase",
    "control_phase",
    "capstone_phase",
]
