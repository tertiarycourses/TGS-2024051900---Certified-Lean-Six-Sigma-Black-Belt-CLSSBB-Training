#!/usr/bin/env python3
"""Foundations teaching slides — Black Belt depth.

The Black Belt Role, Portfolio Selection & Your Capstone. Covers what Six Sigma
is, Lean vs Six Sigma, Y = f(X), sigma level / DPMO / the 1.5 sigma shift, the
belt ladder with an explicit BB-vs-GB contrast, portfolio selection and strategy
alignment, COPQ at portfolio scale, the capstone project, and a full-depth DMAIC
and tollgate-governance recap.
"""
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


def foundations(d):
    K = "FOUNDATIONS - THE BLACK BELT ROLE"

    # ================================================================
    # SECTION OPENER
    # ================================================================
    d.section("FOUNDATIONS", "The Black Belt Role, Portfolio Selection & Your Capstone", "00",
              "BB vs GB - Portfolio selection - Strategy alignment - COPQ - Capstone chartering - DMAIC at altitude")

    d.big_statement(
        "You already know how to run a project.",
        "This week is about running a PORTFOLIO of them, owning the statistics nobody else in the room "
        "can defend, and coaching the Green Belts who report their work to you.",
        "WHY YOU ARE HERE", color=BLUE)

    d.tile_grid(
        "What This Opening Module Delivers",
        [("A shared technical baseline", "Six Sigma, Lean, Y = f(X), sigma level and DPMO re-established at Black Belt precision."),
         ("A clear role boundary", "Exactly what a Black Belt does that a Green Belt does not - and is paid to do."),
         ("A portfolio method", "Criteria, weighted scoring and strategy alignment for choosing which projects live."),
         ("A money language", "COPQ rolled up from one project to a whole programme, in dollars Finance accepts."),
         ("Your capstone project", "You pick your own workplace process today and build it across every lab this week."),
         ("DMAIC and tollgates", "The five phases and the five gates, at the depth needed to mentor others through them.")],
        kicker=K, cols=2, accent=BLUE)

    d.big_statement(
        "Meridian Medical Devices",
        "Our running case all week: infusion pump assemblies built on 6 lines across 3 plants - "
        "Singapore, Penang and Suzhou. OTIF, first-pass yield and warranty returns are the metrics "
        "the board watches. Every worked example lands here.",
        "THE RUNNING SCENARIO", color=TEAL)

    d.tile_grid(
        "Meridian at a Glance - The Numbers You Will Reuse",
        [("Volume", "412,000 infusion pump assemblies shipped last financial year across the three plants."),
         ("First-pass yield", "Singapore 96.1 pct, Penang 91.4 pct, Suzhou 88.7 pct - a 7.4 point spread nobody has explained."),
         ("OTIF", "On-time in-full sits at 87.2 pct against a customer contract commitment of 96 pct."),
         ("Warranty returns", "2,140 field returns last year, average settlement cost SGD 780 per unit."),
         ("Rework", "One line in Penang runs a permanent 4-person rework cell that is not in the standard cost."),
         ("Board pressure", "The CEO has asked for a 30 pct reduction in cost of poor quality within 12 months.")],
        kicker="MERIDIAN MEDICAL DEVICES", cols=2, accent=TEAL)

    # ================================================================
    # 1. WHAT SIX SIGMA IS
    # ================================================================
    d.big_statement(
        "Six Sigma is three things at once.",
        "A statistical measure of capability, a structured improvement method, and a management "
        "philosophy about running the business on data. A Black Belt has to be fluent in all three.",
        "WHAT SIX SIGMA ACTUALLY IS", color=VIOLET)

    d.compare_panels(
        "The Three Faces of Six Sigma",
        [("A metric", "Sigma level and DPMO",
          ["Counts how many standard deviations fit between mean and spec",
           "Six sigma performance = 3.4 defects per million opportunities",
           "Lets you compare a soldering line to an invoicing process",
           "This is the face you defend in front of engineers"]),
         ("A method", "DMAIC and DMADV",
          ["Define, Measure, Analyze, Improve, Control - in that order",
           "Each phase closes at a tollgate with evidence, not opinion",
           "Prevents jumping from symptom straight to pet solution",
           "This is the face you run projects with"]),
         ("A philosophy", "Management by data",
          ["Decisions are made from measured process data, not seniority",
           "Every process has a customer whose voice sets the target",
           "Variation is treated as a cost, not as bad luck",
           "This is the face you sell to the steering committee"])],
        kicker="THREE FACES", accent=VIOLET)

    d.tile_grid(
        "What Six Sigma Is Not",
        [("Not a quality department", "It is a line-management discipline. Quality assurance audits; Six Sigma changes the process."),
         ("Not statistics for its own sake", "Statistics is the evidence, never the deliverable. The deliverable is a changed, controlled process."),
         ("Not a training programme", "Belts without live projects produce certificates and no benefit. Projects are the point."),
         ("Not a substitute for strategy", "It executes strategy faster. It cannot tell you which market to be in.")],
        kicker="CLEARING THE MYTHS", cols=2, accent=RED)

    d.timeline(
        "How We Got Here",
        [("1924", "Shewhart invents the control chart at Western Electric"),
         ("1950s", "Deming and Juran rebuild Japanese manufacturing quality"),
         ("1986", "Bill Smith coins Six Sigma at Motorola"),
         ("1995", "Jack Welch makes it GE's central initiative"),
         ("2002", "Lean and Six Sigma formally merge into Lean Six Sigma"),
         ("Today", "Applied across services, healthcare, finance and software")],
        kicker="A SHORT HISTORY", accent=AMBER)

    d.tile_grid(
        "What Each Era Contributed - And Why It Still Matters to You",
        [("Shewhart, 1924", "Separated common cause from special cause. Without this distinction you tamper and make things worse."),
         ("Deming, 1950s", "94 pct of problems belong to the system, not the worker. This is why you attack process, not people."),
         ("Juran, 1950s", "The vital few versus the trivial many - the logic behind every Pareto chart you will draw."),
         ("Motorola, 1986", "Turned capability into a single comparable number so plants could be ranked honestly."),
         ("GE, 1995", "Tied belt certification to hard financial benefit signed by Finance. Still the standard."),
         ("Toyota, ongoing", "Flow, pull and respect for people - the Lean half of what you now lead.")],
        kicker="THE INHERITANCE", cols=2, accent=AMBER)

    # ================================================================
    # 2. QUALITY, LEAN, LEAN SIX SIGMA
    # ================================================================
    d.compare_panels(
        "Three Definitions of Quality - Only One Survives Scrutiny",
        [("Defect free", "The zero defect answer",
          ["Free of what defect, defined by whom?",
           "A pump with no cosmetic flaw can still arrive late",
           "Silent on everything the buyer actually valued",
           "Verdict: incomplete"]),
         ("Conforms to spec", "The engineering answer",
          ["Measurable and auditable - a real improvement",
           "But who wrote the spec, and from what evidence?",
           "A wrong spec met perfectly is still a failed product",
           "Verdict: necessary but not sufficient"]),
         ("Meets customer needs", "The Six Sigma answer",
          ["The customer defines what good looks like",
           "The spec is then derived from that voice, and traceable to it",
           "Covers delivery, service and cost, not only the part",
           "Verdict: this is the working definition"])],
        kicker="DEFINING QUALITY", accent=BLUE)

    d.vs_diagram(
        "Lean plus Six Sigma equals Lean Six Sigma",
        ("Lean", ["Speed, flow and lead time",
                  "Attacks waste and non-value-add steps",
                  "Fast, visual, shop-floor tools",
                  "Weak on statistical proof"]),
        ("Six Sigma", ["Accuracy, capability and variation",
                       "Attacks defects and inconsistency",
                       "Rigorous data and inferential statistics",
                       "Slow on waste that is already obvious"]),
        ("LEAN SIX SIGMA",
         "Right things, done fast AND done right - waste removal carrying statistical proof, run through DMAIC"),
        kicker="THE COMBINATION")

    d.tile_grid(
        "Which Half Leads - A Black Belt Judgement Call",
        [("Long lead time, few defects", "Lean leads. Map the value stream, attack queues and batch size before touching statistics."),
         ("Short lead time, many defects", "Six Sigma leads. Find the Xs driving variation and bring them under control."),
         ("Both at once", "Lean first to expose the true process, then Six Sigma on the variation that remains."),
         ("Neither is clear", "Measure first. Choosing a toolkit before baseline data is the classic Green Belt error.")],
        kicker="CHOOSING YOUR EMPHASIS", cols=2, accent=BLUE)

    # ================================================================
    # 3. COPQ ICEBERG
    # ================================================================
    d.big_statement(
        "Most of what poor quality costs you is invisible.",
        "Scrap and rework sit above the waterline where accounting can see them. The larger cost - "
        "expediting, lost customers, excess inventory, management attention - never appears in a cost code.",
        "THE COST OF POOR QUALITY", color=RED)

    d.compare_panels(
        "The COPQ Iceberg",
        [("Above the waterline", "Visible and already booked",
          ["Scrap and material write-off",
           "Rework labour and rework cell headcount",
           "Warranty settlements and field returns",
           "Inspection and sorting labour",
           "Typically only 15 to 20 pct of true COPQ"]),
         ("Just below", "Traceable if you look",
          ["Expedited freight and premium shipping",
           "Excess safety stock held to cover variation",
           "Line downtime and unplanned changeovers",
           "Engineering time on recurring deviations",
           "Recoverable with effort from the ERP"]),
         ("Deep below", "Real but never coded",
          ["Lost customers and orders never quoted",
           "Price concessions granted to keep an account",
           "Management hours in escalation meetings",
           "Reputation and audit findings with regulators",
           "Estimated, not extracted - but still real"])],
        kicker="WHERE THE MONEY HIDES", accent=RED)

    d.formula_card(
        "Quantifying COPQ at Meridian",
        [("COPQ as pct of revenue", "COPQ / Revenue x 100",
          "Meridian: SGD 11.4m COPQ on SGD 142m revenue = 8.0 pct. World class is under 1 pct."),
         ("Cost per defect", "Total failure cost / Defect count",
          "2,140 warranty returns x SGD 780 settlement = SGD 1.67m external failure alone."),
         ("Hidden factory ratio", "Rework hours / Total direct hours",
          "Penang rework cell: 4 staff x 1,800 h = 7,200 h against 96,000 direct h = 7.5 pct.")],
        kicker="COPQ ARITHMETIC", accent=RED,
        note="Rule of thumb: a 3 sigma organisation loses 25 to 40 pct of revenue to COPQ; a 5 sigma one loses under 5 pct.")

    d.tile_grid(
        "The Four COPQ Categories - Know Which You Are Attacking",
        [("Internal failure", "Defects caught before the customer - scrap, rework, re-test, downgrade. Cheap to find, expensive to repeat."),
         ("External failure", "Defects the customer caught - warranty, returns, recalls, credits. 10x the cost of internal failure."),
         ("Appraisal", "The cost of checking - inspection, testing, audit. Spending here treats symptoms, not causes."),
         ("Prevention", "The cost of designing defects out - training, capability studies, poka-yoke. The only spend that pays back.")],
        kicker="PREVENTION - APPRAISAL - FAILURE", cols=2, accent=AMBER)

    # ================================================================
    # 4. Y = f(X)
    # ================================================================
    d.big_statement(
        "Y = f(X)",
        "The single most important equation in Six Sigma. You cannot manage the Y. You can only find, "
        "control and improve the Xs that produce it. Every phase of DMAIC exists to move you from the Y to the vital few Xs.",
        "THE CORE MODEL", color=VIOLET)

    d.compare_panels(
        "Reading the Equation Properly",
        [("Y - the output", "The dependent variable",
          ["What the customer feels and the board measures",
           "Always a result, always downstream, always lagging",
           "Cannot be changed directly - only through the Xs",
           "Meridian Y: on-time in-full at 87.2 pct"]),
         ("f - the transfer function", "The relationship",
          ["The process itself: how the Xs combine to make the Y",
           "May be linear, curved, or full of interactions",
           "Discovering f IS the Analyze phase",
           "Regression, ANOVA and DOE are how you estimate it"]),
         ("X - the inputs", "The independent variables",
          ["Materials, methods, machines, people, measures, environment",
           "Controllable, noise, or critical-to-process",
           "Leading indicators - they move before Y does",
           "Meridian Xs: supplier lot, oven profile, operator shift"])],
        kicker="Y = f(X)", accent=VIOLET)

    d.flow_h(
        "How DMAIC Walks You From Y to the Vital Few Xs",
        ["DEFINE - name the Y precisely and set its target",
         "MEASURE - trust the Y measurement, then baseline it",
         "ANALYZE - list 30 candidate Xs, prove which 3 matter",
         "IMPROVE - change those Xs and confirm the Y moved",
         "CONTROL - hold the Xs so the Y never drifts back"],
        kicker="THE FUNNEL", color=VIOLET, colors=DMAIC_COLORS)

    d.tile_grid(
        "Classifying Your Xs - A Black Belt Habit",
        [("Controllable X", "You can set it and hold it - oven temperature, torque setting, approved supplier list."),
         ("Noise X", "Real but not economically controllable - ambient humidity, incoming lot variation, shift fatigue."),
         ("Critical X", "Proven by data to drive the Y. These earn a control plan entry. Usually only 3 to 5 exist."),
         ("Standard operating X", "Already known and already controlled. Do not spend Analyze effort re-proving these."),
         ("Constraint X", "Cannot be changed for regulatory or contractual reasons - design the solution around it."),
         ("Suspect X", "Named by the team but unproven. Stays suspect until hypothesis testing promotes or kills it.")],
        kicker="X CLASSIFICATION", cols=2, accent=VIOLET)

    d.tile_grid(
        "Y = f(X) at Meridian - Worked Through",
        [("Business Y", "Warranty cost per 1,000 units shipped - the figure the board sees each quarter."),
         ("Process Y", "First-pass yield at final electrical test - 88.7 pct at Suzhou versus 96.1 pct at Singapore."),
         ("Candidate Xs", "Solder paste lot, reflow profile, operator certification level, board supplier, shift, humidity."),
         ("Proven X 1", "Reflow zone-3 temperature - explains 41 pct of yield variation by regression."),
         ("Proven X 2", "Solder paste age at point of use - beyond 8 hours yield drops 6 points."),
         ("Everything else", "Twenty-one other suspected Xs tested and found statistically insignificant. That is a result too.")],
        kicker="FROM 27 XS TO 2", cols=2, accent=TEAL)

    # ================================================================
    # 5. SIGMA LEVEL, DPMO, THE SHIFT
    # ================================================================
    d.big_statement(
        "Sigma level is a common currency.",
        "It lets you put a solder line, an invoice process and a discharge ward on the same scale. "
        "As a Black Belt you must be able to compute it, defend the 1.5 sigma shift, and explain both to a sceptical VP.",
        "MEASURING CAPABILITY", color=VIOLET)

    d.normal_curve(
        "Why It Is Called SIX Sigma",
        kicker="THE BELL CURVE",
        note="Six sigma capability means the nearest specification limit sits six standard deviations from the process mean.")

    d.formula_card(
        "The Core Capability Formulas",
        [("Defects per unit", "DPU = Defects / Units",
          "Meridian Suzhou: 1,412 defects found on 12,400 boards = DPU 0.1139."),
         ("DPMO", "DPMO = (Defects / (Units x Opps)) x 1,000,000",
          "1,412 defects, 12,400 boards, 340 solder joints each = 335 DPMO."),
         ("First-pass yield", "FPY = Units passing first time / Units started",
          "11,001 of 12,400 boards passed at first test = 88.7 pct FPY."),
         ("Rolled throughput yield", "RTY = Y1 x Y2 x ... x Yn",
          "0.97 x 0.94 x 0.96 x 0.99 across four Suzhou stations = 86.6 pct RTY.")],
        kicker="FORMULAS YOU MUST OWN", accent=VIOLET,
        note="DPMO normalises for complexity - that is why it can compare a 340-joint board to a 3-field invoice.")

    d.tile_grid(
        "Defining an Opportunity - Where Most Sigma Numbers Go Wrong",
        [("An opportunity is a chance to fail", "One measurable characteristic that can be judged conforming or not - nothing looser."),
         ("Be honest, not generous", "Inflating opportunity count inflates your sigma level. Auditors and peers will find it."),
         ("Count only what you inspect", "If you never test a joint, it is not an opportunity for your DPMO - it is a blind spot."),
         ("Keep the definition frozen", "Change the opportunity definition mid-project and your baseline becomes meaningless."),
         ("Document it in the charter", "The opportunity definition is a tollgate deliverable at Measure, not a footnote."),
         ("Same rule across sites", "Meridian cannot compare Penang to Suzhou unless both count joints the same way.")],
        kicker="THE OPPORTUNITY TRAP", cols=2, accent=RED)

    d.ladder(
        "The Sigma Ladder - Capability Versus Defect Rate",
        [("2 sigma", "308,537 DPMO - 69 pct yield. Most unmanaged manual processes."),
         ("3 sigma", "66,807 DPMO - 93.3 pct yield. The typical unimproved business process."),
         ("4 sigma", "6,210 DPMO - 99.38 pct yield. Where a good Green Belt project lands."),
         ("5 sigma", "233 DPMO - 99.977 pct yield. Requires designed-in control, not inspection."),
         ("6 sigma", "3.4 DPMO - 99.9997 pct yield. Best-in-class, rarely economic everywhere.")],
        kicker="THE SIGMA SCALE", accent=VIOLET,
        note="Each step up is roughly a 10x reduction in defects - and roughly a 10x increase in the discipline required.")

    d.formula_card(
        "Converting Yield to Sigma Level - The Meridian Worked Example",
        [("Step 1 - DPMO", "DPMO = (1 - Yield) x 1,000,000",
          "Suzhou final test yield 0.887 -> DPMO = 0.113 x 1,000,000 = 113,000."),
         ("Step 2 - Look up Z", "Z(short term) from the standard normal table",
          "113,000 DPMO -> long-term Z = 1.21 from the normal distribution."),
         ("Step 3 - Add the shift", "Sigma level = Z(long term) + 1.5",
          "1.21 + 1.5 = 2.71 sigma. Suzhou runs at roughly 2.7 sigma at final test."),
         ("Step 4 - Set the target", "Target DPMO from target sigma",
          "Moving Suzhou to 4 sigma means 6,210 DPMO - a 94 pct reduction in defects.")],
        kicker="YIELD -> DPMO -> SIGMA", accent=VIOLET,
        note="Report the assumption every time: sigma levels quoted here include the conventional 1.5 sigma long-term shift.")

    d.compare_panels(
        "The 1.5 Sigma Shift - What It Is and Why You Must Declare It",
        [("The observation", "Motorola, 1980s",
          ["Short-term studies looked far better than long-run results",
           "Over weeks the mean drifts with tooling, lots and shifts",
           "Empirically the drift averaged about 1.5 standard deviations",
           "So a 6 sigma short-term process yields 3.4 DPMO long term"]),
         ("The convention", "How the industry uses it",
          ["Published sigma tables already bake in the 1.5 shift",
           "Sigma level = long-term Z + 1.5, by convention",
           "Cp / Cpk are short term; Pp / Ppk are long term",
           "6 sigma short term = 4.5 sigma long term = 3.4 DPMO"]),
         ("The Black Belt duty", "Where it goes wrong",
          ["It is an empirical convention, not a law of physics",
           "Some processes drift far more, some barely at all",
           "Never compare a shifted number to an unshifted one",
           "State the assumption on every capability slide you present"])],
        kicker="THE 1.5 SIGMA SHIFT", accent=AMBER)

    d.tile_grid(
        "Sigma Conversion Table - The Numbers to Memorise",
        [("6.0 sigma", "3.4 DPMO - 99.99966 pct yield - best in class"),
         ("5.0 sigma", "233 DPMO - 99.977 pct yield - excellent"),
         ("4.5 sigma", "1,350 DPMO - 99.87 pct yield - strong"),
         ("4.0 sigma", "6,210 DPMO - 99.38 pct yield - industry average plus"),
         ("3.0 sigma", "66,807 DPMO - 93.32 pct yield - industry average"),
         ("2.0 sigma", "308,537 DPMO - 69.15 pct yield - non-competitive")],
        kicker="CONVERSION TABLE", cols=2, accent=VIOLET)

    d.tile_grid(
        "Why 3 Sigma Is Not Good Enough - The Compounding Argument",
        [("One step at 99.38 pct", "Sounds excellent. A 4 sigma single operation looks like a solved problem."),
         ("Ten steps in series", "0.9938 to the power 10 = 93.9 pct RTY. One in sixteen units touched rework."),
         ("Fifty steps in series", "0.9938 to the power 50 = 73.2 pct RTY. Over a quarter of units need intervention."),
         ("Meridian reality", "The pump assembly has 62 sequential process steps across three plants."),
         ("The lesson", "Complexity multiplies defect exposure. Step-level yield flatters system-level truth."),
         ("The response", "Always report RTY, never only final yield. RTY is what exposes the hidden factory.")],
        kicker="THE COMPOUNDING PROBLEM", cols=2, accent=RED)

    # ================================================================
    # 6. THE BELT LADDER
    # ================================================================
    d.big_statement(
        "The belt system is a division of labour, not a hierarchy of intelligence.",
        "Each belt owns a different scope, a different toolset and a different kind of accountability. "
        "Knowing exactly where your boundary sits is what makes a deployment work.",
        "THE BELT ROLES", color=BLUE)

    d.ladder(
        "The Belt Ladder",
        [("White Belt", "Awareness only. Understands the vocabulary and supports projects locally."),
         ("Yellow Belt", "Team member. Collects data, maps process steps, contributes subject knowledge."),
         ("Green Belt", "Leads one project part-time in their own area, with Black Belt support."),
         ("Black Belt", "Full-time. Leads a portfolio, owns the advanced statistics, mentors Green Belts."),
         ("Master Black Belt", "Deploys the programme, trains and certifies belts, owns the methodology."),
         ("Champion / Sponsor", "Selects and funds projects, removes barriers, decides at every tollgate.")],
        kicker="SIX ROLES", accent=BLUE,
        note="Time commitment rises with the rung: Yellow a few hours, Green 20 to 25 pct, Black Belt 100 pct.")

    d.compare_panels(
        "Green Belt Versus Black Belt - The Real Boundary",
        [("Green Belt", "One project, part time",
          ["Leads a single project inside their own department",
           "Uses descriptive stats, basic hypothesis tests, control charts",
           "Escalates anything needing DOE, MSA design or regression",
           "Reports at tollgates - does not run them",
           "Benefit typically SGD 50k to 150k per project"]),
         ("Black Belt", "A portfolio, full time",
          ["Leads 4 to 6 concurrent projects across functions and sites",
           "Owns DOE, regression, ANOVA, MSA design, capability analysis",
           "Mentors and technically reviews the Green Belts' work",
           "Runs the tollgate and prepares the sponsor's decision",
           "Benefit typically SGD 500k to 1m per year of portfolio"]),
         ("The five deltas", "What you now add",
          ["1. Portfolio - selecting and sequencing, not just executing",
           "2. Advanced statistics - you are the last technical authority",
           "3. Mentoring - Green Belt capability is your deliverable too",
           "4. Tollgate governance - you run the gate, sponsor decides",
           "5. Finance validation - benefits signed off, not self-declared"])],
        kicker="BB vs GB - THE DECISIVE COMPARISON", accent=VIOLET)

    d.tile_grid(
        "The Five Black Belt Accountabilities in Detail",
        [("Own a portfolio", "Select, sequence, resource and kill projects. Say no to work that will not deliver."),
         ("Be the statistical authority", "When a result is challenged in a steering meeting, the defence stops with you."),
         ("Develop Green Belts", "Coach through tools, review their analysis, catch their errors before the sponsor does."),
         ("Run disciplined tollgates", "Assemble evidence, frame the decision, let the sponsor decide go, adjust or kill."),
         ("Validate benefit with Finance", "No claimed saving is real until a finance controller signs the calculation."),
         ("Escalate honestly", "Report a failing project early. Concealment is the fastest way to lose a programme.")],
        kicker="WHAT YOU ARE PAID FOR", cols=2, accent=BLUE)

    d.tile_grid(
        "Who Else Is in the Room",
        [("Executive sponsor", "Owns the business objective. Signs the charter, funds the resource, decides at gates."),
         ("Process owner", "Runs the process day to day and inherits the control plan. Must be engaged from Define."),
         ("Master Black Belt", "Your technical coach and the guardian of method. Escalate design-of-experiment doubts here."),
         ("Finance controller", "Independently validates every benefit claim. Involve at Define, not at Control."),
         ("Team members", "Yellow Belts and subject experts who know what actually happens on the floor."),
         ("Deployment leader", "Owns the belt pipeline, the project hopper and the programme-level scorecard.")],
        kicker="THE WIDER CAST", cols=2, accent=TEAL)

    d.matrix2x2(
        "Escalation Rule - When a Green Belt Should Call You",
        "Statistical complexity of the question ->",
        "Business risk ^",
        [("Coach at the next review", "Low complexity, low risk. Let the Green Belt work it out and confirm at the weekly review."),
         ("Take the analysis yourself", "High complexity, high risk. DOE design, regression validity, sample size for a regulated claim."),
         ("Let them run", "Low complexity, low risk. Autonomy builds capability - resist the urge to solve it for them."),
         ("Pair on it", "High complexity, lower risk. The ideal teaching moment - do it together, then let them present it.")],
        kicker="MENTORING JUDGEMENT", accent=VIOLET)

    # ================================================================
    # 7. PORTFOLIO SELECTION
    # ================================================================
    d.big_statement(
        "Choosing the wrong project is the most expensive mistake a Black Belt can make.",
        "A brilliantly executed project on a problem nobody cares about still ends with a cancelled "
        "programme. Selection is a Black Belt skill; a Green Belt is usually handed a project.",
        "PROJECT PORTFOLIO SELECTION", color=AMBER)

    d.flow_h(
        "The Portfolio Selection Cycle",
        ["GENERATE - build a hopper of candidates from COPQ, VOC, audits and strategy",
         "SCREEN - remove anything already solved, out of scope or a known solution",
         "SCORE - rank on weighted criteria with the sponsor in the room",
         "SEQUENCE - schedule against belt capacity and site readiness",
         "CHARTER - convert the top candidates into signed charters",
         "REVIEW - re-score the hopper every quarter as strategy moves"],
        kicker="SIX STEPS", color=AMBER)

    d.tile_grid(
        "Where Good Candidate Projects Come From",
        [("The COPQ analysis", "Follow the money. The biggest failure-cost buckets are usually the biggest opportunities."),
         ("Voice of the customer", "Complaint themes, lost bids and churn interviews name problems customers actually feel."),
         ("Process performance data", "Any metric off target, drifting, or with visibly wide variation is a candidate."),
         ("Audit and regulatory findings", "Repeat non-conformances have a sponsor and a deadline already attached."),
         ("Strategy deployment", "Hoshin breakthrough objectives cascade directly into project candidates."),
         ("Value stream maps", "Bottlenecks, long queues and rework loops identified on the map are ready-made scopes.")],
        kicker="FILLING THE HOPPER", cols=2, accent=AMBER)

    d.tile_grid(
        "The Selection Criteria - What Actually Predicts Success",
        [("Strategic alignment", "Traces to a stated business objective. Without it the sponsor disengages by Analyze."),
         ("Financial benefit", "Hard, quantifiable and Finance-validatable. Soft benefits do not fund a programme."),
         ("Data availability", "If the Y cannot be measured today, Measure phase becomes a six-month data project."),
         ("Scope and duration", "3 to 6 months. Beyond that sponsors change, priorities move and teams disband."),
         ("Solution unknown", "If everyone already knows the fix, it is a just-do-it, not a DMAIC project."),
         ("Process ownership", "A named, willing process owner exists. No owner means no sustained control plan.")],
        kicker="SIX CRITERIA", cols=2, accent=AMBER)

    d.formula_card(
        "The Weighted Scoring Matrix",
        [("Weighted score", "Score = sum of (criterion weight x criterion rating)",
          "Rate each criterion 1 to 5, weights summing to 100 pct. Rank the hopper by total."),
         ("Meridian project A", "Suzhou solder yield improvement",
          "Align 5 x .30, Benefit 5 x .25, Data 4 x .20, Scope 4 x .15, Unknown 5 x .10 = 4.65."),
         ("Meridian project B", "Warehouse label reprint reduction",
          "Align 2 x .30, Benefit 2 x .25, Data 5 x .20, Scope 5 x .15, Unknown 2 x .10 = 2.85."),
         ("The decision", "Charter A, defer B, revisit at the next quarterly hopper review",
          "A is worth SGD 1.4m and is on strategy. B is worth SGD 40k and is a just-do-it.")],
        kicker="SCORING WORKED THROUGH", accent=AMBER,
        note="Do the scoring WITH the sponsor. A matrix scored alone in your office convinces nobody.")

    d.matrix2x2(
        "The Benefit Versus Effort Screen",
        "Effort and complexity ->",
        "Business benefit ^",
        [("QUICK WINS", "High benefit, low effort. Do these immediately - often just-do-it or Kaizen, not full DMAIC."),
         ("MAJOR PROJECTS", "High benefit, high effort. This is where Black Belt DMAIC projects belong. Charter these."),
         ("FILL-INS", "Low benefit, low effort. Good Green Belt training projects. Never occupy Black Belt capacity."),
         ("THANKLESS", "Low benefit, high effort. Say no, and say it early with the scoring matrix as your evidence.")],
        kicker="TRIAGE", accent=AMBER)

    d.tile_grid(
        "Strategy Alignment - Hoshin Kanri Cascade",
        [("Level 1 - Breakthrough objective", "Meridian: reduce cost of poor quality by 30 pct within 12 months."),
         ("Level 2 - Annual objective", "Lift group first-pass yield from 92.1 pct to 96.0 pct this financial year."),
         ("Level 3 - Site target", "Suzhou final-test FPY from 88.7 pct to 95.0 pct by Q3."),
         ("Level 4 - Project Y", "Reduce solder-joint defects at Suzhou reflow from 113,000 DPMO to 20,000 DPMO."),
         ("Catchball", "Targets negotiated up and down until the site genuinely owns them - not imposed."),
         ("The test", "Every project must trace up all four levels. If it cannot, it does not get chartered.")],
        kicker="HOSHIN KANRI", cols=2, accent=BLUE)

    d.tile_grid(
        "Saying No - A Core Black Belt Skill",
        [("No, it is a just-do-it", "The cause and fix are already known. Hand it to the process owner today."),
         ("No, there is no measurable Y", "Without a measurable output there is no baseline, no proof and no control."),
         ("No, the scope is a whole function", "Boil-the-ocean scopes fail. Offer a scoped slice of the same problem instead."),
         ("No, there is no sponsor", "A project without a sponsor has no decision maker and no resource. Decline it."),
         ("Not now - it is queued", "Sequenced behind higher-scoring work. Show the matrix; the ranking does the arguing."),
         ("How to say it", "Never a flat refusal. Show the criteria, the score and what you WILL do instead.")],
        kicker="PORTFOLIO DISCIPLINE", cols=2, accent=RED)

    d.tile_grid(
        "Managing a Live Portfolio of Four to Six Projects",
        [("Stagger the phases", "Never have three projects in Analyze at once - the statistical load lands on you alone."),
         ("One scorecard", "A single portfolio view: phase, tollgate date, benefit forecast, RAG status, blocker."),
         ("Protect Green Belt time", "The commonest cause of stalled projects is a Green Belt pulled back to day job."),
         ("Kill fast", "A project that misses two consecutive tollgates should be killed, not nursed."),
         ("Bank the benefits", "Track realised versus forecast benefit monthly for 12 months after Control."),
         ("Refresh the hopper", "Quarterly re-scoring keeps the portfolio aligned as strategy shifts under you.")],
        kicker="PORTFOLIO MANAGEMENT", cols=2, accent=TEAL)

    d.pareto_chart(
        "Meridian COPQ by Category - Where the Portfolio Should Aim",
        [("Warranty and field returns", 1670),
         ("Rework labour", 1240),
         ("Scrap and write-off", 980),
         ("Expedited freight", 610),
         ("Excess inventory carry", 420),
         ("Inspection and sorting", 310),
         ("Line downtime", 180)],
        kicker="COPQ AT PORTFOLIO SCALE",
        note="SGD thousands. Three categories carry 71 pct of COPQ - that is where the first three charters go.")

    d.tile_grid(
        "Rolling COPQ Up From Project to Programme",
        [("Project level", "One charter, one Y, one benefit figure signed by one finance controller."),
         ("Site level", "Sum the project benefits, subtract double-counting where two projects touch the same cost."),
         ("Programme level", "Aggregate across sites, net of belt cost, training cost and any capital spend."),
         ("The double-count trap", "Two projects both claiming the same scrap reduction is the fastest way to lose credibility."),
         ("The netting rule", "Report gross benefit, programme cost and net benefit separately. Never only the gross."),
         ("Reporting cadence", "Monthly to the deployment leader, quarterly to the steering committee, with Finance present.")],
        kicker="COPQ AT SCALE", cols=2, accent=RED)

    # ================================================================
    # 8. THE CAPSTONE PROJECT
    # ================================================================
    d.big_statement(
        "Your capstone starts today.",
        "Alongside the WSQ assessment, you build a capstone project on YOUR own workplace process - "
        "chosen today, developed in every lab, and presented to a simulated steering committee on Day 5.",
        "YOUR CAPSTONE PROJECT", color=TEAL)

    d.tile_grid(
        "How the Capstone Works",
        [("You choose it today", "Pick a real process you own or influence at work. Real data, real sponsor, real benefit."),
         ("It grows in every lab", "Each lab applies that session's tool to YOUR process, not to a textbook case."),
         ("It accumulates artefacts", "Charter, SIPOC, MSA, capability study, hypothesis tests, DOE, control plan - all yours."),
         ("Day 5 consolidates", "The final day assembles everything into one coherent project storyboard."),
         ("You present to a panel", "A simulated steering committee tollgate review, with challenge questions."),
         ("Additional to the WSQ papers", "You also sit the Written Assessment (SAQ) and the Case Study on Day 5. Both open book.")],
        kicker="THE ASSESSMENT MODEL", cols=2, accent=TEAL)

    d.flow_h(
        "Your Capstone Across the Five Days",
        ["DAY 1 - choose the process, draft the charter, define the Y and the business case",
         "DAY 2 - SIPOC, VOC, CTQ flowdown, MSA and baseline capability on your data",
         "DAY 3 - graphical analysis, hypothesis tests and regression to find your vital few Xs",
         "DAY 4 - DOE, solution design, pilot plan, FMEA and your control plan",
         "DAY 5 - consolidate the storyboard and present to the steering committee panel"],
        kicker="THE FIVE-DAY ARC", color=TEAL)

    d.tile_grid(
        "Choosing a Good Capstone Process - Today",
        [("You can access the data", "Existing measurements you can actually obtain this week. No data, no capstone."),
         ("The Y is measurable", "A continuous or countable output you can baseline - cycle time, yield, error rate, cost."),
         ("The solution is not obvious", "If you already know the fix, choose something else - you will learn nothing."),
         ("Scope is a process, not a function", "One process with a clear start and end. Not 'improve the supply chain'."),
         ("You have standing", "A process you own, support or can influence. Not someone else's department."),
         ("It matters to someone", "A named person would be pleased if it improved. That person is your sponsor.")],
        kicker="CHOOSE WELL - IT RUNS ALL WEEK", cols=2, accent=TEAL)

    d.tile_grid(
        "Your Day 1 Capstone Charter - The Six Boxes",
        [("Problem statement", "What, where, when, how big - in measurable terms. No cause, no blame, no solution."),
         ("Goal statement", "From X to Y by when. Specific, measurable and agreed with the sponsor."),
         ("Business case", "Why now, and what it is worth. Link to COPQ or to a strategic objective."),
         ("Scope", "In scope and explicitly out of scope. The out-of-scope list prevents most scope creep."),
         ("Team and sponsor", "Named sponsor, named process owner, named team members with time committed."),
         ("Milestones", "The five tollgate dates. A charter without dates is an intention, not a plan.")],
        kicker="CHARTER ON DAY 1", cols=2, accent=BLUE)

    d.tile_grid(
        "The Day 5 Steering Committee Presentation",
        [("Format", "15 minutes of storyboard plus 10 minutes of challenge questions from the panel."),
         ("Structure", "One slide per DMAIC phase, showing the evidence that closed each tollgate."),
         ("The data must be yours", "Real numbers from your own process. Invented data is obvious and scores nothing."),
         ("Defend the statistics", "Expect to be asked why that test, that sample size, that confidence level."),
         ("State the benefit", "A quantified benefit with the assumptions visible, as Finance would want to see it."),
         ("Name the risks", "A credible presentation names what could still go wrong and how control handles it.")],
        kicker="DAY 5 - THE FINAL TOLLGATE", cols=2, accent=VIOLET)

    d.tile_grid(
        "How Your Capstone Is Judged",
        [("Correct tool selection", "Did you choose the right tool for the data type and the question asked?"),
         ("Sound execution", "Assumptions checked, sample sizes justified, conclusions supported by the output."),
         ("A clear causal chain", "The Xs you improved are demonstrably the Xs your analysis proved mattered."),
         ("A workable control plan", "Something the process owner could genuinely run after you leave."),
         ("A defensible benefit", "A calculation a finance controller would sign, with assumptions declared."),
         ("Presentation under challenge", "Held your position on evidence, and conceded gracefully where evidence was thin.")],
        kicker="ASSESSMENT CRITERIA", cols=2, accent=AMBER)

    # ================================================================
    # 9. DMAIC AT DEPTH
    # ================================================================
    d.big_statement(
        "You know DMAIC. Now you have to be able to teach it.",
        "The next slides recap all five phases at the depth a Black Belt needs to mentor Green Belts "
        "through them, run their tollgates, and recognise each phase's characteristic failure mode.",
        "DMAIC AT ALTITUDE", color=BLUE)

    d.dmaic_wheel(
        "The DMAIC Roadmap",
        [("D", "Define", ["Charter and business case", "Voice of the customer", "CTQ flowdown", "SIPOC and scope", "Team and sponsor"]),
         ("M", "Measure", ["Operational definitions", "Data collection plan", "Measurement system analysis", "Baseline capability", "Process mapping"]),
         ("A", "Analyze", ["Graphical analysis", "Root cause hypotheses", "Hypothesis testing", "Regression and ANOVA", "Vital few Xs proven"]),
         ("I", "Improve", ["Solution generation", "Design of experiments", "Pilot and validate", "FMEA on the solution", "Implementation plan"]),
         ("C", "Control", ["Control plan", "Statistical process control", "Standard work and training", "Handover to process owner", "Benefit realisation"])],
        kicker="THE FIVE PHASES")

    d.tile_grid(
        "DEFINE - Purpose, Tools, Tollgate, Failure Mode",
        [("Purpose", "Establish what problem is being solved, for whom, worth how much, and within what boundary."),
         ("Core tools", "Project charter, VOC capture, Kano, CTQ tree, SIPOC, stakeholder analysis, RACI."),
         ("Tollgate deliverable", "A signed charter with a measurable Y, an agreed scope and a Finance-acknowledged business case."),
         ("Failure mode", "A vague problem statement that contains a cause or a solution - guarantees a wandering project."),
         ("Mentoring cue", "Green Belts write goals like 'improve quality'. Push until it reads 'from 88.7 pct to 95.0 pct by Q3'."),
         ("Time share", "Roughly 15 pct of project effort. Rushing Define costs three times as much in Analyze.")],
        kicker="PHASE 1 - DEFINE", cols=2, accent=BLUE)

    d.tile_grid(
        "MEASURE - Purpose, Tools, Tollgate, Failure Mode",
        [("Purpose", "Prove the measurement system is trustworthy, then establish an honest baseline of the Y."),
         ("Core tools", "Operational definitions, data collection plan, MSA and Gage R and R, capability study, detailed process map."),
         ("Tollgate deliverable", "A validated measurement system plus a baseline capability figure with its confidence interval."),
         ("Failure mode", "Skipping MSA. If the gauge is the source of variation, every later conclusion is wrong."),
         ("Mentoring cue", "Ask 'how do you know the data is right?' before you ever discuss what the data shows."),
         ("Time share", "Roughly 25 pct of effort. This is where Green Belts most often need Black Belt rescue.")],
        kicker="PHASE 2 - MEASURE", cols=2, accent=TEAL)

    d.tile_grid(
        "ANALYZE - Purpose, Tools, Tollgate, Failure Mode",
        [("Purpose", "Move from a long list of suspected Xs to a short list proven by data to drive the Y."),
         ("Core tools", "Graphical analysis, fishbone, 5 Whys, hypothesis tests, ANOVA, regression, multi-vari studies."),
         ("Tollgate deliverable", "Statistically validated root causes, with the p-values and effect sizes that justify them."),
         ("Failure mode", "Confirmation bias - testing only the cause the team already believed, and stopping there."),
         ("Mentoring cue", "Insist on practical significance alongside statistical significance. A tiny proven effect is still tiny."),
         ("Time share", "Roughly 25 pct. This is the phase where the Black Belt's statistical ownership is most visible.")],
        kicker="PHASE 3 - ANALYZE", cols=2, accent=VIOLET)

    d.tile_grid(
        "IMPROVE - Purpose, Tools, Tollgate, Failure Mode",
        [("Purpose", "Design, test and prove solutions that move the vital few Xs, and therefore move the Y."),
         ("Core tools", "Design of experiments, response surface, solution selection matrix, pilot design, FMEA, poka-yoke."),
         ("Tollgate deliverable", "Piloted solution with before-and-after data proving the Y improved, plus a full implementation plan."),
         ("Failure mode", "Implementing without a pilot, then discovering the side effects in production at full scale."),
         ("Mentoring cue", "Always ask what else this change touches. Optimising one Y at the cost of another is common."),
         ("Time share", "Roughly 20 pct. Tempting to start here on day one - resist it, and stop your Green Belts too.")],
        kicker="PHASE 4 - IMPROVE", cols=2, accent=AMBER)

    d.tile_grid(
        "CONTROL - Purpose, Tools, Tollgate, Failure Mode",
        [("Purpose", "Lock the gain in so the process cannot drift back after the project team disperses."),
         ("Core tools", "Control plan, SPC charts, standard work, visual management, training plan, response plan, audit schedule."),
         ("Tollgate deliverable", "Signed control plan, trained operators, live charts and a formal handover to the process owner."),
         ("Failure mode", "Handing over a control plan nobody was trained on - performance decays within one quarter."),
         ("Mentoring cue", "Return at 3, 6 and 12 months. A gain that is not still there at 12 months was never a gain."),
         ("Time share", "Roughly 15 pct. The most skipped phase and the reason most improvements silently reverse.")],
        kicker="PHASE 5 - CONTROL", cols=2, accent=RED)

    d.tile_grid(
        "When DMAIC Is the Wrong Roadmap",
        [("The process does not exist", "Use DMADV or DFSS. You cannot baseline a process that has never run."),
         ("The cause and fix are known", "Just do it. DMAIC on a known solution wastes months and burns sponsor goodwill."),
         ("The problem is pure waste and flow", "A Kaizen event or value stream mapping workshop moves faster than full DMAIC."),
         ("It is a capital or IT project", "Use project management. DMAIC solves variation problems, not installation problems."),
         ("The scope is a whole business", "Too big. Decompose into chartered projects with individual measurable Ys."),
         ("There is no measurable output", "Fix the measurement system first as a project in its own right, then run DMAIC.")],
        kicker="ROADMAP SELECTION", cols=2, accent=GREY)

    # ================================================================
    # 10. TOLLGATE GOVERNANCE
    # ================================================================
    d.big_statement(
        "The Black Belt runs the tollgate. The sponsor decides.",
        "A tollgate is not a status update. It is a formal decision point where evidence is presented "
        "and the sponsor chooses: proceed, adjust the charter, or kill the project.",
        "TOLLGATE GOVERNANCE", color=VIOLET)

    d.flow_h(
        "The Five Tollgates",
        ["GATE D - is the problem worth solving and properly bounded?",
         "GATE M - can we trust the data, and what is the true baseline?",
         "GATE A - are the root causes statistically proven?",
         "GATE I - does the piloted solution actually move the Y?",
         "GATE C - is the gain locked in and formally handed over?"],
        kicker="FIVE DECISION POINTS", color=VIOLET, colors=DMAIC_COLORS)

    d.compare_panels(
        "What Evidence Closes Each Gate",
        [("Gates D and M", "Problem and baseline",
          ["D: signed charter, measurable Y, agreed scope",
           "D: business case acknowledged by Finance",
           "D: named sponsor, process owner and team",
           "M: MSA result showing an acceptable Gage R and R",
           "M: baseline capability with confidence interval"]),
         ("Gates A and I", "Causes and solution",
          ["A: prioritised cause list with test results",
           "A: p-values, effect sizes and practical significance",
           "A: the vital few Xs explicitly named",
           "I: pilot data showing the Y moved, with statistics",
           "I: FMEA on the new process and an implementation plan"]),
         ("Gate C", "Sustainment",
          ["C: signed control plan with reaction rules",
           "C: live SPC charts owned by the process owner",
           "C: standard work updated and operators trained",
           "C: benefit validated and signed by Finance",
           "C: formal handover minute and 3-6-12 month review dates"])],
        kicker="GATE EVIDENCE", accent=VIOLET)

    d.tile_grid(
        "Who Signs Off What",
        [("Executive sponsor", "The gate decision itself: proceed, adjust or kill. Signs the charter and the closure."),
         ("Process owner", "Accepts the control plan and the standard work at Gate C. Owns it thereafter."),
         ("Finance controller", "Validates the business case at Gate D and the realised benefit at Gate C."),
         ("Master Black Belt", "Assures the methodology - particularly the MSA at Gate M and the statistics at Gate A."),
         ("Black Belt", "Assembles the evidence, runs the meeting, frames the decision. Does not vote on it."),
         ("Quality or regulatory", "Signs where a change touches a validated or regulated process - common at Meridian.")],
        kicker="SIGN-OFF AUTHORITY", cols=2, accent=BLUE)

    d.tile_grid(
        "Running a Tollgate That Actually Decides Something",
        [("Circulate evidence early", "Pre-read 48 hours ahead. A gate is not the first time the sponsor sees the data."),
         ("Open with the decision", "State the decision being asked for in the first minute, not the last."),
         ("Show the gaps honestly", "Name what is incomplete. A sponsor who is surprised later stops trusting you."),
         ("Allow the kill option", "If kill is never available, the gate is theatre and everybody knows it."),
         ("Minute the decision", "Decision, owner, date and conditions recorded. Verbal approval evaporates."),
         ("Re-baseline the charter", "Scope, timing or benefit changes get written into the charter at the gate.")],
        kicker="GATE DISCIPLINE", cols=2, accent=TEAL)

    d.tile_grid(
        "Three Legitimate Gate Outcomes",
        [("Proceed", "Evidence is sufficient. Resource confirmed for the next phase and the next gate date set."),
         ("Adjust", "Scope, target, timing or resource is re-baselined into the charter, then the project continues."),
         ("Kill", "The problem is smaller than believed, the data does not exist, or priorities have moved on."),
         ("Killing is not failure", "A project killed at Gate M has cost weeks. The same project killed at Gate C has cost months."),
         ("The recycle option", "Sometimes the answer is 'go back to Measure' - an adjust decision, not a proceed."),
         ("Track kill rate", "A portfolio with a zero pct kill rate is not being screened honestly at the gates.")],
        kicker="THE DECISION", cols=2, accent=AMBER)

    # ================================================================
    # WRAP
    # ================================================================
    d.tile_grid(
        "Foundations - What You Should Now Be Able to Do",
        [("Explain Six Sigma three ways", "As a metric, as a method and as a management philosophy, to three different audiences."),
         ("Compute a sigma level", "Yield to DPMO to Z to sigma level, declaring the 1.5 shift assumption every time."),
         ("State your own role boundary", "The five things you now own that a Green Belt does not."),
         ("Score a project hopper", "Build and defend a weighted scoring matrix with a sponsor in the room."),
         ("Quantify COPQ at scale", "Roll benefit up from project to programme without double counting."),
         ("Run a tollgate", "Assemble the evidence, frame the decision and let the sponsor decide.")],
        kicker="MODULE CHECKPOINT", cols=2, accent=BLUE)

    d.big_statement(
        "Choose your capstone process before we break.",
        "One real process, one measurable Y, one named sponsor. Everything you learn for the rest of "
        "the week gets applied to it. Bring what data you can access.",
        "YOUR NEXT ACTION", color=TEAL)
