#!/usr/bin/env python3
"""Define teaching slides — Black Belt depth."""
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


def define_phase(d):
    K = "DEFINE - BLACK BELT DEPTH"

    # ================= SECTION 1: what Define means at BB level =================
    d.big_statement(
        "Define decides whether the project is worth doing at all",
        "A Green Belt writes a charter. A Black Belt negotiates the charter, cascades the business Y "
        "to controllable Xs, reads the political terrain and leads the change. Same tools, higher altitude.",
        "DEFINE AT BLACK BELT DEPTH", color=BLUE)

    d.tile_grid(
        "What this phase delivers at Black Belt level", [
            ("A charter that survives contact", "Business case, problem, goal, scope and team, negotiated with the sponsor and re-baselined at every tollgate."),
            ("A validated CTQ flowdown", "Business Y cascaded through sub-Ys to the process Xs a team can actually change."),
            ("A stakeholder and influence map", "Influence versus support, with a named move for every high-influence blocker."),
            ("A resistance diagnosis", "Technical, political or cultural - each demands a different response."),
            ("A change leadership plan", "ADKAR at the individual level, Kotter at the organisation level."),
            ("A mentoring plan for the Green Belts", "You will coach two to four GB charters through Define while running your own."),
        ], kicker=K, cols=2, accent=BLUE)

    d.compare_panels(
        "Green Belt Define versus Black Belt Define", [
            ("GREEN BELT", "Runs one project inside a process", [
                "Uses the charter template as given",
                "Collects VOC for one product or service",
                "Builds one CTQ tree",
                "Names the obvious stakeholders",
                "Escalates resistance to the sponsor",
            ]),
            ("BLACK BELT", "Runs a portfolio and coaches the belts", [
                "Negotiates scope and benefit with the sponsor",
                "Segments customers and reconciles conflicting VOC",
                "Flows the business Y down to controllable Xs",
                "Maps influence, support and coalition paths",
                "Diagnoses and works the resistance directly",
            ]),
            ("MASTER BLACK BELT", "Owns the deployment", [
                "Sets portfolio selection criteria",
                "Certifies charters before they start",
                "Audits benefit claims with Finance",
                "Coaches the Black Belts",
                "Owns the tollgate standard itself",
            ]),
        ], kicker=K, accent=VIOLET)

    d.flow_h(
        "The Define sequence you will run and teach",
        ["Capture and segment the Voice of the Customer",
         "Cluster with affinity, classify with Kano",
         "Build CTQ trees and flow the Y down to Xs",
         "Draft charter, problem, goal, scope, business case",
         "Map stakeholders, diagnose resistance, plan the change",
         "Tollgate: sponsor signs, or the project is killed"],
        kicker=K, color=BLUE)

    d.content(
        "Meridian Medical Devices - the running case for this course", [
            "Three plants: Singapore (HQ and pilot line), Penang (high volume), Suzhou (China domestic).",
            "Six assembly lines building infusion pump assemblies for hospital and homecare customers.",
            "Business pain: on-time in-full (OTIF) delivery is 87.4 percent against a customer commitment of 96 percent.",
            "First-pass yield sits at 91.2 percent group-wide, but Suzhou is 86.1 percent and Singapore is 95.0 percent.",
            "Warranty returns cost SGD 3.4 million last year, of which 61 percent trace to two failure modes.",
            "You will carry Meridian through every phase, and mirror it on your own capstone process.",
        ], kicker=K, size=18)

    # ================= SECTION 2: VOC in depth =================
    d.big_statement(
        "Voice of the Customer: you must be able to teach it, not just use it",
        "Green Belts routinely collect VOC from whoever is easiest to reach. Your job is to make them "
        "segment, sample and capture verbatim before a single CTQ is written.",
        "RECAP IN DEPTH - VOC", color=TEAL)

    d.compare_panels(
        "Two families of VOC sources", [
            ("REACTIVE", "Arrives whether you ask or not", [
                "Complaints and service desk tickets",
                "Warranty claims and field returns",
                "Credit notes, refunds, order cancellations",
                "Audit findings and regulatory observations",
                "Cheap and continuous, but biased to the angry",
            ]),
            ("PROACTIVE", "You must deliberately go and get it", [
                "Structured surveys with a real sampling plan",
                "One-to-one interviews with buyers and users",
                "Focus groups of six to ten customers",
                "Gemba: watch a nurse actually set up the pump",
                "Costlier, but reaches the silent majority",
            ]),
        ], kicker=K, accent=TEAL)

    d.tile_grid(
        "Customer segmentation - VOC is meaningless unsegmented", [
            ("Segment by customer type", "Hospital procurement, ward nursing staff, homecare patients and distributors want different things."),
            ("Segment by geography", "Singapore private hospitals, Malaysian public tenders and China distributors buy on different criteria."),
            ("Segment by volume and value", "The top 8 accounts are 62 percent of Meridian revenue. Weight their voice accordingly."),
            ("Segment by lifecycle stage", "A first-time buyer values setup simplicity; a five-year user values spare parts availability."),
            ("Watch for conflicting voices", "Procurement wants lowest unit price; nursing wants fastest changeover. Both are real."),
            ("Record the segment with the verbatim", "An unattributed quote cannot be reconciled later when voices conflict."),
        ], kicker=K, cols=2, accent=TEAL)

    d.compare_panels(
        "Verbatim capture - the discipline that Green Belts skip", [
            ("CAPTURE VERBATIM", "Their words, not yours", [
                "Write exactly what was said, in quotes",
                "Do not paraphrase into company language",
                "Record who said it, when, and in what role",
                "Keep the emotion - it signals severity",
                "One statement per card or row",
            ]),
            ("WHY IT MATTERS", "Paraphrase destroys evidence", [
                "'Delivery is bad' loses which part is bad",
                "The team's bias enters at paraphrase time",
                "You cannot re-cluster paraphrased data",
                "Sponsors challenge summaries, not quotes",
                "Regulators want the source record",
            ]),
        ], kicker=K, accent=TEAL)

    d.two_col(
        "Meridian - VOC verbatims from four segments",
        [("'Two of the twelve pumps arrived, the rest slipped three weeks.'", 0),
         ("'Nobody told me it was late - my ward planned around it.'", 0),
         ("'Your Suzhou units fail calibration more often than Penang.'", 0),
         ("Source: 148 service tickets and 22 procurement interviews", 1)],
        [("'Setting up the infusion set takes too many steps at 3am.'", 0),
         ("'The alarm tone is indistinguishable from the next bed.'", 0),
         ("'I need a spare battery door within 48 hours, not 3 weeks.'", 0),
         ("Source: 9 ward gemba visits and 31 homecare surveys", 1)],
        kicker=K, lhead="PROCUREMENT AND DISTRIBUTOR VOICE",
        rhead="CLINICAL AND PATIENT VOICE")

    # ================= SECTION 3: affinity diagram =================
    d.big_statement(
        "The affinity diagram turns 200 verbatims into 6 themes",
        "It is a silent, physical, team method. Run it wrong and you get the loudest person's "
        "categories. Run it right and the data speaks.",
        "RECAP IN DEPTH - AFFINITY", color=VIOLET)

    d.flow_h(
        "The affinity method, done properly",
        ["Write one verbatim per card - no editing, no merging",
         "Spread every card on the wall so all are visible",
         "Cluster in SILENCE - anyone may move any card",
         "Stop when movement settles; discuss only then",
         "Name each cluster with a full sentence, not a noun",
         "Check orphan cards - they are often the insight"],
        kicker=K, color=VIOLET)

    d.compare_panels(
        "Naming clusters - weak versus strong", [
            ("WEAK NAMES", "Nouns that hide the meaning", [
                "'Delivery'",
                "'Quality'",
                "'Communication'",
                "'Product issues'",
                "These could contain anything at all",
            ]),
            ("STRONG NAMES", "Full sentences that carry the finding", [
                "'Orders arrive late and we are not told'",
                "'Suzhou units fail calibration more often'",
                "'Setup has too many steps for night shift'",
                "'Spare parts take weeks to reach the ward'",
                "A stranger can act on these",
            ]),
        ], kicker=K, accent=VIOLET)

    d.tile_grid(
        "Meridian - the six affinity themes from 214 verbatims", [
            ("Orders arrive late and unannounced", "68 cards. Late delivery plus no proactive notification. Ties directly to OTIF."),
            ("Partial shipments break ward planning", "41 cards. In-full failure, distinct from the on-time failure."),
            ("Suzhou-built units fail calibration", "37 cards. Plant-specific quality signal, not a design issue."),
            ("Setup takes too many steps", "29 cards. Usability, mostly from night-shift nursing."),
            ("Alarm tones are not distinguishable", "22 cards. Safety-adjacent; escalate to the design authority."),
            ("Spare parts lead time is weeks", "17 cards. Aftermarket supply chain, likely a separate project."),
        ], kicker=K, cols=2, accent=VIOLET)

    # ================= SECTION 4: Kano in full =================
    d.big_statement(
        "Kano tells you which requirements actually buy satisfaction",
        "Not all CTQs are equal. Meeting a Must-Be earns you nothing; missing one loses the account. "
        "A Black Belt must classify before prioritising.",
        "RECAP IN DEPTH - KANO", color=AMBER)

    d.compare_panels(
        "The five Kano categories in full", [
            ("MUST-BE", "Expected, unspoken", [
                "Absence causes severe dissatisfaction",
                "Presence causes no satisfaction at all",
                "Pump must not over-deliver dose",
                "Sterile packaging must be intact",
                "You cannot win here - only lose",
            ]),
            ("ONE-DIMENSIONAL", "More is linearly better", [
                "Satisfaction rises with performance",
                "Customers will state these openly",
                "OTIF percentage, delivery lead time",
                "Battery run time in hours",
                "Where most CTQs and projects sit",
            ]),
            ("DELIGHTER", "Unexpected, unasked", [
                "Presence delights; absence is unnoticed",
                "Customers cannot ask for these",
                "Auto-detection of the infusion set type",
                "Proactive delay alert before the due date",
                "Source of competitive differentiation",
            ]),
        ], kicker=K, accent=AMBER)

    d.compare_panels(
        "The two categories teams forget", [
            ("INDIFFERENT", "Customer does not care either way", [
                "Neither presence nor absence moves satisfaction",
                "Often internally-invented features",
                "Meridian example: 14 configurable report layouts",
                "Nursing staff use exactly one of them",
                "Stop investing here - this is pure waste",
            ]),
            ("REVERSE", "More of it makes it worse", [
                "The feature actively harms satisfaction",
                "Meridian example: extra confirmation prompts",
                "Added for safety, hated at 3am on a ward",
                "Also: verbose alarm logs no one reads",
                "Removing these is a free improvement",
            ]),
        ], kicker=K, accent=RED)

    d.matrix2x2(
        "Kano positioned - satisfaction against fulfilment",
        "Degree of fulfilment  (low  ->  high)",
        "Satisfaction",
        [("DELIGHTER", "Absent and unnoticed. Present and it delights. Nonlinear upside. Meridian: proactive delay alert sent before the promised date."),
         ("ONE-DIMENSIONAL", "Straight line from fulfilment to satisfaction. Meridian: OTIF percentage, first-pass yield, order lead time."),
         ("INDIFFERENT / REVERSE", "Flat or negative. Investment here returns nothing or actively harms. Meridian: 14 report layouts, extra prompts."),
         ("MUST-BE", "Curve saturates fast. Full compliance earns zero credit; any gap is catastrophic. Meridian: dose accuracy, sterile seal.")],
        kicker=K, accent=AMBER)

    d.flow_h(
        "Category migration - Kano decays over time",
        ["A feature enters the market as a DELIGHTER",
         "Competitors copy it; it becomes ONE-DIMENSIONAL",
         "Everyone has it; it becomes a MUST-BE",
         "Regulators or standards codify it as mandatory",
         "Your differentiation is gone - find the next delighter"],
        kicker=K, color=AMBER)

    d.tile_grid(
        "How to run a Kano survey without corrupting it", [
            ("Ask the functional question", "'If the pump alerts you before a delivery is late, how do you feel?'"),
            ("Ask the dysfunctional question", "'If the pump does NOT alert you before a delivery is late, how do you feel?'"),
            ("Use the same five-point scale", "Like it / Expect it / Neutral / Live with it / Dislike it, on both questions."),
            ("Cross-tabulate to classify", "The pair of answers maps to Must-Be, One-Dimensional, Delighter, Indifferent or Reverse."),
            ("Segment the results", "Procurement and nursing will classify the same feature differently. Report both."),
            ("Re-run every 18 to 24 months", "Categories migrate. A two-year-old Kano study is misleading, not merely stale."),
        ], kicker=K, cols=2, accent=AMBER)

    # ================= SECTION 5: CTQ trees in depth =================
    d.big_statement(
        "The CTQ tree converts a feeling into a number with limits",
        "Need, then driver, then measurable requirement. Most weak Green Belt projects fail at the "
        "third level - they stop at a driver and call it a CTQ.",
        "RECAP IN DEPTH - CTQ TREES", color=BLUE)

    d.flow_h(
        "The three levels of the CTQ tree",
        ["NEED - the general requirement behind the verbatim",
         "DRIVER - the specific dimension that satisfies the need",
         "MEASURABLE REQUIREMENT - metric, target and limits"],
        kicker=K, color=BLUE)

    d.compare_panels(
        "Meridian - one need drilled to three CTQs", [
            ("NEED", "What the customer requires", [
                "'My order arrives complete',",
                "'on the date I was promised'",
                "Not measurable as written",
                "One need spawns several drivers",
            ]),
            ("DRIVERS", "The dimensions that satisfy it", [
                "Arrives on the promised date",
                "Arrives complete in quantity",
                "I am told early if it will slip",
                "Each driver becomes its own CTQ",
            ]),
            ("MEASURABLE REQUIREMENTS", "What we will actually measure", [
                "OTIF pct, target 96, LSL 96",
                "Line-fill rate pct, target 99",
                "Delay notice hours before due date,",
                "target at least 48 hours",
            ]),
        ], kicker=K, accent=BLUE)

    d.tile_grid(
        "Every CTQ needs all five of these", [
            ("A metric with a unit", "'OTIF percentage of order lines', not 'delivery performance'."),
            ("An operational definition", "Exactly how it is measured, by whom, from which system, and when the clock starts and stops."),
            ("A target", "The value we are aiming for. Meridian OTIF target is 96.0 percent."),
            ("Specification limits", "The customer's boundary of acceptability. LSL 96.0 percent; there is no upper limit here."),
            ("A defect definition", "The unambiguous statement of what counts as one defect. Here: one order line delivered late or short."),
            ("A data source", "Which system, which field, which report - so the Measure phase is not a rediscovery exercise."),
        ], kicker=K, cols=2, accent=BLUE)

    d.compare_panels(
        "Operational definitions - vague versus operational", [
            ("VAGUE", "Two people will measure differently", [
                "'Delivered on time'",
                "'Pump works correctly'",
                "'Fast changeover'",
                "'Good yield'",
                "Every one of these is arguable",
            ]),
            ("OPERATIONAL", "Two people get the same number", [
                "'Goods receipt timestamp in SAP is on or before the confirmed delivery date on the order line'",
                "'Calibration test passes on first attempt, per procedure QC-114 revision 6'",
                "'Minutes from last good unit of run A to first good unit of run B'",
                "'Units passing all inline tests without rework, divided by units started'",
            ]),
        ], kicker=K, accent=BLUE)

    d.formula_card(
        "Turning a CTQ into a defect rate",
        [("Defect rate", "defects / units", "Meridian: 512 late lines out of 4,060 shipped lines = 12.6 pct defective"),
         ("DPMO", "(defects / (units x opportunities)) x 1,000,000",
          "Meridian pump build: 38 defects, 1,200 units, 14 opportunities = 2,262 DPMO"),
         ("First-pass yield", "units passing first time / units started",
          "Suzhou line 4: 861 of 1,000 pass without rework = 86.1 pct FPY")],
        kicker=K, accent=VIOLET,
        note="If a CTQ cannot be reduced to a countable defect, it is not yet a CTQ.")

    # ================= SECTION 6: CTQ FLOWDOWN (BB only) =================
    d.big_statement(
        "CTQ flowdown is the Black Belt's defining Define skill",
        "A sponsor hands you a business Y such as 'OTIF must reach 96 percent'. Nobody can work on a Y. "
        "Your job is to cascade it until you reach Xs a team can actually turn.",
        "BLACK BELT ONLY - CTQ FLOWDOWN", color=VIOLET)

    d.flow_h(
        "The flowdown cascade, level by level",
        ["BUSINESS Y - the number the sponsor is judged on",
         "SUB-Y - the operational components that sum to Y",
         "PROCESS Y - the output of one process step",
         "CONTROLLABLE X - a setting, method or input a team owns",
         "Verify: Y = f(X). If you cannot state the function, keep going"],
        kicker=K, color=VIOLET)

    d.tile_grid(
        "Meridian - flowing OTIF down to controllable Xs", [
            ("BUSINESS Y: OTIF = 87.4 pct", "Target 96.0 pct. The sponsor's committed number to the top 8 hospital accounts."),
            ("SUB-Y 1: On-time = 91.2 pct", "Order lines with goods receipt on or before the confirmed date."),
            ("SUB-Y 2: In-full = 95.8 pct", "Order lines shipped at full ordered quantity, no partials."),
            ("PROCESS Y: Build cycle time", "Days from works-order release to finished-goods putaway, per line."),
            ("PROCESS Y: First-pass yield", "Units passing all inline tests without rework. Suzhou 86.1, Penang 92.4, Singapore 95.0."),
            ("CONTROLLABLE Xs", "Calibration interval, operator certification level, solder profile setpoint, kit-shortage rule."),
        ], kicker=K, cols=2, accent=VIOLET)

    d.ladder(
        "The flowdown as a ladder you climb DOWN",
        [("CONTROLLABLE X", "Solder reflow peak temperature setpoint on Suzhou line 4. A technician can change this today."),
         ("PROCESS Y", "First-pass yield on Suzhou line 4 - 86.1 pct against 95.0 pct at Singapore."),
         ("SUB-Y", "In-full delivery rate - 95.8 pct, degraded by rework holding stock back."),
         ("BUSINESS Y", "OTIF at 87.4 pct against a 96.0 pct customer commitment. The sponsor's number.")],
        kicker=K, accent=VIOLET,
        note="Read it top down to find the lever; read it bottom up to prove the benefit to Finance.")

    d.formula_card(
        "Proving each level of the cascade arithmetically",
        [("OTIF composition", "OTIF = on-time pct x in-full pct",
          "Meridian: 0.912 x 0.958 = 0.874 = 87.4 pct. The cascade reconciles."),
         ("Yield rollup", "RTY = FPY1 x FPY2 x ... x FPYn",
          "Four Suzhou steps at 0.97, 0.96, 0.95, 0.975 gives RTY = 0.862"),
         ("Benefit trace", "Y gain = sum of sub-Y gains x contribution",
          "Lifting Suzhou FPY 86.1 to 93.0 pct adds an estimated 2.9 pts of OTIF")],
        kicker=K, accent=VIOLET,
        note="If the arithmetic does not reconcile, the flowdown is wrong - not the data.")

    d.tile_grid(
        "Flowdown mistakes that kill projects", [
            ("Stopping at a sub-Y", "'Improve first-pass yield' is still a Y. Nobody can turn it. Keep cascading."),
            ("Jumping straight to a solution", "'Buy a new reflow oven' is an answer, not an X. You have skipped Analyze."),
            ("Picking uncontrollable Xs", "Customer order pattern and exchange rates are noise, not levers, for this team."),
            ("Losing the arithmetic link", "If a 10 pct gain in X cannot be traced to a number in Y, Finance will reject the benefit."),
            ("Cascading only one branch", "OTIF failed on both on-time AND in-full. Chase one and you cap your result."),
            ("Not testing the assumed function", "Y = f(X) is a hypothesis in Define. Analyze must confirm it statistically."),
        ], kicker=K, cols=2, accent=RED)

    # ================= SECTION 7: the charter =================
    d.big_statement(
        "The charter is the contract between you and the sponsor",
        "Six elements: business case, problem statement, goal statement, scope, team and milestones. "
        "Every one of them is negotiated, not merely filled in.",
        "RECAP IN DEPTH - THE CHARTER", color=BLUE)

    d.tile_grid(
        "The six elements of a Six Sigma project charter", [
            ("Business case", "Why this project, why now, and what it is worth. Must be Finance-validated, not team-estimated."),
            ("Problem statement", "What is wrong, where, since when, how big - with no cause and no solution in it."),
            ("Goal statement", "SMART. From baseline to target by a date, expressed in the same metric as the problem."),
            ("Scope in and out", "Process start and stop, sites, product families, shifts - and an explicit out-of-scope list."),
            ("Team and roles", "Sponsor, Black Belt, process owner, Green Belts, SMEs, Finance representative."),
            ("Milestones and tollgates", "A date for each of D-M-A-I-C, and who chairs each tollgate review."),
        ], kicker=K, cols=2, accent=BLUE)

    d.tile_grid(
        "The four-part test for a problem statement", [
            ("1. What is wrong?", "The specific undesirable outcome, in the customer's terms. 'Order lines arrive late or short.'"),
            ("2. Where and when?", "Which process, site, product and period. 'Across all three plants, Jan to Dec 2025.'"),
            ("3. How big is the gap?", "Baseline versus requirement, with the unit. 'OTIF 87.4 pct against a 96.0 pct commitment.'"),
            ("4. What does it cost?", "Business consequence in money or risk. 'SGD 1.9 million in penalties and expedite freight.'"),
        ], kicker=K, cols=2, accent=BLUE)

    d.compare_panels(
        "Problem statements - bad versus good", [
            ("BAD", "Fails the four-part test", [
                "'Delivery performance is poor because Suzhou is slow.'",
                "Contains a CAUSE - that is Analyze's job",
                "'We need a new planning system.'",
                "Contains a SOLUTION in disguise",
                "'Customers are unhappy.'",
                "No metric, no baseline, no gap, no cost",
            ]),
            ("GOOD", "Passes all four parts", [
                "'Between January and December 2025, OTIF delivery",
                "of infusion pump order lines from all three Meridian",
                "plants averaged 87.4 pct against a contracted 96.0 pct.",
                "The 8.6-point gap generated SGD 1.9 million in",
                "contractual penalties and expedite freight and placed",
                "two top-eight hospital accounts under review.'",
            ]),
        ], kicker=K, accent=RED)

    d.compare_panels(
        "Goal statements - bad versus good", [
            ("BAD", "Unmeasurable or unbounded", [
                "'Significantly improve delivery.'",
                "'Achieve world-class OTIF.'",
                "'Reduce lateness as much as possible.'",
                "'Fix the Suzhou plant by Q3.'",
                "None of these can be verified at Control",
            ]),
            ("GOOD", "Verifiable at the Control tollgate", [
                "'Raise OTIF for infusion pump order lines from",
                "87.4 pct to at least 96.0 pct across all three",
                "plants by 31 December 2026, sustained for three",
                "consecutive months, delivering SGD 1.4 million",
                "in validated annualised benefit.'",
            ]),
        ], kicker=K, accent=TEAL)

    d.two_col(
        "Meridian charter - scope in and out",
        [("IN SCOPE", 0),
         ("Infusion pump assemblies - all six lines", 1),
         ("All three plants: Singapore, Penang, Suzhou", 1),
         ("Process from works-order release to goods receipt at customer", 1),
         ("Top eight hospital accounts plus two distributors", 1),
         ("All shifts, including night shift at Penang", 1)],
        [("OUT OF SCOPE", 0),
         ("Spare parts and aftermarket supply - separate project", 1),
         ("Product design changes - owned by the design authority", 1),
         ("Syringe pump product family", 1),
         ("Supplier selection and contract renegotiation", 1),
         ("Anything upstream of the customer purchase order", 1)],
        kicker=K, lhead="WHAT THIS PROJECT OWNS", rhead="WHAT IT EXPLICITLY DOES NOT",
        lcolor=TEAL, rcolor=RED)

    d.tile_grid(
        "Building the business case with Finance, not around them", [
            ("Hard benefit", "Cash that leaves or stops leaving the P&L. Penalties avoided, freight avoided, scrap avoided."),
            ("Soft benefit", "Capacity, time or risk released. Real, but do not claim it as savings without Finance agreeing."),
            ("Cost avoidance", "Spend that would have happened but now will not. Must be a committed, documented plan."),
            ("Get the CFO's rate card", "Use Finance's own labour, freight and scrap rates or your number will be disputed."),
            ("Name a Finance signatory", "One named person validates baseline and final benefit. Without this, benefits evaporate."),
            ("Meridian case", "SGD 1.9 million exposure; validated addressable benefit SGD 1.4 million annualised."),
        ], kicker=K, cols=2, accent=AMBER)

    # ================= SECTION 8: charter governance (BB) =================
    d.big_statement(
        "The charter is a living contract, not a form you file",
        "It is re-baselined at every tollgate. A charter that has not changed by the Analyze gate "
        "usually means nobody has looked at it.",
        "BLACK BELT ONLY - CHARTER GOVERNANCE", color=RED)

    d.flow_h(
        "What happens to the charter at each tollgate",
        ["DEFINE gate - sponsor approves scope, baseline and benefit",
         "MEASURE gate - baseline REVISED to the validated measurement",
         "ANALYZE gate - scope narrowed to the proven vital few Xs",
         "IMPROVE gate - benefit re-forecast from piloted results",
         "CONTROL gate - benefit signed by Finance; charter closed"],
        kicker=K, color=RED, colors=DMAIC_COLORS)

    d.tile_grid(
        "Legitimate re-baselining versus scope creep", [
            ("LEGITIMATE: measurement corrected", "MSA shows the OTIF report double-counted partials. Baseline moves 87.4 to 89.1. Re-baseline."),
            ("LEGITIMATE: scope narrowed by data", "Analyze proves 78 pct of the gap sits at Suzhou. Narrow the project. Re-baseline."),
            ("LEGITIMATE: external change", "A top-eight account is lost. The benefit basis changed. Re-baseline or kill."),
            ("CREEP: new problem added", "'While you are there, also fix the syringe pump line.' That is a second charter."),
            ("CREEP: target quietly lowered", "Target slides 96 to 93 with no data reason. This is failure being renamed success."),
            ("CREEP: date extended without cause", "Every extension must be traded against a named constraint at the tollgate."),
        ], kicker=K, cols=2, accent=RED)

    d.tile_grid(
        "How a Black Belt runs a tollgate review", [
            ("Circulate the pack 48 hours ahead", "Nobody should first see your data in the room. Objections land before, not during."),
            ("Open with the charter as it stands", "One slide: baseline, target, scope, benefit, and what has changed since last gate."),
            ("Show the evidence, not the effort", "Sponsors do not fund activity. Show what the data now proves that it did not before."),
            ("State the decision you are asking for", "Go, adjust or kill. Never let a tollgate end without an explicit sponsor decision."),
            ("Record and publish the decision", "Written, circulated same day. Verbal approvals evaporate under pressure."),
            ("Be willing to recommend a kill", "A Black Belt who has never killed a project is not testing hard enough."),
        ], kicker=K, cols=2, accent=BLUE)

    # ================= SECTION 9: SIPOC =================
    d.big_statement(
        "SIPOC fixes the boundary before anyone argues about the middle",
        "Build it right to left, starting from the customer. Teams that start at Suppliers "
        "map the process they wish they had.",
        "RECAP IN DEPTH - SIPOC", color=TEAL)

    d.flow_h(
        "Build SIPOC right to left",
        ["C - Who receives the output? Name them.",
         "O - What exactly do they receive? Tie to CTQs.",
         "P - The 4 to 7 high-level steps that produce it.",
         "I - What the process consumes to run those steps.",
         "S - Who provides each input, internal or external."],
        kicker=K, color=TEAL)

    d.sipoc_diagram(
        "Meridian - SIPOC for the pump fulfilment process",
        [["Component suppliers", "Contract PCB assembler", "Sterile packaging vendor", "Planning (works orders)", "Freight forwarders"],
         ["Purchase orders", "PCB sub-assemblies", "Pump housings and sets", "Works order schedule", "Calibration standards"],
         ["Release works order", "Build and assemble", "Calibrate and test", "Pack and label", "Ship and confirm"],
         ["Calibrated pump units", "Certificate of conformity", "Packing list and ASN", "Delivery confirmation", "Goods receipt record"],
         ["Hospital biomed teams", "Ward nursing staff", "Homecare patients", "Distributors (MY, CN)", "Meridian service desk"]],
        kicker=K)

    d.tile_grid(
        "SIPOC discipline points a Black Belt must enforce", [
            ("Fix the START and STOP explicitly", "Meridian: starts at works-order release, stops at customer goods receipt. Written on the charter."),
            ("Keep the process to 4 to 7 steps", "More than seven and you have drifted into a process map, which belongs in Measure."),
            ("Verb-noun for every step", "'Calibrate and test', not 'Calibration'. Nouns hide who does what."),
            ("Outputs must tie to the CTQs", "If an output has no CTQ, ask whether the customer values it at all."),
            ("Name the customers as people", "'Ward nursing staff', not 'the hospital'. You cannot interview an institution."),
            ("Do it in the room in 45 minutes", "SIPOC is an alignment device. Perfecting it offline defeats its purpose."),
        ], kicker=K, cols=2, accent=TEAL)

    # ================= SECTION 10: stakeholders =================
    d.big_statement(
        "Every project you lead will be decided by people, not by data",
        "You will map influence against support, and you will have a specific, named move "
        "for every person in the top-left quadrant.",
        "BLACK BELT ONLY - STAKEHOLDERS", color=VIOLET)

    d.matrix2x2(
        "Stakeholder grid - influence against support",
        "Support for the project  (low  ->  high)",
        "Influence",
        [("BLOCKERS - work these first", "High influence, low support. Meridian: the Suzhou plant director, who reads this as an audit of his line. Meet privately, before any group session."),
         ("CHAMPIONS - use their air cover", "High influence, high support. Meridian: the VP Operations sponsor. Ask them to open the kickoff and to name the Finance signatory."),
         ("MONITOR - keep informed, cheaply", "Low influence, low support. Meridian: two distributor account managers. Newsletter cadence is enough."),
         ("SUPPORTERS - recruit as advocates", "Low influence, high support. Meridian: ward nursing leads and the Penang quality engineer. Give them the story to spread.")],
        kicker=K, accent=VIOLET)

    d.flow_h(
        "The stakeholder analysis method",
        ["List everyone the change touches or who can stop it",
         "Rate influence: can they stop or accelerate this?",
         "Rate current support: from -2 opposed to +2 advocating",
         "Rate REQUIRED support - it is rarely +2 for everyone",
         "Write a named action and owner for every gap",
         "Re-score at every tollgate - positions move"],
        kicker=K, color=VIOLET)

    d.tile_grid(
        "Meridian - the stakeholder moves that mattered", [
            ("Suzhou plant director", "High influence, opposed. Move: private pre-brief, framed as capacity release, not defect hunting."),
            ("VP Operations (sponsor)", "High influence, advocating. Move: ask them to open the kickoff and mandate data access."),
            ("Group Finance controller", "High influence, neutral. Move: co-author the benefit method before any number is published."),
            ("Penang production manager", "Medium influence, supportive. Move: make him the benchmark story the others learn from."),
            ("Ward nursing leads", "Low influence, strongly supportive. Move: use their verbatims in every steering pack."),
            ("IT / MES data owner", "Low influence, neutral, but blocking. Move: get data access written into the charter itself."),
        ], kicker=K, cols=2, accent=VIOLET)

    d.compare_panels(
        "RACI - who does what on the project", [
            ("R - RESPONSIBLE", "Does the work", [
                "Black Belt: analysis and facilitation",
                "Green Belts: data collection at each plant",
                "Process owner: implements the changes",
                "There can be several R's per task",
            ]),
            ("A - ACCOUNTABLE", "Owns the outcome", [
                "Exactly ONE per task, always",
                "Sponsor is A for benefit realisation",
                "Process owner is A for sustained control",
                "If two people are A, nobody is",
            ]),
            ("C AND I", "Consulted and Informed", [
                "C: consulted BEFORE the decision",
                "Finance, Quality, Regulatory are usually C",
                "I: told AFTER the decision is made",
                "Confusing C with I creates most escalations",
            ]),
        ], kicker=K, accent=BLUE)

    # ================= SECTION 11: resistance =================
    d.big_statement(
        "Resistance is data. Diagnose it before you respond to it",
        "The single most common Black Belt failure is answering a political objection "
        "with a technical argument. It never works, and it hardens the position.",
        "BLACK BELT ONLY - RESISTANCE", color=RED)

    d.compare_panels(
        "Three kinds of resistance, three different responses", [
            ("TECHNICAL", "'I do not believe your data'", [
                "Sounds like: sample too small, wrong period",
                "Root: genuine doubt about method or evidence",
                "RESPONSE: show the MSA, widen the sample,",
                "invite them to audit the data themselves",
                "This is the EASY one - and the rarest",
            ]),
            ("POLITICAL", "'This costs me something'", [
                "Sounds like: 'wrong time', 'no resources'",
                "Root: budget, headcount, status or blame at risk",
                "RESPONSE: negotiate. Find what they gain.",
                "Trade scope, credit or timing. Use the sponsor.",
                "Never argue data at a political objection",
            ]),
            ("CULTURAL", "'That is not how we work here'", [
                "Sounds like: 'we tried that in 2019'",
                "Root: identity, history, professional pride",
                "RESPONSE: slow down. Pilot small, show a local",
                "win, let a respected insider carry the story",
                "The slowest to shift, and the most durable",
            ]),
        ], kicker=K, accent=RED)

    d.tile_grid(
        "Diagnosing which one you are actually facing", [
            ("Listen to what they ask for", "A request for more data is technical. A request for delay is usually political."),
            ("Test with a hypothetical", "'If the data were perfect, would you support it?' A no means it was never technical."),
            ("Ask who else feels this way", "A widely shared objection is cultural. A lone strong one is usually political."),
            ("Check what they lose", "Follow headcount, budget, autonomy and reputation. Political resistance always has a price tag."),
            ("Notice the history", "'We tried that in 2019' is a cultural scar. Find out what actually happened then."),
            ("Escalate last, not first", "Escalation converts a technical or cultural objection into a permanent political one."),
        ], kicker=K, cols=2, accent=RED)

    d.matrix2x2(
        "Resistance response grid - how hard to push",
        "Their influence  (low  ->  high)",
        "Strength of resistance",
        [("NEGOTIATE OR PAUSE", "High influence, strong resistance. Do not force this. Meet privately, find the trade, or delay the branch of scope that threatens them."),
         ("CO-OPT AND CONVERT", "High influence, mild resistance. Involve them in designing the pilot. Ownership converts more reliably than argument."),
         ("PROCEED AND MONITOR", "Low influence, strong resistance. Do not spend your capital here. Proceed, document, and revisit after the first visible win."),
         ("INFORM AND MOVE ON", "Low influence, mild resistance. Standard communication cadence. Most of it dissolves once results appear.")],
        kicker=K, accent=RED)

    # ================= SECTION 12: change leadership =================
    d.big_statement(
        "Six Sigma delivers a solution. Change leadership delivers the result",
        "Two frameworks: ADKAR for the individual, Kotter for the organisation. "
        "You need both, and they operate at different levels.",
        "BLACK BELT ONLY - CHANGE LEADERSHIP", color=TEAL)

    d.ladder(
        "ADKAR - the individual change sequence",
        [("A - AWARENESS", "They know WHY the change is needed. Meridian: show the OTIF gap and the two accounts under review."),
         ("D - DESIRE", "They personally choose to participate. Answer 'what is in it for me?' honestly."),
         ("K - KNOWLEDGE", "They know HOW. Training on the new calibration standard and the escalation rule."),
         ("A - ABILITY", "They can actually do it in the real environment, under time pressure, on night shift."),
         ("R - REINFORCEMENT", "It sticks. Audits, metrics on the board, recognition, and consequence for drift.")],
        kicker=K, accent=TEAL,
        note="ADKAR is sequential. Diagnose which letter a person is stuck on - and fix THAT one only.")

    d.tile_grid(
        "Using ADKAR as a diagnostic, not a checklist", [
            ("Stuck at Awareness", "They say 'what problem?' Fix: share the customer verbatims and the OTIF trend, not the solution."),
            ("Stuck at Desire", "They understand and still will not move. Fix: this is political. Negotiate, do not re-explain."),
            ("Stuck at Knowledge", "Willing but unsure how. Fix: training, work instructions, a job aid at the station."),
            ("Stuck at Ability", "Trained but cannot perform in practice. Fix: coaching at the line, tooling, time, or workload relief."),
            ("Stuck at Reinforcement", "Did it for six weeks, then drifted. Fix: the Control plan and the response plan, not more training."),
            ("Wrong fix, wasted effort", "Training a person stuck on Desire is the classic and expensive Black Belt error."),
        ], kicker=K, cols=2, accent=TEAL)

    d.tile_grid(
        "Kotter's 8 steps - the organisational level", [
            ("1. Create urgency", "Make the status quo feel more dangerous than the change. Two accounts under review does this."),
            ("2. Build a guiding coalition", "Sponsor plus the three plant directors plus Finance. Authority AND credibility."),
            ("3. Form a strategic vision", "'96 percent OTIF, every account, every month' - repeatable in one sentence."),
            ("4. Enlist a volunteer army", "Green Belts and line champions at each plant carry it further than you can."),
            ("5. Enable action, remove barriers", "Get the MES data access and the pilot line time authorised, in writing."),
            ("6. Generate short-term wins", "Penang line 2 pilot: FPY 92.4 to 96.1 in six weeks. Publish it everywhere."),
        ], kicker=K, cols=2, accent=BLUE)

    d.compare_panels(
        "Kotter steps 7 and 8 - where projects actually fail", [
            ("7. SUSTAIN ACCELERATION", "Do not declare victory early", [
                "The pilot win is evidence, not completion",
                "Roll to Suzhou and Singapore lines next",
                "Keep the coalition meeting after the pilot",
                "Most programmes stop here and quietly decay",
            ]),
            ("8. INSTITUTE CHANGE", "Make it the new normal", [
                "Rewrite the SOP and the training pack",
                "Put OTIF on the plant daily management board",
                "Build it into new-hire onboarding",
                "Change the metric people are measured on",
            ]),
        ], kicker=K, accent=AMBER)

    # ================= SECTION 13: communication planning =================
    d.big_statement(
        "Different audiences need different messages at different cadences",
        "A communication plan is a table with five columns, and it is written in Define - "
        "not improvised in Improve when the resistance arrives.",
        "BLACK BELT ONLY - COMMUNICATION", color=AMBER)

    d.flow_h(
        "The five columns of a communication plan",
        ["AUDIENCE - who exactly, by name or role",
         "MESSAGE - what they need to know and to do",
         "CHANNEL - the medium that reaches them",
         "FREQUENCY - the cadence, fixed in advance",
         "OWNER - one named person, not 'the team'"],
        kicker=K, color=AMBER)

    d.tile_grid(
        "Meridian - the communication plan in practice", [
            ("Steering committee", "Benefit, risk, decisions needed. One-page pack plus 30-min review. Monthly. Owner: Black Belt."),
            ("Plant directors", "Site-level data, resource asks, what changes for them. Site visit. Fortnightly. Owner: sponsor."),
            ("Line supervisors", "What changes at the station and when. Shift huddle. Weekly. Owner: process owner."),
            ("Operators (3 shifts)", "The new standard, and why it matters to the patient. Board plus toolbox talk. Weekly."),
            ("Finance", "Baseline method, benefit calculation, validation status. Working session. At each tollgate."),
            ("Customers (top 8)", "Recovery plan and improvement trend, no internal detail. Account review. Quarterly."),
        ], kicker=K, cols=2, accent=AMBER)

    # ================= SECTION 14: mentoring Green Belts =================
    d.big_statement(
        "You will coach two to four Green Belt charters while running your own",
        "The temptation is to rewrite their charter for them. Do that once and you own "
        "their project forever. Coach with questions instead.",
        "BLACK BELT ONLY - MENTORING", color=BLUE)

    d.tile_grid(
        "The Green Belt Define mistakes to watch for", [
            ("Solution in disguise", "'Implement a new scheduling system' is an answer, not a problem. Send them back to the data."),
            ("Scope creep at birth", "A charter covering three processes and two sites will finish none of them. Cut it on day one."),
            ("Unmeasurable CTQs", "'Improve communication' has no metric, no target, no defect definition. It is not a CTQ."),
            ("Cause in the problem statement", "'Late because Suzhou is slow' pre-decides Analyze and biases every subsequent step."),
            ("Baseline taken on faith", "The system report has never been validated. Measure will move the baseline - warn them now."),
            ("No sponsor, or the wrong one", "If the sponsor cannot authorise the change to the process, they are not the sponsor."),
        ], kicker=K, cols=2, accent=RED)

    d.compare_panels(
        "Coaching by question, not by correction", [
            ("INSTEAD OF TELLING", "You own it the moment you write it", [
                "'Your problem statement is wrong.'",
                "'Change the target to 96 percent.'",
                "'Take Suzhou out of scope.'",
                "'Here, I have rewritten it for you.'",
            ]),
            ("ASK", "They own it, and they learn", [
                "'How would you prove that gap to Finance?'",
                "'What does one defect look like, exactly?'",
                "'Which part of this could you finish in 90 days?'",
                "'Who has to agree, and have you asked them?'",
            ]),
        ], kicker=K, accent=TEAL)

    d.tile_grid(
        "The Define tollgate checklist you will apply", [
            ("VOC evidence exists", "Real verbatims, segmented, from more than one channel. Not the team's opinion."),
            ("CTQs are measurable", "Metric, operational definition, target, spec limits, defect definition, data source."),
            ("Flowdown reconciles", "The business Y decomposes arithmetically to the Xs the team proposes to work on."),
            ("Charter passes all four tests", "Problem is testable, goal is SMART, scope is bounded, business case is Finance-validated."),
            ("Stakeholders are mapped", "Every high-influence, low-support person has a named owner and a dated action."),
            ("Sponsor has decided", "An explicit, recorded go, adjust or kill. Not 'looks good, carry on'."),
        ], kicker=K, cols=2, accent=BLUE)

    d.big_statement(
        "If Define is wrong, everything downstream is precisely wrong",
        "You can run flawless statistics on the wrong Y and deliver nothing. Spend the time here, "
        "negotiate hard, and be willing to recommend that the project should not run at all.",
        "DEFINE - CLOSE", color=BLUE)
