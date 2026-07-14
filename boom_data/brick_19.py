BRICK = {
    "brick_num": 19,
    "brick_title": "Carbohydrates and Carbohydrate Metabolism Overview I: Glycogen, Lactose Intolerance, and Galactosemia",
    "games": [
        {
            "slug": "galactose_enzymes",
            "title": "Enzymes of Galactose Metabolism",
            "subtitle": "Match each enzyme to its reaction, the molecule it consumes, and its clinical or kinetic note",
            "categories": ["Reaction Catalyzed", "Molecule Consumed / Coenzyme", "Clinical or Kinetic Note"],
            "data": {
                "Galactokinase": {
                    "Reaction Catalyzed": "Galactose to galactose-1-phosphate",
                    "Molecule Consumed / Coenzyme": "ATP (to ADP)",
                    "Clinical or Kinetic Note": "Low Km (high affinity), high Vmax; deficient in mild type II"
                },
                "GALT (galactose-1-P uridyl transferase)": {
                    "Reaction Catalyzed": "Galactose-1-phosphate to glucose-1-phosphate",
                    "Molecule Consumed / Coenzyme": "UDP-glucose (group exchange)",
                    "Clinical or Kinetic Note": "Deficient in classic (type I) galactosemia, the most severe form"
                },
                "UDP-galactose epimerase (GALE)": {
                    "Reaction Catalyzed": "Interconverts UDP-galactose and UDP-glucose",
                    "Molecule Consumed / Coenzyme": "None consumed (reversible isomerization)",
                    "Clinical or Kinetic Note": "Deficient in rare type III galactosemia"
                },
                "Aldose reductase": {
                    "Reaction Catalyzed": "Galactose to galactitol",
                    "Molecule Consumed / Coenzyme": "NADPH (to NADP+)",
                    "Clinical or Kinetic Note": "Very high Km; active only when galactose is in excess"
                }
            }
        },
        {
            "slug": "carb_disorders",
            "title": "Carbohydrate Metabolism Disorders",
            "subtitle": "Match each disorder to its deficient enzyme, the molecule that accumulates, and its main clinical feature",
            "categories": ["Deficient Enzyme", "Key Accumulated Product", "Main Clinical Feature"],
            "data": {
                "Classic galactosemia (type I)": {
                    "Deficient Enzyme": "Galactose-1-phosphate uridyl transferase (GALT)",
                    "Key Accumulated Product": "Galactose-1-phosphate",
                    "Main Clinical Feature": "Failure to thrive, hepatomegaly, jaundice, cataracts, intellectual disability"
                },
                "Galactokinase deficiency (type II)": {
                    "Deficient Enzyme": "Galactokinase",
                    "Key Accumulated Product": "Galactose and galactitol (no galactose-1-phosphate)",
                    "Main Clinical Feature": "Isolated cataracts; otherwise mild, no liver or mental disease"
                },
                "Congenital lactase deficiency": {
                    "Deficient Enzyme": "Lactase",
                    "Key Accumulated Product": "Undigested lactose in the gut lumen",
                    "Main Clinical Feature": "Newborn watery diarrhea, weight loss, and dehydration"
                },
                "Andersen disease (type IV GSD)": {
                    "Deficient Enzyme": "Glycogen branching enzyme",
                    "Key Accumulated Product": "Abnormal unbranched glycogen",
                    "Main Clinical Feature": "Hepatic inflammation, cirrhosis, usually fatal within about 2 years"
                },
                "Hereditary fructose intolerance": {
                    "Deficient Enzyme": "Aldolase B",
                    "Key Accumulated Product": "Fructose-1-phosphate",
                    "Main Clinical Feature": "ATP depletion and phosphate trapping after fructose ingestion"
                }
            }
        },
        {
            "slug": "glycogen_structure",
            "title": "Glycogen Structure and Dynamics",
            "subtitle": "Match each structural element to what it is and the functional benefit it provides",
            "categories": ["Description", "Functional Benefit"],
            "data": {
                "Alpha-1,4 glycosidic bond": {
                    "Description": "Joins glucose units within the linear chains",
                    "Functional Benefit": "Forms the backbone core of glycogen and reconnects glucose within branches"
                },
                "Alpha-1,6 glycosidic bond": {
                    "Description": "Formed at branch points every 8 to 12 glucose units",
                    "Functional Benefit": "Generates branches, producing many terminal ends"
                },
                "Non-reducing ends": {
                    "Description": "Numerous free terminal ends on the branches",
                    "Functional Benefit": "Allow degradative enzymes to release glucose simultaneously and rapidly"
                },
                "Reducing end": {
                    "Description": "Single end covalently attached to glycogenin",
                    "Functional Benefit": "Serves as the nucleation point for glycogen synthesis"
                },
                "Highly branched architecture": {
                    "Description": "One large polymer instead of many free monosaccharides",
                    "Functional Benefit": "Minimizes osmotic water influx and cell swelling"
                }
            }
        },
        {
            "slug": "lactose_intolerance",
            "title": "Lactose Intolerance",
            "subtitle": "Match each component or concept to its mechanism and its resulting effect or feature",
            "categories": ["Mechanism", "Result or Feature"],
            "data": {
                "Lactase": {
                    "Mechanism": "Cleaves lactose into glucose and galactose",
                    "Result or Feature": "Monosaccharides absorbed into the intestinal wall via SGLT"
                },
                "Bacterial fermentation of lactose": {
                    "Mechanism": "Colonic bacteria metabolize undigested lactose",
                    "Result or Feature": "Produce gas (CO2, methane) and lactic acid"
                },
                "Gas production": {
                    "Mechanism": "Release of CO2 and methane by bacteria",
                    "Result or Feature": "Bloating and flatulence"
                },
                "Lactic acid": {
                    "Mechanism": "Osmotically active fermentation byproduct",
                    "Result or Feature": "Water influx, wall distention, peristalsis, watery diarrhea"
                },
                "Hydrogen breath test": {
                    "Mechanism": "Measures H2, methane, or hydrogen sulfide after a test carbohydrate",
                    "Result or Feature": "Diagnoses lactose intolerance, SIBO, and fructose malabsorption"
                },
                "Congenital lactase deficiency": {
                    "Mechanism": "Autosomal recessive, lactase absent from birth",
                    "Result or Feature": "Severe newborn diarrhea, unlike mild adult hypolactasia"
                }
            }
        }
    ]
}
