"""
Domain 4 — The IMPROVE phase at Black Belt depth. Labs 22-26.

Every lab advances the learner's OWN capstone project.

Recap in depth: solution generation, selection matrices, Lean countermeasures,
FMEA, piloting.
Black Belt only: full factorial DOE, fractional factorial and confounding,
resolution, response surface methodology, robust/Taguchi design.
"""

from data_domain1 import CAPSTONE_NOTE

DOMAIN4 = [
    dict(
        num=22, topic=4,
        title="Solution Generation, Selection and Lean Countermeasures — In Depth",
        objective="Generate and select improvements targeting your proven root causes (A5).",
        desc="Re-derive solution generation and the full Lean countermeasure toolkit, then select "
             "rigorously with a weighted matrix. Every solution must attack a PROVEN root cause "
             "from Lab 21 — solutions that address unproven causes are how projects quietly "
             "fail. " + CAPSTONE_NOTE,
        build="A scored solution selection matrix mapping each solution to a proven root cause.",
        services="Brainstorming, brainwriting, SCAMPER, benchmarking, 5S, poka-yoke, pull/JIT, Heijunka, Jidoka, standard work, selection matrix",
        steps=[
            ("Take your ranked proven root causes from Lab 21. Every solution generated in this lab must trace to one of them.", ""),
            ("Recap divergent generation techniques in full: brainstorming, brainwriting (6-3-5), SCAMPER, anti-solution thinking and analogy from other industries.", ""),
            ("Recap benchmarking and its four steps — plan, collect, analyse, adapt. Look outside your industry, where the best analogous processes usually are.", ""),
            ("Generate at least three candidate solutions for each proven root cause. One solution per cause means you have not really explored the space.", ""),
            ("Recap the Lean countermeasure toolkit in full: 5S, poka-yoke, pull systems, JIT, Heijunka (levelling), Jidoka (autonomation) and standard work.", ""),
            ("Recap poka-yoke levels specifically: prevention (error impossible), detection (error caught immediately) and warning (error flagged). Always prefer prevention.", ""),
            ("Map each Lean tool to the root causes in your capstone it could plausibly address, and generate at least two poka-yoke ideas.", ""),
            ("Build the weighted solution selection matrix. Criteria typically: impact on Y, implementation cost, time to benefit, technical risk, ease of adoption and sustainability.", ""),
            ("Weight the criteria with your sponsor, not alone — the weighting reflects business priorities that are theirs to set.", ""),
            ("Score every candidate solution and compute weighted totals.", ""),
            ("Sanity-check the top-ranked solutions: do they collectively address the causes explaining most of the Y gap? If not, revisit generation.", ""),
            ("Identify which solutions have controllable factors suitable for DOE optimisation in Labs 23-25.", ""),
        ],
        test="Every solution traces to a proven root cause, criteria weights are agreed with the sponsor, and your selected set collectively addresses the majority of the quantified Y gap.",
    ),
    dict(
        num=23, topic=4,
        title="Full Factorial Design of Experiments (Black Belt Only)",
        objective="Design, run and analyse a full factorial experiment on your capstone process (A3, A5, K2).",
        desc="BLACK BELT ONLY — the Green Belt course mentions DOE in passing; the Black Belt owns "
             "it. One-factor-at-a-time experimentation is slower, less informative and structurally "
             "incapable of detecting interactions. Full factorial designs estimate every main "
             "effect AND every interaction. " + CAPSTONE_NOTE,
        build="A designed 2^k full factorial experiment with main effects and interaction analysis.",
        services="OFAT vs DOE, 2^k factorial, factors & levels, randomisation, replication, blocking, main effects, interaction plots, effect significance",
        steps=[
            ("Understand why OFAT fails: it cannot detect interactions at all, and it requires more runs for less information than a factorial design.", ""),
            ("Recap the DOE vocabulary in full: factor, level, response, run, effect, interaction, replication, randomisation, blocking and experimental error.", ""),
            ("Select 3 factors from your capstone that you can actually control and vary — temperature, speed, pressure, batch size, staffing level or method variant.", ""),
            ("Set two levels for each factor — low (-1) and high (+1). Set them wide enough to produce a detectable effect but within safe operating limits.", ""),
            ("Build the 2^3 design matrix: 8 runs covering every combination of the three factors, in standard order.", ""),
            ("Decide replication. Replicates give an estimate of pure experimental error and let you test effect significance — 2 replicates gives 16 runs.", ""),
            ("RANDOMISE the run order. Randomisation protects against unknown time-varying nuisance factors and is not optional.", ""),
            ("Use blocking if runs must span shifts, days or material lots — block on the nuisance factor so it does not contaminate the effects.", ""),
            ("Execute the experiment, holding all non-experimental factors constant and recording anything unexpected during each run.", ""),
            ("Calculate main effects: the average response at the high level minus the average at the low level, for each factor.", ""),
            ("Calculate interaction effects for AB, AC, BC and the three-way ABC.", ""),
            ("Plot main effects (steeper slope means larger effect) and interaction plots (non-parallel lines mean interaction present).", ""),
            ("Test effect significance using a Pareto of effects or a normal probability plot of effects — points off the line are real effects.", ""),
            ("Build the prediction equation from the significant effects and identify the factor settings that optimise your Y.", ""),
            ("Run confirmation trials at the predicted optimum. If the confirmation fails, the model is missing something — do not roll out.", ""),
        ],
        test="Your design is fully randomised with replication, you have computed and plotted both main effects and interactions, effect significance is assessed statistically, and confirmation runs validate the predicted optimum.",
    ),
    dict(
        num=24, topic=4,
        title="Fractional Factorial Designs, Confounding and Resolution (Black Belt Only)",
        objective="Screen many factors efficiently and interpret confounded effects correctly (A3, K2).",
        desc="BLACK BELT ONLY. A full factorial on 7 factors needs 128 runs — usually unaffordable. "
             "Fractional factorials screen many factors in a fraction of the runs by deliberately "
             "trading away the ability to separate certain effects. The critical skill is knowing "
             "exactly WHAT you traded away, which is what resolution tells you. " + CAPSTONE_NOTE,
        build="A fractional factorial screening design with a documented confounding structure.",
        services="2^(k-p) designs, generators, defining relation, alias structure, confounding, Resolution III/IV/V, screening, fold-over designs",
        steps=[
            ("Understand the economics: 2^7 full factorial = 128 runs; a 2^(7-4) fractional = 16 runs. The saving is real but it is paid for in resolving power.", ""),
            ("Understand confounding (aliasing): in a fractional design, some effects are mathematically indistinguishable from others.", ""),
            ("Learn the generator and defining relation — the algebra that determines exactly which effects are aliased with which.", ""),
            ("Learn the resolution scale precisely. RESOLUTION III: main effects aliased with two-factor interactions. RESOLUTION IV: main effects clear of two-factor interactions, but two-factor interactions aliased with each other. RESOLUTION V: main effects and two-factor interactions all clear.", ""),
            ("Understand the selection rule: use Resolution III only for early screening of many factors; use IV or V when you intend to interpret interactions.", ""),
            ("Select 5 or more candidate factors from your capstone for a screening experiment.", ""),
            ("Choose your fraction based on your run budget, and write down the resulting resolution BEFORE running anything.", ""),
            ("Generate the design matrix and write out the complete alias structure. You must be able to state what each estimated effect is confounded with.", ""),
            ("Apply effect sparsity and hierarchy: usually few factors dominate, and low-order effects are more likely to be real than high-order ones.", ""),
            ("Randomise and execute the screening experiment.", ""),
            ("Analyse the effects and identify the vital few factors. Where an important effect is confounded, state the ambiguity explicitly rather than assuming the main effect is the real one.", ""),
            ("Resolve critical ambiguity with a fold-over design — a second fraction that de-aliases the effects you care about.", ""),
            ("Take the screened vital few factors forward to a full factorial or RSM study in Lab 25.", ""),
        ],
        test="You stated the design resolution before running, wrote out the complete alias structure, and any ambiguous conclusion is either declared explicitly or resolved by a fold-over.",
    ),
    dict(
        num=25, topic=4,
        title="Response Surface Methodology and Robust Design (Black Belt Only)",
        objective="Optimise factor settings using RSM and make the process robust to noise (A5, K2).",
        desc="BLACK BELT ONLY. Factorial designs find WHICH factors matter; RSM finds the OPTIMUM "
             "SETTINGS by modelling curvature that a two-level design cannot see. Taguchi robust "
             "design then goes further — setting the process so it performs consistently despite "
             "noise you cannot control. " + CAPSTONE_NOTE,
        build="An RSM study locating optimal settings plus a robust design analysis against noise factors.",
        services="Curvature & centre points, steepest ascent, central composite design, Box-Behnken, contour & surface plots, Taguchi, signal-to-noise, control vs noise factors",
        steps=[
            ("Understand the limitation of 2-level designs: with only two levels per factor they fit a straight line and cannot detect curvature at all.", ""),
            ("Add CENTRE POINTS to your factorial design to test for curvature. A significant centre-point effect means the true response is curved and a linear model will mislead you.", ""),
            ("If no curvature is present and you are far from the optimum, use steepest ascent — move the factor settings in the direction of greatest improvement and re-experiment.", ""),
            ("Once curvature appears, you are near the optimum and need a second-order design.", ""),
            ("Learn the central composite design (CCD): a factorial core, plus centre points, plus axial (star) points that add the third level needed to estimate quadratic terms.", ""),
            ("Learn the Box-Behnken alternative: fewer runs than CCD and it never requires extreme corner combinations, which matters when corners are unsafe or infeasible.", ""),
            ("Design and run an RSM study on the 2-3 vital factors from Lab 24.", ""),
            ("Fit the second-order model including linear, quadratic and interaction terms.", ""),
            ("Generate contour and 3D surface plots to visualise the response surface and locate the optimum region.", ""),
            ("Find the stationary point and classify it — maximum, minimum or saddle. A saddle point means the optimum lies at a boundary, not in the middle.", ""),
            ("Use desirability functions if you must optimise several responses at once with competing optima.", ""),
            ("Now robust design. Separate your factors into CONTROL factors (you set them) and NOISE factors (ambient conditions, material variation, operator, wear).", ""),
            ("Understand the Taguchi insight: choose control factor settings at which the response is LEAST SENSITIVE to noise — a slightly lower mean with far less variation usually wins.", ""),
            ("Compute the signal-to-noise ratio for candidate settings, using the correct form for your objective (smaller-is-better, larger-is-better or nominal-is-best).", ""),
            ("Select the robust operating window and run confirmation trials under deliberately varied noise conditions.", ""),
        ],
        test="Curvature is tested with centre points, your second-order model is visualised as a contour or surface plot with a classified stationary point, and the robust settings are confirmed under varied noise conditions.",
    ),
    dict(
        num=26, topic=4,
        title="FMEA, Pilot Design and Implementation Planning — In Depth",
        objective="De-risk and pilot your capstone improvement before full rollout (A5).",
        desc="Re-derive FMEA in full, then design the pilot that proves your improvement works before "
             "it is scaled. A Black Belt never rolls out an unpiloted change across sites — the "
             "cost of being wrong at scale is exactly what the pilot buys down. " + CAPSTONE_NOTE,
        build="A completed FMEA with re-scored RPNs and a full pilot plan with success criteria.",
        services="FMEA, severity/occurrence/detection, RPN, risk mitigation, pilot design, success criteria, implementation planning, cost-benefit",
        steps=[
            ("Recap FMEA in full: failure mode, effect, cause, current controls, and the three ratings that combine into the risk priority number.", ""),
            ("Recap the scoring scales precisely: Severity (impact if it occurs), Occurrence (likelihood) and Detection (probability of catching it BEFORE the customer does — note the inverted scale).", ""),
            ("Build the FMEA for your selected improvement. For each process step, ask what could fail, what happens if it does, and what would cause it.", ""),
            ("Score S, O and D on 1-10 scales and calculate RPN = S x O x D.", ""),
            ("Apply the severity override rule: any failure mode with Severity 9-10 requires action regardless of how low its RPN is.", ""),
            ("Rank by RPN and define mitigation for every high-RPN mode, targeting the component you can most cheaply move — usually Detection, sometimes Occurrence.", ""),
            ("RE-SCORE after mitigation and record the residual RPN. An FMEA without re-scoring has not demonstrated that risk was actually reduced.", ""),
            ("Design the pilot: scope (which line, site or segment), duration, sample size and the exact data to be collected.", ""),
            ("Define quantitative success criteria BEFORE the pilot starts, expressed against your Lab 3 baseline. Criteria defined afterwards get rationalised.", ""),
            ("Plan the comparison: before/after, or better, a control group running the unchanged process concurrently to rule out external effects.", ""),
            ("Define the stop conditions — what result would cause you to halt the pilot rather than push through.", ""),
            ("Build the implementation plan: tasks, owners, dates, training, communication, systems changes and documentation updates.", ""),
            ("Complete the cost-benefit analysis: implementation cost, annualised benefit, payback period and NPV where the investment is material.", ""),
            ("Run the pilot (or design it fully for post-course execution) and test the results statistically against the baseline — a visual improvement is not proof.", ""),
        ],
        test="Your FMEA is re-scored post-mitigation with the severity override applied, pilot success criteria were defined before starting, and the improvement is tested statistically against the documented baseline.",
    ),
]
