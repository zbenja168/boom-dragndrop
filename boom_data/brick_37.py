BRICK = {
    "brick_num": 37,
    "brick_title": "Inborn Errors of Carbohydrate Metabolism",
    "games": [
        {
            "slug": "glycogen_storage_diseases",
            "title": "Glycogen Storage Diseases",
            "subtitle": "Match each glycogen storage disease to its deficient enzyme, main tissue, and hallmark clue",
            "categories": ["Deficient Enzyme", "Main Tissue Affected", "Hallmark Clinical Clue"],
            "data": {
                "von Gierke (Type I)": {
                    "Deficient Enzyme": "Glucose-6-phosphatase",
                    "Main Tissue Affected": "Liver (and kidney)",
                    "Hallmark Clinical Clue": "Severe fasting hypoglycemia with lactic acidosis and hyperuricemia"
                },
                "Pompe (Type II)": {
                    "Deficient Enzyme": "Lysosomal acid alpha-glucosidase (acid maltase)",
                    "Main Tissue Affected": "Cardiac and skeletal muscle",
                    "Hallmark Clinical Clue": "Hypertrophic cardiomyopathy and macroglossia with normal glucose"
                },
                "Cori (Type III)": {
                    "Deficient Enzyme": "Debranching enzyme (alpha-1,6-glucosidase)",
                    "Main Tissue Affected": "Liver and muscle",
                    "Hallmark Clinical Clue": "Limit dextrin accumulation; mild hypoglycemia without lactic acidosis"
                },
                "McArdle (Type V)": {
                    "Deficient Enzyme": "Muscle glycogen phosphorylase",
                    "Main Tissue Affected": "Skeletal muscle",
                    "Hallmark Clinical Clue": "Second-wind phenomenon with exercise-induced myoglobinuria"
                },
                "Andersen (Type IV)": {
                    "Deficient Enzyme": "Glycogen branching enzyme",
                    "Main Tissue Affected": "Liver",
                    "Hallmark Clinical Clue": "Amylopectin-like glycogen, early cirrhosis, death by ~2 years"
                },
                "Hers (Type VI)": {
                    "Deficient Enzyme": "Hepatic glycogen phosphorylase",
                    "Main Tissue Affected": "Liver",
                    "Hallmark Clinical Clue": "Mild hypoglycemia and ketosis; milder form of type I"
                }
            }
        },
        {
            "slug": "rbc_and_hemoglobin_disorders",
            "title": "Red Cell and Hemoglobin Disorders",
            "subtitle": "Match each disorder to its defect, red-cell consequence, and key distinguishing finding",
            "categories": ["Deficient Enzyme / Defect", "Red-Cell or Hb Consequence", "Key Distinguishing Finding"],
            "data": {
                "G6PD deficiency": {
                    "Deficient Enzyme / Defect": "Glucose-6-phosphate dehydrogenase (low NADPH)",
                    "Red-Cell or Hb Consequence": "Oxidative injury with episodic hemolysis",
                    "Key Distinguishing Finding": "Heinz bodies and bite cells after triggers (fava beans, drugs, infection)"
                },
                "Pyruvate kinase deficiency": {
                    "Deficient Enzyme / Defect": "Pyruvate kinase (low glycolytic ATP)",
                    "Red-Cell or Hb Consequence": "Rigid, spiculated red cells with chronic hemolysis",
                    "Key Distinguishing Finding": "Elevated 2,3-BPG and hemolysis present from birth"
                },
                "Congenital methemoglobinemia": {
                    "Deficient Enzyme / Defect": "Cytochrome b5 reductase",
                    "Red-Cell or Hb Consequence": "Met-Hb (ferric Fe3+) cannot bind oxygen",
                    "Key Distinguishing Finding": "Cyanosis with chocolate-brown blood; treated with methylene blue"
                },
                "Tarui (Type VII)": {
                    "Deficient Enzyme / Defect": "Muscle phosphofructokinase",
                    "Red-Cell or Hb Consequence": "Exertional myopathy with hemolytic anemia (partial RBC PFK loss)",
                    "Key Distinguishing Finding": "Absence of the second-wind phenomenon (unlike McArdle)"
                }
            }
        },
        {
            "slug": "gluconeogenesis_and_pyruvate",
            "title": "Gluconeogenesis and Pyruvate Metabolism Errors",
            "subtitle": "Match each enzyme deficiency to the pathway it compromises and its distinguishing feature",
            "categories": ["Deficient Enzyme", "Pathway(s) Compromised", "Distinguishing Feature"],
            "data": {
                "PEPCK deficiency": {
                    "Deficient Enzyme": "Phosphoenolpyruvate carboxykinase",
                    "Pathway(s) Compromised": "Hepatic gluconeogenesis",
                    "Distinguishing Feature": "Fasting hypoglycemia and mild lactic acidosis without hyperammonemia"
                },
                "Pyruvate carboxylase deficiency": {
                    "Deficient Enzyme": "Pyruvate carboxylase",
                    "Pathway(s) Compromised": "Gluconeogenesis, TCA cycle, and urea cycle",
                    "Distinguishing Feature": "Hyperammonemia from reduced oxaloacetate formation"
                },
                "PDH complex deficiency": {
                    "Deficient Enzyme": "Pyruvate dehydrogenase complex",
                    "Pathway(s) Compromised": "Link of glycolysis to TCA cycle (acetyl-CoA)",
                    "Distinguishing Feature": "Neurologic dysfunction and ataxia with lactic acidosis"
                },
                "von Gierke (Type I)": {
                    "Deficient Enzyme": "Glucose-6-phosphatase",
                    "Pathway(s) Compromised": "Gluconeogenesis and glycogenolysis",
                    "Distinguishing Feature": "Hepatomegaly with hyperuricemia and hyperlipidemia"
                }
            }
        },
        {
            "slug": "treatment_strategies",
            "title": "Treatment Strategies",
            "subtitle": "Match each condition to its management strategy and the rationale behind it",
            "categories": ["Condition", "Management Strategy", "Rationale"],
            "data": {
                "von Gierke disease": {
                    "Condition": "Glucose-6-phosphatase deficiency",
                    "Management Strategy": "Uncooked cornstarch; avoid fructose, galactose, and sucrose",
                    "Rationale": "Slow glucose release prevents hypoglycemia; simple sugars worsen G6P buildup"
                },
                "McArdle disease": {
                    "Condition": "Muscle glycogen phosphorylase deficiency",
                    "Management Strategy": "Simple sugars before activity; favor dynamic aerobic exercise",
                    "Rationale": "Supplies fuel the muscle cannot get from glycogen; avoid intense exertion"
                },
                "PDH complex deficiency": {
                    "Condition": "Pyruvate dehydrogenase deficiency",
                    "Management Strategy": "Ketogenic diet plus thiamine and lipoic acid",
                    "Rationale": "Ketone-derived acetyl-CoA bypasses the blocked pyruvate step to fuel the CNS"
                },
                "Pompe disease": {
                    "Condition": "Acid alpha-glucosidase deficiency",
                    "Management Strategy": "Enzyme replacement therapy (approved 2006)",
                    "Rationale": "Replaces the deficient lysosomal enzyme to improve cardiac and muscle function"
                },
                "Methemoglobinemia": {
                    "Condition": "Cytochrome b5 reductase deficiency",
                    "Management Strategy": "Methylene blue administration",
                    "Rationale": "Reduces ferric met-Hb back to functional Hb in an NADPH-dependent manner"
                }
            }
        }
    ]
}
