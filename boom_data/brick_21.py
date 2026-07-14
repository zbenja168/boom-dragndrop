BRICK = {
    "brick_num": 21,
    "brick_title": "Carbohydrates and Carbohydrate Metabolism Overview II: Fructose, HFCS, the Polyol Pathway, and Fructose Disorders",
    "games": [
        {
            "slug": "sugar_metabolism_enzymes",
            "title": "Enzymes of Sugar Metabolism",
            "subtitle": "Match each enzyme to its substrate, product, and key feature",
            "categories": ["Substrate", "Product", "Key Feature"],
            "data": {
                "Fructokinase": {
                    "Substrate": "Fructose (plus ATP)",
                    "Product": "Fructose 1-phosphate",
                    "Key Feature": "Low Km, high Vmax; rapidly consumes ATP in the liver"
                },
                "Aldolase B": {
                    "Substrate": "Fructose 1-phosphate",
                    "Product": "DHAP and glyceraldehyde 3-phosphate",
                    "Key Feature": "Deficient in hereditary fructose intolerance"
                },
                "Glucokinase": {
                    "Substrate": "Glucose (plus ATP)",
                    "Product": "Glucose 6-phosphate",
                    "Key Feature": "High Km, high Vmax; first step of hepatic glycolysis"
                },
                "PFK-1": {
                    "Substrate": "Fructose 6-phosphate",
                    "Product": "Fructose 1,6-bisphosphate",
                    "Key Feature": "Major control point inhibited by ATP and citrate"
                },
                "Aldose reductase": {
                    "Substrate": "Glucose (plus NADPH)",
                    "Product": "Sorbitol",
                    "Key Feature": "High Km; active only when glucose is in excess"
                },
                "Sorbitol dehydrogenase": {
                    "Substrate": "Sorbitol",
                    "Product": "Fructose",
                    "Key Feature": "Second enzyme of the polyol pathway"
                }
            }
        },
        {
            "slug": "polyol_pathway_damage",
            "title": "The Polyol Pathway and Diabetic Damage",
            "subtitle": "Match each player to its identity, pathway role, and pathologic consequence",
            "categories": ["Identity", "Role in Polyol Pathway", "Pathologic Consequence"],
            "data": {
                "Aldose reductase": {
                    "Identity": "Rate-limiting enzyme with a high Km for glucose",
                    "Role in Polyol Pathway": "Reduces glucose to sorbitol, consuming NADPH",
                    "Pathologic Consequence": "NADPH depletion drives oxidative stress"
                },
                "Sorbitol": {
                    "Identity": "Sugar alcohol (polyol) of glucose",
                    "Role in Polyol Pathway": "Intermediate that accumulates inside cells",
                    "Pathologic Consequence": "Osmotic stress with water influx and swelling"
                },
                "Sorbitol dehydrogenase": {
                    "Identity": "Second enzyme of the pathway",
                    "Role in Polyol Pathway": "Oxidizes sorbitol into fructose",
                    "Pathologic Consequence": "Fructose causes glycative stress on proteins"
                },
                "NADPH": {
                    "Identity": "Reducing cofactor and electron donor",
                    "Role in Polyol Pathway": "Consumed during sorbitol production",
                    "Pathologic Consequence": "Oxidized GSSG accumulates and cannot quench ROS"
                },
                "Retina and nerve cells": {
                    "Identity": "Tissues rich in GLUTs and polyol enzymes",
                    "Role in Polyol Pathway": "Take up glucose rapidly, independent of insulin",
                    "Pathologic Consequence": "Cataract formation and neuropathy in diabetes"
                }
            }
        },
        {
            "slug": "fructose_galactose_disorders",
            "title": "Disorders of Fructose and Galactose Metabolism",
            "subtitle": "Match each disorder to its deficient enzyme, accumulated substrate, and key features",
            "categories": ["Deficient Enzyme", "Accumulated Substrate", "Key Clinical Features"],
            "data": {
                "Essential fructosuria": {
                    "Deficient Enzyme": "Fructokinase",
                    "Accumulated Substrate": "Fructose",
                    "Key Clinical Features": "Benign; fructose in urine or blood, usually asymptomatic"
                },
                "Hereditary fructose intolerance": {
                    "Deficient Enzyme": "Aldolase B",
                    "Accumulated Substrate": "Fructose 1-phosphate",
                    "Key Clinical Features": "Hypoglycemia, vomiting, hepatomegaly, jaundice"
                },
                "Classic galactosemia (Type I)": {
                    "Deficient Enzyme": "Galactose 1-phosphate uridyltransferase (GALT)",
                    "Accumulated Substrate": "Galactose 1-phosphate",
                    "Key Clinical Features": "Cataracts, hepatomegaly, jaundice, intellectual disability"
                },
                "Galactokinase deficiency (Type II)": {
                    "Deficient Enzyme": "Galactokinase",
                    "Accumulated Substrate": "Galactose",
                    "Key Clinical Features": "Cataracts, typically as an isolated finding"
                }
            }
        },
        {
            "slug": "hfcs_and_fructose_physiology",
            "title": "High Fructose Corn Syrup and Fructose Physiology",
            "subtitle": "Match each item to its identity, key detail, and significance",
            "categories": ["Identity", "Key Detail", "Application or Significance"],
            "data": {
                "Alpha-amylase": {
                    "Identity": "Starch-digesting enzyme",
                    "Key Detail": "Hydrolyzes corn starch (glucose polymers) into free glucose",
                    "Application or Significance": "Produces conventional corn syrup"
                },
                "Glucose isomerase": {
                    "Identity": "Isomerase used only in HFCS production",
                    "Key Detail": "Converts free glucose into fructose",
                    "Application or Significance": "Turns corn syrup into high fructose corn syrup"
                },
                "HFCS-42": {
                    "Identity": "42% fructose formulation",
                    "Key Detail": "Remainder of the dry weight is glucose",
                    "Application or Significance": "Used in processed foods and cereals"
                },
                "HFCS-55": {
                    "Identity": "55% fructose formulation",
                    "Key Detail": "Higher fructose fraction than HFCS-42",
                    "Application or Significance": "Used extensively in soft drink formulation"
                },
                "Fructose": {
                    "Identity": "Monosaccharide metabolized almost entirely in the liver",
                    "Key Detail": "Low glycemic index (~20); no acute insulin spike",
                    "Application or Significance": "Bypasses PFK-1, promoting lipogenesis and weight gain"
                }
            }
        }
    ]
}
