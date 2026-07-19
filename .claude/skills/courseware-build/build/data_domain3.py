"""
Domain 3 — The ANALYZE phase at Black Belt depth. Labs 15-21.

Every lab advances the learner's OWN capstone project.

Recap in depth: variation, run charts, Pareto, fishbone, 5 Whys, hypothesis
testing, simple regression.
Black Belt only: multiple regression and model diagnostics, ANOVA and
interactions, non-parametric tests, multi-vari studies, chi-square.
"""

from data_domain1 import CAPSTONE_NOTE

DOMAIN3 = [
    dict(
        num=15, topic=3,
        title="Variation, Run Charts, Pareto and Stratification — In Depth",
        objective="Separate common from special cause variation and stratify your capstone data (A3).",
        desc="A full re-derivation of the foundation of all Six Sigma analysis: the distinction "
             "between common and special cause variation. Acting on common cause as if it were "
             "special (tampering) makes processes worse — this is the single most expensive "
             "mistake in process management. " + CAPSTONE_NOTE,
        build="A run chart with pattern analysis, a Pareto chart and a stratified defect analysis.",
        services="Common vs special cause, run chart patterns, tampering, Pareto principle, stratification, boxplots",
        steps=[
            ("Recap common versus special cause variation in full, with the management response each demands — process change versus local investigation.", ""),
            ("Understand tampering (Deming's funnel): adjusting a stable process in response to common-cause noise increases variation. Demonstrate it with the bead or funnel experiment.", ""),
            ("Plot your capstone Y as a run chart over time, with the median as the centre line.", ""),
            ("Recap and apply the six run chart patterns in full: trend, shift, cluster, mixture, oscillation and bias — with the run rules that detect each.", ""),
            ("Mark any special-cause signals and investigate what changed at that point in time. Special causes must be explained, not averaged away.", ""),
            ("Recap the Pareto principle and build a Pareto chart of defect categories for your capstone, with the cumulative percentage line.", ""),
            ("Identify the vital few categories accounting for roughly 80 percent of the impact. Weight by cost, not count, where defect costs differ materially.", ""),
            ("Now stratify. Re-draw the Pareto separately by plant, line, shift, operator, product family and supplier.", ""),
            ("Look for a stratification factor where the Pareto shape changes dramatically — that factor is a strong candidate X and tells you where to focus.", ""),
            ("Build boxplots of your Y across each stratification factor to compare medians, spread and outliers visually before testing statistically.", ""),
            ("Record your top three candidate Xs from stratification — these feed directly into the hypothesis tests in Lab 17.", ""),
        ],
        test="Your run chart is assessed against all six patterns, your Pareto is weighted appropriately, and stratification has produced at least three named candidate Xs for statistical testing.",
    ),
    dict(
        num=16, topic=3,
        title="Fishbone, 5 Whys and Cause Prioritisation — In Depth",
        objective="Generate and prioritise candidate root causes for your capstone (A3, K2).",
        desc="Re-derive cause-and-effect analysis in full — to the depth at which you can facilitate "
             "it for a Green Belt team, which is a core Black Belt accountability. The output is a "
             "prioritised, testable cause list, not an unmanageable wall of sticky notes. " + CAPSTONE_NOTE,
        build="A fishbone diagram, 5 Whys chains and a prioritised list of testable candidate causes.",
        services="Ishikawa 5M+E, brainstorming facilitation, 5 Whys, multi-voting, cause-and-effect matrix, hypothesis formulation",
        steps=[
            ("Recap brainstorming facilitation in full: divergence before convergence, no criticism during generation, and how to stop the highest-paid opinion from dominating.", ""),
            ("Recap the fishbone structure: the effect at the head, and 5M+E bones — Manpower, Method, Machine, Material, Measurement, Environment.", ""),
            ("Write your capstone problem statement precisely at the head of the fishbone. A vague effect produces vague causes.", ""),
            ("Facilitate the fishbone with your team, generating at least 25 candidate causes across all six bones. Thin bones signal blind spots, not absence of causes.", ""),
            ("Recap the 5 Whys and its discipline: continue until the answer is a process or system failure, never a person to blame.", ""),
            ("Apply 5 Whys to your top five fishbone causes. Note where a single chain branches — real causal chains are often trees, not lines.", ""),
            ("Recap multi-voting and apply it to reduce your cause list to the ten most plausible candidates.", ""),
            ("Build a cause-and-effect matrix: score each candidate cause against each CTQ, weighted by CTQ importance, to produce a ranked cause list.", ""),
            ("Filter the ranked list for TESTABILITY — for each cause, can you state a hypothesis and obtain data? An untestable cause cannot be proven in Analyze.", ""),
            ("Convert your top five testable causes into formal hypothesis statements ready for Lab 17.", ""),
            ("Note how you would coach a Green Belt team through this session, and the two facilitation mistakes you would watch for.", ""),
        ],
        test="Your fishbone carries 25+ causes across all six bones, 5 Whys chains terminate at process rather than person, and you have five testable causes written as formal hypotheses.",
    ),
    dict(
        num=17, topic=3,
        title="Hypothesis Testing — In Depth, With Test Selection",
        objective="Test your capstone's candidate causes with correctly selected hypothesis tests (A3, K2).",
        desc="A full re-derivation of hypothesis testing, including the test selection logic that "
             "Green Belts most often get wrong. You must be able to choose the right test, defend "
             "the choice, and explain the result in business language. " + CAPSTONE_NOTE,
        build="Completed hypothesis tests on your capstone's candidate causes with documented conclusions.",
        services="H0/Ha, alpha, beta, power, p-values, t-tests, paired t, F-test, proportion tests, test selection logic",
        steps=[
            ("Recap the logic of hypothesis testing in full: assume H0 (no difference), then ask how likely the observed data would be if H0 were true.", ""),
            ("Recap H0 and Ha formulation. H0 always contains the equality; Ha carries the claim you are trying to establish.", ""),
            ("Recap alpha, beta and power. Alpha is producer's risk (Type I, false alarm); beta is consumer's risk (Type II, missed signal); power = 1 - beta.", ""),
            ("Understand the practical consequence: an underpowered test that fails to reject H0 has proven nothing. Check power before concluding 'no difference'.", ""),
            ("Learn the test selection logic in full. Continuous Y: 1 sample vs target = 1-sample t; 2 independent groups = 2-sample t; paired = paired t; 3+ groups = ANOVA; variances = F-test or Levene.", ""),
            ("Learn the discrete-Y branch: 1 proportion = 1-proportion test; 2 proportions = 2-proportion test; categorical association = chi-square.", ""),
            ("Check the assumptions before every test: normality, independence and equal variance. A violated assumption invalidates the p-value entirely.", ""),
            ("Take your five candidate causes from Lab 16 and select the correct test for each. Write down the justification for each selection.", ""),
            ("State H0 and Ha for each test, set alpha (normally 0.05), and confirm you have adequate sample size and power.", ""),
            ("Run each test and record the p-value. Apply the decision rule: p < alpha rejects H0.", ""),
            ("Distinguish statistical from PRACTICAL significance. A p-value of 0.001 on a 0.2 percent improvement is real but worthless — always report effect size alongside p.", ""),
            ("Build your rejected-causes log so nobody re-litigates cleared causes in Improve, and record confirmed causes in your capstone pack.", ""),
        ],
        test="Every test has a documented selection justification and assumption check, results report effect size alongside the p-value, and you maintain both a confirmed-cause and a rejected-cause log.",
    ),
    dict(
        num=18, topic=3,
        title="Multiple Regression and Model Diagnostics (Black Belt Only)",
        objective="Build and validate a multiple regression model of your capstone Y (A3, K2).",
        desc="BLACK BELT ONLY — the Green Belt course teaches simple linear regression with one X. "
             "Real processes have several interacting Xs. Multiple regression models them together, "
             "but a model that fits is not yet a model that is valid, so the diagnostics matter as "
             "much as the coefficients. " + CAPSTONE_NOTE,
        build="A validated multiple regression model with full residual and multicollinearity diagnostics.",
        services="Multiple regression, coefficients, adjusted R-squared, residual analysis, multicollinearity/VIF, model selection, overfitting",
        steps=[
            ("Recap simple linear regression: the fitted line, slope interpretation, R-squared and the correlation-is-not-causation trap.", ""),
            ("Extend to multiple regression: Y = b0 + b1X1 + b2X2 + ... + e, where each coefficient is the effect of that X holding all other Xs constant.", ""),
            ("Understand why that 'holding constant' clause matters — it is what makes multiple regression fundamentally different from running several simple regressions.", ""),
            ("Assemble your capstone dataset with the Y and at least four candidate Xs, with enough rows (a common rule of thumb is 10-15 observations per X).", ""),
            ("Fit the full model and record the coefficients, their p-values, R-squared and adjusted R-squared.", ""),
            ("Use ADJUSTED R-squared, not R-squared, to compare models. Plain R-squared always rises when you add an X, even a random one.", ""),
            ("Check multicollinearity with Variance Inflation Factors. VIF > 5 is a concern, VIF > 10 is serious — correlated Xs make coefficients unstable and signs nonsensical.", ""),
            ("Resolve multicollinearity by dropping or combining redundant Xs, then refit.", ""),
            ("Run the residual diagnostics in full: residuals versus fitted values (should show no pattern), normal probability plot of residuals, and residuals versus order (independence).", ""),
            ("Interpret residual patterns: a funnel shape indicates non-constant variance, curvature indicates a missing quadratic term, and drift over order indicates autocorrelation.", ""),
            ("Reduce to the final model using backward elimination — drop the least significant X, refit, and repeat until all remaining Xs are significant.", ""),
            ("Guard against overfitting: hold back a validation subset, or use cross-validation, and confirm the model predicts data it has not seen.", ""),
            ("Translate the final model into business language: for each significant X, state what a one-unit change does to Y in customer or dollar terms.", ""),
        ],
        test="Your final model has all VIFs under 5, residual plots show no pattern, adjusted R-squared is reported, the model has been validated on held-out data, and each coefficient is stated in business terms.",
    ),
    dict(
        num=19, topic=3,
        title="ANOVA, Interactions and Non-Parametric Tests (Black Belt Only)",
        objective="Compare multiple groups using ANOVA and apply non-parametric alternatives (A3, K2).",
        desc="BLACK BELT ONLY. Comparing three or more groups with repeated t-tests inflates the "
             "false-positive rate badly — ANOVA solves this. Two-way ANOVA then reveals interaction "
             "effects that one-factor analysis cannot see. And when normality fails, non-parametric "
             "tests are the correct answer rather than proceeding regardless. " + CAPSTONE_NOTE,
        build="One-way and two-way ANOVA on your capstone data plus a non-parametric confirmation.",
        services="One-way ANOVA, F-statistic, post-hoc Tukey, two-way ANOVA, interaction effects, Mann-Whitney, Kruskal-Wallis, Mood's median",
        steps=[
            ("Understand alpha inflation: comparing 4 groups pairwise needs 6 t-tests, and at alpha = 0.05 the family-wise false-positive risk rises to about 26 percent.", ""),
            ("Recap one-way ANOVA: it partitions total variation into between-group and within-group components, and the F-statistic is their ratio.", ""),
            ("State the ANOVA hypotheses: H0 is that all group means are equal; Ha is that at least one differs — ANOVA does not tell you which.", ""),
            ("Check the ANOVA assumptions: normality of residuals, independence, and equal variances (test with Levene's or Bartlett's).", ""),
            ("Run one-way ANOVA on a capstone factor with 3+ levels — plant, line, shift, product family or supplier.", ""),
            ("If ANOVA is significant, run a post-hoc Tukey HSD to identify WHICH pairs differ, with the family-wise error rate controlled.", ""),
            ("Extend to two-way ANOVA with two factors at once — for example plant AND shift on your capstone Y.", ""),
            ("Read the interaction term. A significant interaction means the effect of one factor DEPENDS on the level of the other — for instance night shift hurts Suzhou but not Singapore.", ""),
            ("Plot the interaction. Non-parallel lines indicate interaction; crossing lines indicate a strong one that invalidates any single-factor conclusion.", ""),
            ("Understand why this matters for Improve: with a significant interaction, a fix that works at one plant may fail or backfire at another.", ""),
            ("Now the non-parametric branch. When normality fails and transformation does not fix it, switch tests rather than ignoring the violation.", ""),
            ("Map each test to its non-parametric equivalent: 2-sample t -> Mann-Whitney; one-way ANOVA -> Kruskal-Wallis; paired t -> Wilcoxon signed-rank; and Mood's median for heavy outliers.", ""),
            ("Re-run one of your significant findings using its non-parametric equivalent. Agreement across both strengthens your Day 5 defence considerably.", ""),
        ],
        test="Your ANOVA assumptions are tested and documented, significant results carry a post-hoc analysis, you have interpreted an interaction plot, and at least one finding is confirmed non-parametrically.",
    ),
    dict(
        num=20, topic=3,
        title="Multi-Vari Studies and Chi-Square Analysis (Black Belt Only)",
        objective="Decompose variation by family using a multi-vari study and test categorical association (A3, K2).",
        desc="BLACK BELT ONLY. Before spending money hunting a root cause, find out WHERE the "
             "variation actually lives. A multi-vari study separates positional, cyclical and "
             "temporal variation — and frequently reveals that the team has been investigating "
             "entirely the wrong family. " + CAPSTONE_NOTE,
        build="A multi-vari chart decomposing your capstone variation plus a chi-square association test.",
        services="Multi-vari studies, positional/cyclical/temporal families, variation decomposition, chi-square, contingency tables, expected frequencies",
        steps=[
            ("Understand the three variation families. POSITIONAL: within a single unit or across positions in a machine. CYCLICAL: unit to unit, batch to batch. TEMPORAL: shift to shift, day to day.", ""),
            ("Understand the payoff: if 70 percent of variation is positional, then investigating shift patterns is wasted effort no matter how thorough the investigation.", ""),
            ("Design a multi-vari sampling plan for your capstone: sample multiple positions within units, consecutive units, and repeat across time periods.", ""),
            ("Ensure the sampling captures all three families simultaneously — this is a nested sampling design, not three separate studies.", ""),
            ("Collect the data and plot the multi-vari chart, with positional variation innermost and temporal outermost.", ""),
            ("Read the chart: the family showing the largest vertical spread dominates. That is where your root cause investigation should concentrate.", ""),
            ("Quantify the contribution of each family as a percentage of total variation using variance components.", ""),
            ("Re-prioritise your candidate cause list from Lab 16 against the dominant variation family, and drop causes that belong to a family contributing little.", ""),
            ("Now chi-square. Build a contingency table of two categorical variables from your capstone — defect type against shift, supplier or line.", ""),
            ("Calculate expected frequencies under independence: expected = (row total x column total) / grand total.", ""),
            ("Check the validity condition: all expected frequencies should be 5 or more, or the chi-square approximation breaks down and categories must be combined.", ""),
            ("Compute the chi-square statistic and its p-value, and conclude whether defect type is associated with your categorical factor.", ""),
            ("Translate a significant association into a testable process hypothesis — association is not causation, but it does tell you where to look.", ""),
        ],
        test="Your multi-vari chart captures all three families with quantified variance contributions, your cause list is re-prioritised against the dominant family, and your chi-square satisfies the expected-frequency condition.",
    ),
    dict(
        num=21, topic=3,
        title="Analyze Tollgate — Proving Root Cause and Telling the Data Story",
        objective="Consolidate your analysis into a defensible root cause conclusion (A3, K1).",
        desc="The Analyze tollgate. Consolidate everything from Labs 15-20 into a proven root cause "
             "set, translate the statistics into business language, and rehearse the challenges you "
             "will face. Sponsors do not fund p-values; they fund decisions. " + CAPSTONE_NOTE,
        build="An Analyze tollgate pack with proven root causes, evidence and a business-language summary.",
        services="Evidence consolidation, root cause validation, statistical-to-business translation, tollgate review, challenge preparation",
        steps=[
            ("Assemble every analytical result from Labs 15-20: stratification, hypothesis tests, regression model, ANOVA, multi-vari and chi-square.", ""),
            ("For each candidate cause, record the verdict — PROVEN (statistically supported), REJECTED (tested and cleared) or UNTESTED (no data available).", ""),
            ("Apply the triangulation rule: a root cause is strongest when supported by more than one independent method — for instance stratification plus a hypothesis test plus a regression coefficient.", ""),
            ("Check each proven cause for practical significance. Quantify how much of the Y gap each explains, in percent and in dollars.", ""),
            ("Rank your proven causes by the size of their contribution to the Y gap.", ""),
            ("Confirm your causes are ACTIONABLE — a proven cause you cannot influence belongs in the risk register, not the improvement plan.", ""),
            ("Translate each finding into one business sentence: 'Night shift at Suzhou runs 2.3 percentage points lower first-pass yield, costing about $180k annually.'", ""),
            ("Build the tollgate pack: baseline, analysis method, proven causes, rejected causes, quantified impact and the recommendation to proceed.", ""),
            ("Rehearse the challenges you should expect: was the sample adequate, were assumptions checked, could a confounding variable explain this, is the measurement system valid?", ""),
            ("Prepare your evidence for each challenge — this is exactly what the Day 5 steering committee will probe.", ""),
            ("Present the tollgate to a peer group and capture their challenges, then strengthen any weak points before Day 4.", ""),
        ],
        test="Every candidate cause carries a verdict, proven causes are triangulated across multiple methods and quantified in dollars, and you have rehearsed a prepared response to each expected challenge.",
    ),
]
