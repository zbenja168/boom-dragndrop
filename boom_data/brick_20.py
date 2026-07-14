BRICK = {
    "brick_num": 20,
    "brick_title": "Carbohydrates and Carbohydrate Metabolism Overview II",
    "games": [
        {
            "slug": "glycolytic_control_points",
            "title": "Glycolytic Control Point Enzymes",
            "subtitle": "Match each irreversible glycolytic enzyme to its step, its inhibitor, and its distinguishing feature",
            "categories": ["Glycolytic Step", "Inhibited By", "Key Feature"],
            "data": {
                "Hexokinase": {
                    "Glycolytic Step": "Step 1 (glucose to glucose 6-phosphate)",
                    "Inhibited By": "Glucose 6-phosphate (its own product)",
                    "Key Feature": "High affinity (low Km), low Vmax; used outside the liver"
                },
                "Glucokinase": {
                    "Glycolytic Step": "Step 1 (glucose to glucose 6-phosphate)",
                    "Inhibited By": "Not inhibited by glucose 6-phosphate",
                    "Key Feature": "Low affinity (high Km), high Vmax; liver isozyme"
                },
                "Phosphofructokinase-1": {
                    "Glycolytic Step": "Step 3 (the committed step)",
                    "Inhibited By": "ATP and citrate",
                    "Key Feature": "Activated by AMP and fructose 2,6-bisphosphate"
                },
                "Pyruvate kinase": {
                    "Glycolytic Step": "Step 10 (PEP to pyruvate)",
                    "Inhibited By": "ATP, alanine, and glucagon (PKA phosphorylation)",
                    "Key Feature": "Activated by fructose 1,6-bisphosphate; regulated in liver"
                }
            }
        },
        {
            "slug": "gluconeogenesis_bypass",
            "title": "Gluconeogenesis Bypass Enzymes",
            "subtitle": "Match each gluconeogenic enzyme to its reaction, the glycolytic step it bypasses, and a key detail",
            "categories": ["Reaction Catalyzed", "Glycolytic Step Bypassed", "Key Detail"],
            "data": {
                "Pyruvate carboxylase": {
                    "Reaction Catalyzed": "Pyruvate to oxaloacetate (adds CO2)",
                    "Glycolytic Step Bypassed": "Pyruvate kinase (step 10)",
                    "Key Detail": "Requires biotin (vitamin B7); activated by acetyl-CoA"
                },
                "PEP carboxykinase (PEPCK)": {
                    "Reaction Catalyzed": "Oxaloacetate to phosphoenolpyruvate",
                    "Glycolytic Step Bypassed": "Pyruvate kinase (step 10)",
                    "Key Detail": "Works with pyruvate carboxylase to reverse step 10"
                },
                "Fructose 1,6-bisphosphatase": {
                    "Reaction Catalyzed": "Fructose 1,6-bisphosphate to fructose 6-phosphate",
                    "Glycolytic Step Bypassed": "Phosphofructokinase-1 (step 3)",
                    "Key Detail": "Cleaves one phosphate off fructose 1,6-bisphosphate"
                },
                "Glucose 6-phosphatase": {
                    "Reaction Catalyzed": "Glucose 6-phosphate to free glucose",
                    "Glycolytic Step Bypassed": "Hexokinase / glucokinase (step 1)",
                    "Key Detail": "Yields glucose exportable via GLUT2 to the blood"
                }
            }
        },
        {
            "slug": "pdh_coenzymes",
            "title": "PDH Complex Coenzymes and Their Sources",
            "subtitle": "Match each coenzyme required by the pyruvate dehydrogenase complex to its parent molecule and vitamin",
            "categories": ["Active Coenzyme", "Parent Molecule", "Source Vitamin"],
            "data": {
                "Thiamin pyrophosphate": {
                    "Active Coenzyme": "TPP (decarboxylation of the alpha-ketoacid)",
                    "Parent Molecule": "Thiamin",
                    "Source Vitamin": "Vitamin B1"
                },
                "Flavin adenine dinucleotide": {
                    "Active Coenzyme": "FAD (accepts electrons)",
                    "Parent Molecule": "Riboflavin",
                    "Source Vitamin": "Vitamin B2"
                },
                "Nicotinamide adenine dinucleotide": {
                    "Active Coenzyme": "NAD+ (final electron acceptor, forms NADH)",
                    "Parent Molecule": "Niacin",
                    "Source Vitamin": "Vitamin B3"
                },
                "Coenzyme A": {
                    "Active Coenzyme": "CoA (carries the acetyl group as acetyl-CoA)",
                    "Parent Molecule": "Pantothenate",
                    "Source Vitamin": "Vitamin B5"
                },
                "Lipoate": {
                    "Active Coenzyme": "Lipoamide (transfers the acetyl group)",
                    "Parent Molecule": "Octanoic acid",
                    "Source Vitamin": "A fatty acid, not a vitamin"
                }
            }
        },
        {
            "slug": "fates_of_pyruvate",
            "title": "Fates of Pyruvate by Tissue and Condition",
            "subtitle": "Match each tissue or metabolic state to the fate of pyruvate and the enzyme or purpose involved",
            "categories": ["Tissue / Condition", "Fate of Pyruvate", "Enzyme / Purpose"],
            "data": {
                "Active muscle or CNS (aerobic)": {
                    "Tissue / Condition": "Metabolically active tissue with oxygen and mitochondria",
                    "Fate of Pyruvate": "Converted to acetyl-CoA and oxidized in the TCA cycle",
                    "Enzyme / Purpose": "Pyruvate dehydrogenase; yields ATP"
                },
                "Liver (glucose abundance, insulin)": {
                    "Tissue / Condition": "Hepatocyte during excess glucose and high insulin",
                    "Fate of Pyruvate": "Acetyl-CoA directed to fatty acid synthesis",
                    "Enzyme / Purpose": "PFK-2 raises fructose 2,6-bisphosphate to drive glycolysis"
                },
                "Liver (fasting, glucagon)": {
                    "Tissue / Condition": "Hepatocyte during low glucose and high glucagon",
                    "Fate of Pyruvate": "Feeds gluconeogenesis to export glucose",
                    "Enzyme / Purpose": "Alanine supplies pyruvate via ALT"
                },
                "Red blood cell": {
                    "Tissue / Condition": "Cell lacking mitochondria, fully reliant on glycolysis",
                    "Fate of Pyruvate": "Reduced to lactate",
                    "Enzyme / Purpose": "Lactate dehydrogenase regenerates NAD+ for glycolysis"
                }
            }
        }
    ]
}
