BRICK = {
    "brick_num": 33,
    "brick_title": "Amino Acid Metabolism I: Nitrogen Balance and Urea Cycle",
    "games": [
        {
            "slug": "urea_cycle_enzymes",
            "title": "Enzymes of the Urea Cycle",
            "subtitle": "Match each urea cycle enzyme to its cellular location, substrate, and product",
            "categories": ["Cellular location", "Substrate(s)", "Product(s)"],
            "data": {
                "Carbamoyl phosphate synthetase-I (CPS-I)": {
                    "Cellular location": "Mitochondria of hepatocytes",
                    "Substrate(s)": "Ammonia plus carbon dioxide",
                    "Product(s)": "Carbamoyl phosphate"
                },
                "Ornithine transcarbamylase (OTC)": {
                    "Cellular location": "Mitochondria of hepatocytes",
                    "Substrate(s)": "Carbamoyl phosphate and ornithine",
                    "Product(s)": "Citrulline"
                },
                "Argininosuccinate synthetase": {
                    "Cellular location": "Cytoplasm of hepatocytes",
                    "Substrate(s)": "Citrulline plus aspartate and ATP",
                    "Product(s)": "Argininosuccinate"
                },
                "Argininosuccinate lyase": {
                    "Cellular location": "Cytoplasm of hepatocytes",
                    "Substrate(s)": "Argininosuccinate",
                    "Product(s)": "Arginine plus fumarate"
                },
                "Arginase": {
                    "Cellular location": "Cytoplasm of hepatocytes",
                    "Substrate(s)": "Arginine",
                    "Product(s)": "Ornithine plus urea"
                }
            }
        },
        {
            "slug": "urea_cycle_disorders",
            "title": "Urea Cycle Disorders",
            "subtitle": "Match each urea cycle disorder to its inheritance, key lab marker, and distinguishing feature",
            "categories": ["Inheritance pattern", "Characteristic lab marker", "Distinguishing feature"],
            "data": {
                "OTC deficiency": {
                    "Inheritance pattern": "X-linked recessive; more common in men",
                    "Characteristic lab marker": "Low citrulline with high orotic acid",
                    "Distinguishing feature": "Most common urea cycle defect; orotic aciduria without anemia"
                },
                "CPS-I deficiency": {
                    "Inheritance pattern": "Autosomal recessive",
                    "Characteristic lab marker": "Low citrulline with normal or low orotic acid",
                    "Distinguishing feature": "Non-responsive to carbamylglutamate"
                },
                "Citrullinemia (argininosuccinate synthetase deficiency)": {
                    "Inheritance pattern": "Autosomal recessive",
                    "Characteristic lab marker": "High citrulline with low argininosuccinic acid",
                    "Distinguishing feature": "Low ASA distinguishes it from lyase deficiency"
                },
                "Argininosuccinic aciduria (argininosuccinate lyase deficiency)": {
                    "Inheritance pattern": "Autosomal recessive",
                    "Characteristic lab marker": "High citrulline and high argininosuccinic acid",
                    "Distinguishing feature": "Both citrulline and ASA are elevated"
                },
                "Arginase deficiency": {
                    "Inheritance pattern": "Autosomal recessive",
                    "Characteristic lab marker": "Arginine three- to four-fold above reference range",
                    "Distinguishing feature": "Upper motor spasticity mimicking cerebral palsy"
                },
                "NAGS deficiency": {
                    "Inheritance pattern": "Autosomal recessive",
                    "Characteristic lab marker": "Low intermediates from ineffective CPS-I activation",
                    "Distinguishing feature": "Responds to carbamylglutamate, a synthetic NAG analog"
                }
            }
        },
        {
            "slug": "interorgan_nitrogen_cycles",
            "title": "Interorgan Nitrogen and Carbon Cycles",
            "subtitle": "Match each shuttle to the molecule it carries, its key enzyme, and its primary role",
            "categories": ["Molecule carried", "Key enzyme", "Primary role"],
            "data": {
                "Glucose-alanine (Cahill) cycle": {
                    "Molecule carried": "Alanine",
                    "Key enzyme": "Alanine aminotransferase (ALT)",
                    "Primary role": "Shuttles nitrogen from muscle to liver during exercise or fasting"
                },
                "Cori cycle": {
                    "Molecule carried": "Lactate",
                    "Key enzyme": "No transaminase required",
                    "Primary role": "Recycles muscle and erythrocyte lactate back to glucose"
                },
                "Glutamine transport": {
                    "Molecule carried": "Glutamine",
                    "Key enzyme": "Glutamine synthetase and glutaminase",
                    "Primary role": "Predominant nitrogen transporter delivering nitrogen to the liver"
                },
                "Aspartate-fumarate (AST) shuttle": {
                    "Molecule carried": "Aspartate",
                    "Key enzyme": "Aspartate aminotransferase (AST)",
                    "Primary role": "Donates the second nitrogen atom of urea, regenerating from fumarate"
                }
            }
        },
        {
            "slug": "hyperammonemia_management",
            "title": "Management of Hyperammonemia",
            "subtitle": "Match each therapy to its mechanism, target molecule, and clinical note",
            "categories": ["Mechanism", "Molecule removed or targeted", "Clinical note"],
            "data": {
                "Sodium phenylbutyrate": {
                    "Mechanism": "Converted to phenylacetate, then conjugates its target",
                    "Molecule removed or targeted": "Glutamine",
                    "Clinical note": "Removes the predominant nitrogen transporter, excreted in urine"
                },
                "Sodium benzoate": {
                    "Mechanism": "Covalently binds its target to form a urinary derivative",
                    "Molecule removed or targeted": "Glycine",
                    "Clinical note": "Increases demand for glycine synthesis, diverting nitrogen from urea"
                },
                "Lactulose": {
                    "Mechanism": "Acidifies the colon through microbial metabolism",
                    "Molecule removed or targeted": "Ammonium ions in the gut",
                    "Clinical note": "Traps ammonium and stimulates bowel movement for excretion"
                },
                "Carbamylglutamate": {
                    "Mechanism": "Synthetic NAG analog that directly activates CPS-I",
                    "Molecule removed or targeted": "Excess nitrogenous waste",
                    "Clinical note": "Well tolerated in NAGS deficiency, often avoiding protein restriction"
                },
                "Dialysis": {
                    "Mechanism": "Extracorporeal clearance of a toxic solute",
                    "Molecule removed or targeted": "Ammonia",
                    "Clinical note": "Immediate treatment to rapidly remove toxic ammonia"
                }
            }
        }
    ]
}
