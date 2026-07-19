"""
Domain 2 — The MEASURE phase at Black Belt depth. Labs 8-14.

Every lab advances the learner's OWN capstone project (see data_domain1.SCENARIO
for the Meridian fallback scenario).

Recap in depth: process mapping, VSM, data types, sampling, sample size,
continuous Gage R&R, yield/DPMO/capability.
Black Belt only: attribute MSA and Kappa, nested and destructive gauge studies,
non-normal capability with Box-Cox, Cpk vs Ppk, rational subgrouping.
"""

from data_domain1 import CAPSTONE_NOTE

DOMAIN2 = [
    dict(
        num=8, topic=2,
        title="Value Stream Mapping, Takt Time and the Eight Wastes — In Depth",
        objective="Build a value stream map of your capstone process and quantify waste (A2, A4).",
        desc="A full re-derivation of value stream mapping — material AND information flow, "
             "value-added ratio, takt time and the eight wastes — then applied to your own "
             "capstone process to expose where lead time is actually consumed. " + CAPSTONE_NOTE,
        build="A current-state VSM with a value-added ratio, takt time and a quantified waste log.",
        services="VSM icons, material & information flow, lead time ladder, takt time, VA/NVA ratio, eight wastes",
        steps=[
            ("Recap the VSM in full: what it shows that a process map does not — inventory, information flow, lead time and the push/pull signal.", ""),
            ("Recap the standard VSM icons: process box, data box, inventory triangle, push arrow, supermarket, truck, information flow and the timeline ladder.", ""),
            ("Map the current state of your capstone value stream from customer order to delivery. Include the information flow that triggers each step.", ""),
            ("Populate each data box: cycle time, changeover time, uptime, batch size, number of operators and first-pass yield.", ""),
            ("Draw the timeline ladder underneath. Put value-added time on the lower rung and waiting/queue time on the upper rung.", ""),
            ("Calculate total lead time, total value-added time, and the value-added ratio (VA time / lead time). Most processes land under 5 percent.", ""),
            ("Calculate takt time = available production time / customer demand for the period. Compare takt against each step's cycle time to find the bottleneck.", ""),
            ("Recap the eight wastes in full (DOWNTIME: Defects, Overproduction, Waiting, Non-utilised talent, Transport, Inventory, Motion, Extra processing).", ""),
            ("Walk your value stream and log every instance of each waste. Quantify each in time or money — an unquantified waste will not win funding.", ""),
            ("Mark the three points on the VSM where the largest waste concentrates. These become improvement candidates for Day 4.", ""),
        ],
        test="Your VSM shows both material and information flow, you have calculated the value-added ratio and takt time from real numbers, and every logged waste carries a time or dollar quantification.",
    ),
    dict(
        num=9, topic=2,
        title="Data Types, Operational Definitions and the Data Collection Plan",
        objective="Build a rigorous data collection plan for your capstone (A4).",
        desc="Re-derive data classification and operational definitions in full, then build the data "
             "collection plan that will feed every statistical test in Days 3 and 4. Bad data "
             "collected now cannot be rescued by clever statistics later. " + CAPSTONE_NOTE,
        build="A data collection plan with operational definitions for every metric in your capstone.",
        services="Continuous vs discrete, nominal/ordinal/interval/ratio, operational definitions, data collection plan, stratification factors",
        steps=[
            ("Recap the data hierarchy in full: nominal, ordinal, interval and ratio — and why the type determines which statistical test is legal.", ""),
            ("Recap continuous versus discrete (attribute) data, and why continuous data needs far smaller samples to reach the same confidence.", ""),
            ("List every metric your capstone requires: the project Y, each sub-Y from your flowdown, and each candidate X you intend to test.", ""),
            ("Classify each metric by data type. Flag any metric currently collected as attribute that could be captured as continuous — convert it if you can.", ""),
            ("Write a complete operational definition for each metric: what is measured, the instrument, the unit, the sampling point, the collector and the defect criterion.", ""),
            ("Test each operational definition by having two people apply it independently to the same item. If they disagree, the definition is not yet operational.", ""),
            ("Identify your stratification factors — plant, line, shift, operator, product family, supplier. You must capture these at collection time or you can never stratify later.", ""),
            ("Build the data collection plan table: metric, definition, type, source, sample size, frequency, collector, stratification fields and start date.", ""),
            ("Design the check sheet or data form. Make the easy path the correct path, or collectors will improvise.", ""),
            ("Dry-run the plan on a small batch and fix whatever breaks before committing to full collection.", ""),
        ],
        test="Every capstone metric has a written operational definition that two people apply identically, stratification fields are captured at source, and the plan has survived a dry run.",
    ),
    dict(
        num=10, topic=2,
        title="Sampling Strategy, Sample Size and Rational Subgrouping",
        objective="Determine defensible sample sizes and design rational subgroups for your capstone (A4).",
        desc="Re-derive sampling schemes and sample size formulas in full, then go beyond Green Belt "
             "with RATIONAL SUBGROUPING — the decision that silently determines what your control "
             "charts in Day 4 will be capable of detecting at all. " + CAPSTONE_NOTE,
        build="Calculated sample sizes for your capstone metrics and a rational subgrouping scheme.",
        services="Random/stratified/systematic/cluster sampling, sample size for continuous & discrete data, rational subgrouping, sampling bias",
        steps=[
            ("Recap the four sampling schemes in full: simple random, stratified, systematic and cluster — with the failure mode of each.", ""),
            ("Identify the sampling bias risks in your capstone: convenience sampling, day-shift-only sampling, and sampling only when the process is running well.", ""),
            ("Recap the continuous-data sample size formula n = (1.96 s / d)^2, where s is the estimated standard deviation and d is the precision you require.", ""),
            ("Apply it to your project Y. Estimate s from historical data or a pilot sample, choose your required precision d, and calculate n.", ""),
            ("Recap the discrete-data formula n = (1.96/d)^2 x p(1-p), where p is the estimated proportion defective.", ""),
            ("Apply it to your attribute metrics. Note how much larger n becomes — this is the cost of measuring in pass/fail.", ""),
            ("Now design rational subgroups. A subgroup must contain only common-cause variation, so that between-subgroup variation shows up as a signal.", ""),
            ("Decide what varies WITHIN your subgroup and what varies BETWEEN subgroups. Getting this backwards makes control limits so wide that nothing ever signals.", ""),
            ("Set subgroup size and sampling frequency for your capstone Y, and state what shift size you would be able to detect.", ""),
            ("Document the sampling plan and check it against the data collection plan from Lab 9 for consistency.", ""),
        ],
        test="Your sample sizes are calculated from a real estimate of s or p, your subgrouping scheme places common-cause variation within subgroups, and you can state the shift size your plan can detect.",
    ),
    dict(
        num=11, topic=2,
        title="Continuous Gage R&R — In Depth",
        objective="Validate a continuous measurement system for your capstone using Gage R&R (A4).",
        desc="A full re-derivation of measurement system analysis for continuous data. Before any "
             "of the statistics in Days 3 and 4 can be trusted, the measurement system must be "
             "proven — an invalid gauge invalidates every conclusion that follows. " + CAPSTONE_NOTE,
        build="A completed crossed Gage R&R study with %study variation and ndc for your capstone metric.",
        services="Accuracy, bias, linearity, stability, repeatability, reproducibility, %study variation, ndc, %tolerance",
        steps=[
            ("Recap the components of measurement variation in full: observed variation = actual process variation + measurement system variation.", ""),
            ("Recap the five MSA properties: accuracy (bias), linearity, stability, repeatability (equipment) and reproducibility (operator).", ""),
            ("Distinguish repeatability from reproducibility precisely — same operator repeating, versus different operators on the same part.", ""),
            ("Design a crossed Gage R&R for your capstone metric: 10 parts spanning the full process range, 3 operators, 3 repeat measurements each.", ""),
            ("Select parts that span the real range of production. Parts clustered near the mean will flatter the gauge and hide its weakness.", ""),
            ("Randomise the measurement order and blind the operators to previous readings, or you will measure memory rather than the gauge.", ""),
            ("Run the study and record all 90 measurements in the standard crossed layout.", ""),
            ("Calculate %study variation for repeatability, reproducibility and total Gage R&R. Apply the acceptance rule: under 10% acceptable, 10-30% marginal, over 30% unacceptable.", ""),
            ("Calculate the number of distinct categories (ndc). ndc must be 5 or more for the gauge to distinguish parts usefully.", ""),
            ("If the gauge fails, decide the fix: recalibrate, retrain operators, tighten the operational definition or replace the instrument. Then re-run.", ""),
        ],
        test="Your study uses parts spanning the full process range with randomised blinded order, and you have computed %study variation and ndc with a stated accept/reject decision.",
    ),
    dict(
        num=12, topic=2,
        title="Attribute MSA and Kappa Analysis (Black Belt Only)",
        objective="Validate a judgement-based measurement system using attribute agreement and Kappa (A4, K2).",
        desc="BLACK BELT ONLY — the Green Belt course does not teach this. When the measurement is a "
             "human judgement (pass/fail, cosmetic grade, claim approve/reject), Gage R&R does not "
             "apply at all. Attribute agreement analysis and Cohen's/Fleiss' Kappa are the correct "
             "tools, and most organisations discover their inspectors agree far less than assumed. " + CAPSTONE_NOTE,
        build="An attribute agreement study with within-, between- and versus-standard Kappa values.",
        services="Attribute agreement analysis, Cohen's Kappa, Fleiss' Kappa, within/between appraiser agreement, agreement vs standard",
        steps=[
            ("Establish why Gage R&R fails for attribute data: there is no continuous scale on which to compute variance components.", ""),
            ("Identify a judgement-based measurement in your capstone — visual inspection, cosmetic grading, document approval, claim adjudication or defect classification.", ""),
            ("Select 30 to 50 sample items spanning clear-pass, clear-fail and deliberately borderline cases. Borderline items are where agreement actually breaks down.", ""),
            ("Have an expert establish the KNOWN STANDARD (true) classification for every item. Without a standard you can measure consistency but never correctness.", ""),
            ("Have 3 appraisers each classify every item twice, in randomised order, blinded to their own previous answer and to each other.", ""),
            ("Calculate WITHIN-appraiser agreement — does each inspector agree with themselves? Self-disagreement is the most common and most ignored failure.", ""),
            ("Calculate BETWEEN-appraiser agreement — do the inspectors agree with each other?", ""),
            ("Calculate agreement VERSUS THE STANDARD — are they collectively correct, or consistently wrong together?", ""),
            ("Compute Cohen's Kappa for appraiser pairs and Fleiss' Kappa across all appraisers. Kappa corrects raw agreement for agreement expected by chance.", ""),
            ("Apply the acceptance rule: Kappa >= 0.90 excellent, 0.75-0.90 acceptable, below 0.75 requires action. Note that 90% raw agreement can still yield a poor Kappa.", ""),
            ("Where agreement fails, prescribe the fix: boundary samples, photographic standards, tightened operational definitions or appraiser retraining. Then re-run.", ""),
        ],
        test="Your study includes borderline items and a known standard, you have computed within-appraiser, between-appraiser and versus-standard agreement plus Kappa, and you have an action plan for any Kappa below 0.75.",
    ),
    dict(
        num=13, topic=2,
        title="Nested and Destructive Gauge Studies (Black Belt Only)",
        objective="Design a valid MSA when parts cannot be measured repeatedly (A4, K2).",
        desc="BLACK BELT ONLY. The crossed Gage R&R of Lab 11 assumes every operator can measure "
             "every part repeatedly. Destructive tests (tensile, burst, seal strength, chemical "
             "assay) break that assumption entirely — measuring consumes the part. The nested "
             "design is the correct answer, and using a crossed study here produces confident "
             "nonsense. " + CAPSTONE_NOTE,
        build="A nested gauge study design and analysis for a destructive or single-measurement test.",
        services="Nested vs crossed designs, destructive testing MSA, homogeneous batches, part-to-part confounding, variance components",
        steps=[
            ("State precisely why a crossed design is invalid for destructive tests: the part no longer exists to be measured a second time.", ""),
            ("Identify a destructive or non-repeatable measurement in your capstone — or use the Meridian seal-strength test on infusion pump tubing.", ""),
            ("Understand the nested design: each operator measures DIFFERENT parts, and parts are nested within batch rather than crossed with operator.", ""),
            ("Establish homogeneous batches. The design assumes parts within a batch are effectively identical — if they are not, part variation contaminates repeatability.", ""),
            ("Justify batch homogeneity: same lot, same machine, same setup, consecutive production, minimal elapsed time.", ""),
            ("Design the study: 3 operators, 10 batches, 3 parts per operator per batch, all parts within a batch treated as replicates.", ""),
            ("Run the study and record results in the nested layout — operator within batch, not operator crossed with part.", ""),
            ("Compute variance components for repeatability and reproducibility using the nested model. Note that repeatability is now confounded with within-batch part variation.", ""),
            ("State that confounding explicitly in your report. A nested study OVERSTATES repeatability variation, so it is a conservative test.", ""),
            ("Decide accept/reject, and record the design choice and its rationale for the Day 5 presentation — expect this to be challenged.", ""),
        ],
        test="You can explain why a crossed study is invalid for your measurement, your batches are justified as homogeneous, and your report states the repeatability/part-variation confounding explicitly.",
    ),
    dict(
        num=14, topic=2,
        title="Baseline Capability — Cp, Cpk, Pp, Ppk and Non-Normal Data",
        objective="Establish baseline capability for your capstone, handling non-normal data correctly (A4, K2).",
        desc="Re-derive capability analysis in full, then go beyond Green Belt: the distinction "
             "between Cpk and Ppk that most practitioners get wrong, and what to do when the data "
             "is not normal — which is most of the time in cycle-time and defect data. " + CAPSTONE_NOTE,
        build="A baseline capability study for your capstone Y with a documented normality decision.",
        services="Cp, Cpk, Pp, Ppk, within vs overall variation, normality testing, Box-Cox transformation, non-normal capability",
        steps=[
            ("Recap capability in full: Cp = (USL - LSL) / 6 sigma measures spread only; Cpk also accounts for centring and is always <= Cp.", ""),
            ("Recap the acceptance benchmarks: Cpk >= 1.33 capable, >= 1.67 for critical characteristics, and the relationship between Cpk and sigma level.", ""),
            ("Learn the distinction most practitioners get wrong: Cp/Cpk use WITHIN-subgroup (short-term) variation; Pp/Ppk use TOTAL (long-term) variation.", ""),
            ("Understand the consequence: reporting Cpk on an unstable process flatters it, because between-subgroup drift is excluded from the estimate.", ""),
            ("Establish the rule — the process must be STABLE before capability means anything. Check stability with a control chart first.", ""),
            ("Test your capstone Y for normality using Anderson-Darling or Shapiro-Wilk. Read the p-value: p < 0.05 rejects normality.", ""),
            ("Recognise that cycle time, waiting time and defect counts are routinely non-normal and usually right-skewed — this is expected, not an error.", ""),
            ("For non-normal data, choose your route: apply a Box-Cox or Johnson transformation, or fit the correct distribution (Weibull, lognormal, exponential) directly.", ""),
            ("Apply the transformation, re-test normality, then compute capability on the transformed scale — and report results in the ORIGINAL units.", ""),
            ("Calculate both Cpk and Ppk for your capstone Y and explain the gap between them. A large gap means the process drifts between subgroups.", ""),
            ("Record the baseline capability in your capstone pack alongside the Lab 3 sigma level.", ""),
        ],
        test="You have confirmed stability before computing capability, tested and documented normality with a p-value, handled non-normality by transformation or distribution fitting, and reported both Cpk and Ppk with an explanation of the gap.",
    ),
]
