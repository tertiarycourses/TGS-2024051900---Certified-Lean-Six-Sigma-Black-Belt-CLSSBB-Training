#!/usr/bin/env python3
"""Control teaching slides - Black Belt depth."""
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


def control_phase(d):
    K = "CONTROL - BLACK BELT DEPTH"

    # ============================================================
    # SECTION A - WHAT CONTROL DELIVERS
    # ============================================================
    d.big_statement("An improvement you cannot hold",
                    "is an improvement you did not make. Control is where the money is banked.",
                    K, color=RED)

    d.tile_grid("What Control delivers at Black Belt level", [
        ("Recap taught to teaching depth", "SPC, chart selection, run rules, capability, control plan - deep enough to coach"),
        ("Advanced detection schemes", "CUSUM and EWMA find the small sustained shifts Shewhart charts miss for weeks"),
        ("Charts for awkward processes", "Short-run SPC for high-mix, multivariate SPC for correlated characteristics"),
        ("Autocorrelation handled", "Chemical and continuous-flow data breaks the Shewhart assumption outright"),
        ("Portfolio control plan governance", "You audit control plans across every project, not just your own"),
        ("Finance-validated benefits", "Hard, soft and cost-avoidance benefits signed off before closure"),
    ], kicker=K, cols=2, accent=RED)

    p = _dg(d, "control-steps")
    if p:
        d.image_slide("The Control phase step sequence", p, kicker=K,
                      caption="Monitor the improved process, document it, then hand it over "
                              "to a named owner with a written reaction plan.",
                      accent=RED)

    # ============================================================
    # SECTION B - SPC RECAP IN DEPTH
    # ============================================================
    d.big_statement("Statistical Process Control",
                    "Re-derived in full - because you must be able to teach it, not merely use it.",
                    "RECAP IN DEPTH - SPC", color=BLUE)

    p = _dg(d, "control-charts-intro")
    if p:
        d.image_slide("Anatomy of a control chart", p, kicker="RECAP - SPC",
                      caption="Centre line at the process average, upper and lower control limits "
                              "at plus and minus 3 sigma of the plotted statistic.",
                      accent=BLUE)

    d.tile_grid("Chart anatomy - every element and what it means", [
        ("Centre line (CL)", "The process average of the plotted statistic - Xbar-bar, Rbar, pbar"),
        ("Upper control limit (UCL)", "CL + 3 sigma of the plotted statistic - the voice of the process"),
        ("Lower control limit (LCL)", "CL - 3 sigma; truncated at zero for ranges and attribute counts"),
        ("Plotted points", "Subgroup statistics IN TIME ORDER - order is the entire information content"),
        ("Zones A, B, C", "Each 1 sigma wide either side of CL - the run rules are defined on these"),
        ("Sample and frequency", "Rational subgroup size and interval, chosen deliberately, recorded on the chart"),
    ], kicker="RECAP - SPC", cols=2, accent=BLUE)

    d.compare_panels("Why 3 sigma - and not 2 or 4", [
        ("At 3 sigma", "Shewhart's economic balance", [
            "False alarm rate 0.27 percent - about 1 in 370 points",
            "Roughly one false signal per year on a daily chart",
            "Cheap enough that people still trust the chart",
            "Wide enough to ignore ordinary common cause noise",
            "Not a statistical law - an economic compromise",
        ]),
        ("At 2 sigma", "Too many false alarms", [
            "False alarm rate 4.6 percent - 1 in 22 points",
            "A daily chart cries wolf every month",
            "Operators stop investigating - the chart dies",
        ]),
        ("At 4 sigma", "Too many missed signals", [
            "False alarms almost vanish - so do real signals",
            "Real shifts sit inside the limits for months",
            "The chart becomes decorative",
        ]),
    ], kicker="RECAP - SPC", accent=BLUE)

    d.big_statement("Control limits are NOT specification limits",
                    "They come from different sources, mean different things, and must never be plotted together.",
                    "RECAP - THE CLASSIC ERROR", color=RED)

    d.compare_panels("Control limits vs specification limits", [
        ("Control limits", "The VOICE OF THE PROCESS", [
            "Calculated FROM the process data itself",
            "Answer: what is this process actually doing?",
            "Move when the process genuinely changes",
            "Used to detect special causes",
            "Live on the control chart",
        ]),
        ("Specification limits", "The VOICE OF THE CUSTOMER", [
            "Set by the customer, design or regulator",
            "Answer: what does the customer require?",
            "Change only via engineering change control",
            "Used to judge conformance and capability",
            "Live on the drawing and in the capability study",
        ]),
    ], kicker="RECAP - SPC", accent=RED)

    d.tile_grid("Four consequences of confusing the two", [
        ("Spec limits drawn on the chart", "Every point inside spec looks fine - real special causes are invisible"),
        ("Limits widened to pass", "Somebody sets UCL at the spec so the chart stops alarming. Fraud, not control"),
        ("In control read as capable", "A stable process can be stably terrible. Control says nothing about the spec"),
        ("Capable read as in control", "A capable process can be drifting. Capability says nothing about stability"),
    ], kicker="RECAP - SPC", cols=2, accent=RED)

    # ============================================================
    # SECTION C - CHART SELECTION LOGIC
    # ============================================================
    d.big_statement("Chart selection is a decision tree",
                    "Data type, then subgroup size, then what you are counting. Get it wrong and the limits are wrong.",
                    "RECAP - CHART SELECTION", color=TEAL)

    p = _dg(d, "control-chart-selection")
    if p:
        d.image_slide("The control chart selection map", p, kicker="RECAP - CHART SELECTION",
                      caption="Continuous data branches on subgroup size; attribute data branches "
                              "on defectives versus defects and on constant versus varying sample.",
                      accent=TEAL)

    d.tile_grid("CONTINUOUS data - select on subgroup size n", [
        ("n = 1  ->  I-MR", "Individuals and moving range. Slow processes, batch results, one reading per period"),
        ("n = 2 to 8  ->  Xbar-R", "Average and range. The workhorse - range is easy for operators to compute"),
        ("n >= 9  ->  Xbar-S", "Average and standard deviation. At large n the range wastes information"),
        ("Always a PAIR", "One chart for the centre, one for the spread. Read the spread chart FIRST"),
        ("Why the pair matters", "If the range chart is out of control, the Xbar limits are computed from noise"),
        ("Meridian example", "Fill volume n=5 every hour -> Xbar-R; monthly OTIF percentage n=1 -> I-MR"),
    ], kicker="RECAP - CHART SELECTION", cols=2, accent=TEAL)

    d.tile_grid("ATTRIBUTE data - defectives versus defects", [
        ("DEFECTIVE = the unit fails", "One pump either passes or fails. Binomial. Count units, not faults"),
        ("DEFECT = one fault found", "One pump may carry three faults. Poisson. Count faults, not units"),
        ("np chart", "Number defective, CONSTANT sample size - e.g. exactly 200 pumps inspected daily"),
        ("p chart", "Proportion defective, VARYING sample size - limits step in and out with n"),
        ("c chart", "Count of defects, CONSTANT opportunity - faults per finished pump assembly"),
        ("u chart", "Defects per unit, VARYING opportunity - faults per batch of differing size"),
    ], kicker="RECAP - CHART SELECTION", cols=2, accent=AMBER)

    d.compare_panels("Meridian - four attribute charts chosen correctly", [
        ("np chart", "Singapore final test", [
            "Exactly 250 pumps tested every shift",
            "Count of pumps failing final test",
            "Constant n, defectives -> np",
        ]),
        ("p chart", "Penang incoming inspection", [
            "Lot sizes vary from 80 to 600 units",
            "Proportion of lots rejected",
            "Varying n, defectives -> p",
        ]),
        ("c chart", "Suzhou cosmetic audit", [
            "One finished pump audited per hour",
            "Number of cosmetic faults per pump",
            "Constant opportunity, defects -> c",
        ]),
        ("u chart", "Warranty returns", [
            "Faults reported per 1000 units shipped",
            "Shipment volume varies each month",
            "Varying opportunity, defects -> u",
        ]),
    ], kicker="RECAP - CHART SELECTION", accent=AMBER)

    # ============================================================
    # SECTION D - CONTROL LIMIT CALCULATION
    # ============================================================
    p = _dg(d, "control-limits-calc")
    if p:
        d.image_slide("Computing control limits with the constants", p, kicker="RECAP - LIMITS",
                      caption="The A2, D3 and D4 constants convert the average range into "
                              "3-sigma limits without ever computing a standard deviation.",
                      accent=VIOLET)

    d.formula_card("Xbar-R control limits - the constants", [
        ("Xbar chart", "UCL/LCL = Xbar-bar +/- A2 x Rbar", "A2 depends only on subgroup size n"),
        ("R chart upper", "UCL(R) = D4 x Rbar", "D4 = 2.114 at n=5"),
        ("R chart lower", "LCL(R) = D3 x Rbar", "D3 = 0 for n <= 6, so LCL(R) = 0"),
    ], kicker="RECAP - LIMITS", accent=VIOLET,
        note="A2 = 0.577 at n=5, 0.729 at n=4, 1.023 at n=3. The constants replace a sigma estimate.")

    d.formula_card("Meridian worked example - Singapore fill volume, n = 5", [
        ("Data", "Xbar-bar = 10.02 mL, Rbar = 0.18 mL", "25 subgroups of 5, hourly, over 3 shifts"),
        ("Xbar limits", "10.02 +/- 0.577 x 0.18", "UCL = 10.124, LCL = 9.916 mL"),
        ("R chart limits", "UCL = 2.114 x 0.18 = 0.381", "LCL = 0 x 0.18 = 0 (n = 5)"),
    ], kicker="RECAP - LIMITS", accent=VIOLET,
        note="Spec is 9.80 to 10.20 mL. The control limits sit well inside spec - process voice narrower than customer voice.")

    # ============================================================
    # SECTION E - WESTERN ELECTRIC RUN RULES
    # ============================================================
    d.big_statement("A point inside the limits can still be a signal",
                    "The Western Electric run rules read the PATTERN, not just the extremes.",
                    "RECAP - RUN RULES", color=RED)

    p = _dg(d, "spc-out-of-control")
    if p:
        d.image_slide("Out-of-control patterns on a chart", p, kicker="RECAP - RUN RULES",
                      caption="Beyond-limit points, runs on one side, trends and hugging - each "
                              "pattern has a different physical cause.",
                      accent=RED)

    d.tile_grid("The Western Electric rules in full", [
        ("Rule 1 - beyond 3 sigma", "Any single point outside a control limit. The classic special cause"),
        ("Rule 2 - 2 of 3 beyond 2 sigma", "Two of three consecutive points in zone A on the SAME side"),
        ("Rule 3 - 4 of 5 beyond 1 sigma", "Four of five consecutive points beyond 1 sigma, SAME side"),
        ("Rule 4 - 8 on one side", "Eight consecutive points on one side of the centre line - a shift"),
        ("Rule 5 - trend", "Six or seven consecutive points steadily rising or falling - tool wear, fouling"),
        ("Rule 6 - hugging the CL", "15 consecutive points inside 1 sigma. Suspiciously good - check the data"),
    ], kicker="RECAP - RUN RULES", cols=2, accent=RED)

    d.tile_grid("The Black Belt caveat on run rules", [
        ("Rules multiply false alarms", "Each rule has its own false-alarm rate - all six together is far above 0.27 percent"),
        ("All six on a daily chart", "Combined false alarm roughly 1 percent - about one nuisance signal per quarter"),
        ("Choose rules deliberately", "Rules 1 and 4 on a stable, well-understood process is often enough"),
        ("Never let software decide", "Default rule sets differ between packages. Specify yours in the control plan"),
    ], kicker="RECAP - RUN RULES", cols=2, accent=AMBER)

    # ============================================================
    # SECTION F - CAPABILITY RECAP
    # ============================================================
    d.big_statement("Capability recap - Cp, Cpk, Pp, Ppk",
                    "Four indices, two questions: is the spread small enough, and is it centred?",
                    "RECAP - CAPABILITY", color=VIOLET)

    d.formula_card("The four capability indices", [
        ("Cp", "Cp = (USL - LSL) / (6 x s-within)", "Potential - spread only, ignores centring"),
        ("Cpk", "Cpk = min[(USL-Xbar), (Xbar-LSL)] / (3 x s-within)", "Actual - penalises off-centre"),
        ("Pp / Ppk", "Same formulas with s-TOTAL", "Long-term performance including shift-to-shift drift"),
    ], kicker="RECAP - CAPABILITY", accent=VIOLET,
        note="Cp and Cpk use WITHIN-subgroup variation; Pp and Ppk use TOTAL variation. Reporting the wrong pair flatters the process.")

    d.formula_card("Meridian worked example - Suzhou seal force", [
        ("Given", "USL = 62 N, LSL = 48 N, Xbar = 56.4 N", "s-within = 1.55 N, s-total = 2.10 N"),
        ("Cp and Cpk", "Cp = 14 / 9.30 = 1.51", "Cpk = min(5.6, 8.4) / 4.65 = 1.20"),
        ("Pp and Ppk", "Pp = 14 / 12.60 = 1.11", "Ppk = 5.6 / 6.30 = 0.89"),
    ], kicker="RECAP - CAPABILITY", accent=VIOLET,
        note="Cpk 1.20 but Ppk 0.89 - the process is good within a shift and drifts BETWEEN shifts. That gap is the project.")

    d.tile_grid("Reading the gaps between the indices", [
        ("Cp much greater than Cpk", "Spread is fine, process is OFF-CENTRE. Re-centre - do not launch variation work"),
        ("Cpk much greater than Ppk", "Good within subgroup, drifting between them. Hunt the between-shift X"),
        ("Cp roughly equals Cpk", "Centred. Any shortfall is genuine spread - variation reduction is the right project"),
        ("Cpk equals Ppk", "Within and total variation agree - the process is genuinely stable over time"),
    ], kicker="RECAP - CAPABILITY", cols=2, accent=VIOLET)

    # ============================================================
    # SECTION G - CONTROL PLAN, SOP, VISUAL MANAGEMENT
    # ============================================================
    p = _dg(d, "control-plan-format")
    if p:
        d.image_slide("The control plan format", p, kicker="RECAP - CONTROL PLAN",
                      caption="One row per characteristic: what is measured, how, how often, "
                              "by whom, against what limits, and what happens on a signal.",
                      accent=TEAL)

    d.tile_grid("Every control plan row - the mandatory columns", [
        ("Process step and characteristic", "Where in the flow, and exactly which X or Y is being controlled"),
        ("Specification and limits", "Target with tolerance, plus the control limits if charted"),
        ("Measurement method and gauge", "Which instrument, and the MSA result that qualified it"),
        ("Sample size and frequency", "The rational subgroup and interval, chosen not inherited"),
        ("Control method", "Chart type, checklist, poka-yoke, automated interlock"),
        ("Reaction plan and owner", "The named person and the exact action on an out-of-control signal"),
    ], kicker="RECAP - CONTROL PLAN", cols=2, accent=TEAL)

    d.compare_panels("The three layers that hold a gain", [
        ("SOP", "The method written down", [
            "The new way of working, step by step",
            "Version controlled with an effective date",
            "Training record for every affected operator",
            "Reviewed when the process changes",
        ]),
        ("Visual management", "The state visible at a glance", [
            "Chart at the machine, not in a monthly pack",
            "Red/green status visible from the aisle",
            "Shadow boards, floor markings, andon",
            "A stranger can see if the process is healthy",
        ]),
        ("Response plan", "The action on a signal", [
            "IF the chart signals THEN do exactly this",
            "Contain, adjust, escalate - in that order",
            "Named owner and escalation path",
            "Rehearsed, not written and filed",
        ]),
    ], kicker="RECAP - CONTROL PLAN", accent=TEAL)

    d.tile_grid("Mistake-proofing beats monitoring", [
        ("Level 1 - eliminate", "Redesign so the error is physically impossible. The strongest control"),
        ("Level 2 - prevent", "Poka-yoke: the fixture only accepts the part one way round"),
        ("Level 3 - detect at source", "Automatic interlock stops the line the moment the error occurs"),
        ("Level 4 - detect downstream", "Inspection or a control chart finds it after the fact"),
        ("Level 5 - depend on people", "Training and vigilance. The weakest control - it decays"),
        ("Design rule", "Push every control as far UP this list as the budget allows"),
    ], kicker="RECAP - CONTROL PLAN", cols=2, accent=BLUE)

    # ============================================================
    # SECTION H - BLACK BELT: ARL AND THE LIMITS OF SHEWHART
    # ============================================================
    d.tile_grid("Average Run Length - the honest measure of a chart", [
        ("ARL definition", "The average number of subgroups plotted before the chart signals"),
        ("ARL-0 - in control", "How long between FALSE alarms. For 3-sigma Shewhart, ARL-0 = 370"),
        ("ARL-1 - out of control", "How long to DETECT a real shift. Smaller is better"),
        ("The number that matters", "ARL-1 for the smallest shift you actually care about catching"),
        ("Chart comparison rule", "Compare charts at EQUAL ARL-0, then see which has the lower ARL-1"),
        ("Why it is not taught at GB", "Green Belts use the chart. Black Belts choose between charts"),
    ], kicker="BLACK BELT ONLY - ARL", cols=2, accent=RED)

    d.formula_card("Shewhart ARL - the uncomfortable arithmetic", [
        ("In control", "ARL-0 = 1 / 0.0027 = 370", "One false alarm every 370 subgroups"),
        ("3-sigma shift", "ARL-1 = about 2", "Detected almost immediately - the easy case"),
        ("1-sigma shift", "ARL-1 = about 44", "Forty-four subgroups before the chart notices"),
    ], kicker="BLACK BELT ONLY - ARL", accent=RED,
        note="Rule 1 alone, subgroup n=5. The 1-sigma case is the one that quietly destroys the project benefit.")

    d.compare_panels("Meridian - what an ARL of 44 costs", [
        ("The shift", "Penang line 2 fill volume", [
            "Fill mean drifts 1 sigma high after a pump reseal",
            "Still inside spec - no customer complaint yet",
            "Xbar-R chart, subgroups hourly, n = 5",
        ]),
        ("The delay", "44 subgroups = 44 hours", [
            "Roughly 5.5 shifts before the chart signals",
            "About 26,000 units filled off target",
            "Overfill cost alone about SGD 19,000",
        ]),
        ("The structural cause", "The chart has no memory", [
            "Each point judged ALONE against the limits",
            "Yesterday's evidence is discarded entirely",
            "A shift small relative to sigma never breaches",
        ]),
    ], kicker="BLACK BELT ONLY - ARL", accent=RED)

    # ============================================================
    # SECTION I - CUSUM
    # ============================================================
    d.big_statement("BLACK BELT ONLY: CUSUM",
                    "Accumulate every small deviation from target until the total becomes undeniable.",
                    "BLACK BELT ONLY - CUSUM", color=VIOLET)

    d.tile_grid("How the CUSUM works", [
        ("Deviation from TARGET", "Each point contributes its distance from target, not from the mean"),
        ("Deviations accumulate", "Small biased-high deviations add up; random ones cancel out"),
        ("Reset at zero", "The sum is floored at zero so an in-control process stays flat"),
        ("Two one-sided sums", "An UPPER CUSUM for high shifts and a LOWER CUSUM for low shifts"),
        ("Signal on h", "Signal when either sum exceeds the decision interval h"),
        ("The payoff", "A 1-sigma shift detected in about 8 subgroups instead of 44"),
    ], kicker="BLACK BELT ONLY - CUSUM", cols=2, accent=VIOLET)

    d.formula_card("The CUSUM equations", [
        ("Upper CUSUM", "C+(i) = max[0, x(i) - (T + k) + C+(i-1)]", "Accumulates evidence of a HIGH shift"),
        ("Lower CUSUM", "C-(i) = max[0, (T - k) - x(i) + C-(i-1)]", "Accumulates evidence of a LOW shift"),
        ("Signal rule", "Signal if C+ > h or C- > h", "h is the decision interval, in sigma units"),
    ], kicker="BLACK BELT ONLY - CUSUM", accent=VIOLET,
        note="T = target. Both sums start at zero and are floored at zero - that floor is what keeps a stable process flat.")

    d.tile_grid("Choosing k and h - the two design parameters", [
        ("k = the reference value", "Set k to HALF the shift you want to detect, in sigma units"),
        ("k for a 1-sigma shift", "k = 0.5 sigma. This is by far the most common setting"),
        ("h = the decision interval", "Typically 4 to 5 sigma. h = 5 with k = 0.5 gives ARL-0 near 465"),
        ("Larger h", "Fewer false alarms, slower detection. Trades ARL-1 for ARL-0"),
        ("Smaller k", "Tuned for smaller shifts, but slower against large ones"),
        ("The trade you are making", "CUSUM is fast on SMALL shifts and slightly SLOWER than Shewhart on huge ones"),
    ], kicker="BLACK BELT ONLY - CUSUM", cols=2, accent=VIOLET)

    d.formula_card("Meridian worked CUSUM - Penang fill volume", [
        ("Design", "T = 10.00 mL, sigma = 0.04, k = 0.02, h = 0.20", "k = 0.5 sigma, h = 5 sigma"),
        ("Points 1-4", "10.01, 10.02, 10.03, 10.04", "C+ = 0, 0, 0.01, 0.03 - accumulating"),
        ("Points 5-8", "10.04, 10.05, 10.04, 10.05", "C+ = 0.05, 0.08, 0.10, 0.13 - climbing"),
    ], kicker="BLACK BELT ONLY - CUSUM", accent=VIOLET,
        note="By point 11 C+ exceeds h = 0.20 and signals. No individual point came near the 3-sigma Shewhart limit of 10.12.")

    d.compare_panels("CUSUM versus Shewhart on the same Penang data", [
        ("Shewhart Xbar-R", "Judges each point alone", [
            "UCL = 10.124 mL - never breached",
            "Rule 4 (8 on one side) eventually fires at point 13",
            "No signal at all if the drift is under 8 points",
            "Detected the 1-sigma shift at subgroup 44 on average",
        ]),
        ("CUSUM", "Accumulates the evidence", [
            "Signals at point 11 in this run",
            "Average detection about 8 subgroups",
            "Roughly 5 times faster on this shift size",
            "The plotted sum also estimates WHEN the shift began",
        ]),
    ], kicker="BLACK BELT ONLY - CUSUM", accent=VIOLET)

    # ============================================================
    # SECTION J - EWMA
    # ============================================================
    d.big_statement("BLACK BELT ONLY: EWMA",
                    "Exponentially weighted moving average - tunable memory, and it survives autocorrelation.",
                    "BLACK BELT ONLY - EWMA", color=TEAL)

    d.formula_card("The EWMA statistic", [
        ("The recursion", "z(i) = lambda x(i) + (1 - lambda) z(i-1)", "z(0) = target; lambda between 0 and 1"),
        ("Weight decay", "Weight on the point k steps back = lambda(1-lambda)^k", "Geometrically decaying memory"),
        ("Control limits", "T +/- L x sigma x sqrt[lambda / (2 - lambda)]", "L is typically 2.7 to 3.0"),
    ], kicker="BLACK BELT ONLY - EWMA", accent=TEAL,
        note="Every past point still contributes - but its weight halves away geometrically. That is the memory.")

    d.tile_grid("Choosing lambda - the single design decision", [
        ("lambda = 0.10 to 0.20", "Long memory, narrow limits. Best for SMALL sustained shifts. The usual choice"),
        ("lambda = 0.20", "The most common default - detects a 1-sigma shift in about 10 subgroups"),
        ("lambda = 0.40 and above", "Short memory, wider limits - behaviour approaches a Shewhart chart"),
        ("lambda = 1.00", "No memory at all - the EWMA IS the individuals chart"),
        ("Match lambda to shift size", "Small shift to detect -> small lambda. Large shift -> larger lambda"),
        ("Set L with lambda", "L = 2.7 with lambda = 0.10 gives ARL-0 near 500. Tune the pair, not one"),
    ], kicker="BLACK BELT ONLY - EWMA", cols=2, accent=TEAL)

    d.formula_card("Meridian worked EWMA - Suzhou cure oven temperature", [
        ("Design", "T = 180 C, sigma = 1.2, lambda = 0.20, L = 2.7", "Steady-state limits 180 +/- 1.08 C"),
        ("Points 1-4", "180.6, 181.1, 180.9, 181.4", "z = 180.12, 180.32, 180.43, 180.63"),
        ("Points 5-7", "181.2, 181.6, 181.5", "z = 180.75, 180.92, 181.03 - signals at point 8"),
    ], kicker="BLACK BELT ONLY - EWMA", accent=TEAL,
        note="Individual readings never exceed 183.6 (the 3-sigma individuals limit). The smoothed statistic crosses in 8 points.")

    d.compare_panels("CUSUM or EWMA - choosing between them", [
        ("CUSUM", "Sharper on a known shift size", [
            "Slightly faster when you know the shift to detect",
            "The sum estimates when the shift started",
            "Two statistics to plot and read",
            "Less intuitive for operators",
        ]),
        ("EWMA", "More forgiving and more general", [
            "One smoothed line plotted like a normal chart",
            "Performs well across a RANGE of shift sizes",
            "Handles AUTOCORRELATED data - CUSUM does not",
            "Easier for operators to interpret",
        ]),
        ("In practice", "The Black Belt's default", [
            "EWMA for most processes - readability wins",
            "CUSUM when the shift size is known and detection speed is critical",
            "Either one ALWAYS paired with a Shewhart chart for spikes",
        ]),
    ], kicker="BLACK BELT ONLY - EWMA", accent=TEAL)

    # ============================================================
    # SECTION K - AUTOCORRELATION
    # ============================================================
    d.big_statement("BLACK BELT ONLY: Autocorrelation",
                    "If this reading predicts the next one, Shewhart limits are far too narrow - and the chart screams.",
                    "BLACK BELT ONLY - AUTOCORRELATION", color=RED)

    d.tile_grid("Where autocorrelation comes from", [
        ("Chemical and batch processes", "Reactor contents carry over - this hour's concentration sets next hour's"),
        ("Continuous flow", "Tanks, ovens and dryers have thermal inertia measured in hours"),
        ("High-frequency sampling", "Sample faster than the process can change and every reading resembles the last"),
        ("Feedback control loops", "A PID controller deliberately makes the next reading depend on the last"),
        ("Meridian case", "Suzhou adhesive viscosity sampled every 5 minutes from a 400 L heated vessel"),
        ("The tell-tale", "Lag-1 autocorrelation above about 0.5 on the baseline data"),
    ], kicker="BLACK BELT ONLY - AUTOCORRELATION", cols=2, accent=RED)

    d.compare_panels("What autocorrelation does to a Shewhart chart", [
        ("The mechanism", "Sigma is underestimated", [
            "Moving-range sigma assumes consecutive points are independent",
            "Correlated points sit close together, so MR is small",
            "Small MR gives a small sigma estimate",
            "Small sigma gives limits far too narrow",
        ]),
        ("The symptom", "Constant false alarms", [
            "20 to 40 percent of points outside the limits",
            "Long runs on one side firing Rule 4 continually",
            "The process is genuinely stable - the chart is wrong",
        ]),
        ("The damage", "The chart is abandoned", [
            "Operators learn every signal is noise",
            "They stop investigating - including the real ones",
            "This is how SPC programmes quietly die",
        ]),
    ], kicker="BLACK BELT ONLY - AUTOCORRELATION", accent=RED)

    d.flow_h("Diagnosing and fixing autocorrelation", [
        "Plot the data in time order and look for long smooth waves",
        "Compute the lag-1 autocorrelation on 50+ baseline points",
        "If it exceeds about 0.5, the Shewhart assumption is broken",
        "Fix 1: sample LESS often, until consecutive readings are independent",
        "Fix 2: use an EWMA chart, which tolerates the correlation",
        "Fix 3: fit a time-series model and chart the RESIDUALS",
    ], kicker="BLACK BELT ONLY - AUTOCORRELATION", color=RED)

    # ============================================================
    # SECTION L - SHORT-RUN SPC
    # ============================================================
    d.big_statement("BLACK BELT ONLY: Short-run SPC",
                    "High-mix low-volume never gets 25 subgroups per part number. Chart the deviation instead.",
                    "BLACK BELT ONLY - SHORT RUN", color=AMBER)

    d.tile_grid("The short-run problem", [
        ("The rule you cannot meet", "Control limits need 25+ subgroups. A 40-unit run gives you 8"),
        ("High mix, low volume", "Meridian Singapore runs 34 pump variants across one assembly cell"),
        ("Per-part charts fail", "34 charts, none with enough data, all with meaningless limits"),
        ("The cell is the constant", "The same fixture, operator and method make every variant"),
        ("The insight", "Chart the PROCESS, not the part. Variation belongs to the cell"),
        ("The method", "Transform every part onto one common scale, then chart them together"),
    ], kicker="BLACK BELT ONLY - SHORT RUN", cols=2, accent=AMBER)

    d.formula_card("The two short-run transformations", [
        ("DNOM chart", "plotted = x - nominal(part)", "Deviation from nominal. Use when spread is similar across parts"),
        ("Standardised chart", "plotted = (x - nominal) / sigma(part)", "Use when parts have DIFFERENT spreads"),
        ("Limits", "DNOM: 0 +/- A2 x Rbar-pooled", "Standardised: 0 +/- 3, always"),
    ], kicker="BLACK BELT ONLY - SHORT RUN", accent=AMBER,
        note="Both centre every part at zero, so one chart carries the whole product mix on a single scale.")

    d.formula_card("Meridian worked DNOM - Singapore assembly cell", [
        ("Part A", "Nominal 24.0 mm, measured 24.03", "Plotted = +0.03"),
        ("Part B", "Nominal 31.5 mm, measured 31.46", "Plotted = -0.04"),
        ("Part C", "Nominal 18.2 mm, measured 18.25", "Plotted = +0.05"),
    ], kicker="BLACK BELT ONLY - SHORT RUN", accent=AMBER,
        note="Three different parts, one chart, one set of limits. The cell now has 300 points instead of 34 charts of 8.")

    # ============================================================
    # SECTION M - MULTIVARIATE SPC
    # ============================================================
    d.big_statement("BLACK BELT ONLY: Multivariate SPC",
                    "Five separate charts inflate your false alarms - and still miss the failure that matters most.",
                    "BLACK BELT ONLY - MULTIVARIATE", color=BLUE)

    d.formula_card("Problem 1 - false alarm inflation", [
        ("One chart", "P(signal) = 0.0027", "The familiar 3-sigma false alarm rate"),
        ("Five charts", "1 - (1 - 0.0027)^5 = 0.0134", "1.34 percent - five times worse"),
        ("Ten charts", "1 - (1 - 0.0027)^10 = 0.0267", "2.67 percent - a false alarm every 37 points"),
    ], kicker="BLACK BELT ONLY - MULTIVARIATE", accent=BLUE,
        note="The same alpha-inflation logic as repeated t-tests. More charts means more crying wolf.")

    d.compare_panels("Problem 2 - the failure separate charts CANNOT see", [
        ("Two correlated CTQs", "Meridian pump body", [
            "Bore diameter and piston diameter",
            "Historically they track together - r = 0.86",
            "Both machined from the same billet, same thermal cycle",
        ]),
        ("Both charts pass", "Each looks perfectly normal", [
            "Bore = 12.03 mm, well inside its limits",
            "Piston = 11.88 mm, well inside its limits",
            "Two green charts, no signal, no action taken",
        ]),
        ("The product is scrap", "The COMBINATION is impossible", [
            "That bore-piston pair has never occurred before",
            "Clearance is 0.15 mm against a 0.06 mm design",
            "The correlation broke - only a joint chart sees it",
        ]),
    ], kicker="BLACK BELT ONLY - MULTIVARIATE", accent=RED)

    d.formula_card("Hotelling's T-squared", [
        ("The statistic", "T2 = n (x-bar - mu)' S-inverse (x-bar - mu)", "Squared distance in p dimensions"),
        ("What S-inverse does", "The covariance matrix inverse", "It accounts for the CORRELATION between variables"),
        ("Control limit", "UCL from the F-distribution", "Function of p variables, m subgroups, n subgroup size"),
    ], kicker="BLACK BELT ONLY - MULTIVARIATE", accent=BLUE,
        note="T2 is a generalised squared distance from the process centroid, scaled by how the variables normally co-vary.")

    d.tile_grid("Reading the T-squared chart", [
        ("One chart, all variables", "A single line replaces p separate charts - and one honest alpha"),
        ("NO lower control limit", "T2 is a squared distance, so it cannot be negative. Only an upper limit"),
        ("The limit comes from F", "UCL uses the F-distribution, not 3 sigma - the geometry is different"),
        ("It sees correlation breaks", "A point can signal with EVERY variable inside its own limits"),
        ("It does not say which variable", "The signal is a distance. Diagnosis needs decomposition"),
        ("Pair it with a spread chart", "T2 watches the centroid; a generalised variance chart watches the spread"),
    ], kicker="BLACK BELT ONLY - MULTIVARIATE", cols=2, accent=BLUE)

    d.tile_grid("When multivariate SPC earns its keep", [
        ("Use it when CTQs correlate", "Correlation above about 0.5 - separate charts are then misleading"),
        ("Use it when p is large", "Five or more characteristics on one product or process"),
        ("Use it for assemblies", "Mating dimensions where the FIT, not each part, is the requirement"),
        ("Do NOT use it if independent", "Uncorrelated variables - separate charts are clearer and diagnostic"),
        ("Do NOT use it without software", "The matrix algebra is not a spreadsheet job for the shop floor"),
        ("Do NOT use it without training", "A T2 signal with no decomposition is a mystery, not a control"),
    ], kicker="BLACK BELT ONLY - MULTIVARIATE", cols=2, accent=BLUE)

    # ============================================================
    # SECTION N - CONTROL PLAN GOVERNANCE
    # ============================================================
    d.big_statement("BLACK BELT ONLY: Governing control plans",
                    "You do not audit your own project. You audit the portfolio - and find the decay.",
                    "BLACK BELT ONLY - GOVERNANCE", color=TEAL)

    d.tile_grid("The audit cadence across a portfolio", [
        ("30 days after handover", "Is the chart being plotted? Does the owner know they own it?"),
        ("60 days", "Have any signals occurred? Was the reaction plan actually followed?"),
        ("90 days", "Is capability holding? Has the benefit rate held against the Finance model?"),
        ("Then quarterly", "Rolling sample of control plans across all closed projects"),
        ("Trigger audits", "Any customer complaint, scrap spike or process change forces an off-cycle audit"),
        ("Report to the steering committee", "Sustainment status by project - a standing agenda item"),
    ], kicker="BLACK BELT ONLY - GOVERNANCE", cols=2, accent=TEAL)

    d.compare_panels("The common decay mode - and how to catch it", [
        ("What auditors see", "Everything looks compliant", [
            "Charts printed, posted, up to date",
            "SOP present at the workstation",
            "Owner named on the control plan",
            "The tick-box audit passes cleanly",
        ]),
        ("What is actually happening", "Signals are never actioned", [
            "Out-of-control points plotted and left uncircled",
            "No investigation record for any of them",
            "The chart has become a record, not a control",
            "The gain has already begun to erode",
        ]),
        ("The audit that catches it", "Trace signals, not charts", [
            "Pick the last three out-of-control points",
            "Demand the dated investigation for each",
            "No record means the control plan has failed",
            "This one test finds most sustainment failures",
        ]),
    ], kicker="BLACK BELT ONLY - GOVERNANCE", accent=RED)

    # ============================================================
    # SECTION O - FINANCIAL BENEFITS VALIDATION
    # ============================================================
    d.big_statement("BLACK BELT ONLY: Benefits are not real",
                    "until Finance signs them. Hard, soft and cost-avoidance are booked in three different ways.",
                    "BLACK BELT ONLY - FINANCE", color=VIOLET)

    d.compare_panels("The three benefit categories", [
        ("HARD benefit", "Hits the P&L", [
            "A cost line genuinely falls or revenue genuinely rises",
            "Scrap, rework, overtime, freight, warranty claims",
            "Traceable to a general ledger account",
            "Finance books it into the budget",
            "Meridian: scrap down SGD 340k per year",
        ]),
        ("SOFT benefit", "Capacity or time released", [
            "Hours or machine capacity freed but not yet monetised",
            "Real only if the freed resource is REDEPLOYED",
            "Finance will not book it without a redeployment plan",
            "Claim it separately, never inside the hard number",
            "Meridian: 2.1 FTE of inspection time released",
        ]),
        ("COST AVOIDANCE", "A future cost prevented", [
            "A cost that would have occurred but now will not",
            "Avoided capital, avoided headcount, avoided penalty",
            "Never reduces the current budget - nothing to cut",
            "Requires an agreed counterfactual baseline",
            "Meridian: SGD 1.2M line avoided by capacity gain",
        ]),
    ], kicker="BLACK BELT ONLY - FINANCE", accent=VIOLET)

    d.tile_grid("Why Finance treats them differently", [
        ("Hard benefits cut a budget", "A real budget line is reduced and somebody is held to the new number"),
        ("Soft benefits cut nothing", "Freed hours stay on the payroll until redeployed or removed"),
        ("Avoidance never appears", "There is no line item for a cost that never happened"),
        ("Double counting is the risk", "Two projects touching the same scrap line both claim the full saving"),
        ("Annualisation is disputed", "Three good months does not entitle you to a twelve-month number"),
        ("Credibility is the real asset", "One inflated claim and the programme's numbers are discounted forever"),
    ], kicker="BLACK BELT ONLY - FINANCE", cols=2, accent=VIOLET)

    d.flow_h("The benefits validation and sign-off process", [
        "Agree the baseline and measurement method with Finance BEFORE Improve",
        "Measure the post-improvement performance over at least 3 months",
        "Apply the agreed standard costs - Finance owns the rates, not you",
        "Separate hard, soft and cost-avoidance into three explicit lines",
        "Finance controller signs; benefit enters the tracker at the SIGNED figure",
    ], kicker="BLACK BELT ONLY - FINANCE", color=VIOLET)

    d.formula_card("Meridian worked benefit - Penang fill volume project", [
        ("Hard", "26,000 units x 0.09 mL overfill x SGD 0.14/mL", "SGD 328k per year, scrap line reduced"),
        ("Soft", "0.8 FTE of rework released", "SGD 46k - claimed ONLY with a redeployment plan"),
        ("Avoidance", "Recall provision no longer required", "SGD 180k - stated separately, never added in"),
    ], kicker="BLACK BELT ONLY - FINANCE", accent=VIOLET,
        note="Report SGD 328k signed hard benefit. Soft and avoidance are shown, labelled, and never merged into the headline.")

    # ============================================================
    # SECTION P - HANDOVER AND CLOSURE
    # ============================================================
    d.big_statement("Closure is a transaction",
                    "Ownership transfers, sustainment is verified, lessons are harvested - then the project ends.",
                    "CONTROL - CLOSURE", color=RED)

    d.flow_h("The handover sequence", [
        "Process owner named and formally accepts the control plan",
        "Operators trained on the new SOP with a signed training record",
        "Charts running in production with a rehearsed reaction plan",
        "30/60/90-day sustainability audits scheduled in the owner's calendar",
        "Finance signs the benefit; steering committee formally closes",
    ], kicker="CONTROL - CLOSURE", color=RED)

    d.tile_grid("The 30/60/90-day sustainability audit", [
        ("Day 30 - is it running?", "Charts plotted, SOP in use, owner engaged. Fix mechanics now, cheaply"),
        ("Day 60 - is it working?", "Signals investigated and closed. Reaction plan actually exercised"),
        ("Day 90 - is it holding?", "Capability at or above the improved level, benefit rate on plan"),
        ("If it has slipped", "Reopen with the sponsor. Do NOT quietly write off the benefit"),
        ("Who does the audit", "The Black Belt, not the process owner. Independence is the point"),
        ("The output", "A one-page sustainment status per project into the portfolio review"),
    ], kicker="CONTROL - CLOSURE", cols=2, accent=RED)

    d.tile_grid("Control phase - what you must be able to do now", [
        ("Select and build any chart", "Continuous or attribute, and justify the choice from first principles"),
        ("Explain why Shewhart is slow", "ARL, the lack of memory, and what a 1-sigma shift costs"),
        ("Design a CUSUM or EWMA", "Choose k and h, or lambda and L, for a stated shift size"),
        ("Handle awkward data", "Autocorrelation, short runs, correlated multivariate characteristics"),
        ("Govern control plans", "Audit a portfolio and detect the signals-never-actioned decay mode"),
        ("Validate the money", "Split hard, soft and avoidance, and defend attribution to a CFO"),
    ], kicker=K, cols=2, accent=RED)
