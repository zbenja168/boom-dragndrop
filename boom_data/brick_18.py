BRICK = {
    "brick_num": 18,
    "brick_title": "Carbohydrates and Carbohydrate Metabolism Overview I",
    "games": [
        {
            "slug": "dietary_sugars",
            "title": "Common Dietary Carbohydrates",
            "subtitle": "Match each carbohydrate to its class, structure, and distinguishing feature.",
            "categories": ["Sugar Class", "Components / Structure", "Distinguishing Feature"],
            "data": {
                "Glucose": {
                    "Sugar Class": "Monosaccharide",
                    "Components / Structure": "Aldohexose (6 carbons, C1 aldehyde)",
                    "Distinguishing Feature": "Preferred neuronal fuel and sole energy source for RBCs"
                },
                "Fructose": {
                    "Sugar Class": "Monosaccharide",
                    "Components / Structure": "Ketohexose (6 carbons, C2 ketone)",
                    "Distinguishing Feature": "Very sweet; enriched in high-fructose corn syrup"
                },
                "Galactose": {
                    "Sugar Class": "Monosaccharide",
                    "Components / Structure": "Aldohexose released from lactose",
                    "Distinguishing Feature": "Highly enriched in dairy products"
                },
                "Sucrose": {
                    "Sugar Class": "Disaccharide",
                    "Components / Structure": "Glucose + fructose joined by an alpha-1,2 bond",
                    "Distinguishing Feature": "Nonreducing table sugar (both anomeric carbons linked)"
                },
                "Lactose": {
                    "Sugar Class": "Disaccharide",
                    "Components / Structure": "Galactose + glucose joined by a beta-1,4 bond",
                    "Distinguishing Feature": "Milk sugar cleaved by brush-border lactase"
                },
                "Maltose": {
                    "Sugar Class": "Disaccharide",
                    "Components / Structure": "Glucose + glucose joined by an alpha-1,4 bond",
                    "Distinguishing Feature": "Malt sugar found in beer and bread"
                }
            }
        },
        {
            "slug": "carb_terminology",
            "title": "Carbohydrate Structural Terms",
            "subtitle": "Match each nomenclature term to what it describes and a concrete example.",
            "categories": ["What It Classifies", "Definition", "Example"],
            "data": {
                "Aldose": {
                    "What It Classifies": "Carbonyl group present",
                    "Definition": "Sugar containing an aldehyde functional group",
                    "Example": "Glucose"
                },
                "Ketose": {
                    "What It Classifies": "Carbonyl group present",
                    "Definition": "Sugar containing a ketone functional group",
                    "Example": "Fructose"
                },
                "Pyranose": {
                    "What It Classifies": "Ring size when cyclized",
                    "Definition": "Six-membered sugar ring",
                    "Example": "alpha-D-glucopyranose"
                },
                "Furanose": {
                    "What It Classifies": "Ring size when cyclized",
                    "Definition": "Five-membered sugar ring",
                    "Example": "alpha-D-fructofuranose"
                },
                "Anomeric carbon": {
                    "What It Classifies": "Reactive hemiacetal carbon",
                    "Definition": "Former carbonyl carbon that closes the ring and defines alpha vs beta",
                    "Example": "C1 in aldoses, C2 in ketoses"
                },
                "Reducing sugar": {
                    "What It Classifies": "Oxidation capability",
                    "Definition": "Sugar with a free anomeric carbon that can be oxidized",
                    "Example": "All monosaccharides; maltose"
                }
            }
        },
        {
            "slug": "glut_transporters",
            "title": "Glucose Transporters (GLUTs)",
            "subtitle": "Match each transporter to its tissue, kinetics, and key function.",
            "categories": ["Primary Tissue", "Transport Kinetics", "Key Function"],
            "data": {
                "SGLT": {
                    "Primary Tissue": "Renal proximal tubule and intestinal apical membrane",
                    "Transport Kinetics": "Secondary active transport via Na+ symport, against gradient",
                    "Key Function": "Reabsorbs glucose from urine and takes up glucose/galactose"
                },
                "GLUT1": {
                    "Primary Tissue": "RBCs and barrier tissues (brain, retina, placenta, testis)",
                    "Transport Kinetics": "Low Km (high affinity)",
                    "Key Function": "Basal glucose uptake even during fasting"
                },
                "GLUT2": {
                    "Primary Tissue": "Liver, pancreatic beta-cells, basolateral enterocytes",
                    "Transport Kinetics": "High Km (low affinity), high Vmax, bidirectional",
                    "Key Function": "Glucose sensing for insulin release and hepatic glucose export"
                },
                "GLUT3": {
                    "Primary Tissue": "Neurons; major CNS transporter",
                    "Transport Kinetics": "Low Km (high affinity)",
                    "Key Function": "Reserves scarce blood glucose for neurons at low levels"
                },
                "GLUT4": {
                    "Primary Tissue": "Skeletal muscle and adipose tissue",
                    "Transport Kinetics": "Low Km, insulin-responsive (also recruited by exercise)",
                    "Key Function": "Insulin-stimulated glucose uptake for glycogen and fat storage"
                },
                "GLUT5": {
                    "Primary Tissue": "Intestinal luminal epithelium and sperm",
                    "Transport Kinetics": "Moderate Km (between GLUT1 and GLUT2)",
                    "Key Function": "Primary fructose transporter"
                }
            }
        },
        {
            "slug": "glucose_fates",
            "title": "Metabolic Fates of Glucose",
            "subtitle": "Match each pathway to its immediate substrate, key products, and purpose.",
            "categories": ["Immediate Substrate", "Key Product(s)", "Metabolic Purpose"],
            "data": {
                "Glycolysis": {
                    "Immediate Substrate": "Glucose",
                    "Key Product(s)": "Pyruvate and ATP",
                    "Metabolic Purpose": "Universal breakdown of glucose for energy"
                },
                "Pentose phosphate pathway": {
                    "Immediate Substrate": "Glucose-6-phosphate",
                    "Key Product(s)": "NADPH and ribose-5-phosphate",
                    "Metabolic Purpose": "Supplies reducing power and nucleotide precursors"
                },
                "Glycogenesis": {
                    "Immediate Substrate": "Glucose-6-phosphate",
                    "Key Product(s)": "Glycogen",
                    "Metabolic Purpose": "Stores glucose as a branched polymer"
                },
                "Lipogenesis": {
                    "Immediate Substrate": "Acetyl-CoA",
                    "Key Product(s)": "Fatty acids for triglyceride storage",
                    "Metabolic Purpose": "Stores excess glucose carbon as fat"
                },
                "TCA cycle": {
                    "Immediate Substrate": "Acetyl-CoA",
                    "Key Product(s)": "NADH, FADH2, and CO2",
                    "Metabolic Purpose": "Oxidizes acetyl-CoA to capture energy"
                }
            }
        }
    ]
}
