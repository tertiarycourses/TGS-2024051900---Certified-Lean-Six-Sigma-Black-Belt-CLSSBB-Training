"""
Domain 6 — DAY 5: CAPSTONE CONSOLIDATION AND PRESENTATION. Labs 31-34.

This is where the capstone the learner has been building since Lab 1 is
consolidated, rehearsed, presented and defended. There is NO practice exam and no
written/practical assessment paper in this course — the capstone project and its
steering committee presentation ARE the assessment.

By this point the learner already holds, from Labs 1-30:
    charter, portfolio map, Y=f(X), baseline sigma, VOC/Kano, CTQ flowdown,
    SIPOC & swimlane map, stakeholder & change plan, VSM, data collection plan,
    sampling plan, Gage R&R, attribute MSA/Kappa, nested gauge study, capability,
    run/Pareto/stratification, fishbone & 5 Whys, hypothesis tests, multiple
    regression, ANOVA & interactions, multi-vari, chi-square, Analyze tollgate,
    solution matrix, full factorial DOE, fractional factorial, RSM & robust
    design, FMEA & pilot plan, SPC charts, CUSUM/EWMA/short-run, T-squared &
    control plan, and the Finance-validated benefit.

Day 5 assembles those artifacts into one narrative and defends it.
"""

from data_domain1 import CAPSTONE_NOTE

DOMAIN6 = [
    dict(
        num=31, topic=6,
        title="Consolidating Your Capstone — The A3 Storyboard",
        objective="Consolidate all DMAIC artifacts from Labs 1-30 into a single A3 storyboard (A1-A5, K1).",
        desc="You have been building this project since Lab 1. Now assemble thirty labs' worth of "
             "artifacts into ONE page that tells the whole story. The A3 discipline is deliberately "
             "constraining — if it does not fit on one page, you do not yet understand which parts "
             "matter.",
        build="A complete A3 storyboard covering your full DMAIC project on a single page.",
        services="A3 thinking, storyboard structure, artifact selection, visual summary, narrative flow",
        steps=[
            ("Retrieve every artifact you have produced since Lab 1 and lay them out in DMAIC order. You should have thirty or more pieces.", ""),
            ("Learn the A3 structure: Background, Current State, Goal, Root Cause Analysis, Countermeasures, Results, and Follow-up Actions.", ""),
            ("Write the Background in three sentences: the business context and why this project was selected from the portfolio.", ""),
            ("Present the Current State using your baseline — sigma level, capability, run chart and the quantified COPQ from Lab 1.", ""),
            ("State the Goal exactly as chartered, with the SMART target and the deadline.", ""),
            ("Summarise Root Cause Analysis with your strongest evidence only — the Pareto or stratification, the key hypothesis test result and the regression or ANOVA finding.", ""),
            ("Present Countermeasures: the selected solutions, the DOE optimum settings and the FMEA-driven risk mitigations.", ""),
            ("Present Results: before/after comparison, the statistical significance test, the control chart showing sustained performance, and the Finance-validated benefit.", ""),
            ("List Follow-up Actions: the control plan owner, audit schedule, open risks and the next project in the portfolio.", ""),
            ("Now edit ruthlessly to one page. Every element must earn its place — cut anything that does not change the reader's understanding or decision.", ""),
            ("Apply the visual test: a sponsor should grasp the whole story in 60 seconds from the charts alone, without reading the text.", ""),
            ("Have a peer read your A3 cold and tell you what the project did. If they get it wrong, the A3 is not yet finished.", ""),
        ],
        test="Your A3 fits on one page, covers all seven sections, carries your real project data throughout, and a peer reading it cold can correctly summarise the project.",
    ),
    dict(
        num=32, topic=6,
        title="Building the Steering Committee Presentation",
        objective="Build a presentation that leads with business impact and defends the analysis (A1-A5).",
        desc="Sponsors are not statisticians. They want the decision, the money and the risk in the "
             "first two minutes, with the statistics available underneath as supporting evidence. "
             "This lab builds the deck you will deliver and defend in Lab 33.",
        build="A 15-minute steering committee presentation with an appendix of supporting analysis.",
        services="Executive communication, data storytelling, chart selection, structuring for decisions, appendix strategy",
        steps=[
            ("Understand your audience: the sponsor wants the business outcome; the process owner wants the operational change; Finance wants the benefit validated.", ""),
            ("Open with the headline: what the project achieved, what it is worth annually, and what decision you need from the committee.", ""),
            ("Apply the two-minute rule — if the committee stopped you after two minutes, they should already have everything needed to make a decision.", ""),
            ("Structure the main body against DMAIC, but at business altitude: the problem, what the data showed, what you changed, what resulted.", ""),
            ("Select your charts carefully. One before/after comparison, one root cause chart, one control chart showing sustained gain. Resist showing everything you built.", ""),
            ("Design each chart for a projector at the back of a room: large fonts, direct labels, no unexplained jargon and no default spreadsheet styling.", ""),
            ("State the statistics in business language. 'The difference is statistically significant (p = 0.003)' beats a table of test output.", ""),
            ("Present the benefit precisely: hard, soft and cost avoidance separated, with the Finance sign-off named explicitly.", ""),
            ("Present the risks honestly, along with their mitigations. A presentation with no risks reads as naive and invites harder challenge.", ""),
            ("Close with the specific ask: approve the rollout, release resources, or approve the next project in the portfolio.", ""),
            ("Build the APPENDIX with your full analysis — regression output, ANOVA tables, DOE design and alias structure, MSA study and control plan. This is where challenges get answered.", ""),
            ("Rehearse to time. Fifteen minutes means fifteen minutes; overrunning signals you cannot prioritise.", ""),
        ],
        test="Your presentation delivers the decision, benefit and ask within the first two minutes, charts are projector-legible, statistics are stated in business language, and every likely challenge has an appendix slide behind it.",
    ),
    dict(
        num=33, topic=6,
        title="Capstone Presentation and Defence",
        objective="Present and defend your capstone project to a simulated steering committee (A1-A5, K1, K2).",
        desc="The capstone assessment. Present your project to a simulated steering committee of "
             "peers and the trainer, then defend the analysis under challenge. Defending your "
             "methodology under pressure is the skill that separates a Black Belt from a Green "
             "Belt.",
        build="A delivered 15-minute presentation with a defended Q&A session.",
        services="Presentation delivery, handling challenge, methodological defence, peer assessment, professional judgement",
        steps=[
            ("Deliver your 15-minute presentation to the steering committee panel.", ""),
            ("Hold the two-minute rule under pressure — lead with outcome, benefit and ask.", ""),
            ("Take questions. Expect challenge on sample adequacy: was your sample size justified, and what power did your tests have?", ""),
            ("Expect challenge on the measurement system: how do you know the data is trustworthy? Have your Gage R&R or Kappa result ready.", ""),
            ("Expect challenge on assumptions: did you test normality, equal variance and independence, and what did you do when they failed?", ""),
            ("Expect challenge on confounding: what else changed during the period, and how do you know your intervention caused the improvement?", ""),
            ("Expect challenge on DOE: what was your design resolution, what effects were aliased, and did confirmation runs validate the optimum?", ""),
            ("Expect challenge on sustainability: what stops this from decaying in six months once attention moves elsewhere?", ""),
            ("Expect challenge on the benefit: is it hard or soft, who in Finance validated it, and over what period?", ""),
            ("Answer with evidence, not assertion. Go to your appendix. Where you do not know, say so and state how you would find out — this is far stronger than bluffing.", ""),
            ("Where a challenge reveals a genuine weakness, acknowledge it and state the mitigation. Defensiveness costs more credibility than the weakness itself.", ""),
            ("Observe the other presentations and record challenges you had not anticipated for your own project.", ""),
        ],
        test="You delivered within time, answered challenges with evidence from your appendix rather than assertion, and acknowledged genuine weaknesses with a stated mitigation.",
    ),
    dict(
        num=34, topic=6,
        title="Lessons Learned, Mentoring Green Belts and Your Black Belt Journey",
        objective="Harvest lessons, plan your mentoring practice and map your continuing development (K1).",
        desc="Close the course as you would close a project. Harvest what transfers, then turn to the "
             "accountability that most defines the role: mentoring Green Belts. A Black Belt is "
             "measured not only by their own projects but by the belts they develop.",
        build="A lessons-learned record, a Green Belt mentoring plan and a personal development roadmap.",
        services="Lessons learned, knowledge transfer, mentoring model, coaching questions, certification pathway, continuing practice",
        steps=[
            ("Run your own lessons learned: what worked in your capstone, what did not, and what you would do differently next time.", ""),
            ("Separate lessons that are project-specific from those that transfer to any project. Only the transferable ones belong in the organisational knowledge base.", ""),
            ("Record the two analytical techniques from this course you found most difficult, and plan how you will build fluency in them.", ""),
            ("Now the mentoring role. Understand the core principle: a Black Belt coaches Green Belts through their analysis rather than performing it for them.", ""),
            ("Learn the coaching question set: what does your data show, what have you ruled out, what assumption is that resting on, and how would you know if you were wrong?", ""),
            ("Identify where Green Belts most commonly need intervention — scope creep, wrong test selection, confusing correlation with causation, and skipping MSA entirely.", ""),
            ("Plan your tollgate review approach: what evidence you require at each gate before allowing a Green Belt project to proceed.", ""),
            ("Decide when to intervene directly versus letting a Green Belt learn from a recoverable mistake. Both have costs.", ""),
            ("Draft a mentoring plan for one Green Belt in your organisation: their project, their development gaps, your review cadence.", ""),
            ("Map your certification pathway: project logging requirements, the certification body's criteria and any remaining evidence you need.", ""),
            ("Identify your next portfolio project from the Lab 2 map, and set a start date.", ""),
            ("Write your 90-day plan: complete or hand over the capstone, begin mentoring, and select the next project.", ""),
        ],
        test="Your lessons are separated into project-specific and transferable, you have a named Green Belt mentoring plan with a review cadence, and your 90-day plan has dated commitments.",
    ),
]
