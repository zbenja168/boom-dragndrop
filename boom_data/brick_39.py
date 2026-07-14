BRICK = {
    "brick_num": 39,
    "brick_title": "Dyslipidemias, Lipid Storage Disorders, and other defects in Lipid Metabolism (2 of 2)",
    "games": [
        {
            "slug": "sphingolipidoses_biochem",
            "title": "Sphingolipidoses: Enzyme and Substrate",
            "subtitle": "Match each lysosomal storage disease to its deficient enzyme, accumulated substrate, and signature clue",
            "categories": ["Deficient Enzyme", "Accumulated Substrate", "Signature Clue"],
            "data": {
                "Tay-Sachs disease": {
                    "Deficient Enzyme": "Hexosaminidase A",
                    "Accumulated Substrate": "GM2 ganglioside",
                    "Signature Clue": "Cherry-red macula with NO hepatosplenomegaly"
                },
                "Niemann-Pick disease": {
                    "Deficient Enzyme": "Sphingomyelinase",
                    "Accumulated Substrate": "Sphingomyelin",
                    "Signature Clue": "Cherry-red macula WITH hepatosplenomegaly"
                },
                "Gaucher disease": {
                    "Deficient Enzyme": "Glucocerebrosidase",
                    "Accumulated Substrate": "Glucocerebroside",
                    "Signature Clue": "Crinkled-paper macrophages (Gaucher cells)"
                },
                "Fabry disease": {
                    "Deficient Enzyme": "Alpha-galactosidase A",
                    "Accumulated Substrate": "Ceramide trihexoside",
                    "Signature Clue": "Angiokeratomas and acroparesthesia of hands and feet"
                },
                "Krabbe disease": {
                    "Deficient Enzyme": "Galactocerebrosidase",
                    "Accumulated Substrate": "Galactocerebroside",
                    "Signature Clue": "Multinucleated globoid cells in nervous tissue"
                }
            }
        },
        {
            "slug": "storage_disease_course",
            "title": "Storage Diseases: Course and Prognosis",
            "subtitle": "Match each disorder to its typical onset, key physical finding, and outcome",
            "categories": ["Typical Onset", "Key Physical Finding", "Prognosis / Treatment"],
            "data": {
                "Tay-Sachs disease": {
                    "Typical Onset": "Weakness at 3-6 months in a normal-appearing infant",
                    "Key Physical Finding": "Increased startle response, seizures, blindness",
                    "Prognosis / Treatment": "Death 2-3 years after a vegetative state; no cure"
                },
                "Niemann-Pick type A": {
                    "Typical Onset": "First 6 months of life",
                    "Key Physical Finding": "Massive hepatosplenomegaly with rapid neurologic decline",
                    "Prognosis / Treatment": "Death around age 3 years"
                },
                "Niemann-Pick type B": {
                    "Typical Onset": "Later than type A, most common subtype",
                    "Key Physical Finding": "Progressive hepatosplenomegaly with NO neurologic signs",
                    "Prognosis / Treatment": "Pulmonary disease and cirrhosis; death in adolescence"
                },
                "Gaucher type 1": {
                    "Typical Onset": "Childhood or young adulthood",
                    "Key Physical Finding": "Spleen up to 85x normal size and painful bone crises",
                    "Prognosis / Treatment": "Enzyme replacement allows a relatively normal lifespan"
                },
                "Fabry disease": {
                    "Typical Onset": "Adulthood with slow progression",
                    "Key Physical Finding": "Hypohidrosis, angiokeratomas, renal and cardiac disease",
                    "Prognosis / Treatment": "Death in the 3rd-4th decade despite recombinant enzyme"
                }
            }
        },
        {
            "slug": "peroxisome_players",
            "title": "Peroxisome Biology: Molecular Players",
            "subtitle": "Match each peroxisomal molecule to its role, location, and defining detail",
            "categories": ["Role", "Location / Context", "Defining Detail"],
            "data": {
                "Catalase": {
                    "Role": "Reduces hydrogen peroxide to water",
                    "Location / Context": "Peroxisomal matrix enzyme",
                    "Defining Detail": "Protects the cell from toxic H2O2 byproduct"
                },
                "Peroxins (PEX)": {
                    "Role": "Import proteins into the peroxisome",
                    "Location / Context": "Receptor proteins in the peroxisomal membrane",
                    "Defining Detail": "Recognize the PTS and enable peroxisome biogenesis"
                },
                "Acyl-CoA oxidase": {
                    "Role": "Catalyzes the first step of peroxisomal beta-oxidation",
                    "Location / Context": "Peroxisome-specific oxidation enzyme",
                    "Defining Detail": "Transfers electrons to oxygen, generating H2O2"
                },
                "Peroxisome targeting signal (PTS)": {
                    "Role": "Tags a protein for delivery to the peroxisome",
                    "Location / Context": "Carried on peroxisomal proteins made in cytoplasm",
                    "Defining Detail": "Recognized by PEX receptor proteins"
                },
                "Carnitine acetyltransferase": {
                    "Role": "Transports activated acyl groups out of the peroxisome",
                    "Location / Context": "Peroxisome's own transport enzyme",
                    "Defining Detail": "Sends shortened products to mitochondria to finish"
                },
                "Very-long-chain fatty acid (VLCFA)": {
                    "Role": "Substrate broken down by peroxisomal beta-oxidation",
                    "Location / Context": "Chains longer than 22 carbons",
                    "Defining Detail": "Too large for mitochondria; shortened to medium-chain"
                }
            }
        },
        {
            "slug": "peroxisome_vs_lysosome",
            "title": "Peroxisomal vs Lysosomal Disease",
            "subtitle": "Sort each disorder by its defective organelle function, affected molecule, and clinical clue",
            "categories": ["Defective Organelle Function", "Affected Molecule", "Clinical Clue"],
            "data": {
                "Zellweger syndrome": {
                    "Defective Organelle Function": "Absent peroxisome biogenesis from loss of PEX",
                    "Affected Molecule": "VLCFAs accumulate in liver and brain",
                    "Clinical Clue": "Widely spaced eyes, high forehead, death before age 1"
                },
                "X-linked adrenoleukodystrophy": {
                    "Defective Organelle Function": "Impaired VLCFA import via defective ABC transporter",
                    "Affected Molecule": "VLCFAs accumulate in blood and tissues",
                    "Clinical Clue": "Adrenal insufficiency plus neurologic decline in childhood"
                },
                "Tay-Sachs disease": {
                    "Defective Organelle Function": "Deficient lysosomal hexosaminidase A (acts at pH 5)",
                    "Affected Molecule": "GM2 ganglioside accumulates in neurons",
                    "Clinical Clue": "Cherry-red macula without hepatosplenomegaly"
                },
                "Krabbe disease": {
                    "Defective Organelle Function": "Deficient lysosomal galactocerebrosidase",
                    "Affected Molecule": "Galactocerebroside (psychosine) accumulates in myelin",
                    "Clinical Clue": "Globoid cells, optic atrophy, refractory seizures"
                }
            }
        }
    ]
}
