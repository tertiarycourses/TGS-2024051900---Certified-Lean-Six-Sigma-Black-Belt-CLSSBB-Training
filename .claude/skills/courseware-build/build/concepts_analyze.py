#!/usr/bin/env python3
"""Analyze teaching slides — Black Belt depth."""
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


def analyze_phase(d):
    K = "ANALYZE - BLACK BELT DEPTH"
    KR = "ANALYZE - RECAP IN DEPTH"
    KB = "ANALYZE - BLACK BELT ONLY"

    # ============================================================
    # SECTION 0 - OPENING
    # ============================================================
    d.big_statement(
        "Analyze is where the Black Belt earns the title",
        "Measure told us Meridian runs 8.9 percent OTIF misses and 91.4 percent first-pass "
        "yield. Analyze proves WHICH Xs drive that - with statistics a sponsor will fund and "
        "an auditor will accept.",
        K, color=VIOLET)

    d.tile_grid("What Analyze delivers at Black Belt level", [
        ("A validated, ranked list of Xs", "Two or three proven drivers, each with a p-value and an effect size in units"),
        ("A fitted predictive model", "Y = f(X) with coefficients, adjusted R-squared and validated residuals"),
        ("Interaction knowledge", "Which fixes work everywhere and which only work at one plant"),
        ("A variation family diagnosis", "Positional, cyclical or temporal - so Improve spends money in the right place"),
        ("Assumption-clean evidence", "Every test with its normality, independence and variance check documented"),
        ("A translated business case", "Coefficients converted into dollars, risk and a decision the sponsor can sign"),
    ], kicker=K, cols=2, accent=VIOLET)

    d.compare_panels("Green Belt Analyze vs Black Belt Analyze", [
        ("GREEN BELT", "One X at a time", [
            "2-sample t-test, chi-square, simple regression",
            "Tests one factor against Y in isolation",
            "Reports r and R-squared, stops there",
            "Assumes normality without checking it",
            "Answers: is this X related to Y?",
        ]),
        ("BLACK BELT", "Many Xs, with diagnostics", [
            "Multiple regression, ANOVA, multi-vari, non-parametrics",
            "Models several Xs simultaneously and their interactions",
            "Reports adjusted R-squared, VIF and residual plots",
            "Tests every assumption and switches test when violated",
            "Answers: how much of Y does each X explain, and is it valid?",
        ]),
        ("THE MENTOR ROLE", "You coach both", [
            "You must teach a Green Belt the simple tools cleanly",
            "You must know when their simple tool is wrong",
            "You review their test selection before they run it",
            "You catch the assumption they did not check",
            "You translate their output for the sponsor",
        ]),
    ], kicker=K, accent=BLUE)

    d.flow_h("The Analyze route map for this module", [
        "Recap variation, run charts, Pareto and cause tools in full depth",
        "Recap hypothesis testing and build the test-selection decision tree",
        "Advance into multiple regression and model diagnostics",
        "Advance into ANOVA, interactions and non-parametric alternatives",
        "Run a multi-vari study to isolate the variation family",
        "Translate every statistic into money and a sponsor decision",
    ], kicker=K, color=VIOLET)

    d.tile_grid("The Meridian Medical Devices case we will use throughout", [
        ("Three plants", "Singapore (lines 1-2), Penang (lines 3-4), Suzhou (lines 5-6)"),
        ("The product", "Infusion pump assemblies - Class IIb regulated medical devices"),
        ("Primary Y", "OTIF delivery to hospital distributors, currently 91.1 percent"),
        ("Secondary Y", "First-pass yield at final functional test, currently 91.4 percent"),
        ("The pain", "Warranty returns at 2.8 percent, costing SGD 4.1 million per year"),
        ("The mandate", "Steering committee wants OTIF to 97 percent within two quarters"),
    ], kicker=K, cols=2, accent=TEAL)

    # ============================================================
    # SECTION 1 - RECAP: VARIATION
    # ============================================================
    d.big_statement(
        "Recap 1 - Variation, and the discipline not to react",
        "A Black Belt is asked about a moved number every single day. Everything you do in "
        "Analyze rests on telling ordinary variation from a real signal.",
        KR, color=TEAL)

    d.compare_panels("Common cause vs special cause variation", [
        ("COMMON CAUSE", "Inherent, random, always present", [
            "Built into the process design itself",
            "Many small sources acting together at once",
            "Predictable within a range - the process is stable",
            "Fix requires a SYSTEM change owned by management",
            "Meridian: line 3 yield varying between 89 and 94 percent",
        ]),
        ("SPECIAL CAUSE", "Assignable to one identifiable event", [
            "Something changed - it is not part of the system",
            "One traceable source you can name and date",
            "Unpredictable - appears as a signal on the chart",
            "Fix is LOCAL: find it, remove it, prevent recurrence",
            "Meridian: Suzhou yield fell to 71 percent the week the solder pot was replaced",
        ]),
    ], kicker=KR, accent=TEAL)

    d.tile_grid("Why the distinction decides your entire strategy", [
        ("Wrong diagnosis, wrong owner", "Special cause is a local fix. Common cause needs management to change the system."),
        ("Blame follows the error", "Treating common cause as special sends you hunting an operator who is not at fault."),
        ("Roughly 85 percent is systemic", "Deming: most defects come from the process, not the person running it."),
        ("It picks the tool", "Special cause: investigate the event. Common cause: run the full DMAIC."),
        ("Stability comes first", "You cannot judge capability or test causes on an unstable process."),
        ("It licenses inaction", "Knowing variation is common cause is what permits you to leave the process alone."),
    ], kicker=KR, cols=2, accent=TEAL)

    d.big_statement(
        "Tampering - the most expensive habit in manufacturing",
        "Adjusting a stable process in response to common cause variation does not reduce "
        "variation. It roughly DOUBLES it. Deming proved this with a funnel and a marble.",
        KR, color=RED)

    d.flow_h("The Deming funnel experiment", [
        "Fix a funnel above a target, drop 50 marbles, mark where each lands",
        "Rule 1: never move the funnel. Marbles scatter in a stable circle around the target",
        "Rule 2: move the funnel to correct each miss. Scatter grows about 40 percent wider",
        "Rule 3: move the funnel from the target to the opposite of the last drop. Scatter explodes",
        "Rule 4: aim the funnel at the last marble. The pattern drifts away without limit",
        "Lesson: adjusting a stable process on one data point always makes it worse",
    ], kicker=KR, color=RED)

    d.compare_panels("Tampering at Meridian - a real Tuesday", [
        ("THE TRIGGER", "One ordinary point moves", [
            "Penang line 4 first-pass yield drops from 92 to 89 percent",
            "Both values sit inside normal common cause range",
            "Nothing in the process actually changed",
            "But the number appears in red on the daily dashboard",
        ]),
        ("THE REACTION", "The supervisor adjusts", [
            "Reflow oven zone 3 setpoint raised by 6 degrees C",
            "Two operators moved from line 3 to line 4 for the shift",
            "The adjustment is well intentioned and quick",
            "No data supports it - only the single point",
        ]),
        ("THE RESULT", "Variation roughly doubles", [
            "Line 3 now understaffed and starts missing takt",
            "Higher reflow temperature warps two connector housings",
            "Next swing is bigger, prompting a bigger correction",
            "Rule: never adjust a stable process on one data point",
        ]),
    ], kicker=KR, accent=RED)

    # --------- RUN CHARTS ---------
    d.big_statement(
        "Run charts - six patterns, six run rules",
        "The run chart is the cheapest signal detector in the toolkit. A Black Belt reads all "
        "six patterns and knows the exact rule that fires each one.",
        KR, color=BLUE)

    p = _dg(d, "run-chart-base")
    if p:
        d.image_slide("Anatomy of a run chart", p, kicker=KR,
                      caption="Time on the horizontal axis, the measure on the vertical axis, and a "
                              "MEDIAN centre line - not a mean, because the median resists outliers.",
                      accent=BLUE)

    d.tile_grid("How to build a run chart correctly", [
        ("Plot in TIME ORDER", "Sequence is the whole point - sorting the data destroys the information"),
        ("Use the MEDIAN centre line", "The median is not dragged by the extreme points you are hunting"),
        ("At least 15 to 20 points", "Fewer points cannot reliably reveal a trend, shift or oscillation"),
        ("Keep the interval constant", "Daily or weekly - do not mix, and do not skip periods"),
        ("Annotate known events", "Mark the oven rebuild or the supplier change so signals can be explained"),
        ("Read patterns, not points", "One high point is noise. A PATTERN is a signal worth investigating."),
    ], kicker=KR, cols=2, accent=BLUE)

    d.tile_grid("The six run chart patterns", [
        ("TREND", "6 or more consecutive points all rising or all falling"),
        ("SHIFT", "8 or more consecutive points all on one side of the median"),
        ("CLUSTER", "Points bunched in one region - grouping by an untracked variable"),
        ("MIXTURE", "Too few crossings - points avoid the median, two populations combined"),
        ("OSCILLATION", "Rapid regular up-down sawtooth - usually the fingerprint of tampering"),
        ("BIAS", "Astronomical point far outside the rest - a one-off assignable event"),
    ], kicker=KR, cols=2, accent=BLUE)

    d.formula_card("Run rules - the arithmetic behind the patterns", [
        ("Too few runs\n(mixture)", "runs < expected\nexpected = n/2 + 1",
         "24 points, expect 13 runs. Meridian line 5 gave 6 runs - two populations mixed."),
        ("Too many runs\n(oscillation)", "runs > n/2 + 1\nwith no long runs",
         "24 points gave 20 runs - a sawtooth. Operators were re-tuning the tester every shift."),
        ("Shift", "8 consecutive points\none side of median",
         "Suzhou line 6 yield sat below median for 11 straight days after the stencil change."),
        ("Trend", "6 consecutive points\nall increasing or decreasing",
         "Penang line 3 cycle time rose 7 shifts in a row as the feeder wore."),
    ], kicker=KR, accent=BLUE,
        note="A run is an unbroken sequence of points on the same side of the median. Points sitting exactly on the median are ignored.")

    d.run_chart("Meridian line 1 first-pass yield - 12 weeks (percent)",
                [("W1", 91.4), ("W2", 92.8), ("W3", 90.6), ("W4", 92.1), ("W5", 91.0),
                 ("W6", 93.2), ("W7", 90.2), ("W8", 92.5), ("W9", 91.7), ("W10", 90.9),
                 ("W11", 92.9), ("W12", 91.3)],
                kicker=KR,
                note="Points scatter randomly either side of the median with no run, trend or "
                     "oscillation - a STABLE process showing only common cause variation.")

    d.run_chart("Meridian line 3 - a TREND appears (cycle time, minutes)",
                [("W1", 42.1), ("W2", 41.6), ("W3", 42.4), ("W4", 41.9), ("W5", 43.0),
                 ("W6", 44.2), ("W7", 45.1), ("W8", 45.9), ("W9", 46.8), ("W10", 47.6),
                 ("W11", 48.3), ("W12", 49.1)],
                kicker=KR,
                note="Seven consecutive rising points from W6 - the TREND rule fires. Investigation "
                     "found progressive wear on the component feeder cam.")

    d.run_chart("Meridian line 6 - a SHIFT appears (yield, percent)",
                [("W1", 93.1), ("W2", 92.4), ("W3", 93.6), ("W4", 92.9), ("W5", 88.2),
                 ("W6", 87.6), ("W7", 88.4), ("W8", 87.1), ("W9", 88.0), ("W10", 87.4),
                 ("W11", 88.6), ("W12", 87.9)],
                kicker=KR,
                note="Eight consecutive points below the median from W5 - the SHIFT rule fires. "
                     "Traced to the new solder paste stencil installed that weekend.")

    # --------- PARETO AND STRATIFICATION ---------
    d.big_statement(
        "Recap 2 - Stratification and Pareto, weighted by COST",
        "Counting defects tells you what happens most. Costing defects tells you what to fix "
        "first. These are frequently not the same list.",
        KR, color=AMBER)

    d.tile_grid("Stratification - the questions that split the data", [
        ("WHO", "Operator, team, shift, inspector, supervisor"),
        ("WHAT", "Product family, model variant, defect type, component supplier"),
        ("WHERE", "Plant, line, station, geographic customer region"),
        ("WHEN", "Shift, day of week, hour of shift, month, before or after a change"),
        ("HOW", "Method version, machine, tooling set, changeover type"),
        ("HOW MUCH", "Batch size, run length, order value, order line count"),
    ], kicker=KR, cols=2, accent=AMBER)

    d.pareto_chart("Meridian warranty returns by defect type - BY COUNT",
                   [("Occlusion alarm false trip", 412), ("Battery pack under-capacity", 268),
                    ("Keypad membrane delamination", 191), ("Flow rate drift", 96),
                    ("Door latch wear", 74), ("Display pixel fault", 41),
                    ("Other", 33)],
                   kicker=KR,
                   note="By COUNT, occlusion alarm false trips dominate at 38 percent of all returns. "
                        "This is where a Green Belt would stop.")

    d.pareto_chart("Meridian warranty returns by defect type - BY COST (SGD 000)",
                   [("Occlusion alarm false trip", 288), ("Battery pack under-capacity", 938),
                    ("Keypad membrane delamination", 134), ("Flow rate drift", 1344),
                    ("Door latch wear", 30), ("Display pixel fault", 12),
                    ("Other", 46)],
                   kicker=KR,
                   note="By COST the order inverts. Flow rate drift is only 96 units but each one "
                        "triggers a field recall investigation at SGD 14,000. Fix cost, not count.")

    d.formula_card("Weighting a Pareto correctly", [
        ("Cost weight", "cost = count x unit cost\nof one occurrence",
         "Flow rate drift: 96 x SGD 14,000 = SGD 1,344,000 - the true top category."),
        ("Cumulative percent", "cum% = running total /\ngrand total x 100",
         "Flow drift 49%, battery 84%. Two categories carry 84 percent of the money."),
        ("Vital few test", "Do 20 percent of\ncategories carry 80 percent",
         "2 of 7 categories (29 percent) carry 84 percent of cost - a valid Pareto."),
    ], kicker=KR, accent=AMBER,
        note="If every category is roughly equal, there is no vital few - stratify on a different dimension before proceeding.")

    d.compare_panels("Boxplots - what they show that a Pareto cannot", [
        ("THE FIVE NUMBERS", "What the box is made of", [
            "Minimum (excluding outliers) at the lower whisker",
            "Q1 at the bottom of the box - 25th percentile",
            "Median as the line inside the box",
            "Q3 at the top of the box - 75th percentile",
            "IQR = Q3 - Q1, the width of the middle half",
        ]),
        ("WHAT TO READ", "Shape, spread, outliers", [
            "Box width shows spread - narrower is more consistent",
            "Median off-centre in the box means skew",
            "Points beyond 1.5 x IQR are flagged outliers",
            "Side-by-side boxes compare groups instantly",
            "Overlapping boxes warn you the difference may not be real",
        ]),
        ("MERIDIAN EXAMPLE", "Yield by plant", [
            "Singapore: median 93.1, IQR 1.8 - tight and high",
            "Penang: median 92.4, IQR 2.1 - similar and stable",
            "Suzhou: median 88.6, IQR 6.4 - lower AND far more variable",
            "The spread difference matters as much as the mean difference",
            "This is what sends us to a variance test, not just a t-test",
        ]),
    ], kicker=KR, accent=TEAL)

    # ============================================================
    # SECTION 2 - RECAP: CAUSE TOOLS
    # ============================================================
    d.big_statement(
        "Recap 3 - Generating causes you can actually test",
        "The fishbone does not find the root cause. It produces a candidate list good enough "
        "that the statistics have something worth testing.",
        KR, color=VIOLET)

    d.fishbone("Fishbone 5M plus E - Meridian flow rate drift", "Flow rate drift\nin field units",
               [("MACHINE", ["Pump head calibration drift", "Test rig reference aging", "Motor bearing wear"]),
                ("METHOD", ["Calibration interval 12 months", "No verification after transport", "Single-point calibration only"]),
                ("MATERIAL", ["Tubing durometer varies by lot", "Two silicone suppliers in use", "Seal compound batch variation"]),
                ("MANPOWER", ["Calibration training not refreshed", "Three technicians, no agreement study", "Night shift skips warm-up"]),
                ("MEASUREMENT", ["Flow meter gage R and R at 24 percent", "Ambient temperature not recorded", "Resolution 0.5 mL/hr"]),
                ("ENVIRONMENT", ["Test bay temperature 22 to 31 C", "Suzhou humidity above 80 percent", "Bench vibration near press"])],
               kicker=KR)

    d.tile_grid("The 5M plus E categories - what belongs in each", [
        ("MACHINE", "Equipment, tooling, fixtures, software, calibration state"),
        ("METHOD", "Procedures, work instructions, sequence, settings, sampling plan"),
        ("MATERIAL", "Raw material, components, consumables, supplier and lot variation"),
        ("MANPOWER", "Skill, training, experience, staffing level, fatigue, handover"),
        ("MEASUREMENT", "Gage capability, resolution, inspector agreement, data capture"),
        ("ENVIRONMENT", "Temperature, humidity, vibration, cleanliness, layout, lighting"),
    ], kicker=KR, cols=2, accent=VIOLET)

    d.ladder("5 Whys on Meridian occlusion false trips", [
        ("WHY 1", "Units false-trip the occlusion alarm in the field"),
        ("WHY 2", "The pressure sensor baseline drifts upward over 6 months"),
        ("WHY 3", "Baseline is set once at final test and never re-zeroed"),
        ("WHY 4", "Firmware has no auto-zero routine on power-up"),
        ("WHY 5", "The design FMEA rated sensor drift as low severity in 2019"),
    ], kicker=KR, accent=TEAL,
        note="Root cause lands on a PROCESS decision (the design FMEA rating), not on a person. That is the discipline.")

    d.tile_grid("5 Whys discipline - the rules that keep it honest", [
        ("Stop at a process, never a person", "'The technician forgot' is not a root cause - ask why the process allowed it"),
        ("Each why must be verifiable", "If you cannot get data to confirm a link, you are guessing not analysing"),
        ("Five is a guide, not a quota", "Sometimes three, sometimes seven - stop when the answer is actionable"),
        ("Branch when there are two answers", "A why with two valid causes becomes two chains, not a forced single line"),
        ("Test the chain backwards", "Read it as 'therefore' from the bottom up - it must still make sense"),
        ("Confirm the fix breaks the chain", "If removing the root cause would not stop the effect, you have the wrong root"),
    ], kicker=KR, cols=2, accent=TEAL)

    d.flow_h("Multi-voting a 40-cause fishbone down to 5", [
        "Cluster duplicate and near-duplicate causes and re-word them clearly",
        "Give each person N/3 votes where N is the number of causes",
        "Vote silently and simultaneously - no discussion during voting",
        "Tally, keep the top third, discard the rest into the parked log",
        "Repeat with fewer votes until 5 to 7 candidates remain",
        "Rank the survivors on the cause-and-effect matrix before testing",
    ], kicker=KR, color=AMBER)

    d.formula_card("The cause-and-effect matrix - scoring what to test first", [
        ("Output weight", "Each Y rated 1-10\nby customer importance",
         "Meridian: OTIF weight 9, first-pass yield 8, warranty cost 10."),
        ("Relationship score", "Each X vs each Y:\n0, 1, 3 or 9",
         "Sensor baseline drift vs warranty cost = 9 (strong direct relationship)."),
        ("Total score", "sum of\n(weight x relationship)",
         "Sensor drift: 9x1 + 8x3 + 10x9 = 123 - the highest scoring X, test it first."),
    ], kicker=KR, accent=VIOLET,
        note="The matrix converts opinion into a ranked test order. It does NOT prove anything - the hypothesis test does.")

    d.matrix2x2("Choosing which causes to test with statistics", "EFFORT / COST TO TEST",
                "STRENGTH OF SUSPICION",
                [("TEST FIRST", "High suspicion, cheap to test. Sensor baseline drift - data already in the test log. Run it this week."),
                 ("BUILD A CASE", "High suspicion, expensive to test. Requires a designed experiment or new instrumentation - charter it."),
                 ("QUICK CLEAR", "Low suspicion, cheap to test. Run it anyway to close the theory and stop it being re-raised."),
                 ("PARK", "Low suspicion, expensive. Log it in the rejected-causes register with the reason and move on.")],
                kicker=KR, accent=VIOLET)

    # ============================================================
    # SECTION 3 - RECAP: HYPOTHESIS TESTING IN FULL
    # ============================================================
    d.big_statement(
        "Recap 4 - Hypothesis testing, in full",
        "This is the single most-taught and most-misused topic in Six Sigma. As a Black Belt "
        "you must be able to derive it, defend it and correct a Green Belt who has it wrong.",
        KR, color=BLUE)

    d.flow_h("The hypothesis testing procedure", [
        "State the practical question in plain business language",
        "Formulate H0 and Ha, and decide one-tail or two-tail",
        "Choose alpha and the required power, then compute the sample size",
        "Select the correct test from the Y and X data types",
        "Check the assumptions: normality, independence, equal variance",
        "Run the test, read the p-value, then translate back to the business",
    ], kicker=KR, color=BLUE)

    d.compare_panels("H0 and Ha - formulating them correctly", [
        ("NULL - H0", "The status quo, the boring answer", [
            "Always contains equality: =, <= or >=",
            "'There is no difference' / 'the change did nothing'",
            "It is what we ASSUME true until the data forces us to abandon it",
            "We never 'accept' H0 - we fail to reject it",
            "Meridian: mean yield Singapore = mean yield Suzhou",
        ]),
        ("ALTERNATIVE - Ha", "The claim you must prove", [
            "Never contains equality: not equal, > or <",
            "'There IS a difference' / 'the change helped'",
            "It carries the burden of proof",
            "It is what you write the project benefit against",
            "Meridian: mean yield Singapore is not equal to mean yield Suzhou",
        ]),
        ("COMMON ERRORS", "What a Black Belt corrects", [
            "Putting the interesting claim in H0",
            "Writing Ha after seeing the data",
            "Using a one-tail test to rescue a marginal p-value",
            "Reporting 'we proved there is no difference'",
            "Testing a hypothesis nobody could act on either way",
        ]),
    ], kicker=KR, accent=BLUE)

    d.matrix2x2("Type I and Type II error - the decision table", "THE TRUTH ABOUT THE PROCESS",
                "YOUR DECISION",
                [("CORRECT", "H0 is true and you fail to reject it. You correctly concluded nothing changed. Probability = 1 - alpha."),
                 ("TYPE I ERROR - alpha", "H0 is true but you reject it. A FALSE ALARM. You claim a difference that is not there. PRODUCER'S RISK."),
                 ("TYPE II ERROR - beta", "H0 is false but you fail to reject it. A MISS. A real difference goes undetected. CONSUMER'S RISK."),
                 ("CORRECT - POWER", "H0 is false and you reject it. You detected a real difference. Probability = 1 - beta = POWER.")],
                kicker=KR, accent=RED)

    d.compare_panels("Producer's risk vs consumer's risk", [
        ("TYPE I - PRODUCER'S RISK", "alpha, typically 0.05", [
            "You reject a good batch, or claim a fix that does nothing",
            "Meridian: scrapping a conforming lot of pump housings",
            "Cost falls on the PRODUCER - wasted material and rework",
            "You spend money implementing an improvement with no effect",
            "Controlled directly by your choice of alpha",
        ]),
        ("TYPE II - CONSUMER'S RISK", "beta, often 0.10 to 0.20", [
            "You pass a bad batch, or miss a real improvement",
            "Meridian: shipping drifting pumps to a hospital",
            "Cost falls on the CUSTOMER - and on your warranty and reputation",
            "In a regulated medical device this is the risk that ends careers",
            "Controlled by sample size and effect size, via power",
        ]),
        ("THE TRADE-OFF", "You cannot minimise both", [
            "Lowering alpha to 0.01 raises beta at fixed n",
            "The only way to reduce both is a LARGER SAMPLE",
            "Choose alpha by consequence, not by habit",
            "Medical device safety claim: alpha 0.01 is defensible",
            "Exploratory screening: alpha 0.10 is defensible",
        ]),
    ], kicker=KR, accent=RED)

    d.formula_card("Alpha, beta, power and confidence", [
        ("Alpha", "alpha = P(reject H0\n| H0 true)",
         "alpha = 0.05 means a 5 percent chance of a false alarm on this test."),
        ("Confidence level", "confidence = 1 - alpha",
         "alpha = 0.05 gives a 95 percent confidence level and 95 percent CI."),
        ("Beta", "beta = P(fail to reject H0\n| H0 false)",
         "beta = 0.20 means a 20 percent chance of missing a real difference."),
        ("Power", "power = 1 - beta",
         "power = 0.80: an 80 percent chance of detecting the shift you care about."),
    ], kicker=KR, accent=BLUE,
        note="Standard practice: alpha = 0.05, power >= 0.80. Raise power to 0.90 or 0.95 for safety-critical medical device decisions.")

    d.formula_card("Sample size - worked for Meridian", [
        ("2-sample t\nsample size", "n per group =\n2 x (Z_a/2 + Z_b)^2 x s^2 / d^2",
         "Detect a 1.5 pp yield gap, s = 2.2, alpha .05, power .80: n = 2 x 7.85 x 4.84 / 2.25 = 34 per line."),
        ("1-proportion\nsample size", "n = (Z_a/2)^2 x p(1-p) / d^2",
         "Confirm OTIF at 91 percent within 2 pp: n = 3.84 x 0.0819 / 0.0004 = 787 orders."),
        ("Effect of\nhalving delta", "n scales as 1 / d^2",
         "Halving the detectable gap from 1.5 pp to 0.75 pp needs FOUR times the sample: 136 per line."),
    ], kicker=KR, accent=AMBER,
        note="Z for alpha 0.05 two-tail = 1.96; Z for power 0.80 = 0.84. Always compute n BEFORE collecting data.")

    d.big_statement(
        "The p-value - what it actually means",
        "The p-value is the probability of seeing data this extreme or more extreme IF the "
        "null hypothesis were true. It is not the probability that H0 is true.",
        KR, color=VIOLET)

    d.compare_panels("What a p-value is and is not", [
        ("IT IS", "A conditional probability", [
            "P(data this extreme | H0 is true)",
            "A measure of how surprising your data is under H0",
            "p < alpha means reject H0",
            "Meridian p = 0.003: data this extreme would be rare if plants matched",
            "'If it ain't low, let it go' - the field mnemonic",
        ]),
        ("IT IS NOT", "Four common misreadings", [
            "NOT the probability that H0 is true",
            "NOT the probability your conclusion is wrong",
            "NOT a measure of how big or important the effect is",
            "NOT proof of no difference when p is large",
            "p = 0.06 and p = 0.04 are not meaningfully different evidence",
        ]),
        ("ALWAYS REPORT WITH", "The context that makes it useful", [
            "The effect size in real units, not just significance",
            "The confidence interval around that effect",
            "The sample size the test ran on",
            "Which assumptions were checked and how",
            "The business consequence of the effect",
        ]),
    ], kicker=KR, accent=VIOLET)

    # --------- TEST SELECTION ---------
    d.big_statement(
        "The test selection decision tree",
        "Almost every hypothesis testing mistake is a test SELECTION mistake. Start from the "
        "data type of Y, then the data type and number of levels of X.",
        KR, color=TEAL)

    d.flow_h("How to select the right test in four questions", [
        "What is the data type of Y - continuous or discrete/attribute",
        "What is the data type of X - and how many levels or groups does it have",
        "Are the samples independent, or paired on the same units",
        "Do the assumptions hold - normal, independent, equal variance",
    ], kicker=KR, color=TEAL)

    d.tile_grid("CONTINUOUS Y - which test", [
        ("1-sample t-test", "One group vs a target value. Is Suzhou mean yield equal to 93 percent?"),
        ("2-sample t-test", "Two independent groups. Singapore line 1 vs Penang line 3 cycle time."),
        ("Paired t-test", "Same units measured twice. Yield before and after the stencil change, same line."),
        ("One-way ANOVA", "Three or more groups, one factor. Yield across all 6 Meridian lines."),
        ("Two-way ANOVA", "Two factors at once plus their interaction. Plant x shift on yield."),
        ("F-test / Levene", "Comparing VARIANCES, not means. Is Suzhou more variable than Singapore?"),
    ], kicker=KR, cols=2, accent=TEAL)

    d.tile_grid("DISCRETE / ATTRIBUTE Y - which test", [
        ("1-proportion test", "One proportion vs a target. Is OTIF equal to the 97 percent goal?"),
        ("2-proportion test", "Two proportions compared. Penang scrap rate vs Suzhou scrap rate."),
        ("Chi-square test", "Association between two categorical variables. Defect type vs shift."),
        ("Chi-square goodness of fit", "Does the observed distribution match an expected one?"),
        ("Fisher's exact test", "Same as chi-square but for small expected counts below 5."),
        ("Logistic regression", "Predict a pass/fail Y from continuous Xs - beyond this course's core"),
    ], kicker=KR, cols=2, accent=AMBER)

    d.compare_panels("The decision tree in three branches", [
        ("Y CONTINUOUS, X DISCRETE", "Comparing means or variances", [
            "1 group vs target -> 1-sample t",
            "2 independent groups -> 2-sample t",
            "2 paired measurements -> paired t",
            "3+ groups, 1 factor -> one-way ANOVA",
            "2 factors -> two-way ANOVA with interaction",
        ]),
        ("Y CONTINUOUS, X CONTINUOUS", "Quantifying relationship", [
            "One X -> correlation then simple regression",
            "Several Xs -> multiple regression",
            "Curved relationship -> add a quadratic term",
            "Always follow with residual diagnostics",
            "Never report r without a scatterplot",
        ]),
        ("Y DISCRETE", "Comparing proportions", [
            "1 proportion vs target -> 1-proportion test",
            "2 proportions -> 2-proportion test",
            "Two categorical variables -> chi-square contingency",
            "Expected cell count below 5 -> Fisher's exact",
            "Discrete Y from continuous X -> logistic regression",
        ]),
    ], kicker=KR, accent=BLUE)

    d.formula_card("Worked 2-sample t-test - Singapore vs Suzhou yield", [
        ("The hypotheses", "H0: mu_SG = mu_SZ\nHa: mu_SG not= mu_SZ",
         "Two-tailed, alpha = 0.05. n = 40 lots per plant."),
        ("The data", "SG: xbar 93.1, s 1.9\nSZ: xbar 88.6, s 4.7",
         "Levene p = 0.002 -> variances are NOT equal, so use Welch's t-test."),
        ("The statistic", "t = (93.1 - 88.6) /\nsqrt(1.9^2/40 + 4.7^2/40)",
         "t = 4.5 / 0.801 = 5.62, df approx 51.4, p < 0.001. Reject H0."),
        ("The translation", "4.5 pp yield gap,\n95% CI [2.9, 6.1]",
         "4.5 pp on 210,000 Suzhou units = 9,450 fewer good units, SGD 2.6M at SGD 275 margin."),
    ], kicker=KR, accent=BLUE,
        note="Note the sequence: hypotheses BEFORE data, assumption check BEFORE the test, business translation AFTER the p-value.")

    d.normal_curve("Where alpha lives on the distribution", kicker=KR,
                   note="With alpha = 0.05 two-tailed, the rejection regions are the outer 2.5 percent in each "
                        "tail. A test statistic landing there is judged too extreme to be chance alone.")

    # ============================================================
    # SECTION 4 - RECAP: CORRELATION AND SIMPLE REGRESSION
    # ============================================================
    d.big_statement(
        "Recap 5 - Correlation and simple regression",
        "Hypothesis tests tell you IF an X matters. Regression tells you HOW MUCH. This is the "
        "foundation everything in the Black Belt half of Analyze is built on.",
        KR, color=VIOLET)

    d.formula_card("Correlation and simple linear regression", [
        ("Correlation r", "r = cov(X,Y) /\n(s_x x s_y)",
         "Meridian oven zone-3 temp vs yield: r = -0.72. Strong negative linear relationship."),
        ("Coefficient of\ndetermination", "R-squared = r^2",
         "r = -0.72 gives R-squared = 0.52. Oven temperature explains 52 percent of yield variation."),
        ("Regression line", "Y = b0 + b1 X",
         "Yield = 118.4 - 0.104 x (oven temp C). Each extra degree costs 0.104 pp of yield."),
        ("Slope meaning", "b1 = change in Y per\none unit change in X",
         "Running 6 C hotter costs 0.62 pp yield = about 1,300 units a year at Penang volume."),
    ], kicker=KR, accent=VIOLET,
        note="Always plot the scatter before trusting r. A curved or clustered relationship can produce a misleading r.")

    d.compare_panels("Correlation is not causation - the four explanations", [
        ("X CAUSES Y", "The one you hope for", [
            "The mechanism is physically plausible",
            "X precedes Y in time",
            "Changing X in a trial changes Y",
            "Meridian: reflow temperature -> solder joint quality",
            "Only a designed experiment can confirm this",
        ]),
        ("Y CAUSES X", "Reverse causation", [
            "The arrow runs the other way",
            "Meridian: high scrap correlates with more inspectors",
            "The scrap did not come from the inspectors",
            "The inspectors were added BECAUSE of the scrap",
            "Check which came first before writing the story",
        ]),
        ("A THIRD VARIABLE", "Confounding or coincidence", [
            "Z drives both X and Y",
            "Meridian: humidity drives both scrap and absenteeism",
            "Or pure coincidence in a small sample",
            "Or you tested 40 Xs and 2 came up 'significant' by chance",
            "This is why a Black Belt confirms in Improve with a DOE",
        ]),
    ], kicker=KR, accent=RED)

    # ============================================================
    # SECTION 5 - BLACK BELT: MULTIPLE REGRESSION
    # ============================================================
    d.big_statement(
        "BLACK BELT ONLY - Multiple regression",
        "A Green Belt models Y against one X. Real processes have several Xs acting at once, "
        "and they are correlated with each other. From here on, this is beyond Green Belt.",
        KB, color=RED)

    d.formula_card("The multiple regression model", [
        ("The model", "Y = b0 + b1X1 + b2X2\n+ ... + bkXk + e",
         "Y = first-pass yield; X1 oven temp, X2 humidity, X3 paste age, X4 line speed."),
        ("Intercept b0", "Predicted Y when every\nX equals zero",
         "b0 = 118.4. Often has no physical meaning - do not over-interpret it."),
        ("Coefficient bi", "Change in Y per unit of Xi,\nHOLDING all other Xs CONSTANT",
         "b1 = -0.081: one extra degree C costs 0.081 pp yield at fixed humidity, paste age and speed."),
        ("Error term e", "Everything the model\ndoes not explain",
         "Assumed independent, normal, mean zero, constant variance. The residuals test this."),
    ], kicker=KB, accent=RED,
        note="'Holding other Xs constant' is the whole point of multiple regression, and the phrase Green Belts most often omit.")

    d.formula_card("Meridian fitted model - first-pass yield", [
        ("Fitted equation", "Yield = 118.4 - 0.081(Temp)\n- 0.147(Humidity)\n- 0.043(PasteAge) + 0.019(Speed)",
         "Fitted on 180 lots across all 6 lines over 9 months of production data."),
        ("Coefficient p-values", "Temp .000, Humidity .001\nPasteAge .014, Speed .382",
         "Line speed is not significant at alpha .05 - it is a candidate for removal."),
        ("Model fit", "R-squared = 0.741\nadj R-squared = 0.735",
         "The four Xs together explain about 74 percent of yield variation between lots."),
    ], kicker=KB, accent=BLUE,
        note="Read the coefficient WITH its p-value. A large coefficient with p = 0.38 is noise dressed as insight.")

    d.compare_panels("Interpreting a coefficient the right way", [
        ("SAY THIS", "Correct and defensible", [
            "Each 1 C rise in oven temp is associated with 0.081 pp lower yield",
            "...holding humidity, paste age and line speed constant",
            "...within the observed range of 232 to 251 C",
            "...with 95 percent CI [-0.104, -0.058]",
            "Association, quantified, bounded, with uncertainty",
        ]),
        ("NOT THIS", "Overclaims a Black Belt must catch", [
            "'Temperature causes 0.081 pp of yield loss' - regression is not a DOE",
            "'Cutting temp 20 C gains 1.6 pp' - extrapolating outside the data range",
            "'Temp is the biggest driver' - coefficients in different units are not comparable",
            "'The model explains yield' - it explains 74 percent of the VARIATION observed",
            "Any causal verb without an experiment behind it",
        ]),
    ], kicker=KB, accent=RED)

    d.flow_h("Backward elimination - building a parsimonious model", [
        "Fit the full model with every candidate X you have reason to include",
        "Find the term with the highest p-value above your cutoff, typically 0.10",
        "Remove that single term and refit the entire model",
        "Check adjusted R-squared - it should hold or rise, never drop materially",
        "Repeat until every remaining term is significant",
        "Validate the final model on held-out data before you present it",
    ], kicker=KB, color=BLUE)

    d.formula_card("Backward elimination on the Meridian model", [
        ("Step 0 - full model", "4 terms, adj R2 = 0.735\nSpeed p = 0.382",
         "Speed has the highest p-value and is well above the 0.10 cutoff. Remove it."),
        ("Step 1 - refit", "3 terms, adj R2 = 0.737\nPasteAge p = 0.011",
         "Adjusted R-squared actually ROSE. Speed was costing more than it contributed."),
        ("Step 2 - check", "All p-values below 0.05\nadj R2 = 0.737",
         "Final model: Yield = 119.1 - 0.079(Temp) - 0.151(Humidity) - 0.045(PasteAge)."),
    ], kicker=KB, accent=BLUE,
        note="Never remove more than one term at a time - removing an X changes every other coefficient in the model.")

    d.compare_panels("Overfitting - the trap that ends careers", [
        ("WHAT IT LOOKS LIKE", "Suspiciously good", [
            "R-squared of 0.97 on 24 data points with 9 terms",
            "Every coefficient significant, none physically explainable",
            "Interaction and quadratic terms nobody can justify",
            "The model predicts the training data almost perfectly",
            "It fails completely on next month's production",
        ]),
        ("WHY IT HAPPENS", "The model learns noise", [
            "Too many terms relative to the number of observations",
            "Terms chosen by p-value hunting, not by process knowledge",
            "The same data used to both build and judge the model",
            "Rule of thumb: at least 10 to 15 observations per term",
            "Meridian: 180 lots supports about 12 terms, not 40",
        ]),
        ("HOW TO PREVENT IT", "Discipline, not software", [
            "Hold out 20 to 30 percent of the data before you start modelling",
            "Fit on the training set only, never touch the holdout",
            "Compare R-squared on training vs holdout - a big drop means overfit",
            "Prefer terms you can explain physically",
            "Judge on adjusted R-squared, and keep the model small",
        ]),
    ], kicker=KB, accent=RED)

    d.formula_card("Validating the Meridian model on held-out data", [
        ("Split", "180 lots ->\n135 train / 45 holdout",
         "Split by TIME: months 1-7 train, months 8-9 holdout. Mimics real deployment."),
        ("Training fit", "adj R2 = 0.737\nRMSE = 1.12 pp",
         "Fitted on 135 lots. Three terms, all significant at alpha 0.05."),
        ("Holdout performance", "R2 on holdout = 0.708\nRMSE = 1.24 pp",
         "Only a small drop - the model generalises. A drop to R2 0.31 would mean overfit."),
    ], kicker=KB, accent=TEAL,
        note="If holdout performance collapses, the model is describing last quarter, not the process. Do not present it.")

    # ============================================================
    # SECTION 6 - BLACK BELT: MODEL DIAGNOSTICS
    # ============================================================
    d.big_statement(
        "BLACK BELT ONLY - Model diagnostics",
        "A model that FITS is not yet a model that is VALID. Adjusted R-squared says nothing "
        "about whether the assumptions hold. The residuals do.",
        KB, color=VIOLET)

    d.tile_grid("The four residual plots you must always produce", [
        ("Residuals vs FITTED", "Should be a formless cloud. Any pattern means the model is wrong."),
        ("Normal probability plot", "Residuals should follow the straight line - confirms the normality assumption."),
        ("Residuals vs ORDER", "Plotted in time order. Any drift or cycling means the errors are not independent."),
        ("Histogram of residuals", "Should look roughly bell shaped and centred on zero"),
        ("Residuals vs each X", "Curvature against one X shows exactly which term needs a quadratic"),
        ("The rule", "If any plot shows structure, the model is not finished - fix it before presenting"),
    ], kicker=KB, cols=2, accent=VIOLET)

    d.compare_panels("Residuals vs fitted - diagnosing the shape", [
        ("FUNNEL SHAPE", "Non-constant variance", [
            "Spread widens as fitted values rise (heteroscedasticity)",
            "Prediction intervals are wrong at the wide end",
            "Meridian: yield errors are larger at low-yield lots",
            "Fix: transform Y (log or Box-Cox), or use weighted regression",
            "Do NOT just report it and move on",
        ]),
        ("CURVATURE", "A missing quadratic term", [
            "Residuals arc: negative, then positive, then negative",
            "The relationship is real but not linear",
            "Meridian: yield falls off at BOTH low and high oven temperature",
            "Fix: add a squared term (Temp^2) and refit",
            "Adjusted R-squared usually jumps sharply when you do",
        ]),
        ("DRIFT vs ORDER", "Autocorrelation", [
            "Residuals plotted in time order trend or cycle",
            "The independence assumption is violated - p-values are wrong",
            "Meridian: paste age drifts up through the week and resets Monday",
            "Fix: add the time-varying X to the model, or use a time-series method",
            "Never ignore - this makes every p-value optimistic",
        ]),
    ], kicker=KB, accent=RED)

    d.flow_h("What to do when a residual plot shows structure", [
        "Identify which plot failed and what shape it showed",
        "Funnel: transform Y with log or Box-Cox and refit",
        "Curvature: add the squared term for the offending X and refit",
        "Drift: add the time-varying X, or block by time period",
        "Outliers: investigate physically before deciding to keep or exclude",
        "Refit and re-plot - never present a model whose residuals you have not seen",
    ], kicker=KB, color=VIOLET)

    d.big_statement(
        "Multicollinearity - when your Xs explain each other",
        "If two Xs move together, the model cannot tell which one drives Y. Coefficients "
        "become unstable, signs flip, and standard errors inflate.",
        KB, color=AMBER)

    d.formula_card("Variance Inflation Factor", [
        ("VIF", "VIF_i = 1 / (1 - R2_i)",
         "R2_i is from regressing Xi against all the OTHER Xs, not against Y."),
        ("VIF = 1", "Xi is uncorrelated\nwith the other Xs",
         "Ideal. The coefficient estimate is as precise as the data allows."),
        ("VIF > 5", "R2_i > 0.80\nCONCERN",
         "Meridian: oven temp VIF = 6.2, conveyor speed VIF = 5.9 - they move together."),
        ("VIF > 10", "R2_i > 0.90\nSERIOUS",
         "Standard error inflated over 3x. The coefficient is effectively uninterpretable."),
    ], kicker=KB, accent=AMBER,
        note="VIF above 5 warrants action; above 10 the coefficient must not be quoted to a sponsor as a standalone effect.")

    d.compare_panels("Meridian collinearity worked through", [
        ("THE PROBLEM", "Two Xs, one signal", [
            "Oven temperature and conveyor speed correlate at r = 0.91",
            "Operators raise temperature whenever they raise speed",
            "Temp coefficient -0.081, speed coefficient +0.019 with p = 0.38",
            "VIF: temp 6.2, speed 5.9 - both above the concern threshold",
            "The model cannot separate their effects from this data",
        ]),
        ("THE FIX", "Engineer one variable", [
            "Create thermal exposure index = time above 217 C liquidus",
            "That single variable captures what both Xs jointly control",
            "Refit: index coefficient -0.196, p < 0.001, VIF = 1.3",
            "Adjusted R-squared holds at 0.734 with one fewer term",
            "The coefficient is now stable and physically meaningful",
        ]),
        ("THE LESSON", "Design beats correction", [
            "Observational data cannot break a correlation the process created",
            "Only a designed experiment can vary temp and speed independently",
            "This is exactly why Analyze hands over to DOE in Improve",
            "Report VIF alongside every multiple regression, always",
            "Never present a coefficient with VIF above 10",
        ]),
    ], kicker=KB, accent=VIOLET)

    # ============================================================
    # SECTION 7 - BLACK BELT: ANOVA
    # ============================================================
    d.big_statement(
        "BLACK BELT ONLY - Analysis of Variance",
        "Six lines, one question: are their mean yields the same? Running fifteen t-tests "
        "would guarantee a false alarm. ANOVA answers it in one test.",
        KB, color=TEAL)

    d.formula_card("Alpha inflation - why repeated t-tests fail", [
        ("Number of pairs", "pairs = k(k-1)/2",
         "4 groups gives 6 pairwise t-tests. Meridian's 6 lines gives 15."),
        ("Family-wise error", "FWE = 1 - (1 - alpha)^m",
         "4 groups, 6 tests, alpha .05: FWE = 1 - 0.95^6 = 0.265 - about 26 percent."),
        ("At 6 groups", "1 - 0.95^15",
         "FWE = 0.537. You are MORE likely than not to raise at least one false alarm."),
        ("ANOVA's answer", "One test, one alpha",
         "One F-test at alpha = 0.05 keeps the overall false alarm risk at 5 percent."),
    ], kicker=KB, accent=RED,
        note="This is the single clearest reason a Black Belt reaches for ANOVA rather than a stack of t-tests.")

    d.formula_card("The F-statistic - between over within", [
        ("The logic", "F = variance BETWEEN groups\n/ variance WITHIN groups",
         "If the groups are really the same, both estimate the same sigma^2 and F is near 1."),
        ("Between (MS treatment)", "SS_between / (k-1)",
         "Meridian 6 lines: SS_between = 214.7, df = 5, MS = 42.9."),
        ("Within (MS error)", "SS_within / (N-k)",
         "SS_within = 361.2, df = 174, MS = 2.08. This is the pooled noise."),
        ("The test", "F = MS_between / MS_within",
         "F = 42.9 / 2.08 = 20.6, df 5 and 174, p < 0.001. At least one line differs."),
    ], kicker=KB, accent=TEAL,
        note="A large F means the gaps between group means are large relative to the noise inside the groups.")

    d.big_statement(
        "Post-hoc testing - which lines actually differ",
        "The F-test says 'somebody is different'. Tukey's HSD tells you who, while holding the "
        "family-wise error rate at your chosen alpha.",
        KB, color=VIOLET)

    d.formula_card("Tukey's Honestly Significant Difference", [
        ("The statistic", "HSD = q_(alpha,k,df) x\nsqrt(MS_error / n)",
         "q from the studentised range table: k=6, df=174, alpha .05 gives q = 4.03."),
        ("Meridian HSD", "4.03 x sqrt(2.08 / 30)",
         "HSD = 4.03 x 0.263 = 1.06 pp. Any two line means differing by more than 1.06 pp differ significantly."),
        ("The comparison", "|mean_i - mean_j| > HSD",
         "Line 1 93.2 vs line 5 88.4: gap 4.8 pp > 1.06 -> significantly different."),
        ("The non-difference", "Line 1 93.2 vs line 2 92.9",
         "Gap 0.3 pp < 1.06 -> NOT significantly different. Do not chase this gap."),
    ], kicker=KB, accent=VIOLET,
        note="Tukey controls family-wise error across ALL pairwise comparisons - which a stack of t-tests does not.")

    d.compare_panels("Post-hoc results across the six Meridian lines", [
        ("GROUP A - HIGH", "Not different from each other", [
            "Line 1 Singapore: mean 93.2 pp",
            "Line 2 Singapore: mean 92.9 pp",
            "Line 3 Penang: mean 92.4 pp",
            "All pairwise gaps below HSD of 1.06",
            "Treat these three as one performance population",
        ]),
        ("GROUP B - MIDDLE", "Distinct from both others", [
            "Line 4 Penang: mean 91.1 pp",
            "Differs from line 1 (2.1 pp) and from line 5 (2.7 pp)",
            "Sits alone between the two clusters",
            "Worth a separate targeted investigation",
            "Recent stencil change is the leading hypothesis",
        ]),
        ("GROUP C - LOW", "The project target", [
            "Line 5 Suzhou: mean 88.4 pp",
            "Line 6 Suzhou: mean 88.9 pp",
            "Not different from each other - a PLANT effect, not a line effect",
            "4.8 pp below the best lines, worth SGD 2.6M a year",
            "Analyze focus moves to what is common to Suzhou",
        ]),
    ], kicker=KB, accent=TEAL)

    # ============================================================
    # SECTION 8 - BLACK BELT: TWO-WAY ANOVA AND INTERACTIONS
    # ============================================================
    d.big_statement(
        "BLACK BELT ONLY - Two-way ANOVA and interaction effects",
        "One factor at a time hides the most important finding in a multi-site business: that "
        "a fix which works at one plant can backfire at another.",
        KB, color=RED)

    d.formula_card("The two-way ANOVA model and its three tests", [
        ("The model", "Y = mu + A_i + B_j\n+ (AB)_ij + e",
         "A = plant main effect, B = shift main effect, AB = the interaction term."),
        ("Main effect A", "F_A = MS_A / MS_error",
         "Plant: F = 27.4, p < 0.001. Plant means genuinely differ."),
        ("Main effect B", "F_B = MS_B / MS_error",
         "Shift: F = 1.58, p = 0.211. Overall, shift does NOT move yield on average."),
        ("Interaction AB", "F_AB = MS_AB / MS_error",
         "Plant x shift: F = 4.12, p = 0.004. The shift effect DEPENDS on which plant."),
    ], kicker=KB, accent=RED,
        note="Read the INTERACTION first. If it is significant, the main effects cannot be interpreted on their own.")

    d.compare_panels("The Meridian plant x shift interaction", [
        ("SINGAPORE", "Night shift is BETTER", [
            "Day shift yield 92.6 pp",
            "Night shift yield 93.8 pp - 1.2 pp better",
            "Air conditioning load is lower overnight",
            "Bay temperature holds within 2 C at night",
            "Night shift looks like the model to copy",
        ]),
        ("PENANG", "Almost no shift effect", [
            "Day shift yield 91.9 pp",
            "Night shift yield 91.6 pp - a 0.3 pp gap, not significant",
            "Climate control is independent of external load",
            "Shift makes essentially no difference here",
            "A shift-based intervention would waste money",
        ]),
        ("SUZHOU", "Night shift is WORSE", [
            "Day shift yield 89.7 pp",
            "Night shift yield 87.6 pp - 2.1 pp WORSE",
            "Overnight humidity rises above 80 percent, no dehumidification",
            "Solder paste absorbs moisture; voiding rises",
            "Copying Singapore's night-shift practice would HURT Suzhou",
        ]),
    ], kicker=KB, accent=RED)

    d.big_statement(
        "This is why interactions matter for Improve",
        "The main effect said shift does not matter (p = 0.21). The interaction said it matters "
        "in opposite directions at two plants. Roll out the wrong fix and you destroy value.",
        KB, color=RED)

    # ============================================================
    # SECTION 9 - BLACK BELT: NON-PARAMETRIC TESTS
    # ============================================================
    d.big_statement(
        "BLACK BELT ONLY - Non-parametric tests",
        "Cycle times, repair times and warranty ages are almost never normal. When the "
        "assumption fails and transformation does not rescue it, switch tests - do not proceed.",
        KB, color=TEAL)

    d.compare_panels("Parametric vs non-parametric", [
        ("PARAMETRIC", "Assumes a distribution", [
            "Assumes the data or residuals are normal",
            "Tests MEANS, using the actual data values",
            "More powerful WHEN the assumption holds",
            "Sensitive to outliers and skew",
            "t-tests, ANOVA, regression",
        ]),
        ("NON-PARAMETRIC", "Distribution-free", [
            "Makes no distributional assumption",
            "Tests MEDIANS, using the RANKS of the data",
            "Slightly less powerful when normality does hold",
            "Robust to outliers and to heavy skew",
            "Mann-Whitney, Kruskal-Wallis, Wilcoxon, Mood's median",
        ]),
        ("WHEN TO SWITCH", "The decision rule", [
            "Anderson-Darling p < 0.05 and Box-Cox does not fix it",
            "Small sample where normality cannot be assessed at all",
            "Ordinal data - satisfaction scores, severity grades",
            "Heavy outliers that are real and cannot be excluded",
            "When the MEDIAN is the more meaningful business measure",
        ]),
    ], kicker=KB, accent=TEAL)

    d.formula_card("Mann-Whitney - Penang vs Suzhou repair time", [
        ("The situation", "Repair time is right-skewed\nAD p = 0.001",
         "Box-Cox did not normalise it. A 2-sample t-test is not defensible here."),
        ("The hypotheses", "H0: median_PN = median_SZ\nHa: medians differ",
         "n = 45 repairs per plant, alpha = 0.05, two-tailed."),
        ("The method", "Rank all 90 values\ntogether, sum by group",
         "W = 1642 for Penang. Compare against the Mann-Whitney distribution."),
        ("The result", "p = 0.008\nReject H0",
         "Median 4.2 hours Penang vs 6.8 hours Suzhou. A real 2.6-hour gap."),
    ], kicker=KB, accent=TEAL,
        note="Report the MEDIANS, never the means, when you have used a rank-based test.")

    d.formula_card("Kruskal-Wallis across all six lines", [
        ("The situation", "Yield residuals non-normal\nafter an oven fault",
         "Two lines carry genuine outliers that engineering confirmed are real."),
        ("The hypotheses", "H0: all 6 medians equal\nHa: at least one differs",
         "N = 180 lots, alpha = 0.05."),
        ("The statistic", "H approximately\nchi-square with k-1 df",
         "H = 41.7, df = 5, p < 0.001. At least one line median differs."),
        ("Follow-up", "Pairwise Mann-Whitney\nwith Bonferroni",
         "alpha adjusted to 0.05/15 = 0.0033. Suzhou lines separate from the rest, as ANOVA found."),
    ], kicker=KB, accent=VIOLET,
        note="Kruskal-Wallis is the ANOVA of ranks. It answers the same question without the normality assumption.")

    d.compare_panels("Wilcoxon signed-rank and Mood's median", [
        ("WILCOXON SIGNED-RANK", "The paired test", [
            "Same units measured before and after a change",
            "Ranks the ABSOLUTE differences, then applies the signs",
            "Meridian: calibration time before vs after the new fixture, 30 techs",
            "Median saving 11 minutes, p = 0.002",
            "The non-parametric replacement for the paired t-test",
        ]),
        ("MOOD'S MEDIAN", "The robust test", [
            "Counts how many observations per group are above the grand median",
            "Then runs a chi-square on that contingency table",
            "Extremely robust to outliers and to unequal spread",
            "The least powerful of the non-parametric family",
            "Use when the data is badly contaminated but must still be tested",
        ]),
    ], kicker=KB, accent=BLUE)

    # ============================================================
    # SECTION 10 - BLACK BELT: MULTI-VARI STUDIES
    # ============================================================
    d.big_statement(
        "BLACK BELT ONLY - Multi-vari studies",
        "Before spending money hunting one X, find out WHERE the variation lives. Most teams "
        "chase machine settings when the variation is actually within a single part.",
        KB, color=VIOLET)

    d.compare_panels("The three families of variation", [
        ("POSITIONAL", "Within-piece / within-run", [
            "Variation WITHIN a single part or across positions",
            "Left cavity vs right cavity in the same mould",
            "Position 1 to 12 across the panel on the SMT line",
            "Meridian: connector pin 1 vs pin 20 solder volume",
            "Points to: fixturing, tooling, thermal gradient, layout",
        ]),
        ("CYCLICAL", "Piece-to-piece / batch-to-batch", [
            "Variation between consecutive pieces or batches",
            "Unit 1 vs unit 2 vs unit 3 in the same run",
            "Lot A vs lot B of the same material",
            "Meridian: paste lot changes between production batches",
            "Points to: material lots, setup, operator, changeover",
        ]),
        ("TEMPORAL", "Time-to-time", [
            "Variation across hours, shifts, days, weeks",
            "Morning vs afternoon; Monday vs Friday",
            "Before vs after a maintenance event",
            "Meridian: humidity rising through the Suzhou night shift",
            "Points to: environment, wear, drift, fatigue, seasonality",
        ]),
    ], kicker=KB, accent=VIOLET)

    d.tile_grid("Nested sampling design at Meridian - line 5 Suzhou", [
        ("Y measured", "Solder paste deposit volume in cubic mm at final inspection"),
        ("POSITIONAL level", "3 positions on each panel: left, centre, right"),
        ("CYCLICAL level", "3 consecutive panels sampled back-to-back at each time point"),
        ("TEMPORAL level", "5 time points across the shift: 07:00, 10:00, 13:00, 16:00, 19:00"),
        ("Total observations", "3 x 3 x 5 = 45 measurements over one full shift"),
        ("Rule during study", "Change nothing - no setting adjustment, no lot change, no operator swap"),
    ], kicker=KB, cols=2, accent=TEAL)

    d.formula_card("Variance components from the Meridian study", [
        ("Total variation", "s2_total = s2_pos +\ns2_cyc + s2_temp",
         "Total observed variance in deposit volume: 0.0412 mm^6."),
        ("Positional", "s2_pos / s2_total",
         "0.0289 / 0.0412 = 70.1 percent. Left-to-right across the panel dominates."),
        ("Cyclical", "s2_cyc / s2_total",
         "0.0071 / 0.0412 = 17.2 percent. Panel-to-panel variation is modest."),
        ("Temporal", "s2_temp / s2_total",
         "0.0052 / 0.0412 = 12.7 percent. Drift across the shift is the smallest family."),
    ], kicker=KB, accent=VIOLET,
        note="70 percent positional redirects the whole project: the answer is stencil and squeegee, not shift scheduling.")

    d.compare_panels("Reading the multi-vari chart", [
        ("WHAT YOU SEE", "Three visual signatures", [
            "Tall vertical spread within each small group = POSITIONAL",
            "Groups sitting at different heights close together = CYCLICAL",
            "The whole cluster drifting left to right = TEMPORAL",
            "One glance tells you which family dominates",
            "No statistics needed to see the answer",
        ]),
        ("MERIDIAN RESULT", "Positional dominates", [
            "Within each panel, left to right spans 0.34 mm^3",
            "Between consecutive panels, means differ by only 0.09 mm^3",
            "Across the shift, the cluster drifts just 0.07 mm^3",
            "The vertical spread visibly dwarfs everything else",
            "Confirmed by variance components at 70 percent positional",
        ]),
        ("WHAT IT KILLS", "Theories now closed", [
            "'It is the night shift' - temporal is only 12.7 percent",
            "'It is the paste lot' - cyclical is only 17.2 percent",
            "'It is operator technique' - would show as cyclical, and does not",
            "Three expensive investigations avoided in one shift of data",
            "Log them in the rejected-causes register with the numbers",
        ]),
    ], kicker=KB, accent=TEAL)

    # ============================================================
    # SECTION 11 - CHI-SQUARE
    # ============================================================
    d.big_statement(
        "Chi-square and contingency tables",
        "When both Y and X are categorical - defect type against shift, line or supplier - "
        "chi-square is the test that decides whether the association is real.",
        KB, color=AMBER)

    d.formula_card("The chi-square test of independence", [
        ("Hypotheses", "H0: the two variables\nare INDEPENDENT",
         "Ha: there is an association between defect type and plant."),
        ("Expected count", "E = (row total x col total)\n/ grand total",
         "Row 'solder void' 240, col 'Suzhou' 300, grand 900: E = 240x300/900 = 80."),
        ("The statistic", "chi2 = sum of\n(O - E)^2 / E",
         "Suzhou solder voids: observed 118 vs expected 80 -> (38)^2/80 = 18.05 for that cell."),
        ("Degrees of freedom", "df = (rows-1) x (cols-1)",
         "4 defect types x 3 plants: df = 3 x 2 = 6. chi2 = 47.3, p < 0.001. Reject H0."),
    ], kicker=KB, accent=AMBER,
        note="A significant chi-square proves association, not causation, and does not say WHICH cells drive it.")

    d.tile_grid("Meridian contingency table - defect type by plant", [
        ("Solder void", "Singapore 54, Penang 68, Suzhou 118. Expected 80 each - Suzhou is far over."),
        ("Sensor drift", "Singapore 41, Penang 47, Suzhou 62. Mildly over-represented at Suzhou."),
        ("Keypad delamination", "Singapore 62, Penang 58, Suzhou 60. Almost exactly as expected everywhere."),
        ("Battery capacity", "Singapore 43, Penang 87, Suzhou 60. Penang is the outlier here."),
        ("Column totals", "Singapore 200, Penang 260, Suzhou 300, grand total 760 defects"),
        ("Conclusion", "chi2 = 47.3, p < 0.001. Defect PROFILE differs by plant, not just defect volume."),
    ], kicker=KB, cols=2, accent=AMBER)

    # ============================================================
    # SECTION 12 - TRANSLATION AND CLOSE
    # ============================================================
    d.big_statement(
        "From statistics to a decision the sponsor can make",
        "No steering committee has ever approved funding because of a p-value. Your last job in "
        "Analyze is translation - into money, into risk, into a decision.",
        K, color=BLUE)

    d.compare_panels("Translating three statistics into business language", [
        ("A COEFFICIENT", "b = -0.151 for humidity", [
            "Statistical: each 1 percent RH costs 0.151 pp of yield",
            "Business: Suzhou runs 22 percent RH above Singapore",
            "That is 3.3 pp of yield, or 6,900 units a year",
            "At SGD 275 contribution margin: SGD 1.9M a year",
            "Decision: fund the SGD 340k dehumidification retrofit",
        ]),
        ("A P-VALUE", "p = 0.004 on the interaction", [
            "Statistical: the shift effect depends on the plant",
            "Business: the Singapore night-shift practice must NOT be rolled out globally",
            "Copying it to Suzhou would cost about 2.1 pp of yield",
            "Risk avoided: roughly SGD 1.2M a year of value destruction",
            "Decision: approve plant-specific solutions, not one standard",
        ]),
        ("AN R-SQUARED", "adj R-squared = 0.737", [
            "Statistical: three Xs explain 74 percent of yield variation",
            "Business: control these three and most of the problem is controllable",
            "The remaining 26 percent needs a designed experiment to find",
            "Confidence: we know where to aim the Improve phase budget",
            "Decision: approve a DOE on the three confirmed Xs",
        ]),
    ], kicker=K, accent=TEAL)

    d.tile_grid("Analyze tollgate checklist", [
        ("Root causes validated", "Each surviving X has a test, a p-value and an effect size in real units"),
        ("Assumptions documented", "Normality, independence and variance checks shown for every test"),
        ("Model diagnostics clean", "Residual plots produced, VIF reported, holdout validation done"),
        ("Rejected causes logged", "Every cleared theory recorded with the evidence that cleared it"),
        ("Benefit quantified", "Each confirmed X carries a dollar value the finance partner accepts"),
        ("Improve scope defined", "The DOE factors and the pilot sites are named and agreed"),
    ], kicker=K, cols=2, accent=TEAL)

    d.big_statement(
        "Analyze is complete when the causes are PROVEN",
        "Not brainstormed, not suspected, not obvious. Proven - with a test, an effect size, "
        "a validated model and a dollar figure attached to each one.",
        K, color=VIOLET)

    d.tile_grid("Apply it to YOUR capstone this afternoon", [
        ("Chart your Y over time", "Run chart with median and run rules - is your process even stable?"),
        ("Pareto your defects by COST", "Weight by cost of one occurrence, not by count"),
        ("Run one fishbone and 5 Whys", "Multi-vote to five testable candidate Xs"),
        ("Select and run two tests", "Use the decision tree; document the assumption checks"),
        ("Fit a multiple regression", "Report adjusted R-squared, VIF and all four residual plots"),
        ("Write two sponsor sentences", "The decision you want, and the dollar value behind it"),
    ], kicker=K, cols=2, accent=AMBER)
