BRICK = {
    "brick_num": 14,
    "brick_title": "Proteins, Enzymatic Machines and Introduction to Protein-based Disorders I (2 of 2)",
    "games": [
        {
            "slug": "molecular_defect",
            "title": "The Molecular Defect",
            "subtitle": "Match each protein-based disorder to its defective protein, gene, and core molecular consequence",
            "categories": ["Defective Protein/Enzyme", "Gene", "Core Molecular Consequence"],
            "data": {
                "G6PD deficiency": {
                    "Defective Protein/Enzyme": "Glucose 6-phosphate dehydrogenase",
                    "Gene": "G6PD (X-linked)",
                    "Core Molecular Consequence": "No NADPH from pentose phosphate pathway, so oxidized glutathione builds up in RBCs"
                },
                "Classic PKU": {
                    "Defective Protein/Enzyme": "Phenylalanine hydroxylase",
                    "Gene": "PAH",
                    "Core Molecular Consequence": "Phenylalanine cannot be hydroxylated to tyrosine and accumulates to neurotoxic levels"
                },
                "Hurler syndrome": {
                    "Defective Protein/Enzyme": "Alpha-L-iduronidase",
                    "Gene": "IDUA",
                    "Core Molecular Consequence": "Heparan and dermatan sulfate glycosaminoglycans accumulate in the lysosome"
                },
                "I-cell disease": {
                    "Defective Protein/Enzyme": "GlcNAc-1-phosphotransferase",
                    "Gene": "GNPTAB (mucolipidosis II)",
                    "Core Molecular Consequence": "No mannose-6-phosphate tag, so all lysosomal enzymes are mistrafficked and spill into circulation"
                },
                "Marfan syndrome": {
                    "Defective Protein/Enzyme": "Fibrillin-1",
                    "Gene": "FBN1 (autosomal dominant)",
                    "Core Molecular Consequence": "Defective elastin scaffold and secondarily increased TGF-beta activity"
                },
                "AAT deficiency": {
                    "Defective Protein/Enzyme": "Alpha-1 antitrypsin",
                    "Gene": "SERPINA1",
                    "Core Molecular Consequence": "Unopposed neutrophil elastase degrades the alveolar extracellular matrix"
                }
            }
        },
        {
            "slug": "g6pd_hemolysis",
            "title": "G6PD Deficiency and Hemolysis",
            "subtitle": "Match each finding or component to what it is and the mechanism behind it",
            "categories": ["Finding / Component", "What It Is", "Underlying Mechanism"],
            "data": {
                "Reduced glutathione (GSH)": {
                    "Finding / Component": "Antioxidant tripeptide inside RBCs",
                    "What It Is": "Tripeptide of glutamate, cysteine, and glycine",
                    "Underlying Mechanism": "Cysteine residue lets it cycle to neutralize oxidizing agents; regenerated using NADPH"
                },
                "Heinz bodies": {
                    "Finding / Component": "Dark inclusions seen on peripheral smear",
                    "What It Is": "Insoluble aggregates of oxidatively denatured hemoglobin",
                    "Underlying Mechanism": "Loss of NADPH and reduced glutathione lets oxidizing agents damage Hb"
                },
                "Bite cells": {
                    "Finding / Component": "RBCs that look like a cookie was bitten",
                    "What It Is": "Red cells missing chunks of membrane and cytoplasm",
                    "Underlying Mechanism": "Macrophages remove Heinz-body regions perceived as non-self"
                },
                "Jaundice / scleral icterus": {
                    "Finding / Component": "Yellow skin/sclera with dark tea-colored urine",
                    "What It Is": "Elevated bilirubin, a conjugated ring system that absorbs light",
                    "Underlying Mechanism": "Fragile RBCs lyse and release porphyrin/Hb breakdown products"
                },
                "Increased reticulocyte count": {
                    "Finding / Component": "Rise in immature circulating red cells",
                    "What It Is": "Newly released RBCs that still contain RNA remnants",
                    "Underlying Mechanism": "Bone marrow ramps up production to replace hemolyzed RBCs"
                }
            }
        },
        {
            "slug": "look_alike_disorders",
            "title": "Distinguishing Look-Alike Disorders",
            "subtitle": "Match each disorder to its hallmark presentation, distinguishing clue, and diagnostic biomarker",
            "categories": ["Hallmark Presentation", "Distinguishing Clue", "Diagnostic Biomarker"],
            "data": {
                "Hurler syndrome": {
                    "Hallmark Presentation": "Coarse gargoyle-like facies and corneal clouding by 6-12 months",
                    "Distinguishing Clue": "Corneal clouding is present, unlike in Hunter",
                    "Diagnostic Biomarker": "Increased mucopolysaccharides in the urine"
                },
                "Hunter syndrome": {
                    "Hallmark Presentation": "Milder Hurler-like features with aggressive behavior",
                    "Distinguishing Clue": "X-linked, no corneal clouding, iduronate sulfatase deficient",
                    "Diagnostic Biomarker": "Heparan and dermatan sulfate accumulation"
                },
                "I-cell disease": {
                    "Hallmark Presentation": "Severe, progressive course with death in the first decade",
                    "Distinguishing Clue": "All lysosomal enzymes are mistrafficked at the Golgi",
                    "Diagnostic Biomarker": "Elevated lysosomal enzymes in plasma with normal urinary mucopolysaccharides"
                },
                "Marfan syndrome": {
                    "Hallmark Presentation": "Tall, arachnodactyly, aortic dissection and aneurysm",
                    "Distinguishing Clue": "Lens dislocates up and out (superotemporal)",
                    "Diagnostic Biomarker": "Increased TGF-beta activity driving aortic disease"
                },
                "Homocystinuria": {
                    "Hallmark Presentation": "Marfanoid habitus with thrombosis and intellectual disability",
                    "Distinguishing Clue": "Lens dislocates down and in (inferonasal)",
                    "Diagnostic Biomarker": "Elevated homocysteine excreted in the urine"
                },
                "AAT deficiency": {
                    "Hallmark Presentation": "Early lower-lobe emphysema with or without liver disease",
                    "Distinguishing Clue": "Course worsened by smoking; Z allele misfolds in liver",
                    "Diagnostic Biomarker": "Glu342Lys (Z allele) misfolded alpha-1 antitrypsin"
                }
            }
        },
        {
            "slug": "cofactors_and_vitamins",
            "title": "Cofactors and Vitamins in Protein Disorders",
            "subtitle": "Match each cofactor or vitamin to the enzyme it serves and its clinical relevance",
            "categories": ["Cofactor / Vitamin", "Enzyme It Serves", "Clinical Relevance"],
            "data": {
                "Tetrahydrobiopterin (BH4)": {
                    "Cofactor / Vitamin": "GTP-derived organic cofactor",
                    "Enzyme It Serves": "Phenylalanine hydroxylase",
                    "Clinical Relevance": "Supplementation partially rescues some milder PKU variants"
                },
                "Pyridoxal phosphate (vitamin B6)": {
                    "Cofactor / Vitamin": "Modified form of pyridoxine",
                    "Enzyme It Serves": "Cystathionine beta-synthase",
                    "Clinical Relevance": "Aids roughly 25% of homocystinuria cases when supplemented"
                },
                "FAD (vitamin B2)": {
                    "Cofactor / Vitamin": "Flavin derived from riboflavin",
                    "Enzyme It Serves": "Glutathione reductase",
                    "Clinical Relevance": "This pathway is used to diagnose vitamin B2 deficiency"
                },
                "Folate (B9) and cobalamin (B12)": {
                    "Cofactor / Vitamin": "One-carbon and methyl-carrier vitamins",
                    "Enzyme It Serves": "Homocysteine remethylation to methionine",
                    "Clinical Relevance": "Regulate homocysteine; dietary insufficiency raises cardiovascular risk"
                }
            }
        }
    ]
}
