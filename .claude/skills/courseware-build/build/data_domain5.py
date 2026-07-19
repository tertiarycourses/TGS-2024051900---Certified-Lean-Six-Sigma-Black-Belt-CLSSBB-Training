"""
Domain 5 — The CONTROL phase at Black Belt depth. Labs 27-30.

Every lab advances the learner's OWN capstone project.

Recap in depth: SPC chart anatomy, chart selection, control limits,
out-of-control rules, control plans, SOPs.
Black Belt only: CUSUM, EWMA, short-run SPC, multivariate SPC (Hotelling T2),
control plan governance across a portfolio, financial benefits validation.
"""

from data_domain1 import CAPSTONE_NOTE

DOMAIN5 = [
    dict(
        num=27, topic=5,
        title="Statistical Process Control and Chart Selection — In Depth",
        objective="Select and construct the correct control chart for your capstone Y (A5, K1).",
        desc="A full re-derivation of SPC — chart anatomy, the selection logic, control limits and "
             "the out-of-control rules. You must be able to teach this to Green Belts and audit "
             "their chart choices, which is a core Black Belt accountability. " + CAPSTONE_NOTE,
        build="A correctly selected and constructed control chart for your capstone Y with applied run rules.",
        services="Chart anatomy, control limits, Xbar-R, Xbar-S, I-MR, p, np, c, u charts, Western Electric rules, control vs spec limits",
        steps=[
            ("Recap SPC purpose in full: distinguish signal from noise over time, so drift is caught before it becomes a defect.", ""),
            ("Recap chart anatomy: centre line, upper and lower control limits at +/- 3 sigma, and why 3 sigma balances false alarms against missed signals.", ""),
            ("Establish the critical distinction: CONTROL limits come from the process's own voice (the data); SPECIFICATION limits come from the customer. They are unrelated and must never be drawn on the same axis as if comparable.", ""),
            ("Learn the chart selection logic in full. Continuous data: subgroup size 1 = I-MR; 2-8 = Xbar-R; 9+ = Xbar-S.", ""),
            ("Learn the attribute branch: defectives with constant sample size = np; varying = p. Defects with constant opportunity = c; varying = u.", ""),
            ("Select the correct chart for your capstone Y and write down the justification. Selecting the wrong chart produces wrong limits and false confidence.", ""),
            ("Collect at least 25 subgroups of baseline data — fewer gives control limits too unstable to be trustworthy.", ""),
            ("Calculate the control limits using the correct constants (A2, D3, D4 for Xbar-R; equivalent constants for other charts).", ""),
            ("Plot the chart and apply the Western Electric run rules in full: 1 point beyond 3 sigma; 2 of 3 beyond 2 sigma; 4 of 5 beyond 1 sigma; 8 consecutive on one side; trends; and hugging the centre line.", ""),
            ("Investigate every signal. If a special cause is found and removed, recalculate the limits excluding that point — but only with a documented assignable cause.", ""),
            ("Confirm the process is stable before proceeding. An unstable process has no meaningful capability and cannot be controlled by a control plan alone.", ""),
        ],
        test="Your chart selection is justified against the selection logic, limits are computed from 25+ subgroups with the correct constants, and all run rules are applied with every signal investigated.",
    ),
    dict(
        num=28, topic=5,
        title="CUSUM, EWMA and Short-Run SPC (Black Belt Only)",
        objective="Detect small sustained shifts using CUSUM and EWMA, and chart high-mix processes (A5, K2).",
        desc="BLACK BELT ONLY. Shewhart charts are poor at detecting small sustained shifts — they "
             "may take dozens of subgroups to react to a 1-sigma drift, which is precisely how a "
             "process degrades unnoticed after a project closes. CUSUM and EWMA solve this, and "
             "short-run methods handle high-mix low-volume processes Shewhart cannot chart at "
             "all. " + CAPSTONE_NOTE,
        build="CUSUM and EWMA charts on your capstone data plus a short-run standardised chart.",
        services="ARL, CUSUM, decision interval, V-mask, EWMA, lambda weighting, autocorrelation, short-run standardised charts, DNOM",
        steps=[
            ("Understand Average Run Length (ARL): the expected number of subgroups before a chart signals. For a 1-sigma shift, a Shewhart Xbar chart has an ARL around 44 — far too slow.", ""),
            ("Understand the structural reason: a Shewhart chart considers only the CURRENT point and has no memory of the recent past.", ""),
            ("Learn CUSUM: it accumulates deviations from target, so a small persistent bias adds up into a detectable signal rather than being repeatedly dismissed as noise.", ""),
            ("Set up the CUSUM parameters: the reference value k (typically half the shift you want to detect) and the decision interval h (typically 4 or 5 sigma).", ""),
            ("Build upper and lower CUSUM statistics for your capstone data and plot them against the decision interval.", ""),
            ("Compare the CUSUM detection point against the Shewhart chart from Lab 27 on the same data — CUSUM typically detects a sustained small shift several subgroups sooner.", ""),
            ("Learn EWMA: each point is a weighted average of all history, with weights decaying geometrically. Lambda controls the memory.", ""),
            ("Choose lambda deliberately: small lambda (0.1-0.2) gives long memory and strong small-shift detection; large lambda (0.4+) approaches Shewhart behaviour.", ""),
            ("Build the EWMA chart with its widening initial control limits, and note that EWMA also handles autocorrelated data far better than Shewhart.", ""),
            ("Test your capstone data for autocorrelation. Chemical, batch and continuous-flow processes are frequently autocorrelated, which makes Shewhart limits far too narrow and generates constant false alarms.", ""),
            ("Now short-run SPC. Understand the problem: high-mix low-volume processes never accumulate 25 subgroups of any single part number.", ""),
            ("Learn the deviation-from-nominal (DNOM) approach: plot (measurement - part nominal) so different part numbers share one chart.", ""),
            ("Learn the standardised approach for parts with differing variances: plot (measurement - nominal) / sigma_part, putting all parts on a common scale.", ""),
            ("Build a short-run chart for a multi-product step in your capstone, or for Meridian's shared assembly line across pump variants.", ""),
            ("Decide which chart type belongs in your capstone control plan and justify the choice against shift size, autocorrelation and product mix.", ""),
        ],
        test="You have built CUSUM and EWMA charts and compared their detection speed against Shewhart on the same data, tested for autocorrelation, and justified your final chart selection for the control plan.",
    ),
    dict(
        num=29, topic=5,
        title="Multivariate SPC and Control Plan Governance (Black Belt Only)",
        objective="Monitor correlated characteristics with Hotelling's T-squared and govern control plans (A5, K1).",
        desc="BLACK BELT ONLY. When several correlated characteristics matter, running separate "
             "charts inflates false alarms and — more dangerously — misses failures visible only "
             "in the correlation structure. Then step up to the portfolio view: the Black Belt "
             "audits control plans across projects, not just their own. " + CAPSTONE_NOTE,
        build="A Hotelling T-squared chart plus a governed control plan for your capstone.",
        services="Multivariate SPC, Hotelling T-squared, correlation structure, false alarm inflation, control plan, response plan, audit cadence",
        steps=[
            ("Understand the false alarm problem: 5 separate charts each at alpha = 0.0027 gives a combined false alarm rate over 1.3 percent — five times intended.", ""),
            ("Understand the more serious failure: two characteristics can each sit within their own limits while their COMBINATION is impossible, and separate charts will never see it.", ""),
            ("Identify a set of correlated characteristics in your capstone — dimensions on one part, or related cycle times across linked steps.", ""),
            ("Compute the correlation matrix and confirm the characteristics are genuinely correlated. If they are independent, separate charts are fine.", ""),
            ("Learn Hotelling's T-squared: it collapses several correlated characteristics into one statistic accounting for the covariance structure.", ""),
            ("Build the T-squared chart with its upper control limit from the F-distribution, and note there is no lower limit — T-squared is always positive.", ""),
            ("Understand the interpretation difficulty: a T-squared signal tells you something is wrong but not which variable. Use decomposition or individual charts as a follow-up diagnostic.", ""),
            ("Now build your capstone control plan in full: for each critical X and the Y — the metric, target, specification, measurement method, sample size, frequency, chart type, owner and reaction plan.", ""),
            ("Write the reaction plan for each metric as a specific instruction: containment action, escalation path, named owner and time limit. 'Investigate' is not a reaction plan.", ""),
            ("Add the control plan to the process documentation and update the SOP, training material and visual management boards.", ""),
            ("Step up to portfolio governance: as Black Belt you audit control plans across multiple projects. Define your audit cadence and criteria.", ""),
            ("Define what a control plan audit checks: is the chart still being maintained, are signals being actioned, is the owner still in post, and has the process drifted since handover?", ""),
            ("Identify the most common decay mode — charts maintained but signals never actioned — and write your countermeasure for it.", ""),
        ],
        test="Your correlated characteristics are confirmed by a correlation matrix before applying T-squared, every control plan metric has a specific named reaction plan, and you have defined an audit cadence with explicit criteria.",
    ),
    dict(
        num=30, topic=5,
        title="Financial Benefits Validation, Handover and Project Closure",
        objective="Validate benefits with Finance and formally close your capstone project (A5, K1).",
        desc="Benefits are not real until Finance signs them. This lab converts your improvement into "
             "a validated financial number, transfers ownership to the process owner, and formally "
             "closes the project — the step most often skipped, and the reason gains quietly "
             "evaporate. " + CAPSTONE_NOTE,
        build="A Finance-validated benefits statement and a signed handover and closure pack.",
        services="Hard vs soft benefits, cost avoidance, benefit validation, Finance sign-off, handover, sustainability audit, lessons learned, closure",
        steps=[
            ("Learn the benefit categories precisely. HARD: cost reduction that appears in the P&L. SOFT: capacity or time released without a headcount or cost change. COST AVOIDANCE: costs not incurred that would have been.", ""),
            ("Understand why the distinction matters: Finance books these differently, and claiming soft benefits as hard is the fastest way to lose credibility with a CFO.", ""),
            ("Quantify your capstone's benefit against the Lab 3 baseline, using post-improvement data over a defensible period, not a single good week.", ""),
            ("Verify the improvement is statistically significant, not a favourable run — apply a hypothesis test comparing post-improvement against baseline.", ""),
            ("Confirm sustained performance with your control chart: the shift must hold for a meaningful period before the benefit can be booked.", ""),
            ("Separate your benefit into hard, soft and cost-avoidance components and state each explicitly.", ""),
            ("Take the calculation to Finance and obtain sign-off. Expect challenge on the baseline period, the attribution and whether other changes could explain the result.", ""),
            ("Prepare your attribution argument: what else changed in the period, and why the improvement is attributable to your intervention rather than to those.", ""),
            ("Build the handover pack: control plan, updated SOPs, training records, control charts, reaction plans and the named process owner.", ""),
            ("Conduct the handover meeting with the process owner. They must accept ownership explicitly — an assumed handover is a failed handover.", ""),
            ("Schedule the sustainability audit at 30, 60 and 90 days post-handover, with a named auditor and defined criteria.", ""),
            ("Run the lessons learned session: what worked, what did not, what you would do differently, and what transfers to the Green Belts you mentor.", ""),
            ("Formally close the project with sponsor sign-off, and archive the full DMAIC storyboard.", ""),
            ("Update the project portfolio from Lab 2 — record the closed project's realised benefit and select the next project.", ""),
        ],
        test="Your benefit is separated into hard, soft and cost-avoidance components, validated statistically and signed off by Finance, and the process owner has explicitly accepted handover with a scheduled sustainability audit.",
    ),
]
