"""
Domain 1 — Foundations and the DEFINE phase. Labs 1-7.

THE CAPSTONE STARTS HERE, IN LAB 1.

Unlike the Green Belt course — where every lab runs on a shared fictional
scenario (Northwind) — the Black Belt course runs every lab on the LEARNER'S OWN
workplace process. Lab 1 selects and charters that project; every lab thereafter
adds one artifact to it. By Day 5 the learner is not starting a capstone, they
are consolidating one they have been building for four days.

A worked reference scenario (Meridian Medical Devices) is supplied throughout for
learners who cannot use workplace data — it is deliberately multi-site and
multi-variable so it can carry DOE, multiple regression and portfolio selection,
which the Green Belt's single-site Northwind scenario cannot.
"""

# ---------------------------------------------------------------- shared scenario
SCENARIO = (
    "Meridian Medical Devices manufactures infusion pump assemblies across three "
    "plants (Singapore, Penang, Suzhou) on six production lines, supplying hospital "
    "distributors in 14 countries. The business is missing its on-time-in-full (OTIF) "
    "target, first-pass yield varies significantly between plants, and warranty "
    "returns are rising. The VP of Operations has appointed you as Black Belt to lead "
    "a portfolio of improvement projects — and to mentor the Green Belts running "
    "workstreams beneath you. Use this scenario ONLY if you cannot use a real "
    "process from your own workplace; your own process is always preferred."
)

CAPSTONE_NOTE = (
    "CAPSTONE BUILDING BLOCK — the output of this lab goes directly into your "
    "capstone project pack, which you present to the steering committee on Day 5."
)

DOMAIN1 = [
    dict(
        num=1, topic=0,
        title="Select and Charter Your Capstone Project",
        objective="Select a viable Black Belt project from a candidate portfolio and charter it (A1, A2).",
        desc="This is the most important lab of the course — everything you build for the next "
             "five days attaches to the project you select here. Screen candidate projects the way "
             "a Black Belt does: against strategic fit, financial benefit, data availability and "
             "risk. Then write the charter that will govern the work. " + CAPSTONE_NOTE,
        build="A scored project selection matrix and a signed-off capstone project charter.",
        services="Portfolio screening, strategic alignment, COPQ estimate, project charter, sponsor agreement",
        steps=[
            ("Choose your capstone process. Strongly preferred: a real process from your own workplace where you can obtain data. Fallback: the Meridian Medical Devices scenario.", ""),
            ("List at least five candidate improvement projects within that process or business area. Write each as a PROBLEM, never as a solution.", ""),
            ("Build a project selection matrix. Score each candidate 1-5 on: strategic fit, annualised financial benefit, data availability, scope manageability, sponsor commitment and technical risk.", ""),
            ("Weight the criteria — strategic fit and financial benefit usually carry the highest weight — and compute a weighted total for each candidate.", ""),
            ("Reject any candidate that is a solution in disguise ('deploy a new MES'), has no accessible data, or has no named sponsor. Record WHY each was rejected.", ""),
            ("Select your capstone project — the highest weighted score that survives the rejection filters.", ""),
            ("Estimate the Cost of Poor Quality for the selected project: scrap, rework, warranty, expedite, lost margin and capacity consumed. Annualise it.", ""),
            ("Write the charter: business case, problem statement, goal statement (SMART), scope (in/out), preliminary Y, team, sponsor, milestones and expected benefit.", ""),
            ("Write your problem statement to the four-part test: the process, the time period, the measurable gap and the business impact — with no cause and no solution in it.", ""),
            ("Identify your sponsor and record what you need from them. Where possible, obtain real sign-off before Day 2.", ""),
        ],
        test="You have a weighted selection matrix with at least five scored candidates, a documented rejection rationale, an annualised COPQ figure, and a complete charter whose problem statement contains no cause and no solution.",
    ),
    dict(
        num=2, topic=0,
        title="Portfolio Selection, Strategy Alignment and the Black Belt Role",
        objective="Align a project portfolio to business strategy and define the Black Belt's leadership role (A1, K1).",
        desc="A Green Belt is handed a project; a Black Belt decides which projects exist. Practise "
             "the portfolio view — trace every candidate up to a business objective, balance the "
             "portfolio across DMAIC maturity and risk, and articulate what you as Black Belt own "
             "that a Green Belt does not.",
        build="A strategy-to-project traceability map and a Black Belt accountability charter.",
        services="Hoshin alignment, portfolio balance, belt role matrix, mentoring model, tollgate governance",
        steps=[
            ("Write down your organisation's top three business objectives for the current year (or Meridian's: OTIF to 95%, warranty cost down 30%, yield parity across plants).", ""),
            ("Map each of your five candidate projects from Lab 1 to the objective it serves. Any project that maps to nothing is a candidate for cancellation.", ""),
            ("Build the belt responsibility matrix: White, Yellow, Green, Black, Master Black Belt and Champion. For each, record who leads, who analyses, who mentors and who sponsors.", ""),
            ("List the five things a Black Belt does that a Green Belt does not — lead a portfolio, own advanced statistics, mentor Green Belts, run tollgates, validate benefits with Finance.", ""),
            ("Assess portfolio balance: are all your projects in one phase, one plant or one function? A healthy portfolio is spread across risk and time-to-benefit.", ""),
            ("Identify which of your candidate projects should be delegated to a Green Belt under your mentorship rather than led by you. Record the reasoning.", ""),
            ("Define the tollgate cadence for your capstone: what evidence closes Define, Measure, Analyze, Improve and Control, and who signs each one off.", ""),
            ("Write your Black Belt accountability charter — what you own, what you delegate, what you escalate.", ""),
        ],
        test="Every candidate project traces to a named business objective, your belt matrix distinguishes Black from Green Belt accountability, and your capstone has a defined five-tollgate governance plan.",
    ),
    dict(
        num=3, topic=0,
        title="DMAIC at Depth — Recap, Y = f(X) and Baseline Sigma for Your Project",
        objective="Re-derive the DMAIC roadmap and express your capstone as Y = f(X) with a baseline sigma level (K1, A4).",
        desc="A thorough recap of the DMAIC roadmap — not a skim, because you must be able to mentor "
             "Green Belts through it. Then apply it: express your capstone problem as Y = f(X), and "
             "convert your baseline defect data into DPMO and a sigma level so improvement can be "
             "proven numerically at the end. " + CAPSTONE_NOTE,
        build="A DMAIC tollgate map, a Y = f(X) model and a baseline DPMO / sigma level for your capstone.",
        services="DMAIC roadmap, tollgate deliverables, Y = f(X), DPU, DPO, DPMO, sigma level, sigma shift",
        steps=[
            ("Recap each DMAIC phase in full: its purpose, its core tools, its tollgate deliverable and the most common way teams fail in it.", ""),
            ("For each phase, write the one question that phase answers — Define: what problem? Measure: how big? Analyze: why? Improve: what fix? Control: how do we hold it?", ""),
            ("Write your capstone project Y — the single output metric your customer actually feels. It must be measurable and it must already have data.", ""),
            ("Brainstorm at least twelve candidate Xs that could drive that Y. Classify each as controllable, noise or SOP-governed.", ""),
            ("Write the relationship formally as Y = f(X1, X2, ... Xn), and mark which Xs you can experiment on later in the DOE labs.", ""),
            ("Collect or estimate your baseline: units processed, defects observed and opportunities per unit over a defined recent period.", ""),
            ("Calculate DPU, DPO and DPMO. Show the formulas: DPU = defects/units; DPO = defects/(units x opportunities); DPMO = DPO x 1,000,000.", ""),
            ("Convert DPMO to a baseline sigma level using the conversion table, and state whether the 1.5-sigma long-term shift is included.", ""),
            ("Record this baseline in your capstone pack — every improvement claim on Day 5 is measured against this number.", ""),
        ],
        test="You can explain all five DMAIC tollgates without notes, your Y is a measurable customer-facing output with at least twelve classified Xs, and your baseline DPMO and sigma level are calculated from real counts.",
    ),
    dict(
        num=4, topic=1,
        title="Voice of the Customer, Affinity and Kano — In Depth",
        objective="Capture and classify VOC for your capstone using affinity and Kano analysis (A1, K2).",
        desc="A full re-derivation of VOC, affinity clustering and Kano classification — taught to "
             "the depth at which you could run this session yourself for a Green Belt team. Then "
             "apply all three to your own capstone process. " + CAPSTONE_NOTE,
        build="A VOC log, an affinity diagram and a Kano classification for your capstone customers.",
        services="Reactive & proactive VOC, verbatim capture, affinity clustering, Kano model, customer segmentation",
        steps=[
            ("Recap the VOC sources in full: reactive (complaints, returns, warranty, escalations, social) and proactive (interviews, surveys, gemba, observation).", ""),
            ("Segment your capstone customers — internal and external. Different segments will give contradictory VOC, and that contradiction is itself data.", ""),
            ("Collect at least fifteen verbatim statements about your capstone process. Use the customer's own words; do not summarise them into your own.", ""),
            ("Recap affinity diagram method: silent clustering first to avoid anchoring on the loudest voice, then name the clusters by consensus.", ""),
            ("Build the affinity diagram for your verbatims. Aim for five to eight named themes.", ""),
            ("Recap the Kano model in full: Must-Be, One-Dimensional, Delighter, Indifferent and Reverse — and how categories migrate over time as delighters become expectations.", ""),
            ("Classify each affinity theme against Kano. Note explicitly that Must-Be requirements can only ever cause dissatisfaction, never satisfaction.", ""),
            ("Identify the one or two themes that most drive your project Y, and record them as your CTQ candidates for the next lab.", ""),
            ("Note how you would coach a Green Belt through this exercise — what mistake would you expect them to make?", ""),
        ],
        test="You have fifteen or more verbatims, every verbatim sits in a named affinity cluster, every cluster carries a Kano classification, and your CTQ candidates trace to specific verbatims.",
    ),
    dict(
        num=5, topic=1,
        title="CTQ Trees and CTQ Flowdown to Controllable Xs",
        objective="Translate VOC into measurable CTQs and cascade a business Y down to controllable Xs (A1, A4).",
        desc="A customer need is not measurable; a CTQ is. Re-derive the CTQ tree in full, then go "
             "beyond Green Belt with CTQ FLOWDOWN — cascading a business-level Y through sub-Ys "
             "until you reach process Xs a team can actually control. " + CAPSTONE_NOTE,
        build="A CTQ tree with targets and specification limits, plus a flowdown to controllable Xs.",
        services="CTQ tree, need-driver-requirement, operational definitions, specification limits, Y-to-X cascade",
        steps=[
            ("Recap the CTQ tree structure in full: Need -> Drivers -> Measurable Requirements, with each level more specific than the last.", ""),
            ("Take your top VOC theme and drive it down: what is the need, what drives it, and what specifically must be measured?", ""),
            ("For each CTQ, write a complete operational definition — what is measured, by whom, with what instrument, at what point, and what counts as a defect.", ""),
            ("Set the target, the upper and lower specification limits, and the defect definition for each CTQ. A CTQ without limits cannot generate a defect count.", ""),
            ("Verify each CTQ against the customer: would they agree this number represents what they asked for?", ""),
            ("Now flow down. Write your business-level Y (e.g. OTIF percentage) at the top of a cascade diagram.", ""),
            ("Break that Y into sub-Ys — the process-level outputs that roll up into it (pick accuracy, line yield, changeover time, carrier dwell).", ""),
            ("Break each sub-Y into the Xs that drive it. Continue until you reach Xs a team can directly control or experiment on.", ""),
            ("Mark on the cascade which Xs you will measure in Day 2, test statistically in Day 3, and experiment on in Day 4.", ""),
        ],
        test="Every CTQ has an operational definition, a target and specification limits, and your flowdown reaches at least one layer of Xs that are directly controllable and testable.",
    ),
    dict(
        num=6, topic=1,
        title="SIPOC, Process Mapping and Scope Governance",
        objective="Map your capstone process and govern its scope through the charter (A2).",
        desc="Re-derive SIPOC and detailed process mapping in full, then apply them to bound your "
             "capstone. Scope creep kills more Black Belt projects than bad statistics — this lab "
             "builds the map that makes scope arguments objective. " + CAPSTONE_NOTE,
        build="A SIPOC, a detailed swimlane process map and a documented scope boundary.",
        services="SIPOC, process boundaries, swimlane mapping, handoff analysis, rework loops, scope control",
        steps=[
            ("Recap SIPOC in full: Suppliers, Inputs, Process, Outputs, Customers — and why it is built right-to-left, starting from the customer.", ""),
            ("Open the online SIPOC tool and build the SIPOC for your capstone process at five to seven high-level steps. Agree the first and last step explicitly — that IS your scope.", "https://alfredang.github.io/sipoc/"),
            ("Recap process mapping symbols and conventions, and the difference between as-is and to-be maps.", ""),
            ("Build a detailed swimlane map of your capstone process, with one lane per role or function.", ""),
            ("Mark every handoff between lanes. Handoffs are where defects, delays and ownership gaps concentrate.", ""),
            ("Mark every decision point, inspection, rework loop and queue. Count the rework loops — each is a hidden factory.", ""),
            ("Walk the process physically or through the system (gemba) and correct the map. The map in your head is never the map in reality.", ""),
            ("Compare your map against the charter scope. Anything on the map outside the scope boundary must be explicitly marked out-of-scope.", ""),
            ("Record the three questions you will ask when someone proposes expanding the scope mid-project.", ""),
        ],
        test="Your SIPOC's first and last steps match your charter scope exactly, your swimlane map marks every handoff and rework loop, and the map has been validated by walking the actual process.",
    ),
    dict(
        num=7, topic=1,
        title="Stakeholder Analysis, Resistance Management and Change Leadership",
        objective="Analyse stakeholders and plan change leadership for your capstone (A1, K1).",
        desc="Black Belt projects fail on people far more often than on statistics. Map influence "
             "against support, diagnose resistance by type, and build an ADKAR-based change plan. "
             "This is Black-Belt-only material — the Green Belt course stops at RACI. " + CAPSTONE_NOTE,
        build="A stakeholder influence/support map, a resistance diagnosis and an ADKAR change plan.",
        services="Stakeholder mapping, RACI, influence-support grid, resistance types, ADKAR, Kotter, communication plan",
        steps=[
            ("List every stakeholder in your capstone: sponsor, process owner, operators, support functions, customers, finance, and anyone who can veto.", ""),
            ("Build the RACI for your project — Responsible, Accountable, Consulted, Informed — and check there is exactly one Accountable per deliverable.", ""),
            ("Plot each stakeholder on an influence (high/low) versus support (supportive/neutral/resistant) grid.", ""),
            ("For every high-influence, low-support stakeholder, write a specific named action. 'Communicate more' is not an action.", ""),
            ("Diagnose resistance type for each resistant stakeholder: technical (they doubt the solution), political (they lose something), or cultural (it conflicts with how things are done).", ""),
            ("Match the response to the type — technical resistance needs evidence, political needs negotiation, cultural needs leadership modelling.", ""),
            ("Build an ADKAR plan: how will you create Awareness, Desire, Knowledge, Ability and Reinforcement across the project life?", ""),
            ("Write the communication plan: audience, message, channel, frequency and owner. Sponsors, operators and customers need different messages.", ""),
            ("Identify the single stakeholder most likely to derail your capstone, and write your specific mitigation.", ""),
        ],
        test="Every stakeholder is plotted on the influence/support grid, every high-influence resistor has a named action matched to a diagnosed resistance type, and your ADKAR plan covers all five elements.",
    ),
]
