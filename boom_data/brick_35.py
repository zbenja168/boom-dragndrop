BRICK = {
    "brick_num": 35,
    "brick_title": "Porphyrins and Iron Homeostasis (1 of 2)",
    "games": [
        {
            "slug": "heme_synthesis_enzymes",
            "title": "Heme Synthesis Pathway",
            "subtitle": "Match each enzyme to the reaction it catalyzes and where in the cell it acts",
            "categories": ["Substrate(s)", "Product", "Cellular location"],
            "data": {
                "ALA synthase (ALAS)": {
                    "Substrate(s)": "Succinyl-CoA + glycine",
                    "Product": "delta-Aminolevulinic acid (ALA)",
                    "Cellular location": "Mitochondria (rate-limiting first step)"
                },
                "ALA dehydratase": {
                    "Substrate(s)": "delta-Aminolevulinic acid (ALA)",
                    "Product": "Porphobilinogen",
                    "Cellular location": "Cytosol (inhibited by lead)"
                },
                "Uroporphyrinogen decarboxylase": {
                    "Substrate(s)": "Uroporphyrinogen III",
                    "Product": "Coproporphyrinogen III",
                    "Cellular location": "Cytosol"
                },
                "Coproporphyrinogen oxidase": {
                    "Substrate(s)": "Coproporphyrinogen III",
                    "Product": "Protoporphyrinogen IX",
                    "Cellular location": "Mitochondria"
                },
                "Ferrochelatase": {
                    "Substrate(s)": "Protoporphyrin IX + Fe2+",
                    "Product": "Heme",
                    "Cellular location": "Mitochondria (inhibited by lead)"
                }
            }
        },
        {
            "slug": "heme_degradation",
            "title": "Heme Degradation to Bilirubin",
            "subtitle": "Match each step of heme breakdown to where it happens and its key feature",
            "categories": ["Conversion", "Where it occurs", "Key feature"],
            "data": {
                "Heme oxygenase": {
                    "Conversion": "Heme -> biliverdin",
                    "Where it occurs": "Macrophage",
                    "Key feature": "Releases carbon monoxide and Fe2+"
                },
                "Biliverdin reductase": {
                    "Conversion": "Biliverdin -> unconjugated bilirubin",
                    "Where it occurs": "Macrophage",
                    "Key feature": "Requires NADPH"
                },
                "Albumin transport": {
                    "Conversion": "Unconjugated bilirubin carried to liver",
                    "Where it occurs": "Blood",
                    "Key feature": "Solubilizes water-insoluble bilirubin"
                },
                "UDP-glucuronosyltransferase (UDPGT)": {
                    "Conversion": "Unconjugated -> conjugated bilirubin",
                    "Where it occurs": "Hepatocyte",
                    "Key feature": "Adds glucuronic acid to make it water-soluble"
                },
                "Bacterial metabolism": {
                    "Conversion": "Conjugated bilirubin -> urobilinogen",
                    "Where it occurs": "Gut lumen",
                    "Key feature": "Oxidized to stercobilin (brown stool color)"
                }
            }
        },
        {
            "slug": "hereditary_hyperbilirubinemias",
            "title": "Hereditary Hyperbilirubinemias",
            "subtitle": "Match each inherited disorder to its defect, bilirubin type, and clinical hallmark",
            "categories": ["Molecular defect", "Bilirubin elevated", "Clinical hallmark"],
            "data": {
                "Gilbert syndrome": {
                    "Molecular defect": "Slight decrease in UDPGT",
                    "Bilirubin elevated": "Unconjugated (indirect)",
                    "Clinical hallmark": "Mild jaundice with stress/fasting; benign, common"
                },
                "Crigler-Najjar type 1": {
                    "Molecular defect": "Complete absence of UDPGT",
                    "Bilirubin elevated": "Unconjugated (indirect)",
                    "Clinical hallmark": "Severe infantile jaundice, kernicterus, often fatal"
                },
                "Crigler-Najjar type 2": {
                    "Molecular defect": "Reduced but present UDPGT",
                    "Bilirubin elevated": "Unconjugated (indirect)",
                    "Clinical hallmark": "Milder; responds to phenobarbital"
                },
                "Dubin-Johnson syndrome": {
                    "Molecular defect": "ABCC2 mutation (defective MRP2 transporter)",
                    "Bilirubin elevated": "Conjugated (direct)",
                    "Clinical hallmark": "Glossy black liver"
                },
                "Rotor syndrome": {
                    "Molecular defect": "SLCO1B1 / SLCO1B3 mutation",
                    "Bilirubin elevated": "Conjugated (direct)",
                    "Clinical hallmark": "Like Dubin-Johnson but liver is NOT black"
                }
            }
        },
        {
            "slug": "alas_regulation",
            "title": "Regulators and Clinical Correlations",
            "subtitle": "Match each factor to its role in heme metabolism and its disease association",
            "categories": ["Role", "Effect on heme synthesis", "Clinical association"],
            "data": {
                "Excess heme": {
                    "Role": "End-product feedback signal",
                    "Effect on heme synthesis": "Represses ALAS gene and blocks ALAS mitochondrial import",
                    "Clinical association": "Basis for hemin therapy in acute porphyria"
                },
                "ALAS1 isoform": {
                    "Role": "Enzyme of liver / non-erythroid cells",
                    "Effect on heme synthesis": "Induced by drugs needing P450 and by low glucose",
                    "Clinical association": "Glucose loading dampens porphyria attacks"
                },
                "ALAS2 isoform": {
                    "Role": "Enzyme of erythroid precursors",
                    "Effect on heme synthesis": "Induced by erythropoietin and iron",
                    "Clinical association": "Mutation causes X-linked sideroblastic anemia"
                },
                "Lead (Pb)": {
                    "Role": "Environmental toxin",
                    "Effect on heme synthesis": "Inhibits ALA dehydratase and ferrochelatase, raising ALA",
                    "Clinical association": "Neurotoxicity and microcytic anemia"
                },
                "Vitamin B6 (PLP)": {
                    "Role": "Cofactor for the first ALAS step",
                    "Effect on heme synthesis": "Required to form ALA from glycine and succinyl-CoA",
                    "Clinical association": "Deficiency causes microcytic (sideroblastic) anemia"
                }
            }
        }
    ]
}
