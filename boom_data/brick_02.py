BRICK = {
    "brick_num": 2,
    "brick_title": "Metabolic Overview I: General Reactions (2 of 2)",
    "games": [
        {
            "slug": "atp_generation_pathways",
            "title": "ATP Generation Pathways",
            "subtitle": "Match each pathway to its oxygen requirement, location, and key mechanism",
            "categories": ["Oxygen Requirement", "Cellular Location", "Key Mechanism"],
            "data": {
                "Substrate Level Phosphorylation": {
                    "Oxygen Requirement": "Not required (anaerobic)",
                    "Cellular Location": "Cytoplasm (glycolysis) and one TCA step in mitochondria",
                    "Key Mechanism": "Direct transfer of a phosphoryl group from a donor onto ADP via a kinase"
                },
                "Oxidative Phosphorylation (OXPHOS)": {
                    "Oxygen Requirement": "Completely reliant on oxygen",
                    "Cellular Location": "Mitochondria only",
                    "Key Mechanism": "Proton gradient dissipation coupled to ATP synthase, using the ETC"
                },
                "Glycolysis": {
                    "Oxygen Requirement": "Not required",
                    "Cellular Location": "Cytoplasm",
                    "Key Mechanism": "Oxidizes glucose using substrate level phosphorylation; dependent on NAD+"
                },
                "Lactate Dehydrogenase Reaction": {
                    "Oxygen Requirement": "Favored when oxygen is limited",
                    "Cellular Location": "Cytoplasm",
                    "Key Mechanism": "Reduces pyruvate to lactate while oxidizing NADH to NAD+; produces no ATP"
                }
            }
        },
        {
            "slug": "causes_of_lactic_acidosis",
            "title": "Causes of Lactate Production",
            "subtitle": "Match each cause to its underlying defect, classic setting, and metabolic consequence",
            "categories": ["Underlying Defect", "Classic Setting or Enzyme", "Metabolic Consequence"],
            "data": {
                "Oxygen Depletion": {
                    "Underlying Defect": "OXPHOS diminishes; NADH cannot pass electrons to the ETC",
                    "Classic Setting or Enzyme": "Hypoxia or ischemia with limited O2",
                    "Metabolic Consequence": "NAD+ regenerated via LDH to sustain glycolytic substrate level phosphorylation"
                },
                "Lack of Mitochondria": {
                    "Underlying Defect": "No organelles available for oxidative phosphorylation",
                    "Classic Setting or Enzyme": "Mature red blood cell (erythrocyte)",
                    "Metabolic Consequence": "ATP relies solely on glycolysis and lactate production; cells enriched with LDH"
                },
                "Excess Pyruvate Substrate": {
                    "Underlying Defect": "Substrate abundance shifts the reversible LDH equilibrium",
                    "Classic Setting or Enzyme": "Metabolic overproduction or underusage of pyruvate",
                    "Metabolic Consequence": "Augmented pyruvate is shunted to lactate"
                },
                "Pyruvate Dehydrogenase Deficiency": {
                    "Underlying Defect": "Pyruvate cannot be converted into acetyl-CoA",
                    "Classic Setting or Enzyme": "Enzyme deficiency blocking entry into the TCA cycle",
                    "Metabolic Consequence": "Energy decrement plus lactic acidosis from pyruvate underutilization"
                },
                "Von Gierke's Disease": {
                    "Underlying Defect": "Glucose 6-phosphatase deficiency in the liver (Type I GSD)",
                    "Classic Setting or Enzyme": "Glucose 6-phosphate from glycogenolysis cannot become free glucose",
                    "Metabolic Consequence": "Buildup of glucose 6-phosphate yields excess pyruvate culminating in lactate"
                }
            }
        },
        {
            "slug": "acute_malnutrition_states",
            "title": "Acute Malnutrition States",
            "subtitle": "Match each malnutrition state to its deficiency, hallmark finding, and mechanism",
            "categories": ["Primary Deficiency", "Hallmark Finding", "Key Mechanism"],
            "data": {
                "Marasmus": {
                    "Primary Deficiency": "Total calories deficient across fat, carbohydrate, and protein",
                    "Hallmark Finding": "Broomstick extremities, loss of subcutaneous fat; appears as skin and bones",
                    "Key Mechanism": "Muscle and fat are oxidatively catabolized to sustain energy needs"
                },
                "Kwashiorkor": {
                    "Primary Deficiency": "Protein specifically deficient while overall calories are adequate",
                    "Hallmark Finding": "Edema and hepatomegaly, with weight-for-height that can appear normal",
                    "Key Mechanism": "Low hepatic albumin lowers oncotic pressure, shifting fluid into tissues"
                },
                "Marasmic Kwashiorkor": {
                    "Primary Deficiency": "Combined caloric and protein deprivation (least common state)",
                    "Hallmark Finding": "Combined physical features of both marasmus and kwashiorkor",
                    "Key Mechanism": "Overlap of generalized starvation with severe protein loss"
                },
                "Chronic Malnutrition": {
                    "Primary Deficiency": "Long-term inadequate food quantity and quality",
                    "Hallmark Finding": "Stunting (decreased linear growth) and decreased head circumference",
                    "Key Mechanism": "Unrelenting food deprivation; death often from infection, diarrhea, and dehydration"
                }
            }
        },
        {
            "slug": "enzymes_of_ethanol_oxidation",
            "title": "Enzymes of Ethanol Oxidation",
            "subtitle": "Match each enzyme to its location, reaction, and clinical relevance",
            "categories": ["Location", "Reaction / Cofactor", "Clinical Relevance"],
            "data": {
                "Alcohol Dehydrogenase (ADH)": {
                    "Location": "Liver cytosol",
                    "Reaction / Cofactor": "Ethanol to acetaldehyde while NAD+ is reduced to NADH",
                    "Clinical Relevance": "The major enzyme for the first step of ethanol oxidation"
                },
                "Aldehyde Dehydrogenase (ALDH)": {
                    "Location": "Mitochondria",
                    "Reaction / Cofactor": "Acetaldehyde to acetate while NAD+ is reduced to NADH",
                    "Clinical Relevance": "Sole enzyme family catalyzing the final oxidative step"
                },
                "Cytochrome P450 2E1 (CYP2E1)": {
                    "Location": "Hepatic microsomes",
                    "Reaction / Cofactor": "Ethanol to acetaldehyde using NADPH, H+, and O2",
                    "Clinical Relevance": "Induced by excess routine alcohol; relevant in acetaminophen poisoning and porphyria"
                },
                "Catalase": {
                    "Location": "Peroxisomes",
                    "Reaction / Cofactor": "Uses hydrogen peroxide, converting H2O2 to H2O",
                    "Clinical Relevance": "Metabolizes only a very small amount of alcohol"
                }
            }
        }
    ]
}
