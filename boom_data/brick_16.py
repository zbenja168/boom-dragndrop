BRICK = {
    "brick_num": 16,
    "brick_title": "Proteins, Enzymatic Machines and Introduction to Protein-based Disorders II",
    "games": [
        {
            "slug": "glucose_phosphorylating_kinetics",
            "title": "Hexokinase vs. Glucokinase Kinetics",
            "subtitle": "Match each glucose-handling protein to its Km, tissue, and physiological role",
            "categories": ["Km (glucose affinity)", "Tissue / Location", "Physiological Role"],
            "data": {
                "Hexokinase": {
                    "Km (glucose affinity)": "Low Km, high affinity for glucose",
                    "Tissue / Location": "Neurons, RBCs, most tissues",
                    "Physiological Role": "Makes G6P even when blood glucose is low; low Vmax prevents overaccumulation"
                },
                "Glucokinase (hexokinase IV)": {
                    "Km (glucose affinity)": "High Km, low affinity for glucose",
                    "Tissue / Location": "Liver and pancreas",
                    "Physiological Role": "Phosphorylates glucose only when abundant; spares blood glucose during fasting"
                },
                "Low-Km GLUT transporter": {
                    "Km (glucose affinity)": "Very low Km glucose transporter",
                    "Tissue / Location": "Neurons and RBCs",
                    "Physiological Role": "Brings glucose into the cell even when circulating levels are low"
                },
                "High-Km GLUT transporter": {
                    "Km (glucose affinity)": "High Km glucose transporter",
                    "Tissue / Location": "Liver and pancreas",
                    "Physiological Role": "Admits glucose into the cell only when glucose is abundant"
                }
            }
        },
        {
            "slug": "enzyme_inhibitor_types",
            "title": "Classifying Enzyme Inhibitors",
            "subtitle": "Match each inhibitor class to its binding behavior and effect on Km and Vmax",
            "categories": ["Binding Characteristics", "Effect on Km", "Effect on Vmax"],
            "data": {
                "Reversible competitive": {
                    "Binding Characteristics": "Binds active site noncovalently; resembles substrate; removed by dilution",
                    "Effect on Km": "Increases apparent Km",
                    "Effect on Vmax": "Vmax unchanged (overcome by excess substrate)"
                },
                "Irreversible (suicide)": {
                    "Binding Characteristics": "Binds active site covalently; not removed by dilution",
                    "Effect on Km": "Km unchanged",
                    "Effect on Vmax": "Decreases Vmax"
                },
                "Noncompetitive": {
                    "Binding Characteristics": "Binds allosteric site reversibly; unlike the substrate",
                    "Effect on Km": "Km unchanged",
                    "Effect on Vmax": "Decreases Vmax"
                },
                "Uncompetitive": {
                    "Binding Characteristics": "Binds allosteric site only after substrate is already bound",
                    "Effect on Km": "Decreases Km",
                    "Effect on Vmax": "Decreases Vmax"
                }
            }
        },
        {
            "slug": "detoxification_enzymes",
            "title": "Phase I and Phase II Detoxification Enzymes",
            "subtitle": "Match each hepatic enzyme to its detox phase, reaction, and clinical relevance",
            "categories": ["Detox Phase", "Reaction / Group Added", "Clinical Relevance"],
            "data": {
                "CYP2E1": {
                    "Detox Phase": "Phase I",
                    "Reaction / Group Added": "Oxidation; part of microsomal ethanol oxidizing system (MEOS)",
                    "Clinical Relevance": "High Km for ethanol (~10 mM); induced by alcohol; generates toxic NAPQI and ROS"
                },
                "CYP3A4": {
                    "Detox Phase": "Phase I",
                    "Reaction / Group Added": "Oxidation / hydroxylation of lipophilic drugs",
                    "Clinical Relevance": "Metabolizes ~1/3 of CYP drugs; inhibited by grapefruit, induced by St. John's Wort"
                },
                "Glutathione S-transferase": {
                    "Detox Phase": "Phase II",
                    "Reaction / Group Added": "Conjugates glutathione (GSH, a polar tripeptide)",
                    "Clinical Relevance": "Neutralizes NAPQI; GSH depletion worsens oxidative balance and toxicity"
                },
                "UDP-glucuronosyltransferase": {
                    "Detox Phase": "Phase II",
                    "Reaction / Group Added": "Conjugates glucuronate (an acidic sugar)",
                    "Clinical Relevance": "Conjugates bilirubin for excretion; deficiency causes jaundice"
                },
                "Sulfotransferase": {
                    "Detox Phase": "Phase II",
                    "Reaction / Group Added": "Conjugates sulfate (highly polar oxidized sulfur)",
                    "Clinical Relevance": "Normal route for acetaminophen; increases water solubility for excretion"
                }
            }
        },
        {
            "slug": "acetaminophen_toxicity",
            "title": "Acetaminophen Toxicity Pathway",
            "subtitle": "Match each player to its role in acetaminophen metabolism and its outcome",
            "categories": ["Identity / Role", "Mechanism", "Outcome"],
            "data": {
                "NAPQI": {
                    "Identity / Role": "Cytotoxic intermediate produced by CYP2E1",
                    "Mechanism": "Covalently binds cysteines in cellular proteins once GSH is saturated",
                    "Outcome": "Hepatocellular damage and elevated liver enzymes"
                },
                "Glutathione (GSH)": {
                    "Identity / Role": "Protective tripeptide (glutamate-cysteine-glycine)",
                    "Mechanism": "Added to NAPQI by glutathione S-transferase via a sulfide link",
                    "Outcome": "Forms mercapturic acid excreted in urine; depletion worsens toxicity"
                },
                "N-acetylcysteine": {
                    "Identity / Role": "Antidote for acetaminophen overdose",
                    "Mechanism": "Rapidly replenishes intracellular GSH stores",
                    "Outcome": "Counteracts NAPQI accumulation and prevents cell damage"
                },
                "Ethanol": {
                    "Identity / Role": "CYP2E1 inducer",
                    "Mechanism": "Increases CYP2E1 expression, shunting acetaminophen to the toxic pathway",
                    "Outcome": "Potentiates hepatotoxicity from acetaminophen"
                },
                "Glucuronidation / sulfation": {
                    "Identity / Role": "Normal phase II conjugation route",
                    "Mechanism": "Adds glucuronate or sulfate to acetaminophen to raise polarity",
                    "Outcome": "Non-toxic, water-soluble product cleared by kidney and urine"
                }
            }
        }
    ]
}
