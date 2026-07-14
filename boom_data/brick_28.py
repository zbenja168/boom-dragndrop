BRICK = {
    "brick_num": 28,
    "brick_title": "Cell Signaling in Context: Fed and Fasting Metabolic State (2 of 2)",
    "games": [
        {
            "slug": "insulin_secretion_cascade",
            "title": "Glucose-Stimulated Insulin Secretion",
            "subtitle": "Match each step in the beta-cell secretion cascade to its key molecule and immediate result",
            "categories": ["Key Molecule / Structure", "Triggering Event", "Immediate Result"],
            "data": {
                "Blood glucose rises": {
                    "Key Molecule / Structure": "GLUT2 transporter (high Km, low affinity)",
                    "Triggering Event": "Glucose enters the beta-cell only when blood glucose is elevated",
                    "Immediate Result": "Glucose becomes available for oxidative catabolism"
                },
                "ATP production": {
                    "Key Molecule / Structure": "Glycolysis, TCA cycle, and oxidative phosphorylation",
                    "Triggering Event": "Imported glucose is oxidatively catabolized",
                    "Immediate Result": "Intracellular ATP levels increase"
                },
                "Potassium channel closes": {
                    "Key Molecule / Structure": "ATP-sensitive potassium (K_ATP) channel",
                    "Triggering Event": "Rising ATP allosterically inhibits the channel",
                    "Immediate Result": "K+ leak is blocked and the membrane depolarizes"
                },
                "Calcium entry": {
                    "Key Molecule / Structure": "Voltage-gated calcium channel",
                    "Triggering Event": "Depolarization opens the channel",
                    "Immediate Result": "Cytosolic calcium concentration rises"
                },
                "Insulin release": {
                    "Key Molecule / Structure": "Insulin-containing secretory granules",
                    "Triggering Event": "Calcium activates vesicle trafficking and fusion proteins",
                    "Immediate Result": "Insulin is released by exocytosis"
                }
            }
        },
        {
            "slug": "insulin_processing_forms",
            "title": "Insulin Processing and Physical Forms",
            "subtitle": "Match each insulin species to its composition, origin, and functional significance",
            "categories": ["Composition", "Processing / Origin", "Functional Significance"],
            "data": {
                "Preproinsulin": {
                    "Composition": "Single polypeptide chain with an N-terminal signal peptide",
                    "Processing / Origin": "First translated product before any cleavage",
                    "Functional Significance": "Signal peptide is removed within the endoplasmic reticulum"
                },
                "Proinsulin": {
                    "Composition": "A, B, and C segments held together by disulfide bonds",
                    "Processing / Origin": "Formed after the signal peptide is removed",
                    "Functional Significance": "Inactive precursor awaiting C-peptide cleavage"
                },
                "Mature insulin": {
                    "Composition": "A and B chains as a disulfide-linked heterodimer",
                    "Processing / Origin": "Produced when the C-peptide is proteolytically cleaved",
                    "Functional Significance": "Active hormone that binds the insulin receptor"
                },
                "C-peptide": {
                    "Composition": "Connecting peptide fragment released during cleavage",
                    "Processing / Origin": "Stored equimolar with insulin in secretory granules",
                    "Functional Significance": "Serum marker of endogenous beta-cell insulin production"
                },
                "Insulin hexamer": {
                    "Composition": "Self-associated aggregate of six insulin units",
                    "Processing / Origin": "Favored at the high concentration inside granules",
                    "Functional Significance": "Inactive; cannot bind receptor and favored in long-acting insulin"
                },
                "Insulin monomer": {
                    "Composition": "Single dissociated insulin unit",
                    "Processing / Origin": "Formed as concentrated insulin dilutes in the bloodstream",
                    "Functional Significance": "Most active form; favored in engineered fast-acting insulin"
                }
            }
        },
        {
            "slug": "ampk_energy_sensing",
            "title": "AMPK: The Cellular Energy Sensor",
            "subtitle": "Match each metabolic process to how AMPK regulates it and why",
            "categories": ["AMPK Effect", "Anabolic or Catabolic", "Substrate Handling"],
            "data": {
                "Lipogenesis": {
                    "AMPK Effect": "Inhibited",
                    "Anabolic or Catabolic": "Anabolic (consumes ATP)",
                    "Substrate Handling": "Builds fatty acids and triglycerides for storage"
                },
                "Glycogenesis": {
                    "AMPK Effect": "Inhibited",
                    "Anabolic or Catabolic": "Anabolic (consumes ATP)",
                    "Substrate Handling": "Polymerizes glucose into glycogen"
                },
                "Protein synthesis": {
                    "AMPK Effect": "Inhibited",
                    "Anabolic or Catabolic": "Anabolic (consumes ATP)",
                    "Substrate Handling": "Assembles amino acids into polypeptides"
                },
                "Glycolysis": {
                    "AMPK Effect": "Enhanced",
                    "Anabolic or Catabolic": "Catabolic (produces ATP)",
                    "Substrate Handling": "Breaks glucose down to pyruvate"
                },
                "Beta-oxidation": {
                    "AMPK Effect": "Enhanced",
                    "Anabolic or Catabolic": "Catabolic (produces ATP)",
                    "Substrate Handling": "Breaks fatty acids down to acetyl-CoA"
                },
                "Skeletal muscle GLUT4 expression": {
                    "AMPK Effect": "Enhanced",
                    "Anabolic or Catabolic": "Catabolism-supporting",
                    "Substrate Handling": "Imports glucose to fuel ATP production"
                }
            }
        },
        {
            "slug": "refeeding_syndrome",
            "title": "Re-feeding Syndrome Micronutrients",
            "subtitle": "Match each nutrient to why its serum level falls and its clinical consequence",
            "categories": ["Serum Change", "Reason for the Shift", "Clinical Consequence"],
            "data": {
                "Potassium": {
                    "Serum Change": "Hypokalemia",
                    "Reason for the Shift": "Insulin drives potassium from serum into cells",
                    "Clinical Consequence": "Arrhythmias, weakness, and neurological dysfunction"
                },
                "Phosphate": {
                    "Serum Change": "Hypophosphatemia",
                    "Reason for the Shift": "Consumed as glycolysis and kinase signaling restart",
                    "Clinical Consequence": "Seizures, coma, or death if unresolved"
                },
                "Magnesium": {
                    "Serum Change": "Hypomagnesemia",
                    "Reason for the Shift": "Required for insulin-stimulated metabolic processes",
                    "Clinical Consequence": "Muscle weakness, altered mental status, and arrhythmias"
                },
                "Thiamin (vitamin B1)": {
                    "Serum Change": "Functional deficiency unmasked",
                    "Reason for the Shift": "Demand surges as PDH oxidizes refed glucose",
                    "Clinical Consequence": "Wernicke-Korsakoff syndrome"
                }
            }
        }
    ]
}
