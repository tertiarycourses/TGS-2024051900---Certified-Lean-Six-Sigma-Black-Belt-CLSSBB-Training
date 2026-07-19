#!/usr/bin/env python3
"""Measure teaching slides — Black Belt depth."""
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


def measure_phase(d):
    K = "MEASURE - BLACK BELT DEPTH"

    # ================= 0. OPENING =================
    d.big_statement(
        "A Black Belt owns the integrity of the number",
        "Green Belts learn to measure. Black Belts learn when the measurement itself is lying, "
        "and how to prove it before a single improvement is funded.",
        K, color=TEAL)

    d.tile_grid("What Measure delivers at Black Belt level", [
        ("A mentor-grade recap", "You must be able to teach mapping, VSM, sampling and Gage R&R to your Green Belts."),
        ("Attribute MSA and Kappa", "Judgement data needs agreement analysis, not Gage R&R. Most inspection is judgement."),
        ("Nested and destructive studies", "Crossed Gage R&R is invalid when measuring destroys the part."),
        ("Non-normal capability", "Anderson-Darling, Box-Cox, Johnson and distribution fitting for skewed data."),
        ("Cp vs Cpk vs Pp vs Ppk", "Short-term against long-term variation, and which one you may honestly report."),
        ("Rational subgrouping", "The subgrouping decision made here fixes what your control chart can ever detect."),
    ], kicker=K, cols=2, accent=TEAL)

    d.compare_panels("Green Belt Measure vs Black Belt Measure", [
        ("Green Belt scope", "Apply the standard toolkit", [
            "Map the process and compute a baseline",
            "Run a continuous Gage R&R on a gauge",
            "Assume the data is roughly normal",
            "Report Cpk from the software output",
            "Sample size from the standard formula"]),
        ("Black Belt scope", "Judge, adapt and defend the method", [
            "Choose the RIGHT MSA for the data type",
            "Design nested studies for destructive tests",
            "Test normality and transform or fit correctly",
            "Separate short-term from long-term capability",
            "Design the subgrouping strategy deliberately"]),
        ("Mentoring scope", "Teach and audit others", [
            "Spot a Green Belt's invalid Gage R&R design",
            "Challenge an inflated opportunity count",
            "Catch Cpk reported on an unstable process",
            "Review data collection plans before launch",
            "Sign off the tollgate measurement evidence"]),
    ], kicker=K, accent=BLUE)

    d.flow_h("The Black Belt Measure sequence", [
        "Map the process and the value stream in full detail",
        "Define the data: type, operational definition, collection plan",
        "Design the sampling and subgrouping strategy",
        "Validate the measurement system with the CORRECT MSA method",
        "Test the distribution before computing any capability index",
        "Report baseline yield, DPMO, sigma and honest capability",
    ], kicker=K, color=TEAL)

    # ================= A. PROCESS MAPPING IN DEPTH =================
    d.big_statement(
        "Recap in depth: the process map",
        "You will mentor Green Belts through this. That means knowing not just how to draw it, "
        "but every way a map goes wrong and how to challenge one.",
        K, color=BLUE)

    p = _dg(d, "process-symbols")
    if p:
        d.image_slide("Standard process mapping symbols", p, kicker=K,
                      caption="Oval = start/stop. Rectangle = activity. Diamond = decision. "
                              "D-shape = delay. Document shape = paperwork produced.",
                      accent=BLUE)

    d.flow_h("How to build a defensible process map", [
        "Agree the start and stop boundary in writing with the process owner",
        "Walk the process physically on every shift that runs it",
        "Capture each step with the people who actually do the work",
        "Sequence, then add every decision, delay and rework loop",
        "Validate against a second shift and a second site",
        "Load the data: touch time, queue time, defect rate, headcount",
    ], kicker=K, color=BLUE)

    p = _dg(d, "swimlane-map")
    if p:
        d.image_slide("Swimlane (deployment) process map", p, kicker=K,
                      caption="Each horizontal lane is one role or system. Every lane crossing is a "
                              "handoff: a queue, a re-entry and a chance to lose context.",
                      accent=VIOLET)

    d.two_col("Meridian Suzhou: swimlanes in pump final assembly",
              [("Planning releases the work order to the line", 0),
               ("Handoff 1 to Kitting for component pick", 1),
               ("Kitting stages the assembly kit at the line head", 0),
               ("Handoff 2 to Assembly cell 3", 1),
               ("Assembly builds, then calls Test", 0),
               ("Handoff 3 to Functional Test, then to QA release", 1)],
              [("Eleven lane crossings per work order", 0),
               ("Average queue at each crossing: 25 to 190 minutes", 1),
               ("Touch time across all steps: about 71 minutes", 0),
               ("Everything else is waiting for the next lane", 1),
               ("First-pass yield 88.4 percent on the pump line", 0),
               ("Most failures are found at Test, three lanes late", 1)],
              kicker=K, lhead="THE FLOW", rhead="WHAT THE MAP REVEALED",
              lcolor=BLUE, rcolor=RED)

    d.compare_panels("Value-added analysis - the three categories", [
        ("Value-Added", "The customer would pay for it", [
            "Physically transforms the product",
            "Done right the first time",
            "Meridian: assembly, calibration, sterile pack",
            "Typically 5 to 20 percent of steps",
            "Protect and speed these up"]),
        ("Business-Value-Added", "Required but not customer value", [
            "Design History File records, lot traceability",
            "IEC 60601 test evidence, regulatory retention",
            "In medical devices BVA is large and legitimate",
            "Meridian: DHR completion, sterilisation records",
            "Streamline it - you may not delete it"]),
        ("Non-Value-Added", "Pure waste, delete it", [
            "Inspection, rework, transport, waiting",
            "Meridian: triple inspection before Test",
            "Typically 60 to 90 percent of lead time",
            "This is your improvement opportunity",
            "Attack it first - it is free capacity"]),
    ], kicker=K, accent=AMBER)

    # ================= B. VALUE STREAM MAPPING =================
    d.big_statement(
        "The value stream map is the Black Belt's system view",
        "A process map shows the work. A value stream map shows the work, the signals that trigger it, "
        "and the time the customer actually waits.",
        K, color=TEAL)

    p = _dg(d, "vsm-full")
    if p:
        d.image_slide("A complete value stream map", p, kicker=K,
                      caption="Information flow right to left across the top, material flow left to "
                              "right along the bottom, and the ladder carrying the timeline.",
                      accent=TEAL)

    p = _dg(d, "vsm-icons")
    if p:
        d.image_slide("Standard VSM icons", p, kicker=K,
                      caption="Use the standard icon set so any Lean practitioner in Singapore, "
                              "Penang or Suzhou can read your map without a legend.",
                      accent=TEAL)

    d.flow_h("Building the Meridian pump value stream map", [
        "Choose one product family: the 3-channel infusion pump, Suzhou line 4",
        "Walk the stream backwards from finished goods to the component supplier",
        "Draw material flow with a data box under every process step",
        "Add information flow: MRP release, kanban pull, expedite calls",
        "Draw the ladder: process time below, wait time above",
        "Compute lead time, VA time and process cycle efficiency",
    ], kicker=K, color=TEAL)

    d.formula_card("The VSM timeline ladder - Meridian Suzhou line 4", [
        ("Value-added time", "Sum of the lower rungs",
         "Kitting 8 min + Assembly 44 min + Test 14 min + Pack 5 min = 71 minutes."),
        ("Lead time", "Sum of the upper rungs plus VA",
         "Queues of 190 + 145 + 60 + 25 min plus 71 VA = 491 min, about 8.2 hours."),
        ("Process cycle efficiency", "PCE = VA time / Lead time",
         "71 / 491 = 0.145, so 14.5 percent. Above the 10 percent typical but far from world class."),
    ], kicker=K, accent=TEAL,
        note="World class discrete assembly runs above 25 percent PCE. The queues own the lead time, not the touch time.")

    p = _dg(d, "takt-time")
    if p:
        d.image_slide("Takt time explained", p, kicker=K,
                      caption="Takt = available working time divided by customer demand for the "
                              "same period. It is set by the customer, never by the process.",
                      accent=VIOLET)

    d.formula_card("Takt time - Meridian worked example", [
        ("Available time", "2 shifts x 7.5 h x 3600 s",
         "Suzhou line 4 runs two productive shifts of 7.5 hours = 54,000 seconds per day."),
        ("Takt time", "Takt = Available time / Demand",
         "Demand is 180 pumps per day. Takt = 54,000 / 180 = 300 seconds per pump."),
        ("Interpretation", "One pump every 300 seconds",
         "Assembly cycle time is 44 min = 2,640 s across 9 stations = 293 s per station. Just inside takt."),
    ], kicker=K, accent=VIOLET,
        note="Use productive time only - exclude breaks, shift handover briefings and planned maintenance.")

    d.waste_wheel("The eight wastes of Lean - DOWNTIME", [
        ("D", "Defects"), ("O", "Overproduction"), ("W", "Waiting"),
        ("N", "Non-utilised talent"), ("T", "Transport"), ("I", "Inventory"),
        ("M", "Motion"), ("E", "Extra-processing"),
    ], kicker=K,
        note="Waste consumes capacity, cash and lead time while adding nothing the customer values.")

    d.tile_grid("DOWNTIME at Meridian Medical Devices", [
        ("D - Defects", "Pump occlusion sensors failing functional test and returning to assembly for rework."),
        ("O - Overproduction", "Kitting a full day of assembly kits at 06:00 when only half will be consumed."),
        ("W - Waiting", "Built pumps queuing 145 minutes for a free functional test rig."),
        ("N - Non-utilised talent", "Station 6 operators know the fixture drifts, and were never asked."),
        ("T - Transport", "Sub-assemblies trucked between the Penang and Suzhou plants for calibration."),
        ("I - Inventory", "Six weeks of pressure sensors held against a single-source supply risk."),
        ("M - Motion", "Assemblers reaching behind the bench for the torque driver 400 times a shift."),
        ("E - Extra-processing", "Three manual inspections of the same solder joint before functional test."),
    ], kicker=K, cols=2, accent=RED)

    # ================= C. DATA TYPES AND OPERATIONAL DEFINITIONS =================
    d.big_statement(
        "Data type decides the entire analysis path",
        "Choose the wrong data type and every tool downstream - MSA, capability, hypothesis test, "
        "control chart - is the wrong tool. This decision is made once, in Measure.",
        K, color=AMBER)

    d.tile_grid("The four measurement scales", [
        ("Nominal", "Named categories, no order. Defect type, carrier, plant. Only counts and modes are valid."),
        ("Ordinal", "Ordered categories, unequal gaps. Severity 1-5, cosmetic grade A-D. Median, not mean."),
        ("Interval", "Equal gaps, arbitrary zero. Degrees Celsius, calendar date. Differences valid, ratios not."),
        ("Ratio", "Equal gaps, true zero. Time, weight, pressure, cost. Every statistic is valid."),
        ("Why Black Belts care", "The scale caps which statistics are meaningful, whatever the software will compute."),
        ("The classic error", "Averaging an ordinal severity score. 'Mean severity 2.7' has no physical meaning."),
    ], kicker=K, cols=2, accent=AMBER)

    d.compare_panels("Continuous vs discrete data", [
        ("Continuous (variable)", "Any value on a real scale", [
            "Infinitely divisible: 4.37 hours, 12.63 mL/h",
            "Far more information per data point",
            "Needs 20 to 30 points for a decent estimate",
            "Enables capability, t-tests, regression",
            "Meridian: flow rate, torque, test duration"]),
        ("Discrete (attribute)", "Counts and categories", [
            "Whole counts or categories: 3 defects, pass/fail",
            "Very little information per data point",
            "May need hundreds of points for the same precision",
            "Proportions, chi-square, attribute charts",
            "Meridian: pump passes or fails functional test"]),
        ("The Black Belt move", "Convert up wherever possible", [
            "Behind every pass/fail sits a measured value",
            "'Fail' hides the actual leak rate in mL/min",
            "Record the value, not just the verdict",
            "Sample size drops by an order of magnitude",
            "You also gain an early-warning signal"]),
    ], kicker=K, accent=AMBER)

    d.tile_grid("Operational definitions - two people, one number", [
        ("The test", "Two trained people measure the same unit independently and record the same number."),
        ("Define the measure", "'Occlusion alarm delay' means seconds from full occlusion to audible alarm."),
        ("Define the method", "Which rig, which firmware version, which ambient temperature, which rounding."),
        ("Define the boundary", "What is excluded: engineering builds, retest units, validation lots."),
        ("Define the decision", "The exact criterion separating conforming from non-conforming."),
        ("Pilot it first", "Run it with two appraisers. If they disagree, the definition is not finished."),
    ], kicker=K, cols=2, accent=TEAL)

    d.tile_grid("The data collection plan - the columns that matter", [
        ("What", "The exact measure and its units, tied to a written operational definition."),
        ("Who", "The named person or automated system responsible for each observation."),
        ("When", "Frequency, timing and duration - and whether it spans all shifts and all lines."),
        ("How", "Instrument, fixture, system field, check sheet, exact recording method."),
        ("Sample size", "Calculated from a target precision, never chosen for convenience."),
        ("Stratification", "Factors captured alongside each point: shift, line, operator, lot, plant."),
    ], kicker=K, cols=2, accent=BLUE)

    d.tile_grid("Stratification factors you will wish you had recorded", [
        ("Plant and line", "Singapore, Penang and Suzhou rarely behave as one population."),
        ("Shift and day of week", "Night shift and Monday start-up are classic hidden strata."),
        ("Operator and appraiser", "Needed later to separate reproducibility from process variation."),
        ("Machine, fixture and tool ID", "The only way to find a single drifting station."),
        ("Component lot and supplier", "Incoming variation often explains the output variation."),
        ("Variant and firmware revision", "Mixing variants creates artificial bi-modality in the histogram."),
    ], kicker=K, cols=2, accent=VIOLET)

    # ================= D. SAMPLING AND SAMPLE SIZE =================
    d.big_statement(
        "Sampling is a design decision, not an afterthought",
        "The sampling scheme fixes what questions your data can ever answer. "
        "Get it wrong and no amount of clever analysis later can rescue it.",
        K, color=VIOLET)

    d.tile_grid("The four probability sampling schemes", [
        ("Simple random", "Every unit has an equal chance. Use a generator, never operator intuition."),
        ("Stratified random", "Split into homogeneous strata, sample within each. Best when strata differ."),
        ("Systematic", "Every Nth unit after a random start. Fails if a process cycle matches your interval."),
        ("Cluster", "Randomly select whole groups - a shift, a lot, a line - and measure all within."),
        ("Meridian choice", "Stratify by plant then by shift: the three plants have different equipment ages."),
        ("Never", "Convenience or judgement sampling. Selection probability is unknown, so bias is unmeasurable."),
    ], kicker=K, cols=2, accent=BLUE)

    p = _dg(d, "sampling-techniques")
    if p:
        d.image_slide("Sampling techniques", p, kicker=K,
                      caption="Only probability-based methods support statistical inference. "
                              "Convenience and judgement sampling do not.",
                      accent=RED)

    d.formula_card("Sample size - CONTINUOUS data", [
        ("Formula", "n = (1.96 s / d)^2",
         "s = standard deviation, d = acceptable margin of error, 1.96 = 95 percent confidence z-value."),
        ("Meridian example", "n = (1.96 x 0.42 / 0.15)^2",
         "Estimate mean pump flow-rate error within 0.15 mL/h; pilot of 25 units gave s = 0.42 mL/h."),
        ("Result", "(5.488)^2 = 30.1 -> n = 31",
         "Thirty-one pumps. Always round the calculated sample size UP, never down."),
    ], kicker=K, accent=VIOLET,
        note="Halving the margin of error d quadruples the required sample size. Precision is bought, not wished for.")

    d.formula_card("Sample size - DISCRETE data", [
        ("Formula", "n = (1.96/d)^2 x p(1-p)",
         "p = estimated proportion defective, d = margin of error on that proportion."),
        ("Meridian example", "n = (1.96/0.02)^2 x 0.116 x 0.884",
         "Functional-test failure rate is about 11.6 percent; estimate it within +/- 2 percentage points."),
        ("Result", "9604 x 0.1025 = 984.8 -> n = 985",
         "985 pumps against 31 for the continuous measure. Attribute data is thirty times more expensive."),
    ], kicker=K, accent=RED,
        note="This single comparison is the strongest argument for converting attribute measures to continuous ones.")

    # ================= E. CONTINUOUS GAGE R&R IN FULL =================
    d.big_statement(
        "Recap in depth: continuous Gage R&R",
        "Total observed variation = true process variation + measurement system variation. "
        "Until you have split those two, every number you have is a guess with decimal places.",
        K, color=RED)

    p = _dg(d, "msa-variation-tree")
    if p:
        d.image_slide("Sources of variation - the MSA tree", p, kicker=K,
                      caption="Observed variation splits into true process variation and measurement "
                              "system variation, which splits again into repeatability and reproducibility.",
                      accent=RED)

    d.formula_card("The variation equation", [
        ("Total observed", "Var(total) = Var(process) + Var(MS)",
         "Variances add; standard deviations do not. Always work in variance terms."),
        ("Measurement system", "Var(MS) = Var(repeat) + Var(reprod)",
         "Repeatability is the equipment. Reproducibility is the appraiser."),
        ("Meridian flow rig", "Var(MS) = 0.0064 + 0.0021",
         "sigma(MS) = sqrt(0.0085) = 0.092 mL/h against a total sigma of 0.42 mL/h."),
    ], kicker=K, accent=RED)

    p = _dg(d, "msa-accuracy")
    if p:
        d.image_slide("Accuracy, linearity and stability", p, kicker=K,
                      caption="Accuracy is the offset from truth. Linearity is whether the offset "
                              "changes across the range. Stability is whether it drifts over time.",
                      accent=BLUE)

    p = _dg(d, "msa-repeatability")
    if p:
        d.image_slide("Repeatability and reproducibility", p, kicker=K,
                      caption="Gage R&R quantifies both components, so you know whether to fix the "
                              "equipment or to retrain and re-standardise the people.",
                      accent=VIOLET)

    d.compare_panels("Repeatability vs Reproducibility", [
        ("Repeatability", "Equipment variation - EV", [
            "SAME appraiser, SAME part, repeated trials",
            "Variation inherent in the device or fixture",
            "A poor result means the instrument is the problem",
            "Fix: better gauge, better fixture, finer resolution",
            "Meridian: one technician, one pump, three reads"]),
        ("Reproducibility", "Appraiser variation - AV", [
            "DIFFERENT appraisers, SAME part, same conditions",
            "Variation caused by who is doing the measuring",
            "A poor result means definition or training failed",
            "Fix: operational definitions, training, standard work",
            "Meridian: three technicians on the same 10 pumps"]),
    ], kicker=K, accent=VIOLET)

    d.flow_h("Designing a valid crossed Gage R&R", [
        "Select 10 parts spanning the FULL range of real process variation",
        "Use 3 appraisers who normally perform this measurement",
        "Each appraiser measures every part 3 times: 90 readings total",
        "Randomise the order and blind the appraisers to prior readings",
        "Run ANOVA to partition part, appraiser and interaction variance",
        "Report %study variation, %tolerance, %contribution and ndc",
    ], kicker=K, color=VIOLET)

    d.tile_grid("Design rules a Black Belt must enforce", [
        ("Parts span the real range", "Ten near-identical parts make any gauge look excellent. This is the top error."),
        ("Parts are NOT selected to spec", "Sample from actual production output, not from a bin of known good units."),
        ("Appraisers are the real users", "Studying engineers proves nothing about how night shift measures."),
        ("Randomise and blind", "Otherwise trial 2 measures memory, not the gauge."),
        ("Ten by three by three", "Fewer parts or trials collapses the degrees of freedom for the interaction term."),
        ("ANOVA, not X-bar/R", "The ANOVA method estimates the appraiser-by-part interaction. Range method cannot."),
    ], kicker=K, cols=2, accent=RED)

    d.formula_card("Gage R&R metrics - the calculations", [
        ("% Study Variation", "%SV = 100 x sigma(MS) / sigma(total)",
         "Meridian: 100 x 0.092 / 0.42 = 21.9 percent. Marginal - usable with caution."),
        ("% Tolerance", "%Tol = 100 x 6 sigma(MS) / (USL-LSL)",
         "Spec is +/- 1.0 mL/h so tolerance = 2.0. 100 x 0.552 / 2.0 = 27.6 percent. Marginal."),
        ("Number of distinct categories", "ndc = 1.41 x sigma(part) / sigma(MS)",
         "sigma(part) = sqrt(0.42^2 - 0.092^2) = 0.410. ndc = 1.41 x 0.410/0.092 = 6.3 -> 6."),
    ], kicker=K, accent=VIOLET,
        note="%Contribution is variance-based, so its thresholds are the SQUARES of the %SV thresholds: 1 and 9 percent.")

    d.tile_grid("Gage R&R acceptance rules", [
        ("Under 10 percent", "GOOD. Accept the measurement system for process improvement work."),
        ("10 to 30 percent", "MARGINAL. Acceptable only by cost, criticality and application judgement."),
        ("Over 30 percent", "UNACCEPTABLE. Do not collect a baseline. Fix the system as a mini-project first."),
        ("ndc 5 or more", "The system resolves at least 5 distinct levels of real part variation."),
        ("ndc under 5", "The gauge cannot distinguish good parts from bad. Effectively a go/no-go device."),
        ("Meridian verdict", "21.9 percent SV with ndc 6: usable for improvement, not for lot release."),
    ], kicker=K, cols=2, accent=RED)

    d.compare_panels("Acting on a failing Gage R&R", [
        ("Repeatability dominates", "The equipment is the problem", [
            "Improve gauge resolution or condition",
            "Add a fixture to standardise part positioning",
            "Service, recalibrate or replace the device",
            "Automate the reading where feasible"]),
        ("Reproducibility dominates", "People or method are the problem", [
            "Rewrite the operational definition first",
            "Retrain every appraiser to one written standard",
            "Add master reference samples and visual aids",
            "Create standard work for the measurement itself"]),
        ("Interaction is significant", "Appraisers differ by part type", [
            "One appraiser struggles only with small parts",
            "Usually a fixture or a visibility problem",
            "Look at the appraiser-by-part interaction plot",
            "Fix the physical setup, not the person"]),
    ], kicker=K, accent=RED)

    # ================= F. ATTRIBUTE MSA AND KAPPA (BLACK BELT ONLY) =================
    d.big_statement(
        "BLACK BELT ONLY: when the measurement is a judgement",
        "Most inspection in a medical device plant is a human deciding pass or fail. "
        "Gage R&R computes variances - and a pass/fail verdict has no variance to compute.",
        K, color=RED)

    d.tile_grid("Why continuous Gage R&R fails on judgement data", [
        ("No continuous scale", "Pass/fail has no mean and no standard deviation to partition."),
        ("ANOVA needs variance", "The entire R&R method rests on decomposing variance. There is none here."),
        ("Repeat reads are identical", "An appraiser almost always repeats their own verdict - falsely reassuring."),
        ("The real risk is different", "Not noise around a value, but systematically calling bad units good."),
        ("Right tool: agreement", "Attribute agreement analysis counts matches, then corrects for chance."),
        ("Meridian relevance", "Cosmetic grading, solder-joint judgement and label legibility are all judgement calls."),
    ], kicker=K, cols=2, accent=RED)

    d.compare_panels("Continuous MSA vs Attribute MSA", [
        ("Continuous Gage R&R", "For measured values", [
            "Data: a number on a real scale",
            "Method: ANOVA variance decomposition",
            "Outputs: %SV, %Tolerance, %Contribution, ndc",
            "Design: 10 parts x 3 appraisers x 3 trials",
            "Meridian: pump flow rate in mL/h"]),
        ("Attribute agreement", "For judgements and grades", [
            "Data: a category - pass/fail, grade A to D",
            "Method: agreement counting plus Kappa",
            "Outputs: % agreement and Kappa statistics",
            "Design: 30 to 50 parts x 3 appraisers x 2-3 trials",
            "Meridian: solder joint accept or reject"]),
    ], kicker=K, accent=VIOLET)

    d.flow_h("Running an attribute agreement analysis", [
        "Select 30 to 50 parts, deliberately including borderline cases",
        "Establish the true standard for every part via an expert panel",
        "Label parts with opaque random codes, no grouping or sequence",
        "Each of 3 appraisers assesses every part 2 to 3 times",
        "Fully randomise the order between every trial",
        "Compute within, between and versus-standard agreement plus Kappa",
    ], kicker=K, color=VIOLET)

    d.tile_grid("The three agreement questions", [
        ("Within-appraiser", "Does one appraiser agree with THEMSELVES across repeated trials? Repeatability."),
        ("Between-appraiser", "Do the appraisers agree with EACH OTHER? Reproducibility."),
        ("Versus the standard", "Does each appraiser agree with the KNOWN TRUTH? Accuracy - the one that matters."),
        ("All appraisers vs standard", "Does the whole inspection team, collectively, get it right?"),
        ("The dangerous case", "Perfect within and between agreement, poor versus standard: consistently wrong."),
        ("Meridian example", "Three solder inspectors agreed 96 percent with each other, 78 percent with the standard."),
    ], kicker=K, cols=2, accent=BLUE)

    d.matrix2x2("Diagnosing an attribute MSA result",
                "Agreement with the standard (accuracy)",
                "Agreement between appraisers",
                [("High between, high vs standard",
                  "The measurement system works. Proceed to baseline data collection."),
                 ("High between, LOW vs standard",
                  "Consistently wrong. The written criterion itself is incorrect or mis-taught. Fix the standard, then retrain everyone."),
                 ("LOW between, high vs standard",
                  "Averages out to truth by luck. Individual appraisers disagree - retrain and add reference samples."),
                 ("LOW between, LOW vs standard",
                  "No usable measurement system. Stop. Rebuild the definition, the boundary samples and the training.")],
                kicker=K, accent=RED)

    d.big_statement(
        "Kappa: agreement after chance is removed",
        "Two inspectors flipping coins on a pass/fail decision agree half the time. "
        "Raw agreement rewards them for that. Kappa does not.",
        K, color=VIOLET)

    d.formula_card("Cohen's Kappa - the chance correction", [
        ("Kappa", "K = (Po - Pe) / (1 - Pe)",
         "Po = observed proportion agreeing. Pe = proportion expected to agree by chance alone."),
        ("Numerator", "Po - Pe",
         "Agreement actually achieved ABOVE what random guessing would deliver."),
        ("Denominator", "1 - Pe",
         "The maximum agreement available above chance. So Kappa is the fraction of that maximum earned."),
    ], kicker=K, accent=VIOLET,
        note="K = 1 is perfect agreement. K = 0 is exactly chance. K below 0 means worse than random guessing.")

    d.formula_card("Meridian worked example - why 90 percent can be a poor Kappa", [
        ("The data", "100 solder joints, 2 inspectors",
         "Both said PASS on 88. Both said FAIL on 2. They disagreed on 10 joints."),
        ("Observed agreement", "Po = (88 + 2)/100 = 0.90",
         "Ninety percent raw agreement. This is the number a manager will quote in a meeting."),
        ("Expected by chance", "Pe = (0.93x0.95) + (0.07x0.05)",
         "Inspector A passed 93, B passed 95. Pe = 0.8835 + 0.0035 = 0.887."),
    ], kicker=K, accent=RED,
        note="Now compute Kappa: K = (0.90 - 0.887) / (1 - 0.887) = 0.013 / 0.113 = 0.115. Effectively no real agreement.")

    d.tile_grid("Why the Kappa collapsed at 90 percent agreement", [
        ("The base rate is extreme", "93 to 95 percent of joints pass, so chance agreement alone is already 88.7 percent."),
        ("The 90 percent is nearly free", "Two inspectors who ALWAYS say pass would score 88 percent agreement."),
        ("Kappa exposes it", "0.115 says the inspectors add almost nothing beyond a default 'pass' reflex."),
        ("Where they disagree matters", "All 10 disagreements sit on the defective joints - the only ones that count."),
        ("The lesson", "Never report raw agreement alone on a rare-event judgement. Always report Kappa."),
        ("The fix", "Rebalance the study sample and retrain against physical boundary specimens."),
    ], kicker=K, cols=2, accent=RED)

    d.ladder("Kappa acceptance criteria", [
        ("Below 0.40", "Poor. No usable agreement. Rebuild the whole measurement method."),
        ("0.40 to 0.75", "Marginal. Act now: retrain, add boundary samples, rewrite the criterion."),
        ("0.75 to 0.90", "Acceptable. Usable for improvement work, with monitoring."),
        ("0.90 and above", "Excellent. Suitable for lot release and regulatory decisions."),
    ], kicker=K, accent=TEAL,
        note="Six Sigma practice: below 0.75 you must act. At or above 0.90 the inspection system is genuinely reliable.")

    d.compare_panels("Cohen's Kappa vs Fleiss' Kappa", [
        ("Cohen's Kappa", "Exactly TWO raters", [
            "Pairwise agreement between two appraisers",
            "Or one appraiser against the known standard",
            "Or one appraiser against themselves, trial 1 vs 2",
            "With 3 appraisers you get 3 pairwise Kappas",
            "Meridian: inspector A vs inspector B"]),
        ("Fleiss' Kappa", "THREE OR MORE raters", [
            "One overall statistic across the whole panel",
            "Handles a different rater set per item if needed",
            "Same 0 to 1 scale and same acceptance thresholds",
            "Reports team agreement, not pairwise agreement",
            "Meridian: all 3 solder inspectors together"]),
        ("Weighted Kappa", "For ORDERED categories", [
            "Used when categories have a natural order",
            "Grade A vs B disagreement penalised less than A vs D",
            "Essential for cosmetic grading scales",
            "Unweighted Kappa treats all errors as equal",
            "Meridian: enclosure cosmetic grade A to D"]),
    ], kicker=K, accent=BLUE)

    d.content("Attribute MSA traps that a Black Belt must catch", [
        "Reporting raw percent agreement with no Kappa - the single most common and most misleading error.",
        "A study sample with 95 percent good units, which lets a lazy 'always pass' score above 90 percent.",
        "Omitting the known standard, so you can prove consistency but never prove correctness.",
        "Using only 20 parts, giving a Kappa confidence interval so wide the point estimate is meaningless.",
        "Testing the day-shift engineers when the real inspection happens on night shift with different lighting.",
        "Accepting Kappa 0.72 as 'close enough to 0.75' when the decision releases implanted-device components.",
    ], kicker=K)

    # ================= G. NESTED AND DESTRUCTIVE STUDIES (BB ONLY) =================
    d.big_statement(
        "BLACK BELT ONLY: when measuring destroys the part",
        "Leak testing to burst, peel strength, sterility, weld pull force. The part does not survive, "
        "so no appraiser can ever measure the same part twice. The crossed design is mathematically impossible.",
        K, color=RED)

    d.compare_panels("Crossed vs Nested gauge study designs", [
        ("Crossed design", "The standard Gage R&R", [
            "EVERY appraiser measures EVERY part",
            "Requires the part to survive measurement",
            "Estimates part, appraiser AND their interaction",
            "10 parts x 3 appraisers x 3 trials",
            "Meridian: pump flow rate, non-destructive"]),
        ("Nested design", "For destructive measurement", [
            "Each part is measured by ONE appraiser, ONCE",
            "Parts are NESTED within appraiser or within batch",
            "Cannot estimate the appraiser-by-part interaction",
            "Relies on homogeneous batches as pseudo-repeats",
            "Meridian: seal peel strength, destructive"]),
    ], kicker=K, accent=RED)

    d.tile_grid("The homogeneous batch assumption", [
        ("The core idea", "If parts within a batch are truly identical, different parts act as repeat measures."),
        ("How to build one", "Consecutive units, one lot, one machine, one operator, one short time window."),
        ("The critical risk", "Any real within-batch variation is counted as measurement repeatability."),
        ("Consequence", "Repeatability is CONFOUNDED with within-batch part variation and always overstated."),
        ("So the result is conservative", "A nested study that passes is trustworthy. One that fails may be a false alarm."),
        ("Meridian batches", "Ten seal pouches from one sealer, one reel, one 5-minute window, per batch."),
    ], kicker=K, cols=2, accent=AMBER)

    d.flow_h("Designing a nested destructive study at Meridian", [
        "Form 30 homogeneous batches of 3 sterile-barrier pouches each",
        "Confirm homogeneity: same sealer, reel, settings, 5-minute window",
        "Assign each batch to ONE appraiser at random",
        "That appraiser peel-tests all 3 pouches from their batches",
        "Run a NESTED ANOVA: part within batch, batch within appraiser",
        "Report %study variation, remembering repeatability is inflated",
    ], kicker=K, color=VIOLET)

    d.formula_card("Nested study - Meridian seal peel strength", [
        ("The design", "30 batches x 3 pouches, nested",
         "Ten batches per appraiser, three appraisers, 90 destructive peel tests in total."),
        ("Repeatability estimate", "sigma(rep) = 0.31 N",
         "This is equipment noise PLUS true within-batch pouch variation. It cannot be separated."),
        ("% Study variation", "100 x 0.34 / 1.08 = 31.5%",
         "sigma(MS) = 0.34 N against total 1.08 N. Above 30 percent - but the estimate is inflated."),
    ], kicker=K, accent=RED,
        note="A nested result above 30 percent needs investigation of batch homogeneity BEFORE condemning the gauge.")

    d.tile_grid("Other situations that force a nested design", [
        ("Consumed chemical assays", "The aliquot is gone once it has been analysed. No second read exists."),
        ("Sterility and bioburden", "The test article is destroyed by the test procedure itself."),
        ("Pull-force testing", "Weld, crimp and solder joints are broken in order to obtain the reading."),
        ("Life and burst testing", "The unit is deliberately taken to failure to get the number."),
        ("Altering measurements", "Any test that meaningfully changes the part, even if it survives."),
        ("The rule of thumb", "If measuring twice would not give the same part, you need a nested design."),
    ], kicker=K, cols=2, accent=RED)

    # ================= H. YIELD, DPMO AND SIGMA =================
    d.big_statement(
        "Recap in depth: yield, defects and sigma level",
        "Four different yield numbers can be computed from the same process. "
        "Three of them flatter you. A Black Belt insists on the fourth.",
        K, color=BLUE)

    d.tile_grid("DUDO - agree these four before computing anything", [
        ("D - Defect", "Any single failure to meet a customer requirement - one CTQ unmet on one unit."),
        ("U - Unit", "The deliverable the customer receives. At Meridian: one infusion pump."),
        ("D - Defect opportunity", "Every distinct way one unit could fail. Count only realistic, inspected modes."),
        ("O - Observed defects", "The actual defect count found in the sample you inspected."),
        ("Why opportunities matter", "DPMO normalises complexity so a simple product compares fairly with a complex one."),
        ("Be conservative", "Inflating the opportunity count flatters your sigma level. Auditors always check this."),
    ], kicker=K, cols=2, accent=BLUE)

    d.compare_panels("Four ways to measure yield", [
        ("Classic yield", "Units out / units in", [
            "Counts anything that eventually shipped",
            "Rework and retest are completely invisible",
            "Always the most flattering number available",
            "Meridian pump line: 98.2 percent"]),
        ("First pass yield", "Right first time at ONE step", [
            "Units through with no rework or repair",
            "Computed step by step across the line",
            "Exposes rework at each individual station",
            "Meridian assembly step: 88.4 percent"]),
        ("Rolled throughput yield", "Right first time ACROSS all steps", [
            "RTY = FPY1 x FPY2 x ... x FPYn",
            "Probability a unit passes every step cleanly",
            "Falls fast as the step count rises",
            "Meridian pump line: 71.6 percent"]),
        ("Normalised yield", "The per-step average", [
            "Ynorm = RTY^(1/n) for n steps",
            "The typical yield of an average step",
            "Useful for comparing lines of different lengths",
            "Meridian: 0.716^(1/6) = 94.6 percent"]),
    ], kicker=K, accent=RED)

    d.formula_card("Rolled throughput yield - Meridian Suzhou line 4", [
        ("RTY formula", "RTY = FPY1 x FPY2 x ... x FPYn",
         "Multiply the first pass yield of every step in the chain."),
        ("Six steps", "0.982 x 0.951 x 0.884 x 0.974 x 0.962 x 0.991",
         "Kitting, sub-assembly, main assembly, calibration, functional test, final pack."),
        ("Result", "RTY = 0.716",
         "71.6 percent, against a classic yield of 98.2 percent. The 26.6 point gap is the hidden factory."),
    ], kicker=K, accent=RED,
        note="Each step looks respectable. Only the product of them reveals what the customer experience really is.")

    d.formula_card("DPU, DPO and DPMO", [
        ("DPU", "DPU = Defects / Units",
         "Average number of defects carried by each unit produced."),
        ("DPO", "DPO = Defects / (Units x Opportunities)",
         "Defects per single opportunity, normalised for product complexity."),
        ("DPMO", "DPMO = DPO x 1,000,000",
         "Scaled to a million opportunities so any two processes can be compared directly."),
    ], kicker=K, accent=VIOLET)

    d.formula_card("DPMO - Meridian pump baseline", [
        ("Units and defects", "3,600 pumps, 486 defects",
         "One month of Suzhou line 4 output, with all defect records from every station."),
        ("DPU and DPO", "DPU = 486/3600 = 0.135",
         "With 14 inspected opportunities per pump: DPO = 486 / (3600 x 14) = 0.00964."),
        ("DPMO and sigma", "DPMO = 9,643",
         "Between 4 sigma (6,210) and 3.5 sigma (22,750). Meridian sits at about 3.84 sigma."),
    ], kicker=K, accent=RED,
        note="The 1.5 sigma shift convention is built into these DPMO tables. State that assumption whenever you report sigma level.")

    d.ladder("The sigma scale - DPMO at each level", [
        ("1 sigma", "690,000 DPMO"),
        ("2 sigma", "308,000 DPMO"),
        ("3 sigma", "66,800 DPMO"),
        ("4 sigma", "6,210 DPMO"),
        ("5 sigma", "233 DPMO"),
        ("6 sigma", "3.4 DPMO"),
    ], kicker=K, accent=TEAL,
        note="Each level is roughly a ten-fold defect reduction. Meridian at 3.84 sigma has two full levels to climb.")

    # ================= I. NON-NORMAL CAPABILITY (BB ONLY) =================
    d.big_statement(
        "BLACK BELT ONLY: capability when the data is not normal",
        "Cp, Cpk, Pp and Ppk all assume a normal distribution. Cycle times, leak rates and "
        "impurity levels almost never are. Running the index anyway produces a confident, wrong number.",
        K, color=VIOLET)

    d.normal_curve("The normal distribution and the empirical rule", kicker=K,
                   note="68.26 percent within +/-1 sigma, 95.46 percent within +/-2 sigma, "
                        "99.73 percent within +/-3 sigma. Capability indices depend entirely on this.")

    d.tile_grid("Why non-normality wrecks a capability index", [
        ("Cpk is a tail probability", "It converts a distance in sigma into a defect rate using normal tails."),
        ("Skewed data has fatter tails", "A right-skewed process produces far more high-side defects than Cpk predicts."),
        ("The error is not small", "A Cpk of 1.33 on lognormal data can hide a real defect rate ten times higher."),
        ("Bounded data is never normal", "Leak rate, impurity and cycle time are bounded at zero and skew right."),
        ("Software will not warn you", "It computes Cpk on any column of numbers you give it, silently."),
        ("Black Belt discipline", "Test normality BEFORE computing any capability index. Every single time."),
    ], kicker=K, cols=2, accent=RED)

    d.flow_h("The non-normal capability decision path", [
        "Plot the data: histogram, probability plot, and a time-ordered run chart",
        "Confirm stability first - capability on an unstable process is meaningless",
        "Run Anderson-Darling: p below 0.05 rejects normality",
        "Try a transformation: Box-Cox first, then Johnson if Box-Cox fails",
        "If no transform works, fit the correct distribution: Weibull, lognormal, exponential",
        "Compute capability in that distribution and report in ORIGINAL units",
    ], kicker=K, color=VIOLET)

    d.formula_card("Anderson-Darling normality test", [
        ("The hypotheses", "H0: data is normal",
         "H1: data is not normal. AD is preferred because it weights the TAILS, which drive capability."),
        ("The decision rule", "p < 0.05 -> reject normality",
         "p at or above 0.05 means you have no evidence against normal. Not proof that it IS normal."),
        ("Meridian example", "AD = 1.84, p = 0.002",
         "Pump leak-rate data on 120 units. Normality firmly rejected - do not compute Cpk on this raw data."),
    ], kicker=K, accent=RED,
        note="With very large n, AD rejects trivial departures. With small n it lacks power. Always look at the probability plot too.")

    d.compare_panels("Three routes for non-normal capability", [
        ("Box-Cox transform", "A power transformation family", [
            "Y' = (Y^lambda - 1)/lambda, lambda estimated from data",
            "lambda = 0 is the natural log; 0.5 is the square root",
            "Requires strictly positive data",
            "Simple, widely accepted, easy to explain",
            "Meridian leak rate: lambda = 0 works well"]),
        ("Johnson transform", "A flexible three-family system", [
            "Johnson SB, SL and SU cover bounded and unbounded",
            "Succeeds on many datasets where Box-Cox fails",
            "Handles negative values and bounded ranges",
            "Harder to explain to a steering committee",
            "Use when Box-Cox residuals still fail AD"]),
        ("Fit the distribution", "Model the physics instead", [
            "Weibull for life, strength and time-to-failure",
            "Lognormal for multiplicative, right-skewed data",
            "Exponential for constant-hazard arrival times",
            "No transformation, so no back-transform needed",
            "Preferred when theory suggests the distribution"]),
    ], kicker=K, accent=VIOLET)

    d.formula_card("Box-Cox on Meridian pump leak rate", [
        ("Raw data", "AD p = 0.002, right skewed",
         "120 pumps, leak rate in mL/min, USL 0.50, bounded below at zero. Clearly non-normal."),
        ("Transform", "lambda = 0, so Y' = ln(Y)",
         "Box-Cox estimates lambda near zero, giving the natural log. AD on ln(Y) now gives p = 0.41."),
        ("Capability", "Ppk computed on ln(Y)",
         "USL transformed to ln(0.50) = -0.693. Ppk = 0.94 - back-report as 0.94 in original terms."),
    ], kicker=K, accent=TEAL,
        note="Always transform the SPEC LIMITS too, and always present the final result in the customer's original units.")

    d.content("The percentile method - capability without a transform", [
        "Normal capability compares spec limits against the 0.135 and 99.865 percentiles of the fitted normal.",
        "The percentile method uses the same two percentiles taken from the FITTED non-normal distribution.",
        "Ppu = (USL - median) / (P99.865 - median) and Ppl = (median - LSL) / (median - P0.135).",
        "Ppk is then the smaller of Ppu and Ppl, exactly as in the normal case.",
        "The advantage: the result is already in original units, with no back-transformation needed.",
        "Minitab calls this the ISO / Z-score method; state clearly which one you used in the report.",
    ], kicker=K)

    # ================= J. Cp Cpk Pp Ppk (BB ONLY) =================
    d.big_statement(
        "BLACK BELT ONLY: Cp, Cpk, Pp and Ppk are four different claims",
        "The four indices differ in one thing only: which sigma goes in the denominator. "
        "That single choice decides whether you are describing a good day or a real year.",
        K, color=BLUE)

    d.matrix2x2("The capability index family",
                "Does the index account for centring?",
                "Which sigma is used",
                [("Cp - ignores centring",
                  "Uses WITHIN-subgroup sigma (short-term). Potential capability: what the process could do if perfectly centred."),
                 ("Cpk - accounts for centring",
                  "Uses WITHIN-subgroup sigma (short-term). Actual short-term capability, the smaller of the two one-sided indices."),
                 ("Pp - ignores centring",
                  "Uses TOTAL sigma (long-term). Overall potential performance across everything the process actually did."),
                 ("Ppk - accounts for centring",
                  "Uses TOTAL sigma (long-term). The honest number: what the customer actually received over the period.")],
                kicker=K, accent=BLUE)

    d.formula_card("The four indices", [
        ("Cp and Pp", "(USL - LSL) / 6 sigma",
         "Cp uses sigma-within (from R-bar/d2). Pp uses sigma-total (the ordinary sample sigma)."),
        ("Cpk", "min[(USL-Xbar), (Xbar-LSL)] / 3 s(within)",
         "The worse of the two sides, so an off-centre process is correctly penalised."),
        ("Ppk", "min[(USL-Xbar), (Xbar-LSL)] / 3 s(total)",
         "Same structure, but the denominator includes ALL the between-subgroup variation."),
    ], kicker=K, accent=VIOLET,
        note="sigma-within is estimated from within-subgroup ranges. sigma-total is the plain standard deviation of all data.")

    d.formula_card("Meridian worked example - the Cpk / Ppk gap", [
        ("The process", "Pump flow accuracy, USL +1.0, LSL -1.0",
         "60 subgroups of 5 units over 12 weeks. Overall mean = +0.14 mL/h."),
        ("Short term", "s(within) = 0.19 -> Cpk = 1.51",
         "Cpk = min(1.0-0.14, 0.14+1.0) / (3 x 0.19) = 0.86 / 0.57 = 1.51. Looks comfortably capable."),
        ("Long term", "s(total) = 0.42 -> Ppk = 0.68",
         "Ppk = 0.86 / (3 x 0.42) = 0.68. The same process, honestly reported, is NOT capable."),
    ], kicker=K, accent=RED,
        note="A Cpk of 1.51 with a Ppk of 0.68 does not mean the gauge is wrong. It means the process is drifting between subgroups.")

    d.tile_grid("Reading the Cpk to Ppk gap", [
        ("Cpk approximately Ppk", "The process is stable. Within-subgroup and total variation agree. Trust both."),
        ("Cpk much greater than Ppk", "Significant between-subgroup drift, shift or special cause. Cpk is flattering you."),
        ("Meridian: 1.51 vs 0.68", "A large gap: shift-to-shift and lot-to-lot drift the control chart must catch."),
        ("The ratio is a diagnostic", "Cpk/Ppk is roughly a stability index. Far above 1 means unstable."),
        ("Never report Cpk alone", "On an unstable process Cpk describes a good hour, not the customer's year."),
        ("What the customer got", "Ppk. Always Ppk. That is the number that maps to real received defect rates."),
    ], kicker=K, cols=2, accent=RED)

    d.compare_panels("When to report which index", [
        ("Report Cp / Cpk", "Short-term, stable, controlled", [
            "The process is demonstrably in statistical control",
            "Subgroups are rationally formed",
            "Machine capability studies over a short run",
            "Process validation runs under fixed conditions",
            "State that it is short-term capability"]),
        ("Report Pp / Ppk", "Long-term, real performance", [
            "Baseline capability in the Measure phase",
            "Any process not yet proven stable",
            "Customer or regulator performance reporting",
            "Post-improvement verification in Control",
            "This is the default at Meridian"]),
        ("Report BOTH", "The Black Belt standard", [
            "The gap between them is itself the finding",
            "It quantifies the opportunity from stabilising alone",
            "It prevents the accusation of cherry-picking",
            "It tells the sponsor where to invest first",
            "Always with the sample period stated"]),
    ], kicker=K, accent=TEAL)

    # ================= K. RATIONAL SUBGROUPING (BB ONLY) =================
    d.big_statement(
        "BLACK BELT ONLY: rational subgrouping",
        "How you group the data decides what variation lands inside a subgroup and what lands between them. "
        "That single choice determines what your control chart is capable of ever detecting.",
        K, color=AMBER)

    d.tile_grid("The rational subgrouping principle", [
        ("Within-subgroup", "Should contain ONLY common-cause noise. This becomes the yardstick for the limits."),
        ("Between-subgroup", "Is what the chart tests against that yardstick. This is what you want to detect."),
        ("The design question", "What source of variation do I want this chart to catch? Put it BETWEEN subgroups."),
        ("Consecutive units", "The classic rational subgroup: 5 consecutive pumps, minimising within-subgroup spread."),
        ("Control limits follow", "Limits are computed from within-subgroup variation, so wide subgroups mean wide limits."),
        ("Get it wrong", "Wide limits that flag nothing, or tight limits that flag everything. Both useless."),
    ], kicker=K, cols=2, accent=BLUE)

    d.compare_panels("Two subgrouping strategies, same data", [
        ("Consecutive sampling", "5 units back to back", [
            "Within-subgroup captures only machine noise",
            "Shift and lot differences land BETWEEN subgroups",
            "Control limits are tight",
            "The chart DETECTS shift and lot changes",
            "This is what you almost always want"]),
        ("Spread sampling", "1 unit per hour over 5 hours", [
            "Within-subgroup absorbs the drift across the shift",
            "Drift is now inside, not between, subgroups",
            "Control limits become wide",
            "The chart CANNOT detect the drift it swallowed",
            "A stable-looking chart on a drifting process"]),
    ], kicker=K, accent=RED)

    d.formula_card("Meridian subgrouping - the same 300 pumps, two ways", [
        ("Consecutive design", "5 consecutive pumps, hourly",
         "s(within) = 0.19. Control limits Xbar +/- 0.25. Shift changes flag clearly on the chart."),
        ("Spread design", "1 pump every 12 min for an hour",
         "s(within) = 0.38. Control limits Xbar +/- 0.51. The same shift changes now sit inside the limits."),
        ("The consequence", "Same process, opposite verdict",
         "Design one says 14 out-of-control signals in 12 weeks. Design two says the process is perfectly stable."),
    ], kicker=K, accent=RED,
        note="Nothing about the process changed. Only the subgrouping. This is why the Black Belt owns this decision.")

    # ================= L. BASELINE AND CLOSE =================
    d.run_chart("Meridian Suzhou line 4 - weekly first pass yield",
                [("W1", 88.4), ("W2", 90.1), ("W3", 86.2), ("W4", 89.7), ("W5", 84.1),
                 ("W6", 88.9), ("W7", 91.2), ("W8", 83.6), ("W9", 87.4), ("W10", 90.3),
                 ("W11", 85.8), ("W12", 88.1)],
                kicker=K,
                note="Common-cause variation around a stable median. The process is consistently at 88 percent, "
                     "not occasionally. That means a system fix, not a people fix.")

    d.tile_grid("The Measure tollgate evidence pack", [
        ("Validated process map and VSM", "Walked, verified on a second shift, with the timeline ladder loaded."),
        ("Data collection plan", "Operational definitions, sampling scheme, stratification factors, sample sizes."),
        ("MSA evidence", "The RIGHT study for the data type, with acceptance criteria met or a fix plan attached."),
        ("Distribution evidence", "Normality test result and the transformation or fitted distribution used."),
        ("Baseline performance", "RTY, DPMO, sigma level, and Ppk with Cpk alongside for the stability gap."),
        ("Refined problem statement", "The Define scope narrowed to where the data proves the pain sits."),
    ], kicker=K, cols=2, accent=TEAL)

    d.tile_grid("Black Belt Measure failure modes", [
        ("Gage R&R on judgement data", "Running a variance study on pass/fail data. Use attribute agreement and Kappa."),
        ("Raw agreement with no Kappa", "90 percent agreement on a rare-event call can hide a Kappa near zero."),
        ("Crossed design on destructive tests", "Mathematically impossible. It means the study was never really run."),
        ("Cpk on non-normal data", "A confident index computed on an assumption that was never tested."),
        ("Cpk on an unstable process", "Reporting a good hour as if it were the customer's year. Report Ppk."),
        ("Default subgrouping", "Accepting whatever the software offers, then wondering why nothing ever flags."),
    ], kicker=K, cols=2, accent=RED)

    d.checkpoint("Measure phase - Black Belt checkpoint", [
        "Two inspectors agree on 90 of 100 parts. Why might their Kappa still be near zero?",
        "Your peel test destroys the pouch. Design a valid MSA and state what you cannot estimate.",
        "Anderson-Darling gives p = 0.002 on your leak-rate data. State your next three actions.",
        "Cpk is 1.51 and Ppk is 0.68 on the same data. What does that gap tell you, and what do you report?",
        "You want a chart that detects shift-to-shift differences. How must you form the subgroups, and why?",
        "Compute Meridian's DPMO from 3,600 pumps, 486 defects and 14 opportunities, and give the sigma level.",
    ], K)
