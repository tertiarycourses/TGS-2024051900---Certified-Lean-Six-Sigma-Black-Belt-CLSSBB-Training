#!/usr/bin/env python3
"""Improve teaching slides — Black Belt depth, Design of Experiments core."""
import os
from pptx.util import Inches, Pt
from components import (BLUE, TEAL, AMBER, RED, VIOLET, INK, GREY, LIGHT, WHITE,
                        LINE, DMAIC_COLORS)

HERE = os.path.dirname(os.path.abspath(__file__))


def _dg(d, name):
    """Resolve a diagram imported from the original trainer deck."""
    import glob
    for p in glob.glob(os.path.join(d.REPO_ASSETS, "diagrams", name + ".*")):
        return p
    return None


def improve_phase(d):
    K = "IMPROVE - BLACK BELT DEPTH"
    KD = "IMPROVE - DESIGN OF EXPERIMENTS"

    # ============================================================
    # A. WHAT IMPROVE DELIVERS AT BLACK BELT LEVEL
    # ============================================================
    d.big_statement(
        "Green Belts pick a solution. Black Belts design the experiment that finds it.",
        "Improve at Black Belt level is where Design of Experiments enters the toolkit. "
        "You stop guessing at settings and start estimating effects.",
        "IMPROVE", color=AMBER)

    d.tile_grid("What Improve delivers at Black Belt level", [
        ("A generated solution set", "Many candidates, each traced to a statistically proven root cause"),
        ("A weighted selection decision", "Criteria weighted WITH the sponsor before any solution is scored"),
        ("A designed experiment", "Factors, levels and runs chosen deliberately, not one factor at a time"),
        ("Optimum settings with evidence", "Prediction equation plus confirmation runs at the chosen setpoint"),
        ("A robust operating window", "Settings that hold up against the noise you cannot control"),
        ("A risk-assessed, piloted change", "FMEA re-scored after mitigation, then piloted before rollout"),
    ], kicker=K, cols=2, accent=AMBER)


    d.compare_panels("Green Belt Improve vs Black Belt Improve", [
        ("Green Belt", "Choose and pilot a solution", [
            "Brainstorm, then vote or use a simple matrix",
            "Apply known Lean countermeasures",
            "FMEA the new process, act on top RPNs",
            "Pilot, measure, roll out",
        ]),
        ("Black Belt", "Design experiments to find the optimum", [
            "Everything the Green Belt does, taught well enough to mentor it",
            "Plus: factorial designs to estimate effects and interactions",
            "Plus: fractional screening when factors are many",
            "Plus: RSM and robust design to optimise and de-sensitise",
        ]),
    ], kicker=K, accent=VIOLET)

    # ============================================================
    # B. SOLUTION GENERATION IN DEPTH
    # ============================================================
    d.big_statement(
        "You cannot select a good solution from a shallow list.",
        "Generation and selection are separate cognitive acts. Mixing them kills the "
        "good ideas before they are fully formed.",
        "SOLUTION GENERATION", color=BLUE)

    d.tile_grid("Six generation techniques a Black Belt must run", [
        ("Classic brainstorming", "Aloud, in group; quantity first, zero criticism, build on others"),
        ("Brainwriting 6-3-5", "6 people write 3 ideas in 5 minutes, then pass the sheet on"),
        ("SCAMPER", "Substitute, Combine, Adapt, Modify, Put to other use, Eliminate, Reverse"),
        ("Anti-solution thinking", "Ask how to make it WORSE, then invert every answer"),
        ("Benchmarking", "Borrow proven designs from inside, from rivals, from other industries"),
        ("Analogy and TRIZ prompts", "How does another industry solve the same physical problem?"),
    ], kicker=K, cols=2, accent=BLUE)

    d.flow_h("Brainwriting 6-3-5 mechanics", [
        "Seat 6 people; each gets a 3-column sheet",
        "Round 1: write 3 ideas in 5 minutes, in silence",
        "Pass the sheet to the left",
        "Read what is there, then add 3 BUILDS not 3 new ideas",
        "Repeat until each sheet has been round the table",
        "108 ideas in 30 minutes with no dominant voice",
    ], kicker=K, color=TEAL)



    d.two_col("Anti-solution thinking at Meridian Suzhou",
        [("How could we make first-pass yield MUCH worse?", 0),
         ("Let each operator set cure temperature by feel", 1),
         ("Change adhesive lots mid-shift with no record", 1),
         ("Run the test rig without daily calibration", 1),
         ("Give no torque spec on the housing screws", 1),
         ("Start the shift before the line reaches temperature", 1)],
        [("Now invert each answer into a countermeasure", 0),
         ("Lock cure temperature to a recipe in the controller", 1),
         ("One adhesive lot per shift, logged and traceable", 1),
         ("Daily calibration check as a line-start gate", 1),
         ("Torque-controlled driver with a verified setpoint", 1),
         ("Warm-up interlock before the first unit is released", 1)],
        kicker=K, lhead="Make it worse", rhead="Invert it", lcolor=RED, rcolor=TEAL)


    p = _dg(d, "benchmarking-steps")
    if p:
        d.image_slide("Benchmarking as a repeating cycle", p, kicker=K,
                      caption="Plan, collect, analyse, adapt. The gap analysis is where the learning "
                              "sits - copying the practice without understanding it fails.", accent=TEAL)

    d.compare_panels("Three types of benchmarking at Meridian", [
        ("Internal", "Another Meridian plant or line", [
            "Singapore Line 2 runs 96.4 percent first-pass yield",
            "Suzhou Line 5 runs 91.2 percent on the same product",
            "Cheapest, fastest, fully comparable data",
            "Risk: you only ever copy your own habits",
        ]),
        ("Competitive", "A rival infusion pump maker", [
            "Most relevant comparison of performance",
            "Hardest data to obtain legitimately",
            "Use teardowns, public filings, industry surveys",
            "Risk: confidentiality and competition law",
        ]),
        ("Functional", "Best-in-class in ANY industry", [
            "For leak testing, study automotive fuel systems",
            "For clean assembly, study semiconductor packaging",
            "Usually the source of the breakthrough",
            "Risk: needs the most adaptation effort",
        ]),
    ], kicker=K, accent=TEAL)

    # ============================================================
    # C. LEAN COUNTERMEASURES IN FULL
    # ============================================================
    d.big_statement(
        "Before you design an experiment, exhaust the countermeasures that need no experiment.",
        "Most defects are not an optimisation problem. They are an absence of standard "
        "work, mistake-proofing and flow.",
        "LEAN COUNTERMEASURES", color=TEAL)

    d.tile_grid("The Lean countermeasure toolkit", [
        ("5S", "Workplace organisation so the abnormal condition becomes visible instantly"),
        ("Poka-yoke", "Design so the error cannot be made, or cannot pass undetected"),
        ("Pull systems", "Downstream consumption authorises upstream production - no overproduction"),
        ("Just-in-Time", "The right part, the right quantity, exactly when needed"),
        ("Heijunka", "Level the mix and volume so demand spikes do not propagate"),
        ("Jidoka", "Automation with a human touch - the machine stops itself on abnormality"),
        ("Standard work", "The current best-known method, documented, trained and followed"),
        ("Kaizen events", "Short, focused, cross-functional bursts of improvement on one process"),
    ], kicker=K, cols=2, accent=TEAL)

    p = _dg(d, "5s-wheel")
    if p:
        d.image_slide("5S: the foundation everything else stands on", p, kicker=K,
                      caption="Sort, Set in order, Shine, Standardise, Sustain. Without Sustain the "
                              "other four decay within a quarter.", accent=TEAL)


    d.compare_panels("The three levels of poka-yoke", [
        ("Prevention", "The error cannot occur", [
            "Strongest level - always prefer this",
            "Asymmetric connector: the sensor only fits one way",
            "Fixture will not close on a mis-oriented housing",
            "Cost is in the design, not in the running",
        ]),
        ("Detection", "The error occurs but cannot pass", [
            "Second best - catches it at the source",
            "Vision system rejects a missing O-ring before potting",
            "Torque driver blocks the next step if the count is short",
            "Requires a working sensor and a real interlock",
        ]),
        ("Warning", "The operator is alerted", [
            "Weakest level - relies on human response",
            "Andon light and buzzer on out-of-spec cure temperature",
            "Use only when prevention and detection are infeasible",
            "Degrades fast once alarms become routine",
        ]),
    ], kicker=K, accent=RED)

    p = _dg(d, "poka-yoke-examples")
    if p:
        d.image_slide("Poka-yoke in practice", p, kicker=K,
                      caption="Every good poka-yoke is cheap, obvious and impossible to defeat "
                              "casually. If operators bypass it, the design is wrong.", accent=RED)

    p = _dg(d, "push-vs-pull")
    if p:
        d.image_slide("Push vs pull production", p, kicker=K,
                      caption="Push builds to a forecast and accumulates inventory. Pull builds only "
                              "what the next process has consumed.", accent=BLUE)


    d.tile_grid("JIT, Heijunka and Jidoka: what each one actually does", [
        ("JIT - the goal", "Right part, right quantity, right time; inventory is the enemy"),
        ("JIT - the enabler", "Short changeover, reliable equipment, capable suppliers"),
        ("Heijunka - the goal", "Level the mix so every model is built every day"),
        ("Heijunka - the effect", "A demand spike stops amplifying upstream (no bullwhip)"),
        ("Jidoka - the goal", "Never pass a defect to the next process"),
        ("Jidoka - the effect", "The line stops, the andon pulls help, the cause gets fixed now"),
    ], kicker=K, cols=2, accent=VIOLET)



    # ============================================================
    # D. WEIGHTED SOLUTION SELECTION
    # ============================================================
    d.big_statement(
        "Weight the criteria with the sponsor BEFORE anyone scores a solution.",
        "Weight the criteria after you see the scores and you have not made a decision. "
        "You have rationalised one.",
        "SOLUTION SELECTION", color=VIOLET)

    p = _dg(d, "solution-selection-matrix")
    if p:
        d.image_slide("The weighted solution selection matrix", p, kicker=K,
                      caption="Criteria across the top with agreed weights; solutions down the side; "
                              "weighted total drives the shortlist, not the decision.", accent=VIOLET)


    d.formula_card("Meridian: scoring three candidate solutions", [
        ("Criteria + weights",
         "Impact 40, Cost 25, Speed 20, Risk 15",
         "Weights agreed with the VP Ops before scoring began"),
        ("Fixture redesign",
         "(5x40)+(2x25)+(3x20)+(4x15) = 370",
         "Highest impact, slowest to implement, chosen"),
        ("Extra inspector",
         "(2x40)+(1x25)+(5x20)+(3x15) = 250",
         "Fast and cheap but adds cost forever and detects only"),
    ], kicker=K, accent=VIOLET,
        note="A solution that scores well only because it is cheap and fast is usually a containment, not a fix.")

    d.matrix2x2("Impact vs effort: where the shortlist really sits",
        "Implementation effort  ->", "Impact on Y  ->", [
            ("Just do it", "High impact, low effort. Torque-driver setpoint lock at Penang. "
                           "Implement this week, no experiment needed."),
            ("Major project", "High impact, high effort. Fixture redesign across 6 lines. "
                              "This is where DOE earns its keep."),
            ("Fill-in", "Low impact, low effort. Shadow boards on Line 3. "
                        "Do it, but do not claim it as the project result."),
            ("Question it", "Low impact, high effort. New MES module. "
                            "Say no, and say why, in writing."),
        ], kicker=K, accent=AMBER)

    # ============================================================
    # E. FMEA IN FULL
    # ============================================================
    d.big_statement(
        "FMEA is a design tool, not a paperwork exercise.",
        "Done before implementation it prevents failures. Done after, it documents them.",
        "FMEA", color=RED)

    p = _dg(d, "fmea-example")
    if p:
        d.image_slide("The FMEA worksheet", p, kicker=K,
                      caption="Process step, failure mode, effect, cause, current controls, then S, O, D "
                              "and RPN. Actions, then a re-score.", accent=RED)


    d.compare_panels("Severity, Occurrence, Detection: three different questions", [
        ("Severity (S)", "How bad is the EFFECT?", [
            "Scored on the effect, never on the cause",
            "1 = no discernible effect",
            "10 = hazard without warning, patient harm",
            "Severity can only be changed by REDESIGN",
        ]),
        ("Occurrence (O)", "How often does the CAUSE happen?", [
            "Scored on the cause, from real data if you have it",
            "1 = failure is eliminated by design",
            "10 = failure is almost inevitable",
            "Reduce by attacking the cause: poka-yoke, controls",
        ]),
        ("Detection (D)", "How likely are we to CATCH it?", [
            "The scale is INVERTED - read it carefully",
            "1 = control almost certainly detects it",
            "10 = no control exists, or it cannot detect",
            "Reduce by better detection: sensors, gauges, tests",
        ]),
    ], kicker=K, accent=RED)

    d.big_statement(
        "Detection is scored backwards. Low D means GOOD detection.",
        "This is the single most common FMEA scoring error. A team that scores D=10 for "
        "'we always catch it' inverts every priority in the table.",
        "FMEA - THE DETECTION TRAP", color=RED)

    d.formula_card("RPN and the Meridian cure-station FMEA", [
        ("RPN",
         "RPN = S x O x D",
         "Range 1 to 1000; a rank, not a measurement"),
        ("Incomplete cure",
         "S=9, O=6, D=7  ->  RPN = 378",
         "Field separation risk, cause frequent, dial check is weak"),
        ("Wrong adhesive lot",
         "S=8, O=3, D=4  ->  RPN = 96",
         "Serious effect, rarer cause, lot scan catches most"),
    ], kicker=K, accent=RED,
        note="RPN is ordinal. An RPN of 378 is not 'four times worse' than 96 - it is simply higher priority.")

    d.big_statement(
        "Severity 9 or 10 gets an action regardless of RPN.",
        "A failure that can harm a patient is not acceptable because it is rare and we "
        "usually catch it. The severity override outranks the arithmetic.",
        "FMEA - THE SEVERITY OVERRIDE", color=RED)



    d.formula_card("Re-scoring the Meridian FMEA after mitigation", [
        ("Before",
         "S=9, O=6, D=7  ->  RPN = 378",
         "Dial check by operator; no interlock; cure verified by feel"),
        ("Action taken",
         "Recipe lock + thermocouple interlock",
         "Controller refuses to release below 62 C; logged per unit"),
        ("After",
         "S=9, O=2, D=2  ->  RPN = 36",
         "S unchanged - the effect is still a fluid path breach"),
    ], kicker=K, accent=TEAL,
        note="Severity almost never moves. If your re-scored FMEA shows S falling, challenge it.")


    # ============================================================
    # F. PILOTING AND COST-BENEFIT
    # ============================================================
    d.big_statement(
        "Define success before the pilot starts, or the pilot cannot fail.",
        "A pilot without pre-agreed criteria always succeeds, because the criteria get "
        "written afterwards to match the result.",
        "PILOTING", color=BLUE)

    d.tile_grid("The five things a pilot must define BEFORE it starts", [
        ("Scope", "Which line, which product, which shift. Meridian: Penang Line 3, pump model M400"),
        ("Duration", "Long enough for the effect to show. Meridian: 4 weeks, about 9600 units"),
        ("Success criteria", "The number that decides. First-pass yield at or above 95.5 percent"),
        ("Control group", "Line 4 runs unchanged so you can separate the change from the season"),
        ("Stop conditions", "What ends the pilot early. Any scrap rate above 3 percent, any safety event"),
    ], kicker=K, cols=1, accent=BLUE)


    d.formula_card("Cost-benefit for the Meridian fixture redesign", [
        ("Payback period",
         "Investment / annual net benefit",
         "SGD 285,000 / SGD 610,000 = 0.47 yr, about 5.6 months"),
        ("Net Present Value",
         "NPV = sum of CFt / (1+r)^t  -  I",
         "3 yrs at 8 pct: 565+523+484 = 1572k, minus 285k = SGD 1.287m"),
        ("Decision rule",
         "NPV > 0 and payback < 18 months",
         "Meridian finance gate; both satisfied, project funded"),
    ], kicker=K, accent=TEAL,
        note="Get the benefit number signed by Finance, not by the project team. Credibility depends on it.")

    # ============================================================
    # G. WHY OFAT FAILS - ENTRY TO DOE
    # ============================================================
    d.big_statement(
        "One factor at a time is the most expensive way to learn the least.",
        "OFAT costs more runs, gives narrower conclusions, and is structurally blind to "
        "the one thing that usually matters most: interaction.",
        "DESIGN OF EXPERIMENTS", color=VIOLET)

    d.compare_panels("OFAT vs designed experiment", [
        ("OFAT", "Change one thing, hold the rest", [
            "Feels rigorous and is intuitive to managers",
            "CANNOT detect interactions - structurally impossible",
            "Conclusions valid only at the held levels of the others",
            "Needs more runs for less information",
            "Optimum found is local, not global",
        ]),
        ("Designed experiment", "Change several together, by design", [
            "Every factor varied across every combination",
            "Estimates main effects AND interactions",
            "Each run contributes to every effect estimate (hidden replication)",
            "Fewer runs, tighter estimates, wider validity",
            "The optimum found is defensible across the region",
        ]),
    ], kicker=K, accent=VIOLET)

    d.formula_card("The run-count comparison: 3 factors, 2 levels each", [
        ("OFAT",
         "Baseline + 2 runs per factor",
         "About 12-16 runs with replication, and zero interaction estimates"),
        ("Full factorial",
         "2^3 = 8 runs",
         "8 runs give 3 main effects, 3 two-factor, 1 three-factor interaction"),
        ("Precision",
         "Each effect uses ALL 8 runs",
         "Effect estimate has the precision of a 4-vs-4 comparison, not 1-vs-1"),
    ], kicker=KD, accent=VIOLET,
        note="This is 'hidden replication': every run is used in every effect estimate, so DOE gets more from less.")

    d.tile_grid("Why OFAT cannot see an interaction", [
        ("The setup", "Vary temperature at fixed pressure. Then vary pressure at fixed temperature"),
        ("What you learn", "The effect of temperature AT THAT ONE PRESSURE. Nothing more"),
        ("What you miss", "That temperature helps at high pressure and hurts at low pressure"),
        ("The Meridian case", "Cure temp raised yield at 4.2 bar clamp, lowered it at 2.8 bar"),
        ("The consequence", "OFAT recommended 62 C. The true optimum was 68 C at 4.2 bar"),
        ("The cost", "Six months and 41 confirmation runs before the interaction was found"),
    ], kicker=KD, cols=2, accent=RED)

    # ============================================================
    # H. DOE VOCABULARY
    # ============================================================
    d.tile_grid("DOE vocabulary: the words you must use precisely", [
        ("Factor", "An input X you deliberately set. Cure temperature, clamp pressure, dwell time"),
        ("Level", "A setting of a factor. Low (-1) and high (+1) in a two-level design"),
        ("Response", "The output Y you measure. First-pass yield, bond strength, leak rate"),
        ("Run", "One execution of the process at one specific factor combination"),
        ("Effect", "The change in the mean response caused by moving a factor from low to high"),
        ("Interaction", "When the effect of one factor DEPENDS on the level of another"),
    ], kicker=KD, cols=2, accent=BLUE)


    d.compare_panels("Replication vs repetition: the distinction that matters", [
        ("Replication", "Re-run the whole run", [
            "Set the machine up again from scratch",
            "Captures setup, material and operator variation",
            "This is what gives you PURE ERROR",
            "Meridian: 8 runs replicated twice = 16 trials",
        ]),
        ("Repetition", "Re-measure the same run", [
            "Same setup, measure the part 3 times",
            "Captures only measurement variation",
            "Understates the true error, inflates significance",
            "Useful for MSA, useless as replication",
        ]),
    ], kicker=KD, accent=RED)

    d.big_statement(
        "Randomisation is not optional. It is what makes the inference valid.",
        "Without randomisation, any drift in ambient temperature, tool wear or operator "
        "fatigue is silently added to whichever factor you happened to change last.",
        "DOE - RANDOMISATION", color=RED)


    d.compare_panels("Blocking: when you cannot randomise away a nuisance", [
        ("The problem", "A known nuisance factor", [
            "Meridian must run 16 trials over 2 days",
            "Day-to-day variation is real and large",
            "Randomising alone leaves the day effect in the error",
        ]),
        ("The solution", "Block on the nuisance", [
            "Run 8 trials on day 1, 8 on day 2 as two blocks",
            "Choose which 8 so the block is confounded with ABC only",
            "Day effect is estimated and removed from the error",
        ]),
        ("The trade", "You sacrifice one effect", [
            "The blocked effect can no longer be estimated",
            "Sacrifice the highest-order interaction - ABC",
            "Randomise WITHIN each block, always",
        ]),
    ], kicker=KD, accent=AMBER)

    # ============================================================
    # I. FULL FACTORIAL 2^k
    # ============================================================
    d.big_statement(
        "The 2^k full factorial: every factor at every combination of the others.",
        "k factors at 2 levels means 2^k runs. It estimates every main effect and every "
        "interaction, cleanly. It is the gold standard when you can afford the runs.",
        "FULL FACTORIAL", color=BLUE)

    d.formula_card("How big is a 2^k design?", [
        ("2 factors",
         "2^2 = 4 runs",
         "2 main effects, 1 two-factor interaction"),
        ("3 factors",
         "2^3 = 8 runs",
         "3 main, 3 two-factor, 1 three-factor interaction"),
        ("5 factors",
         "2^5 = 32 runs",
         "5 main, 10 two-factor, 16 higher-order - runs grow fast"),
    ], kicker=KD, accent=BLUE,
        note="Effects estimated always equals runs minus one. 8 runs estimate 7 effects plus the grand mean.")

    d.tile_grid("The Meridian 2^3 experiment: pump housing bond strength", [
        ("Response Y", "Bond pull strength in newtons; spec is 180 N minimum"),
        ("Factor A", "Cure temperature: 58 C (low, -1) or 68 C (high, +1)"),
        ("Factor B", "Clamp pressure: 2.8 bar (low, -1) or 4.2 bar (high, +1)"),
        ("Factor C", "Dwell time: 20 s (low, -1) or 35 s (high, +1)"),
        ("Design", "2^3 = 8 runs, replicated twice, 16 trials in randomised order"),
        ("Held constant", "Adhesive lot, operator, fixture, ambient humidity band"),
    ], kicker=KD, cols=2, accent=BLUE)

    d.tile_grid("The design matrix in standard (Yates) order", [
        ("Run 1", "A = -1, B = -1, C = -1     Y = 154 N"),
        ("Run 2", "A = +1, B = -1, C = -1     Y = 171 N"),
        ("Run 3", "A = -1, B = +1, C = -1     Y = 162 N"),
        ("Run 4", "A = +1, B = +1, C = -1     Y = 206 N"),
        ("Run 5", "A = -1, B = -1, C = +1     Y = 161 N"),
        ("Run 6", "A = +1, B = -1, C = +1     Y = 180 N"),
        ("Run 7", "A = -1, B = +1, C = +1     Y = 172 N"),
        ("Run 8", "A = +1, B = +1, C = +1     Y = 219 N"),
    ], kicker=KD, cols=2, accent=BLUE)


    d.formula_card("Replication and pure error at Meridian", [
        ("Replicate pairs",
         "Run 1: 154, 149    Run 8: 219, 213",
         "Whole runs re-set-up, not the same part re-measured"),
        ("Pure error SD",
         "s from the within-pair ranges",
         "Average range 5.4 N -> s about 4.8 N across 8 pairs"),
        ("Significance yardstick",
         "Effect significant if it exceeds ~2 x SE",
         "SE of an effect = 2s / sqrt(N) = 2(4.8)/4 = 2.4 -> flag > 4.8 N"),
    ], kicker=KD, accent=VIOLET,
        note="Without replication you have no pure error, so you must rely on normal plots or effect sparsity instead.")

    # ============================================================
    # J. EFFECTS
    # ============================================================
    d.big_statement(
        "A main effect is the average change in Y when a factor goes from low to high.",
        "Average all the runs where A is high, average all the runs where A is low, "
        "subtract. Every run contributes to every effect.",
        "MAIN EFFECTS", color=TEAL)

    d.formula_card("Calculating the main effects at Meridian", [
        ("Effect of A",
         "avg(A high) - avg(A low)",
         "(171+206+180+219)/4 - (154+162+161+172)/4 = 194.0 - 162.25 = +31.75 N"),
        ("Effect of B",
         "avg(B high) - avg(B low)",
         "(162+206+172+219)/4 - (154+171+161+180)/4 = 189.75 - 166.5 = +23.25 N"),
        ("Effect of C",
         "avg(C high) - avg(C low)",
         "(161+180+172+219)/4 - (154+171+162+206)/4 = 183.0 - 173.25 = +9.75 N"),
    ], kicker=KD, accent=TEAL,
        note="Cure temperature (A) is the dominant factor; dwell time (C) is real but small.")

    d.formula_card("Calculating interaction effects", [
        ("AB interaction",
         "avg(AB=+1) - avg(AB=-1)",
         "(154+206+161+219)/4 - (171+162+180+172)/4 = 185.0 - 171.25 = +13.75 N"),
        ("AC interaction",
         "avg(AC=+1) - avg(AC=-1)",
         "(154+162+180+219)/4 - (171+206+161+172)/4 = 178.75 - 177.5 = +1.25 N"),
        ("ABC interaction",
         "Sign column = A x B x C",
         "(171+162+161+219)/4 - (154+206+180+172)/4 = 178.25 - 178.0 = +0.25 N"),
    ], kicker=KD, accent=VIOLET,
        note="Sign column for AB is just A multiplied by B, row by row. Same arithmetic, different column.")


    d.compare_panels("Main effect plot vs interaction plot", [
        ("Main effect plot", "Y against one factor's two levels", [
            "One line per factor, low on the left, high on the right",
            "STEEPER slope means a LARGER effect",
            "Flat line means the factor does nothing in this range",
            "Meridian: A is steepest, C is nearly flat",
        ]),
        ("Interaction plot", "Y against factor A, one line per level of B", [
            "PARALLEL lines mean NO interaction",
            "NON-PARALLEL lines mean an interaction exists",
            "Crossing lines mean a strong reversal of effect",
            "Meridian AB: lines diverge sharply to the right",
        ]),
    ], kicker=KD, accent=TEAL)

    d.tile_grid("Reading the Meridian AB interaction plot", [
        ("At low clamp pressure", "Raising temperature 58 -> 68 C gains only 18 N"),
        ("At high clamp pressure", "The same temperature rise gains 45 N"),
        ("The lines", "Diverge sharply - the classic non-parallel signature"),
        ("The meaning", "Temperature is worth far more when clamp pressure is high"),
        ("The decision", "Set both high; never optimise them independently"),
        ("The OFAT trap", "Testing temperature at 2.8 bar would have concluded 'temperature barely matters'"),
    ], kicker=KD, cols=2, accent=RED)

    d.big_statement(
        "When an interaction is significant, never interpret its main effects alone.",
        "The statement 'raising cure temperature adds 32 N' is only true on average. "
        "It is 18 N in one condition and 45 N in another.",
        "DOE - INTERPRETING INTERACTIONS", color=RED)

    # ============================================================
    # K. SIGNIFICANCE OF EFFECTS
    # ============================================================
    d.compare_panels("Three ways to decide which effects are real", [
        ("Pareto of effects", "Bar chart of absolute effect size", [
            "Bars sorted largest to smallest",
            "A reference line drawn at the critical value",
            "Bars beyond the line are significant",
            "Fastest visual read for a review meeting",
        ]),
        ("Normal plot of effects", "Effects on normal probability paper", [
            "Inert effects fall on a straight line (they are pure noise)",
            "REAL effects fall OFF the line, at the extremes",
            "Works even with NO replication - the key advantage",
            "Half-normal plot is the same idea on absolute values",
        ]),
        ("ANOVA / p-values", "Formal test against pure error", [
            "Requires replication to get pure error",
            "Effect significant at p < 0.05",
            "Gives R-squared and lack-of-fit as a bonus",
            "The number a sponsor will ask you for",
        ]),
    ], kicker=KD, accent=VIOLET)

    d.pareto_chart("Pareto of effects: Meridian bond strength", [
        ("A: Cure temp", 32), ("B: Clamp pressure", 23), ("AB interaction", 14),
        ("C: Dwell time", 10), ("AC", 1), ("BC", 1),
    ], kicker=KD,
        note="Absolute effect size in newtons. Everything above the 4.8 N critical value is real: A, B, AB and C.")

    d.tile_grid("Reading a normal probability plot of effects", [
        ("The logic", "If a factor does nothing, its estimated effect is pure noise, so it is normal"),
        ("Noise effects", "Plot as a straight line through the middle of the chart"),
        ("Real effects", "Fall clearly OFF that line, out at the tails"),
        ("Positive effects", "Sit above and to the right of the line"),
        ("Negative effects", "Sit below and to the left of the line"),
        ("Why it matters", "This works with an unreplicated design where you have no pure error"),
    ], kicker=KD, cols=2, accent=BLUE)

    # ============================================================
    # L. MODEL AND CONFIRMATION
    # ============================================================
    d.formula_card("Building the Meridian prediction equation", [
        ("General form",
         "Y = b0 + b1(A) + b2(B) + b12(AB)",
         "Coefficients are HALF the effects, in coded -1/+1 units"),
        ("Meridian model",
         "Y = 178.1 + 15.9A + 11.6B + 6.9AB",
         "Grand mean 178.1 N; A, B and AB retained; C dropped for cycle time"),
        ("Predicted optimum",
         "A=+1, B=+1",
         "178.1 + 15.9 + 11.6 + 6.9 = 212.5 N predicted at 68 C, 4.2 bar"),
    ], kicker=KD, accent=VIOLET,
        note="Coefficient = effect / 2 because the coded range from -1 to +1 spans 2 units.")


    d.big_statement(
        "If the confirmation runs fail, you do NOT roll out.",
        "A prediction is a hypothesis about the future. Confirmation runs test it. "
        "Rolling out an unconfirmed optimum is gambling with the sponsor's money.",
        "CONFIRMATION RUNS", color=RED)

    d.flow_h("Running the confirmation properly", [
        "Set the process at the predicted optimum: 68 C, 4.2 bar",
        "Run 8-12 independent confirmation trials, randomised",
        "Compare the observed mean to the predicted 212.5 N",
        "Check it falls inside the prediction interval",
        "Only then move to pilot and rollout",
    ], kicker=KD, color=TEAL)

    d.formula_card("Meridian confirmation result", [
        ("Predicted",
         "212.5 N, PI 203 to 222 N",
         "From the model at A=+1, B=+1"),
        ("Observed",
         "n=10, mean 209.4 N, s = 5.1 N",
         "Inside the prediction interval - the model is confirmed"),
        ("Decision",
         "Confirmed -> pilot on Penang Line 3",
         "Bond strength margin over the 180 N spec rises from -12 to +29 N"),
    ], kicker=KD, accent=TEAL,
        note="If observed had come back at 186 N, the model would be rejected and you return to the design.")


    # ============================================================
    # M. FRACTIONAL FACTORIAL
    # ============================================================
    d.big_statement(
        "With 7 factors, a full factorial is 128 runs. A quarter-day of screening is 16.",
        "Fractional factorials buy that economy by deliberately trading away the "
        "high-order interactions you almost certainly do not need.",
        "FRACTIONAL FACTORIAL", color=AMBER)

    d.formula_card("The economics of 2^(k-p)", [
        ("Full factorial",
         "2^7 = 128 runs",
         "At 45 min per run that is 96 hours of line time"),
        ("Half fraction",
         "2^(7-1) = 64 runs",
         "One generator sacrificed; still very expensive"),
        ("Sixteenth fraction",
         "2^(7-4) = 16 runs",
         "12 hours. Screens 7 factors down to the vital 2 or 3"),
    ], kicker=KD, accent=AMBER,
        note="p is the number of factors 'generated' from the others. Each unit of p halves the run count.")

    d.tile_grid("How a fractional design is built", [
        ("Start with a base design", "For 2^(7-4): a full 2^3 in factors A, B, C - just 8 rows"),
        ("Generators", "Assign the extra factors to interaction columns: D=AB, E=AC, F=BC, G=ABC"),
        ("Defining relation", "I = ABD = ACE = BCF = ABCG and all their products"),
        ("Alias structure", "Every effect is aliased with several others; the relation tells you which"),
        ("The consequence", "You estimate a SUM of effects, never one effect on its own"),
        ("The bet", "That the high-order terms in each sum are negligible - effect sparsity"),
    ], kicker=KD, cols=2, accent=AMBER)

    d.formula_card("Working out an alias: the arithmetic", [
        ("Generator",
         "D = AB, so I = ABD",
         "Multiply both sides by D; D squared = I, the identity column"),
        ("Alias of A",
         "A x I = A x ABD = BD",
         "So the A column also carries BD. You estimate A + BD"),
        ("Alias of AB",
         "AB x ABD = D",
         "The AB column IS the D column. They cannot be separated"),
    ], kicker=KD, accent=VIOLET,
        note="Rule: multiply any effect by the defining relation, and any letter squared drops out as I.")

    d.big_statement(
        "Confounding means two effects share one column. You cannot tell them apart.",
        "The design does not fail. It simply reports a sum. Knowing WHICH sum before "
        "you interpret the result is the whole discipline.",
        "CONFOUNDING", color=RED)


    d.compare_panels("Resolution III, IV and V: what each one costs you", [
        ("Resolution III", "Shortest word has 3 letters", [
            "MAIN effects aliased with 2-FACTOR interactions",
            "Cheapest design; 2^(7-4) screens 7 factors in 8 runs",
            "A big 'A' effect might really be a big BC interaction",
            "Use ONLY to screen many factors for the vital few",
            "Never use it to make a final settings decision",
        ]),
        ("Resolution IV", "Shortest word has 4 letters", [
            "Main effects CLEAR of 2-factor interactions",
            "But 2-factor interactions are aliased WITH EACH OTHER",
            "2^(7-3) in 16 runs; the usual screening workhorse",
            "AB + CE is one column: you know an interaction is there",
            "You cannot yet say WHICH interaction it is",
        ]),
        ("Resolution V", "Shortest word has 5 letters", [
            "Main effects AND 2-factor interactions all clear",
            "2FIs aliased only with 3-factor interactions",
            "2^(5-1) in 16 runs; the characterisation standard",
            "Safe to build a prediction model from",
            "Costs more runs - buy it when the decision matters",
        ]),
    ], kicker=KD, accent=VIOLET)



    d.tile_grid("Meridian: screening 7 factors on the Suzhou potting line", [
        ("The factors", "A cure temp, B clamp, C dwell, D adhesive lot, E humidity, F fixture, G operator"),
        ("The design", "2^(7-3) Resolution IV, 16 runs, randomised over 2 blocked days"),
        ("The result", "A, C and F stand off the normal plot; B, D, E, G sit on the line"),
        ("The alias caution", "The AC + FG column was significant - which one is it?"),
        ("The follow-up", "Fold over to de-alias, or run a 2^3 full factorial on A, C, F"),
        ("The outcome", "7 factors reduced to 3 in 12 hours of line time"),
    ], kicker=KD, cols=2, accent=AMBER)


    d.flow_h("Fold-over: de-aliasing without starting again", [
        "Run the original Res III fraction, 8 runs",
        "Reverse ALL signs to build the mirror fraction, 8 more runs",
        "Combine the two: 16 runs total",
        "The combined design is Resolution IV - main effects now clear",
        "Alternative: reverse ONE factor's signs to free that factor and its 2FIs",
    ], kicker=KD, color=VIOLET)


    # ============================================================
    # N. RESPONSE SURFACE METHODOLOGY
    # ============================================================
    d.big_statement(
        "Two-level designs fit planes. Real optima sit on curves.",
        "A 2^k design has only two points per factor. Two points define a straight line. "
        "It is structurally incapable of seeing curvature.",
        "RESPONSE SURFACE METHODOLOGY", color=VIOLET)


    d.compare_panels("Centre points: the cheapest curvature test there is", [
        ("What they are", "Runs at the midpoint of every factor", [
            "Coded (0, 0, 0) - all factors at their mid-level",
            "Meridian: 63 C, 3.5 bar, 27.5 s",
            "Add 3 to 5 of them to any 2-level design",
        ]),
        ("What they test", "Factorial mean vs centre mean", [
            "If no curvature, the centre runs land on the fitted plane",
            "If they sit well above or below, curvature is present",
            "A formal t-test on the difference gives a p-value",
        ]),
        ("Free bonus", "Pure error and drift detection", [
            "Repeated centre points give pure error with no extra design",
            "Run some early and some late to detect process drift",
            "Costs 3-5 runs; tells you whether RSM is even needed",
        ]),
    ], kicker=KD, accent=TEAL)

    d.formula_card("Meridian curvature test at the potting station", [
        ("Factorial mean",
         "avg of the 8 corner runs",
         "178.1 N"),
        ("Centre mean",
         "avg of 5 centre-point runs",
         "196.3 N - well above the plane, not on it"),
        ("Curvature",
         "196.3 - 178.1 = +18.2 N, p = 0.003",
         "Significant curvature -> the linear model is inadequate, go to RSM"),
    ], kicker=KD, accent=VIOLET,
        note="A positive curvature this large usually means the optimum lies INSIDE the region you tested.")

    d.flow_h("Steepest ascent: getting to the right neighbourhood first", [
        "Fit the first-order model in the current region",
        "The gradient points in the direction of steepest improvement",
        "Take steps along that path, proportional to each coefficient",
        "Run single trials along the path until Y stops improving",
        "Set up a new factorial with centre points at that best point",
        "Test for curvature there; if present, run the RSM design",
    ], kicker=KD, color=AMBER)


    d.compare_panels("The two standard response surface designs", [
        ("Central Composite (CCD)", "Factorial + centre + axial", [
            "Factorial core: the 2^k corner points",
            "Centre points: 3 to 6 replicated runs at (0,0)",
            "Axial or 'star' points at (+/-alpha, 0) and (0, +/-alpha)",
            "5 levels per factor; alpha = 1.682 for k=3 gives rotatability",
            "2^3 CCD = 8 + 6 + 6 = 20 runs",
        ]),
        ("Box-Behnken (BBD)", "Midpoints of the edges", [
            "No corner points at all - only edge midpoints and centres",
            "Only 3 levels per factor, easier to set on real equipment",
            "Never runs all factors at their extremes simultaneously",
            "Use when a corner combination is unsafe or impossible",
            "3-factor BBD = 15 runs, slightly cheaper than the CCD",
        ]),
    ], kicker=KD, accent=BLUE)


    d.formula_card("The Meridian quadratic model", [
        ("Model form",
         "Y = b0 + b1A + b2B + b11A^2 + b22B^2 + b12AB",
         "Six terms for two factors; needs at least 6 distinct design points"),
        ("Fitted",
         "Y = 218.4 + 9.1A + 6.2B - 7.8A^2 - 4.1B^2 + 3.4AB",
         "R-squared 0.96; both quadratic terms strongly significant"),
        ("Stationary point",
         "Solve dY/dA = 0 and dY/dB = 0",
         "A = +0.71, B = +1.05 -> 71.4 C and 4.4 bar, predicted 224.7 N"),
    ], kicker=KD, accent=VIOLET,
        note="Both quadratic coefficients are negative, so the surface is a dome and the stationary point is a MAXIMUM.")

    d.compare_panels("Classifying the stationary point: three outcomes", [
        ("Maximum", "Both quadratic terms negative", [
            "The surface is a dome; contours are closed ellipses",
            "The stationary point is the optimum you want",
            "Meridian bond strength: -7.8 and -4.1, a clean maximum",
        ]),
        ("Minimum", "Both quadratic terms positive", [
            "A bowl; contours are closed ellipses around the low point",
            "This is the optimum when smaller Y is better",
            "Leak rate and warranty returns behave this way",
        ]),
        ("SADDLE POINT", "Mixed signs", [
            "A max in one direction and a min in the other",
            "Contours are hyperbolas, not closed ellipses",
            "The stationary point is NOT an optimum - do not set there",
            "Optimise along a ridge, at the edge of the safe region",
        ]),
    ], kicker=KD, accent=RED)

    d.big_statement(
        "A saddle point is the trap. It satisfies the maths and fails in production.",
        "The gradient is zero, so the software reports a stationary point. But move a "
        "little in one direction and Y falls off a cliff.",
        "RSM - THE SADDLE", color=RED)



    d.compare_panels("Optimising several responses at once: desirability", [
        ("The problem", "Responses conflict", [
            "Bond strength wants 71 C and long dwell",
            "Cycle time wants short dwell",
            "Adhesive cost wants low clamp pressure",
            "No single setting is best for all three",
        ]),
        ("Desirability functions", "Convert each Y to 0-1", [
            "d = 0 means completely unacceptable",
            "d = 1 means fully at target",
            "Larger-is-better, smaller-is-better, target-is-best shapes",
            "Weight each response by its business importance",
        ]),
        ("Overall D", "Geometric mean of the d values", [
            "D = (d1 x d2 x ... x dn)^(1/n)",
            "Geometric, so any d = 0 forces D = 0",
            "One unacceptable response kills the whole setting - correctly",
            "Maximise D across the design space to get the compromise",
        ]),
    ], kicker=KD, accent=VIOLET)


    # ============================================================
    # O. ROBUST / TAGUCHI DESIGN
    # ============================================================
    d.big_statement(
        "Do not fight the noise. Design so the noise stops mattering.",
        "Taguchi's insight: you cannot control ambient humidity, but you can find the "
        "settings at which ambient humidity barely affects your output.",
        "ROBUST DESIGN", color=TEAL)

    d.compare_panels("Control factors vs noise factors", [
        ("Control factors", "You set them and they stay set", [
            "Cure temperature setpoint, clamp pressure, dwell time",
            "Fixture design, adhesive grade, recipe parameters",
            "These are the dials you are allowed to turn",
            "Their levels go in the inner array",
        ]),
        ("Noise factors", "Real, influential, not controllable", [
            "Ambient humidity, incoming adhesive viscosity variation",
            "Operator-to-operator differences, tool wear, line voltage",
            "Too expensive or impossible to control in production",
            "Deliberately VARIED in the outer array during the experiment",
        ]),
    ], kicker=KD, accent=BLUE)

    d.big_statement(
        "A lower mean with far less variation usually beats a higher mean that swings.",
        "Meridian setting A gives 224 N plus or minus 22. Setting B gives 214 N plus or "
        "minus 5. B never goes below spec. A does, one batch in twenty.",
        "THE TAGUCHI INSIGHT", color=TEAL)

    d.formula_card("Meridian: two settings, same spec, different risk", [
        ("Setting A",
         "mean 224 N, s = 11 N, LSL 180",
         "Z = (224-180)/11 = 4.0 -> about 32 ppm below spec"),
        ("Setting B",
         "mean 214 N, s = 2.6 N, LSL 180",
         "Z = (214-180)/2.6 = 13.1 -> effectively zero risk"),
        ("Choice",
         "Choose B",
         "10 N of mean given up to remove all the tail risk. Correct trade"),
    ], kicker=KD, accent=TEAL,
        note="Six Sigma is about variation, not averages. The robust setting wins even with a lower mean.")


    d.compare_panels("The three signal-to-noise ratios", [
        ("Smaller-is-better", "Defects, leak rate, cycle time", [
            "S/N = -10 log10( mean of y-squared )",
            "Ideal target is zero; no negative values possible",
            "Meridian leak rate and warranty returns use this",
        ]),
        ("Larger-is-better", "Bond strength, yield, life", [
            "S/N = -10 log10( mean of 1/y-squared )",
            "No upper bound; more is always better",
            "Meridian bond pull strength uses this",
        ]),
        ("Nominal-is-best", "Dimensions, fill volume, flow rate", [
            "S/N = 10 log10( mean-squared / variance )",
            "Two-step: maximise S/N, then adjust the mean to target",
            "Meridian pump flow rate calibration uses this",
        ]),
    ], kicker=KD, accent=AMBER)

    d.formula_card("S/N ratio for the Meridian bond-strength study", [
        ("Setting A",
         "y = 241, 228, 219, 208",
         "S/N (larger-better) = 27.0 dB; mean 224, wide spread"),
        ("Setting B",
         "y = 217, 214, 212, 213",
         "S/N (larger-better) = 26.6 dB; mean 214, very tight"),
        ("Robustness",
         "Compare the SPREAD across noise",
         "A ranges 33 N across the noise conditions; B ranges 5 N"),
    ], kicker=KD, accent=TEAL,
        note="S/N alone can mislead. Always inspect mean and variance separately as well as the ratio.")


    d.tile_grid("The robust operating window", [
        ("Definition", "The range of settings over which Y stays acceptable despite noise"),
        ("Where to find it", "The flat plateau on the response surface, not the sharp peak"),
        ("Meridian's window", "68 to 73 C at 4.1 to 4.6 bar keeps bond strength above 205 N"),
        ("Why it matters", "Production drifts. Setpoints wander. Operators round numbers"),
        ("What you hand over", "A window in the control plan, not a single number nobody can hold"),
        ("The Black Belt test", "Would this setting survive a wet Tuesday in Suzhou? If not, move it"),
    ], kicker=KD, cols=2, accent=AMBER)


    # ============================================================
    # P. PULLING IT TOGETHER
    # ============================================================
    d.big_statement(
        "Screen, characterise, optimise, robustify, confirm.",
        "That sequence is the Black Belt's experimental strategy. Each stage answers a "
        "different question and buys the right amount of information.",
        "DOE STRATEGY", color=BLUE)

    d.flow_h("The complete experimental strategy", [
        "SCREEN: Res III or IV fractional over many factors",
        "CHARACTERISE: full or Res V factorial over the vital few",
        "TEST CURVATURE: add centre points; move by steepest ascent if needed",
        "OPTIMISE: CCD or Box-Behnken, fit the quadratic, find the stationary point",
        "ROBUSTIFY: cross with noise factors, choose the flat window",
        "CONFIRM: independent runs at the chosen setting before any rollout",
    ], kicker=KD, color=BLUE)

    d.ladder("Runs invested at each stage of the Meridian programme", [
        ("Screen", "2^(7-3) Res IV, 16 runs. 7 factors down to 3"),
        ("Characterise", "2^3 full factorial + 3 centre points, 11 runs. Found the AB interaction"),
        ("Optimise", "Central composite, 20 runs. Located the 71.4 C / 4.4 bar maximum"),
        ("Robustify", "8 x 4 crossed array, 32 runs. Moved to the flat window at 70 C"),
        ("Confirm", "10 runs at the chosen setting. Model held; pilot approved"),
    ], kicker=KD, accent=VIOLET,
        note="89 runs total across five stages. A single 2^7 full factorial would have been 128 runs and answered less.")

    d.tile_grid("Meridian Improve phase: the result", [
        ("First-pass yield", "Penang Line 3 moved from 91.2 to 96.8 percent over the 4-week pilot"),
        ("Bond strength margin", "From 12 N below the 180 N spec floor to 29 N above it"),
        ("Warranty returns", "Projected reduction of 61 percent on the M400 pump family"),
        ("FMEA", "Highest RPN fell from 378 to 36 after the recipe lock and interlock"),
        ("Financial", "SGD 610k annual benefit, 5.6 month payback, NPV SGD 1.29m"),
        ("Transferability", "The robust window transferred to Suzhou with no re-optimisation"),
    ], kicker=K, cols=2, accent=TEAL)


    d.big_statement(
        "You have found the optimum. Now the hard part: making it stay.",
        "Every improvement decays without a control system. Control is where the "
        "savings become permanent, or quietly evaporate.",
        "NEXT: CONTROL", color=RED)
