BRICK = {
    "brick_num": 23,
    "brick_title": "Lipids and Lipid Metabolism: Cholesterol Synthesis and Ketone Bodies",
    "games": [
        {
            "slug": "cholesterol_synthesis",
            "title": "Cholesterol Synthesis Pathway",
            "subtitle": "Match each molecule or enzyme to its role, cellular detail, and clinical relevance",
            "categories": ["Step / Role", "Cellular Detail", "Clinical Relevance"],
            "data": {
                "Acetyl-CoA": {
                    "Step / Role": "Starting substrate; three combine to build HMG-CoA",
                    "Cellular Detail": "Cytoplasmic pool feeds sterol synthesis",
                    "Clinical Relevance": "Shared early precursor with ketone body formation"
                },
                "HMG-CoA reductase": {
                    "Step / Role": "Reduces HMG-CoA to mevalonate (rate-limiting step)",
                    "Cellular Detail": "Consumes NADPH; activity peaks overnight",
                    "Clinical Relevance": "Competitively inhibited by statin drugs"
                },
                "Mevalonate": {
                    "Step / Role": "Product of the rate-limiting reduction",
                    "Cellular Detail": "Committed intermediate toward sterols",
                    "Clinical Relevance": "Its formation is blocked when statins act"
                },
                "Squalene": {
                    "Step / Role": "30-carbon linear precursor to cholesterol",
                    "Cellular Detail": "Cyclized into the fused four-ring sterol",
                    "Clinical Relevance": "Immediate precursor of cholesterol"
                },
                "Cholesterol": {
                    "Step / Role": "Final product of the synthetic pathway",
                    "Cellular Detail": "Made mainly by liver and intestine (~80%)",
                    "Clinical Relevance": "Precursor of steroid hormones, bile acids, vitamin D"
                }
            }
        },
        {
            "slug": "statin_effects",
            "title": "Statins and HMG-CoA Reductase",
            "subtitle": "Match each statin-related phenomenon to its mechanism and clinical consequence",
            "categories": ["What Happens", "Underlying Mechanism", "Clinical Consequence"],
            "data": {
                "HMG-CoA reductase inhibition": {
                    "What Happens": "Hepatic cholesterol synthesis falls",
                    "Underlying Mechanism": "Statin competitively blocks the enzyme",
                    "Clinical Consequence": "Less driver of atherosclerotic plaque"
                },
                "Upregulated hepatic LDL receptors": {
                    "What Happens": "Liver pulls cholesterol from the blood",
                    "Underlying Mechanism": "Hepatocytes raise surface LDL-receptor expression",
                    "Clinical Consequence": "Lowers plasma LDL levels"
                },
                "Elevated ALT and AST": {
                    "What Happens": "Liver biomarkers rise during therapy",
                    "Underlying Mechanism": "Hepatocellular effect of the drug",
                    "Clinical Consequence": "Liver enzymes are monitored on statins"
                },
                "Statin-associated myalgia": {
                    "What Happens": "Patients develop muscle aches",
                    "Underlying Mechanism": "Suboptimal coenzyme Q (ubiquinone) in muscle",
                    "Clinical Consequence": "CoQ supplements tried but evidence is lacking"
                },
                "Diurnal enzyme rhythm": {
                    "What Happens": "Reductase activity peaks at night",
                    "Underlying Mechanism": "Circadian regulation during overnight fasting",
                    "Clinical Consequence": "Rationale for evening statin dosing"
                }
            }
        },
        {
            "slug": "ketone_enzymes",
            "title": "Enzymes of Ketone Body Metabolism",
            "subtitle": "Match each enzyme to the reaction it catalyzes, its properties, and a key point",
            "categories": ["Reaction Catalyzed", "Property / Location", "Key Point"],
            "data": {
                "Thiolase": {
                    "Reaction Catalyzed": "Joins two acetyl-CoA into acetoacetyl-CoA",
                    "Property / Location": "Reversible; also the last step of beta-oxidation",
                    "Key Point": "Used in both ketone synthesis and ketolysis"
                },
                "HMG-CoA synthase": {
                    "Reaction Catalyzed": "Adds acetyl-CoA to make HMG-CoA",
                    "Property / Location": "Irreversible; liver mitochondrial matrix",
                    "Key Point": "Only expressed appreciably in the liver"
                },
                "HMG-CoA lyase": {
                    "Reaction Catalyzed": "Cleaves HMG-CoA to acetoacetate",
                    "Property / Location": "Irreversible synthesis step",
                    "Key Point": "Yields the first usable ketone body"
                },
                "3-hydroxybutyrate dehydrogenase": {
                    "Reaction Catalyzed": "Interconverts acetoacetate and beta-hydroxybutyrate",
                    "Property / Location": "Reversible; driven by NADH level",
                    "Key Point": "High fasting NADH favors beta-hydroxybutyrate"
                },
                "beta-ketoacyl-CoA transferase": {
                    "Reaction Catalyzed": "Converts acetoacetate to acetoacetyl-CoA",
                    "Property / Location": "Ketolysis step in peripheral tissues",
                    "Key Point": "Absent in liver, preventing a futile cycle"
                }
            }
        },
        {
            "slug": "ketosis_states",
            "title": "Differentiating Ketotic States",
            "subtitle": "Match each condition to its trigger, mechanism, and distinguishing feature",
            "categories": ["Primary Trigger", "Key Mechanism", "Distinguishing Feature"],
            "data": {
                "Prolonged fasting / starvation": {
                    "Primary Trigger": "Glucose deprivation after glycogen depletion",
                    "Key Mechanism": "Glucagon-driven beta-oxidation floods acetyl-CoA",
                    "Distinguishing Feature": "Physiologic, glucose-sparing, not harmful"
                },
                "Overnight fast": {
                    "Primary Trigger": "Brief fast during sleep",
                    "Key Mechanism": "Low-level ketogenesis supplies muscle fuel",
                    "Distinguishing Feature": "Ketones used by cardiac and skeletal muscle"
                },
                "Alcoholic ketoacidosis": {
                    "Primary Trigger": "Chronic alcohol with malnutrition",
                    "Key Mechanism": "High NADH:NAD+ shunts pyruvate to lactate",
                    "Distinguishing Feature": "Hypoglycemia with combined lactic and ketoacidosis"
                },
                "Diabetic ketoacidosis (DKA)": {
                    "Primary Trigger": "Insulin insufficiency",
                    "Key Mechanism": "Perceived starvation despite high plasma glucose",
                    "Distinguishing Feature": "Most common in type 1 diabetes"
                }
            }
        }
    ]
}
