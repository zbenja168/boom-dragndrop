BRICK = {
    "brick_num": 1,
    "brick_title": "Metabolic Overview I: General Reactions",
    "games": [
        {
            "slug": "catabolism_vs_anabolism",
            "title": "Catabolism vs. Anabolism",
            "subtitle": "Match each metabolic process to its direction, energy relationship, and key transformation",
            "categories": ["Direction", "Net Energy", "Key Transformation"],
            "data": {
                "Ribosomal protein synthesis": {
                    "Direction": "Anabolic",
                    "Net Energy": "Consumes ATP (major cellular ATP expenditure)",
                    "Key Transformation": "Amino acids joined by peptide bonds into a protein"
                },
                "Proteolysis to amino acids": {
                    "Direction": "Catabolic",
                    "Net Energy": "Releases energy",
                    "Key Transformation": "Protein cleaved into peptides and single amino acids"
                },
                "Glycogenesis": {
                    "Direction": "Anabolic",
                    "Net Energy": "Stores energy (consumes ATP)",
                    "Key Transformation": "Glucose polymerized into glycogen for later use"
                },
                "Glycogenolysis": {
                    "Direction": "Catabolic",
                    "Net Energy": "Mobilizes stored fuel",
                    "Key Transformation": "Glycogen degraded to glucose to maintain blood glucose"
                },
                "Glycolysis": {
                    "Direction": "Catabolic",
                    "Net Energy": "Yields ATP and NADH",
                    "Key Transformation": "Glucose oxidatively broken down to pyruvate"
                },
                "Lipogenesis (fatty acid synthesis)": {
                    "Direction": "Anabolic",
                    "Net Energy": "Requires NADPH reducing power",
                    "Key Transformation": "Carbon chain elongated and reduced into fatty acid"
                }
            }
        },
        {
            "slug": "oxidation_vs_reduction",
            "title": "Oxidation vs. Reduction",
            "subtitle": "Match each reaction to its redox classification, structural change, and coenzyme change",
            "categories": ["Redox Classification", "Structural Change", "Coenzyme Change"],
            "data": {
                "Retinol to retinaldehyde (ADH)": {
                    "Redox Classification": "Oxidation",
                    "Structural Change": "Alcohol (CH2OH) loses bonds to hydrogen to form aldehyde (CHO)",
                    "Coenzyme Change": "NAD+ reduced to NADH"
                },
                "Retinaldehyde to retinoic acid (ALDH)": {
                    "Redox Classification": "Oxidation",
                    "Structural Change": "Aldehyde (CHO) gains a bond to oxygen to form acid (COOH)",
                    "Coenzyme Change": "NAD+ reduced to NADH"
                },
                "Glucose to pyruvate": {
                    "Redox Classification": "Oxidation",
                    "Structural Change": "Glucose carbons lose bonds to hydrogen",
                    "Coenzyme Change": "NAD+ reduced to NADH"
                },
                "Fatty acid chain elongation": {
                    "Redox Classification": "Reduction",
                    "Structural Change": "Growing carbon chain gains bonds to hydrogen",
                    "Coenzyme Change": "NADPH oxidized to NADP+"
                },
                "Oxygen to water in the ETC": {
                    "Redox Classification": "Reduction",
                    "Structural Change": "O2 gains bonds to hydrogen to become H2O",
                    "Coenzyme Change": "Accepts electrons as terminal electron acceptor"
                }
            }
        },
        {
            "slug": "fed_fasting_states",
            "title": "Fed, Fasting, and Starvation States",
            "subtitle": "Match each metabolic state to its dominant hormone, predominant pathway, and typical timing",
            "categories": ["Dominant Hormone", "Predominant Pathway", "Typical Timing"],
            "data": {
                "Fed (absorptive) state": {
                    "Dominant Hormone": "Insulin",
                    "Predominant Pathway": "Glycogenesis in liver and skeletal muscle",
                    "Typical Timing": "About 3-4 hours after eating"
                },
                "Sustained glucose excess": {
                    "Dominant Hormone": "Insulin",
                    "Predominant Pathway": "Lipogenesis (glucose converted to lipids)",
                    "Typical Timing": "When glucose stays abundant and sufficient"
                },
                "Fasting (postabsorptive) state": {
                    "Dominant Hormone": "Glucagon",
                    "Predominant Pathway": "Glycogenolysis to maintain blood glucose",
                    "Typical Timing": "More than 4 hours (e.g., overnight)"
                },
                "Starvation (prolonged fasting)": {
                    "Dominant Hormone": "Glucagon",
                    "Predominant Pathway": "Gluconeogenesis with fatty acid oxidation and amino acid catabolism",
                    "Typical Timing": "2-4 days without food intake"
                }
            }
        },
        {
            "slug": "oxygen_and_atp",
            "title": "Oxygen and ATP Production",
            "subtitle": "Match each scenario to its key mechanism, effect on ATP, and clinical correlate",
            "categories": ["Key Mechanism", "Effect on ATP Production", "Clinical or Functional Note"],
            "data": {
                "Electron transport chain": {
                    "Key Mechanism": "O2 is the terminal electron acceptor, reduced to water",
                    "Effect on ATP Production": "Sustains the proton gradient that drives ATP synthase",
                    "Clinical or Functional Note": "ATP production ceases without oxygen present"
                },
                "Anemia": {
                    "Key Mechanism": "Low hematocrit lowers oxygen-carrying capacity",
                    "Effect on ATP Production": "Decreased tissue ATP from limited O2 substrate",
                    "Clinical or Functional Note": "Fatigue, exhaustion, and dyspnea on exertion"
                },
                "Diabetic foot ulcer": {
                    "Key Mechanism": "Hyperglycemia glycates vessels and impairs perfusion",
                    "Effect on ATP Production": "Reduced peripheral O2 hinders ATP for healing",
                    "Clinical or Functional Note": "Poor wound closure; candidate for HBOT"
                },
                "Hyperbaric oxygen therapy": {
                    "Key Mechanism": "Delivers ~100% oxygen, far above atmospheric ~21%",
                    "Effect on ATP Production": "Restores O2 substrate to boost ATP",
                    "Clinical or Functional Note": "Used for burns, necrotizing infection, decompression sickness"
                },
                "Nucleotide catabolism": {
                    "Key Mechanism": "Oxidatively degraded but not coupled to the ETC",
                    "Effect on ATP Production": "Yields no ATP",
                    "Clinical or Functional Note": "Only major biomolecule class that does not produce ATP"
                }
            }
        }
    ]
}
