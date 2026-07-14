BRICK = {
    "brick_num": 3,
    "brick_title": "Metabolic Overview II: OXPHOS",
    "games": [
        {
            "slug": "pathway_locale_io",
            "title": "Central Metabolic Pathways: Locale, Substrate & Product",
            "subtitle": "Match each pathway to its cellular locale, its substrate(s), and its product(s)",
            "categories": ["Cellular Locale", "Substrate(s)", "General Product(s)"],
            "data": {
                "Glycolysis": {
                    "Cellular Locale": "Cytoplasm (cytosol)",
                    "Substrate(s)": "Glucose and NAD+",
                    "General Product(s)": "Pyruvate, ATP, NADH (lactate if anaerobic)"
                },
                "Pentose Phosphate Pathway": {
                    "Cellular Locale": "Cytoplasm (cytosol)",
                    "Substrate(s)": "Glycolytic intermediates (e.g. glucose 6-phosphate)",
                    "General Product(s)": "NADPH and ribose 5-phosphate"
                },
                "Gluconeogenesis": {
                    "Cellular Locale": "Mostly cytosol, plus mitochondria and ER of liver/kidney",
                    "Substrate(s)": "Pyruvate from alanine or lactate, and glycerol",
                    "General Product(s)": "Glucose"
                },
                "Beta-oxidation": {
                    "Cellular Locale": "Mitochondrial matrix (peroxisome for very-long-chain fatty acids)",
                    "Substrate(s)": "Fatty acids",
                    "General Product(s)": "Acetyl-CoA, NADH, FADH2"
                },
                "TCA cycle": {
                    "Cellular Locale": "Mitochondrial matrix",
                    "Substrate(s)": "Acetyl-CoA, NAD+, FAD",
                    "General Product(s)": "NADH, FADH2, ATP"
                },
                "ETC / OXPHOS": {
                    "Cellular Locale": "Mitochondrial inner membrane and intermembrane space",
                    "Substrate(s)": "O2, NADH, FADH2",
                    "General Product(s)": "ATP and water (heat if uncoupled)"
                }
            }
        },
        {
            "slug": "mito_anatomy",
            "title": "Anatomy of the Mitochondrion",
            "subtitle": "Match each mitochondrial compartment to its description and its key function",
            "categories": ["Description", "Key Function"],
            "data": {
                "Outer membrane": {
                    "Description": "Outermost boundary of the double-membrane organelle",
                    "Key Function": "Separates the cytosol from the intermembrane space"
                },
                "Intermembrane space": {
                    "Description": "Compartment between the outer and inner membranes",
                    "Key Function": "Accumulates protons pumped by the ETC, giving it a lower pH than the matrix"
                },
                "Inner membrane": {
                    "Description": "Membrane enclosing the matrix, folded into cristae",
                    "Key Function": "Houses the ETC complexes and ATP synthase"
                },
                "Matrix": {
                    "Description": "Lumen surrounded by the inner membrane",
                    "Key Function": "Site of the TCA cycle, beta-oxidation, and ketogenesis"
                },
                "Cristae": {
                    "Description": "Long invaginations of the inner membrane that protrude into the matrix",
                    "Key Function": "Maximize surface-area-to-volume ratio to augment ATP production"
                }
            }
        },
        {
            "slug": "etc_electron_flow",
            "title": "Electron Transport Chain: Following the Electrons",
            "subtitle": "Match each ETC component to its type, where it receives electrons from, and where it passes them",
            "categories": ["Molecule Type", "Receives Electrons From", "Passes Electrons To"],
            "data": {
                "Complex I": {
                    "Molecule Type": "ETC protein complex in the inner membrane (NADH entry point)",
                    "Receives Electrons From": "NADH",
                    "Passes Electrons To": "Coenzyme Q"
                },
                "Complex II": {
                    "Molecule Type": "ETC protein complex in the inner membrane (FADH2 entry point)",
                    "Receives Electrons From": "FADH2",
                    "Passes Electrons To": "Coenzyme Q"
                },
                "Coenzyme Q (ubiquinone)": {
                    "Molecule Type": "Lipid-soluble mobile electron shuttle",
                    "Receives Electrons From": "Complex I and Complex II",
                    "Passes Electrons To": "Complex III"
                },
                "Complex III": {
                    "Molecule Type": "ETC protein complex in the inner membrane",
                    "Receives Electrons From": "Coenzyme Q",
                    "Passes Electrons To": "Cytochrome c"
                },
                "Cytochrome c": {
                    "Molecule Type": "Mobile electron-carrier shuttle",
                    "Receives Electrons From": "Complex III",
                    "Passes Electrons To": "Complex IV"
                },
                "Complex IV": {
                    "Molecule Type": "Terminal ETC complex that reduces oxygen",
                    "Receives Electrons From": "Cytochrome c",
                    "Passes Electrons To": "O2 (terminal electron acceptor)"
                }
            }
        },
        {
            "slug": "pathway_regulation",
            "title": "Regulation of Central Metabolic Pathways",
            "subtitle": "Match each pathway to its function, what inhibits it, and what stimulates it",
            "categories": ["Primary Function", "Inhibited By", "Stimulated By"],
            "data": {
                "Glycolysis": {
                    "Primary Function": "Generate pyruvate and some ATP",
                    "Inhibited By": "Glucagon, alanine, and a high ATP/ADP ratio",
                    "Stimulated By": "Insulin and AMP"
                },
                "Gluconeogenesis": {
                    "Primary Function": "Make glucose from non-carbohydrate precursors while fasting",
                    "Inhibited By": "Insulin",
                    "Stimulated By": "Glucagon"
                },
                "Pentose Phosphate Pathway": {
                    "Primary Function": "Produce NADPH and ribose 5-phosphate",
                    "Inhibited By": "A high NADPH/NADP+ ratio",
                    "Stimulated By": "Demand for NADPH (a low NADPH/NADP+ ratio)"
                },
                "Beta-oxidation": {
                    "Primary Function": "Generate acetyl-CoA from fatty acids",
                    "Inhibited By": "High NADH/NAD+ and high acetyl-CoA/CoA ratios",
                    "Stimulated By": "Fasting (a low cellular energy charge)"
                },
                "TCA cycle": {
                    "Primary Function": "Oxidize acetyl-CoA to reduced coenzymes",
                    "Inhibited By": "A high NADH/NAD+ ratio",
                    "Stimulated By": "A low energy charge (rising ADP)"
                },
                "ETC / OXPHOS": {
                    "Primary Function": "Produce ATP from reduced coenzyme electron carriers",
                    "Inhibited By": "A high ATP/ADP ratio",
                    "Stimulated By": "A high ADP level (low ATP)"
                }
            }
        }
    ]
}
