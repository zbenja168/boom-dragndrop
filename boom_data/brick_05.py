BRICK = {
    "brick_num": 5,
    "brick_title": "Metabolic Overview III: O2 Delivery (1 of 2)",
    "games": [
        {
            "slug": "rbc_structure_disorders",
            "title": "RBC Structure and Disorders",
            "subtitle": "Match each RBC feature or disorder to its defining property, mechanism, and clinical/lab clue",
            "categories": ["Defining Feature", "Mechanism / Consequence", "Clinical or Lab Clue"],
            "data": {
                "Normal biconcave disc": {
                    "Defining Feature": "Extra membrane and supporting cytoskeleton",
                    "Mechanism / Consequence": "Deforms through narrow vessels and maximizes gas diffusion",
                    "Clinical or Lab Clue": "Central pallor seen on light microscopy"
                },
                "Lack of organelles/nuclei": {
                    "Defining Feature": "Mature RBCs have no mitochondria or nucleus",
                    "Mechanism / Consequence": "Rely on glycolysis and lactate for ATP, sparing O2 for tissues",
                    "Clinical or Lab Clue": "Maximizes internal volume for hemoglobin"
                },
                "Sickle cell disease": {
                    "Defining Feature": "Glutamate replaced by valine in the beta chain",
                    "Mechanism / Consequence": "Low-solubility Hb polymerizes, distorting the cell into a crescent",
                    "Clinical or Lab Clue": "Painful vaso-occlusions and chronic fatigue"
                },
                "Hereditary spherocytosis": {
                    "Defining Feature": "Mutated cytoskeletal or membrane proteins",
                    "Mechanism / Consequence": "Rigid spheres form instead of biconcave discs",
                    "Clinical or Lab Clue": "Loss of central pallor and a positive osmotic fragility test"
                }
            }
        },
        {
            "slug": "cbc_values",
            "title": "CBC Values and Anemia",
            "subtitle": "Match each complete blood count measurement to what it measures, its units, and its clinical significance",
            "categories": ["What It Measures", "Typical Units", "Clinical Significance"],
            "data": {
                "RBC count": {
                    "What It Measures": "Number of red blood cells per microliter of blood",
                    "Typical Units": "x10^6 per microliter",
                    "Clinical Significance": "A low value is one of three criteria that define anemia"
                },
                "Hemoglobin concentration": {
                    "What It Measures": "Concentration of hemoglobin in whole blood",
                    "Typical Units": "grams per deciliter (g/dL)",
                    "Clinical Significance": "Reflects total oxygen-carrying capacity of the blood"
                },
                "Hematocrit (HCT)": {
                    "What It Measures": "Percentage of blood volume contributed by RBCs",
                    "Typical Units": "percent (%)",
                    "Clinical Significance": "Artificially raised by dehydration, lowered by blood loss"
                },
                "Mean corpuscular volume (MCV)": {
                    "What It Measures": "Average volume (size) of the red blood cells",
                    "Typical Units": "femtoliters (fL)",
                    "Clinical Significance": "Classifies anemia as microcytic, normocytic, or macrocytic"
                }
            }
        },
        {
            "slug": "oxygen_carrying_proteins",
            "title": "Oxygen-Carrying Proteins",
            "subtitle": "Match each oxygen-binding protein form to its composition, relative O2 affinity, and key feature",
            "categories": ["Composition / What Binds", "Relative O2 Affinity", "Key Feature or Location"],
            "data": {
                "Myoglobin (Mb)": {
                    "Composition / What Binds": "Single monomer with one heme group",
                    "Relative O2 Affinity": "Highest affinity of the three (P50 about 2.8)",
                    "Key Feature or Location": "Expressed in muscle tissue; hyperbolic curve, no cooperativity"
                },
                "Adult hemoglobin (HbA)": {
                    "Composition / What Binds": "Tetramer of two alpha and two beta chains",
                    "Relative O2 Affinity": "Lowest affinity of the three (P50 about 26)",
                    "Key Feature or Location": "Sigmoidal curve with cooperativity; main Hb in adult RBCs"
                },
                "Fetal hemoglobin (HbF)": {
                    "Composition / What Binds": "Tetramer of two alpha and two gamma chains",
                    "Relative O2 Affinity": "Intermediate; higher than HbA (curve shifted left)",
                    "Key Feature or Location": "Allows O2 exchange between mother and fetus (1-2% of adult Hb)"
                },
                "Carboxyhemoglobin (COHb)": {
                    "Composition / What Binds": "Carbon monoxide bound to the same heme site as O2",
                    "Relative O2 Affinity": "Pathologically increased for the little O2 still bound",
                    "Key Feature or Location": "CO binds over 200x tighter than O2, causing tissue hypoxia"
                }
            }
        },
        {
            "slug": "hb_affinity_modulators",
            "title": "Modulators of Hemoglobin O2 Affinity",
            "subtitle": "Match each condition to its direction of affinity change, curve shift, and physiologic context",
            "categories": ["Direction of Affinity Change", "Curve Shift and Result", "Mechanism or Context"],
            "data": {
                "Low pH (elevated H+)": {
                    "Direction of Affinity Change": "Decreases Hb affinity for oxygen",
                    "Curve Shift and Result": "Right shift, releasing more O2 to tissues",
                    "Mechanism or Context": "Bohr effect; protonated histidines stabilize low-affinity Hb"
                },
                "Increased 2,3-BPG": {
                    "Direction of Affinity Change": "Decreases Hb affinity for oxygen",
                    "Curve Shift and Result": "Right shift, unloading more O2 in the periphery",
                    "Mechanism or Context": "Made from 1,3-BPG by BPG mutase in the Rapoport-Luebering shunt"
                },
                "High temperature": {
                    "Direction of Affinity Change": "Decreases Hb affinity for oxygen",
                    "Curve Shift and Result": "Right shift, favoring rapid dissociation",
                    "Mechanism or Context": "Increased kinetic energy aids a physically active muscle"
                },
                "Respiratory alkalosis": {
                    "Direction of Affinity Change": "Increases Hb affinity for oxygen",
                    "Curve Shift and Result": "Left shift, decreasing delivery to peripheral tissues",
                    "Mechanism or Context": "Hyperventilation blows off CO2, losing H+ and CO2 regulators"
                },
                "Carbon monoxide": {
                    "Direction of Affinity Change": "Increases Hb affinity for oxygen",
                    "Curve Shift and Result": "Left shift, compounding tissue hypoxia",
                    "Mechanism or Context": "Forms carboxyhemoglobin by competing at the heme O2 site"
                }
            }
        }
    ]
}
