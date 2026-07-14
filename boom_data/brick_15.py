BRICK = {
    "brick_num": 15,
    "brick_title": "Proteins, Enzymatic Machines and Introduction to Protein-based Disorders II",
    "games": [
        {
            "slug": "six_enzyme_classes",
            "title": "The Six Enzyme Classes",
            "subtitle": "Match each enzyme class to the reaction it catalyzes, a common subclass, and its key clue",
            "categories": ["Type of Reaction Catalyzed", "Common Subclass", "Vitamin/Cofactor Clue or Key Detail"],
            "data": {
                "Oxidoreductase": {
                    "Type of Reaction Catalyzed": "Oxidation-reduction (electron transfer) reactions",
                    "Common Subclass": "Dehydrogenase or oxidase",
                    "Vitamin/Cofactor Clue or Key Detail": "Oxidative decarboxylation in the TCA cycle uses vitamin B1"
                },
                "Transferase": {
                    "Type of Reaction Catalyzed": "Interchanges a functional group between two substrates",
                    "Common Subclass": "Kinase or transaminase",
                    "Vitamin/Cofactor Clue or Key Detail": "Amino-group transfer (transamination) uses vitamin B6"
                },
                "Hydrolase": {
                    "Type of Reaction Catalyzed": "Breaks bonds using water",
                    "Common Subclass": "Protease, lipase, or nuclease",
                    "Vitamin/Cofactor Clue or Key Detail": "Cleaves peptide, ester, or phosphoester bonds"
                },
                "Isomerase": {
                    "Type of Reaction Catalyzed": "Rearranges a substrate into one of its isomers",
                    "Common Subclass": "Mutase",
                    "Vitamin/Cofactor Clue or Key Detail": "No atoms are added or removed, only repositioned"
                },
                "Lyase": {
                    "Type of Reaction Catalyzed": "Breaks bonds by means other than hydrolysis or oxidation",
                    "Common Subclass": "Decarboxylase",
                    "Vitamin/Cofactor Clue or Key Detail": "Often forms a new double bond or a new ring structure"
                },
                "Ligase": {
                    "Type of Reaction Catalyzed": "Joins two substrates via a covalent bond in an ATP-dependent manner",
                    "Common Subclass": "Carboxylase",
                    "Vitamin/Cofactor Clue or Key Detail": "Adds CO2 to form a carboxylic acid using vitamin B7"
                }
            }
        },
        {
            "slug": "phosphate_handling_enzymes",
            "title": "Phosphate-Handling Enzymes",
            "subtitle": "Sort these commonly confused enzymes by their action, phosphate source, and example",
            "categories": ["Action on Phosphate", "Phosphate Source", "Representative Example"],
            "data": {
                "Kinase": {
                    "Action on Phosphate": "Adds a phosphate group onto a substrate",
                    "Phosphate Source": "ATP, which is converted to ADP",
                    "Representative Example": "Hexokinase forms glucose-6-phosphate from glucose"
                },
                "Phosphorylase": {
                    "Action on Phosphate": "Cleaves a bond and attaches phosphate to the product",
                    "Phosphate Source": "Free inorganic phosphate (Pi)",
                    "Representative Example": "Glycogen phosphorylase yields glucose-1-phosphate"
                },
                "Phosphatase": {
                    "Action on Phosphate": "Removes a phosphate group from a substrate",
                    "Phosphate Source": "Water; the freed Pi is not reattached to a recipient",
                    "Representative Example": "Glucose-6-phosphatase yields free glucose"
                },
                "Phosphoglucomutase": {
                    "Action on Phosphate": "Moves the phosphate between carbons of the sugar",
                    "Phosphate Source": "No net phosphate is added or removed",
                    "Representative Example": "Converts glucose-1-phosphate to glucose-6-phosphate"
                }
            }
        },
        {
            "slug": "enzyme_biomarkers",
            "title": "Enzymes as Disease Biomarkers",
            "subtitle": "Match each plasma enzyme to its tissue source, associated condition, and enzyme family",
            "categories": ["Primary Tissue Source", "Associated Condition", "Enzyme Family"],
            "data": {
                "Alanine transaminase (ALT)": {
                    "Primary Tissue Source": "Liver hepatocytes",
                    "Associated Condition": "Hepatocellular injury or inflammation (e.g., hepatitis)",
                    "Enzyme Family": "Aminotransferase (a transferase)"
                },
                "Lipase": {
                    "Primary Tissue Source": "Pancreas",
                    "Associated Condition": "Acute pancreatitis",
                    "Enzyme Family": "Hydrolase that cleaves lipid esters"
                },
                "Prostate-specific antigen (PSA)": {
                    "Primary Tissue Source": "Prostate gland",
                    "Associated Condition": "Prostate pathology such as cancer",
                    "Enzyme Family": "Protease-type marker (hydrolase family)"
                },
                "Lactate dehydrogenase (LDH)": {
                    "Primary Tissue Source": "Many tissues; highly enriched in red blood cells",
                    "Associated Condition": "Hemolysis (also liver or heart injury)",
                    "Enzyme Family": "Dehydrogenase (an oxidoreductase)"
                },
                "Alkaline phosphatase (ALP)": {
                    "Primary Tissue Source": "Liver and bone",
                    "Associated Condition": "Cholestasis or bone disease",
                    "Enzyme Family": "Phosphatase (a hydrolase)"
                },
                "Creatine kinase-MB (CK-MB)": {
                    "Primary Tissue Source": "Cardiac muscle",
                    "Associated Condition": "Myocardial infarction",
                    "Enzyme Family": "Kinase (a transferase)"
                }
            }
        },
        {
            "slug": "enzyme_affinity_kinetics",
            "title": "Km, Affinity, and Kinetic Behavior",
            "subtitle": "Match each enzyme to its Km, distribution or substrate, and physiologic role",
            "categories": ["Km / Affinity", "Distribution or Substrate", "Physiologic Role"],
            "data": {
                "Hexokinase": {
                    "Km / Affinity": "Km ~0.05 mM (high affinity for glucose)",
                    "Distribution or Substrate": "Widely distributed; important in RBCs and neurons",
                    "Physiologic Role": "Traps glucose even when blood glucose is low"
                },
                "Glucokinase": {
                    "Km / Affinity": "Km ~5 mM (low affinity for glucose)",
                    "Distribution or Substrate": "Restricted to liver and pancreas",
                    "Physiologic Role": "Handles glucose after meals when glucose is abundant"
                },
                "Alcohol dehydrogenase": {
                    "Km / Affinity": "Km ~1-2 mM for ethanol",
                    "Distribution or Substrate": "Liver; substrate is ethanol",
                    "Physiologic Role": "Saturated after moderate drinking, so alcohol accumulates in blood"
                },
                "Carbonic anhydrase (forward)": {
                    "Km / Affinity": "Km ~12 mM forward vs ~26 mM reverse",
                    "Distribution or Substrate": "Kidney and RBCs; hydrates CO2 to carbonic acid",
                    "Physiologic Role": "Lower forward Km makes the forward reaction proceed first at equal concentrations"
                }
            }
        }
    ]
}
