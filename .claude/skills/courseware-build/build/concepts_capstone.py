#!/usr/bin/env python3
"""Capstone teaching slides - Black Belt depth, Day 5."""
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


def capstone_phase(d):
    K = "CAPSTONE - DAY 5"

    # ============================================================
    # SECTION A - THE CAPSTONE IS THE ASSESSMENT
    # ============================================================
    d.big_statement("Two things happen on Day 5",
                    "You sit the WSQ assessment, AND you present the capstone you have been "
                    "building since Lab 1.",
                    K, color=VIOLET)

    d.compare_panels("How this course is assessed", [
        ("THE WSQ ASSESSMENT", "Required for certification", [
            "Written Assessment (WA) - Short-Answer Questions (SAQ)",
            "Case Study (CS) - an applied DMAIC case study",
            "Both are OPEN BOOK - slides, Learner Guide, approved materials",
            "WA covers the knowledge (K1, K2); CS covers the abilities (A1-A5)",
            "75 percent attendance is required to be eligible",
        ]),
        ("THE CAPSTONE", "Additional course deliverable", [
            "The CAPSTONE PROJECT REPORT - your consolidated DMAIC storyboard",
            "The STEERING COMMITTEE PRESENTATION - 15 minutes plus defence",
            "Built from the artifacts you produced in every lab since Lab 1",
            "On TOP of the WSQ papers, not a replacement for them",
        ]),
        ("WHY BOTH", "Certification and capability", [
            "The papers evidence the competency standard for WSQ",
            "The capstone evidences that you can actually run a project",
            "No employer asks for your exam score alone",
            "Defending an analysis under challenge is the real skill",
        ]),
    ], kicker=K, accent=VIOLET)

    # ============================================================
    # SECTION B - THE ACCUMULATED ARTIFACT SET
    # ============================================================
    d.big_statement("You have been building this since Day 1",
                    "Every lab in this course advanced YOUR project by exactly one artifact.",
                    "CAPSTONE - YOUR ARTIFACTS", color=BLUE)

    d.tile_grid("DEFINE - the artifacts you already hold", [
        ("Project charter", "Problem, goal, scope, business case, sponsor, team - re-baselined at each tollgate"),
        ("Y = f(X) statement", "Your business Y named, with the candidate Xs you set out to test"),
        ("Baseline sigma level", "DPMO and sigma computed from real data, before any change"),
        ("VOC and Kano analysis", "Customer needs captured and classified basic, performance, delighter"),
        ("CTQ flowdown", "Business Y cascaded to sub-Ys and then to controllable process Xs"),
        ("SIPOC and stakeholder plan", "Process boundaries agreed, and a move planned per stakeholder"),
    ], kicker="CAPSTONE - YOUR ARTIFACTS", cols=2, accent=DMAIC_COLORS[0] if DMAIC_COLORS else BLUE)

    d.tile_grid("MEASURE - the artifacts you already hold", [
        ("Value stream map", "Current state with cycle time, wait time and the process efficiency ratio"),
        ("Gage R&R study", "Continuous MSA with percent study variation and the accept/reject decision"),
        ("Attribute MSA and Kappa", "Inspector agreement quantified beyond chance, judged against 0.75"),
        ("Baseline capability", "Cp, Cpk, Pp and Ppk with the within-versus-total variation gap explained"),
        ("Data collection plan", "Operational definitions, sampling scheme and the sample size calculation"),
        ("The measurement verdict", "Written evidence that your data was trustworthy BEFORE you analysed it"),
    ], kicker="CAPSTONE - YOUR ARTIFACTS", cols=2, accent=TEAL)

    d.tile_grid("ANALYZE - the artifacts you already hold", [
        ("Pareto analysis", "The vital few categories carrying most of the defect or cost"),
        ("Fishbone and 5 Whys", "Structured cause hypotheses by 5M+E, driven down to root"),
        ("Hypothesis tests", "Named test, assumptions checked, p-value, and the business conclusion"),
        ("Multiple regression model", "Coefficients, adjusted R-squared, VIF and residual diagnostics"),
        ("ANOVA results", "Group means compared without inflating alpha, interactions examined"),
        ("Multi-vari study", "Positional, cyclical and temporal variation separated before spending money"),
    ], kicker="CAPSTONE - YOUR ARTIFACTS", cols=2, accent=AMBER)

    d.tile_grid("IMPROVE and CONTROL - the artifacts you already hold", [
        ("DOE design and results", "Factors, levels, design matrix, resolution, main effects and interactions"),
        ("RSM optimum", "Optimal settings for the vital few Xs, with the confirmation run"),
        ("FMEA before and after", "RPN scored, mitigated, and re-scored to prove the risk actually fell"),
        ("Pilot results", "The improvement confirmed at small scale before the full roll-out"),
        ("SPC and CUSUM/EWMA", "The chart now running in production, with its design justified"),
        ("Control plan and benefit", "Owner, reaction plan, audit schedule, and the Finance-validated number"),
    ], kicker="CAPSTONE - YOUR ARTIFACTS", cols=2, accent=RED)

    d.flow_h("Assembling the artifact set into a narrative", [
        "Lay out all 24 artifacts in DMAIC order on one table",
        "Mark each one: main deck, appendix, or working file only",
        "Check every claim in the main deck has an artifact behind it",
        "Find the gaps - a claim with no artifact is a claim you cannot defend",
        "Build the A3 from the main-deck set only",
    ], kicker="CAPSTONE - YOUR ARTIFACTS", color=BLUE)

    # ============================================================
    # SECTION C - THE A3 STORYBOARD
    # ============================================================
    d.big_statement("The A3 storyboard",
                    "One page. If it does not fit on one page, you have not finished thinking.",
                    "CAPSTONE - A3", color=TEAL)

    d.tile_grid("The seven A3 boxes", [
        ("1. Background", "Why this problem, why now, and which business objective it serves"),
        ("2. Current state", "The baseline with data - process map, capability, cost of the problem"),
        ("3. Goal", "The target condition, measurable, with a date. Specific enough to fail"),
        ("4. Root cause analysis", "The causal chain, and the statistical evidence that established it"),
        ("5. Countermeasures", "What you changed, why that change, and how it was validated"),
        ("6. Results", "Before versus after, with the Finance-signed benefit figure"),
        ("7. Follow-up", "Owner, control plan, audit dates, and the replication targets"),
    ], kicker="CAPSTONE - A3", cols=2, accent=TEAL)

    d.compare_panels("The 60-second visual test", [
        ("The test", "Hand it to a stranger", [
            "Give the A3 to someone outside the project",
            "Give them 60 seconds, then take it back",
            "Ask: what was the problem, and what fixed it?",
            "If they cannot say, the A3 has failed",
        ]),
        ("Why it fails", "The usual causes", [
            "Too much text and not enough charts",
            "Charts with no annotation of the point they make",
            "No visible before-and-after comparison",
            "The benefit figure buried in a paragraph",
        ]),
        ("The fix", "Make it visual", [
            "One clear chart per box, annotated with its conclusion",
            "Before and after side by side, same scale",
            "The money in large type where the eye lands",
            "Words only where a chart genuinely cannot carry it",
        ]),
    ], kicker="CAPSTONE - A3", accent=TEAL)

    d.tile_grid("Meridian A3 - the seven boxes filled in", [
        ("Background", "Penang line 2 overfill costing SGD 41k/month; OTIF at risk from rework"),
        ("Current state", "Fill mean 10.09 mL against 10.00 target; Cpk 0.81; 8.4 percent rework"),
        ("Goal", "Fill mean within 0.02 mL of target and Cpk above 1.33 by end of Q3"),
        ("Root cause", "DOE: pump reseal torque x dwell time interaction drives the mean shift"),
        ("Countermeasures", "Torque spec tightened, dwell time fixed at RSM optimum, poka-yoke fitted"),
        ("Results", "Mean 10.005 mL, Cpk 1.41, rework 1.2 percent, SGD 328k signed hard benefit"),
    ], kicker="CAPSTONE - A3", cols=2, accent=VIOLET)

    # ============================================================
    # SECTION D - THE STEERING COMMITTEE PRESENTATION
    # ============================================================
    d.big_statement("The steering committee is not your team",
                    "They have twenty minutes, three other projects, and one question: what do you need from us?",
                    "CAPSTONE - PRESENTING", color=AMBER)

    d.compare_panels("Three audiences in one room", [
        ("The SPONSOR", "Owns the money and the mandate", [
            "Wants: the benefit, the risk, and the ask",
            "Fears: an overclaim they will have to defend upward",
            "Give them: the signed number and the decision required",
        ]),
        ("The PROCESS OWNER", "Lives with it after you leave", [
            "Wants: to know exactly what changes for their team",
            "Fears: inheriting something unworkable or unresourced",
            "Give them: the control plan, the training, the support",
        ]),
        ("FINANCE", "Guards the credibility of the number", [
            "Wants: baseline, method, attribution, and the split",
            "Fears: soft benefits smuggled into the headline",
            "Give them: hard, soft and avoidance, clearly separated",
        ]),
    ], kicker="CAPSTONE - PRESENTING", accent=AMBER)

    d.big_statement("The two-minute rule",
                    "Decision, benefit and ask in the first two minutes. Everything after that is support.",
                    "CAPSTONE - PRESENTING", color=RED)

    d.compare_panels("Two openings for the same project", [
        ("The wrong opening", "Chronological", [
            "Good morning, I will start with some background",
            "Slide 4: our SIPOC diagram",
            "Slide 9: the Gage R&R results",
            "Slide 22: and so the benefit is...",
            "By slide 9 half the room is on email",
        ]),
        ("The right opening", "Decision first", [
            "I need approval to roll this to Singapore and Suzhou",
            "SGD 328k signed hard benefit, verified over 3 months",
            "The ask is 2 engineer-months and a 4-week line window",
            "One risk: Suzhou uses a different pump. Mitigation follows",
            "The evidence is next. Full analysis in the appendix",
        ]),
    ], kicker="CAPSTONE - PRESENTING", accent=RED)

    d.tile_grid("The 8 to 10 slide main deck", [
        ("1. The decision and the ask", "One slide. The whole point of the meeting"),
        ("2. Problem and business impact", "What it costs, tied to a business objective"),
        ("3. Baseline with data", "Capability or defect rate, before any change"),
        ("4. The root cause established", "One chart that proves the causal X"),
        ("5. What we changed", "The countermeasures, in plain language"),
        ("6. Results and the benefit", "Before versus after, plus the signed number"),
        ("7. How it is sustained", "Owner, control chart, reaction plan, audit dates"),
        ("8. Risks and next steps", "Named risks, mitigations, and the replication plan"),
    ], kicker="CAPSTONE - PRESENTING", cols=2, accent=AMBER)

    d.tile_grid("Projector legibility - the rules that get broken", [
        ("Minimum 18 point", "Anything smaller is unreadable from the back of a boardroom"),
        ("Never paste a spreadsheet", "Screenshot of a 12-column table equals zero communicated"),
        ("Label the axes in words", "Fill volume (mL), not Var1. The room does not know your variables"),
        ("Annotate the conclusion", "Put the takeaway ON the chart, not only in your narration"),
        ("Test on the actual projector", "Pale greys and thin lines vanish on a washed-out screen"),
        ("One idea per slide", "If it needs two headlines, it is two slides"),
    ], kicker="CAPSTONE - PRESENTING", cols=2, accent=AMBER)

    d.compare_panels("Stating statistics in business language", [
        ("What you would write", "Correct but unusable", [
            "p = 0.003, so we reject the null hypothesis",
            "Adjusted R-squared = 0.78, VIF all below 3",
            "Cpk improved from 0.81 to 1.41",
            "The DOE showed a significant AB interaction",
        ]),
        ("What you should say", "Same evidence, business language", [
            "The difference is real - under 1 chance in 300 it is luck",
            "These two factors explain about 78 percent of the variation",
            "Defect risk fell from roughly 1 in 100 to under 1 in 10,000",
            "Torque only matters at the longer dwell time - they interact",
        ]),
        ("The rule", "Numbers in the appendix", [
            "Say the business meaning out loud",
            "Have the statistic on the slide in small type",
            "Have the full output in the appendix, indexed",
            "Never make the room do the translation",
        ]),
    ], kicker="CAPSTONE - PRESENTING", accent=BLUE)

    # ============================================================
    # SECTION E - THE APPENDIX STRATEGY
    # ============================================================
    d.big_statement("The appendix is where you win the challenge",
                    "The main deck makes the case. The appendix proves it - on demand, in seconds.",
                    "CAPSTONE - APPENDIX", color=BLUE)

    d.tile_grid("What belongs in the appendix", [
        ("Full statistical output", "Regression tables, ANOVA tables, test statistics, confidence intervals"),
        ("The complete MSA study", "Gage R&R and Kappa results with the accept/reject decision"),
        ("The full DOE", "Design matrix, alias structure, all effects, the confirmation run"),
        ("Assumption checks", "Normality, equal variance, independence, residual plots"),
        ("The benefit calculation", "Baseline, rates, the Finance method, and the sign-off"),
        ("Alternatives rejected", "The countermeasures considered and why they were not chosen"),
    ], kicker="CAPSTONE - APPENDIX", cols=2, accent=BLUE)

    # ============================================================
    # SECTION F - DEFENDING THE ANALYSIS
    # ============================================================
    d.big_statement("Expect to be challenged",
                    "Answer with evidence, never with assertion. Assertion is what a weak project sounds like.",
                    "CAPSTONE - DEFENCE", color=RED)

    d.compare_panels("Challenge 1 - sample adequacy and power", [
        ("The challenge", "Was 30 really enough?", [
            "How did you choose that sample size?",
            "Could you have missed a real effect?",
            "Is that sample representative of all shifts?",
        ]),
        ("The weak answer", "Assertion", [
            "It is a standard sample size",
            "We collected what we could get",
            "The p-value was significant, so it was enough",
        ]),
        ("The strong answer", "Evidence", [
            "Sized for a 0.05 mL effect at 80 percent power, alpha 0.05 - n = 28, we took 32",
            "Stratified across all three shifts and both operators",
            "Appendix A4 shows the power calculation",
        ]),
    ], kicker="CAPSTONE - DEFENCE", accent=RED)

    d.compare_panels("Challenge 2 - measurement system validity", [
        ("The challenge", "How do you know the data is real?", [
            "Was the gauge capable of seeing this difference?",
            "Do your inspectors even agree with each other?",
            "Could the improvement be a measurement artifact?",
        ]),
        ("The weak answer", "Assertion", [
            "The gauge is calibrated",
            "We have always measured it this way",
            "Calibration is not the same as capability",
        ]),
        ("The strong answer", "Evidence", [
            "Gage R&R at 11.4 percent study variation - acceptable, appendix A2",
            "Attribute Kappa 0.83 across four inspectors, above the 0.75 threshold",
            "MSA was run and passed BEFORE any analysis data was collected",
        ]),
    ], kicker="CAPSTONE - DEFENCE", accent=RED)

    d.compare_panels("Challenge 4 - confounding and attribution", [
        ("The challenge", "How do you know it was YOUR change?", [
            "Volume changed in the same period",
            "A new supplier was qualified at the same time",
            "Could this just be seasonality?",
        ]),
        ("The weak answer", "Assertion", [
            "The metric improved after we implemented",
            "Nothing else changed as far as we know",
            "This is correlation offered as cause",
        ]),
        ("The strong answer", "Evidence", [
            "The DOE established the causal mechanism directly, not just an association",
            "Singapore line 1 held unimproved as a control - it did not move",
            "Volume normalised in the before-after test; effect persists",
        ]),
    ], kicker="CAPSTONE - DEFENCE", accent=RED)

    d.compare_panels("Challenge 5 - DOE resolution and aliasing", [
        ("The challenge", "What did your fraction give away?", [
            "You ran 16 runs for 7 factors - what is confounded?",
            "Could that main effect actually be an interaction?",
            "Did you confirm the optimum?",
        ]),
        ("The weak answer", "Assertion", [
            "The software chose the design",
            "We only care about main effects anyway",
            "This is exactly the answer that loses the room",
        ]),
        ("The strong answer", "Evidence", [
            "Resolution IV: main effects clear of 2-factor interactions, but 2FIs alias in pairs",
            "AB is aliased with CE - we ran 4 fold-over runs to separate them, appendix A7",
            "Confirmation run at the optimum matched prediction within 0.01 mL",
        ]),
    ], kicker="CAPSTONE - DEFENCE", accent=RED)

    d.compare_panels("Challenge 6 - sustainability and benefit type", [
        ("The challenge", "Will it hold, and is the money real?", [
            "What stops this drifting back in six months?",
            "How much of that benefit is soft?",
            "Has Finance actually signed it?",
        ]),
        ("The weak answer", "Assertion", [
            "We have a control plan",
            "The team is committed to sustaining it",
            "Roughly SGD 500k in total benefit",
        ]),
        ("The strong answer", "Evidence", [
            "EWMA chart live in production, named owner, reaction plan rehearsed",
            "30/60/90 audits already in the owner's calendar with dates",
            "SGD 328k HARD, signed by the controller. Soft and avoidance shown separately",
        ]),
    ], kicker="CAPSTONE - DEFENCE", accent=RED)

    d.compare_panels("Acknowledging a genuine weakness", [
        ("Why defensiveness fails", "It costs you the room", [
            "Every project has a weakness. They will find it",
            "Denying it makes them doubt everything else",
            "It turns a technical point into a credibility problem",
        ]),
        ("The strong pattern", "Name, bound, mitigate", [
            "NAME it before they do",
            "BOUND it - say how much it could change the conclusion",
            "MITIGATE it - say what you did or will do about it",
        ]),
        ("Worked example", "Meridian, honestly stated", [
            "Weakness: only 3 months of post-data, so annualisation is an estimate",
            "Bound: even at 70 percent hold rate the benefit exceeds SGD 230k",
            "Mitigation: benefit re-verified at the 6-month audit before full annualisation",
        ]),
    ], kicker="CAPSTONE - DEFENCE", accent=VIOLET)

    # ============================================================
    # SECTION G - LESSONS LEARNED
    # ============================================================
    d.compare_panels("Two kinds of lesson - keep them separate", [
        ("PROJECT-SPECIFIC", "Useful to this process only", [
            "The reseal torque spec was wrong in the drawing",
            "Line 2 operators were trained on the old dwell time",
            "Value: fix it, log it, replicate to sister lines",
            "It does not generalise beyond this equipment",
        ]),
        ("TRANSFERABLE", "Useful to every future project", [
            "We skipped MSA and lost three weeks to bad data",
            "The sponsor changed at month 2 and scope drifted immediately",
            "Screening DOE first would have saved 40 runs",
            "Value: this changes how you and your Green Belts work",
        ]),
    ], kicker="CAPSTONE - LESSONS", accent=TEAL)

    # ============================================================
    # SECTION H - MENTORING GREEN BELTS
    # ============================================================
    d.tile_grid("The coaching question set", [
        ("What does your DATA show?", "Not what you believe - what the data shows. Redirects opinion to evidence"),
        ("What have you RULED OUT?", "Forces them to show the alternatives they tested and eliminated"),
        ("What ASSUMPTION is that resting on?", "Surfaces the normality, independence or causality they assumed"),
        ("How would you know if you were WRONG?", "The single most valuable question. Makes the claim falsifiable"),
        ("What would the sponsor ask?", "Trains them to anticipate challenge before the tollgate"),
        ("Ask, do not tell", "The answer you hand over is forgotten. The one they find, they keep"),
    ], kicker="CAPSTONE - MENTORING", cols=2, accent=BLUE)

    d.tile_grid("Where Green Belts most need intervention", [
        ("Scope creep", "The project quietly grows until it cannot finish. The commonest failure by far"),
        ("Wrong test selection", "A t-test on non-normal data, or repeated t-tests instead of ANOVA"),
        ("Correlation read as causation", "A scatter plot presented as proof of cause. Intervene immediately"),
        ("Skipping MSA", "Analysing data from an unvalidated gauge. Everything after it is worthless"),
        ("Solution jumping", "The countermeasure was chosen on day 2, and Analyze is being back-filled"),
        ("No baseline", "No before number, so no improvement can ever be demonstrated"),
    ], kicker="CAPSTONE - MENTORING", cols=2, accent=AMBER)

    d.compare_panels("When to intervene, and when to let them learn", [
        ("INTERVENE now", "The error is unrecoverable", [
            "MSA skipped - all downstream data is worthless",
            "Scope has grown past what can be finished",
            "A causal claim about to be made to the sponsor",
            "Anything that wastes weeks or damages credibility",
        ]),
        ("LET THEM LEARN", "The error is cheap and instructive", [
            "A fishbone that turns out too broad",
            "A first-draft charter that the sponsor will refine",
            "A hypothesis that the data does not support",
            "Being wrong here is the lesson, not the failure",
        ]),
        ("The judgement", "Cost of the mistake", [
            "Expensive or irreversible -> intervene, and explain why",
            "Cheap and recoverable -> let it run, then debrief",
            "Always debrief. An unexamined mistake teaches nothing",
        ]),
    ], kicker="CAPSTONE - MENTORING", accent=BLUE)

    # ============================================================
    # SECTION I - THE BLACK BELT PATHWAY
    # ============================================================
    d.ladder("Your Black Belt pathway from here", [
        ("Trained", "You have completed the body of knowledge and the capstone"),
        ("Certified", "Capstone project and steering committee defence accepted"),
        ("Practising", "Two to three live projects delivered with Finance-validated benefit"),
        ("Mentoring", "Coaching Green Belts through their own projects"),
        ("Master Black Belt", "Owning the programme, the curriculum and the portfolio"),
    ], kicker="CAPSTONE - PATHWAY", accent=VIOLET,
        note="Certification is the start of practice, not the end of learning.")

    d.flow_h("Your first 90 days back at work", [
        "Days 1-15: present the capstone to your real sponsor and confirm the mandate",
        "Days 16-30: agree the benefit method with Finance BEFORE anything else",
        "Days 31-60: run the next tollgate; recruit and scope one Green Belt project",
        "Days 61-90: audit the control plan at 30/60/90 and verify the benefit is flowing",
        "Ongoing: log every project, mentor by asking, and keep the portfolio honest",
    ], kicker="CAPSTONE - PATHWAY", color=VIOLET)

    d.big_statement("Your capstone is your credential",
                    "Not a certificate on a wall - a project you can defend in any room, to anyone.",
                    K, color=VIOLET)
