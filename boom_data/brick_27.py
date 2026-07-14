BRICK = {
    "brick_num": 27,
    "brick_title": "Cell Signaling in Context: Fed and Fasting Metabolic State",
    "games": [
        {
            "slug": "metabolic_hormones",
            "title": "Metabolic Hormones",
            "subtitle": "Match each hormone to its source, metabolic role, and signaling cascade",
            "categories": ["Source", "Metabolic Role", "Signaling Cascade"],
            "data": {
                "Insulin": {
                    "Source": "Pancreatic beta-cells (rising glucose)",
                    "Metabolic Role": "Anabolic: promotes fuel storage after a meal",
                    "Signaling Cascade": "PI3-kinase to PKB/Akt to protein phosphatases"
                },
                "Glucagon": {
                    "Source": "Pancreatic alpha-cells (falling glucose)",
                    "Metabolic Role": "Catabolic: mobilizes hepatic fuel during fasting",
                    "Signaling Cascade": "GPCR to adenylate cyclase to cAMP to PKA"
                },
                "Epinephrine": {
                    "Source": "Stress (fight-or-flight) hormone",
                    "Metabolic Role": "Mobilizes fuel in acute stress, independent of blood glucose",
                    "Signaling Cascade": "Alpha/beta adrenergic GPCRs to cAMP to PKA"
                },
                "Cortisol": {
                    "Source": "Steroid stress hormone",
                    "Metabolic Role": "Provides fuel for changing requirements during stress",
                    "Signaling Cascade": "Binds intracellular receptor to alter gene expression"
                }
            }
        },
        {
            "slug": "muscle_glycogen_regulators",
            "title": "Regulators of Muscle Glycogen Phosphorylase",
            "subtitle": "Match each signal to its origin, mediator, and effect on glycogen phosphorylase",
            "categories": ["Origin / Trigger", "Second Messenger or Mediator", "Effect on Glycogen Phosphorylase"],
            "data": {
                "Epinephrine": {
                    "Origin / Trigger": "Circulating adrenal hormone binding a GPCR",
                    "Second Messenger or Mediator": "cAMP activating PKA",
                    "Effect on Glycogen Phosphorylase": "Activates it via phosphorylase kinase"
                },
                "AMP": {
                    "Origin / Trigger": "Made by adenylate kinase during muscle contraction",
                    "Second Messenger or Mediator": "AMP itself acting allosterically",
                    "Effect on Glycogen Phosphorylase": "Directly activates the inactive enzyme"
                },
                "Calcium ion": {
                    "Origin / Trigger": "Released from sarcoplasmic reticulum on a nerve impulse",
                    "Second Messenger or Mediator": "Ca2+ bound to calmodulin",
                    "Effect on Glycogen Phosphorylase": "Activates it by promoting phosphorylase kinase"
                },
                "Insulin": {
                    "Origin / Trigger": "Rises in the fed state after a meal",
                    "Second Messenger or Mediator": "PI3-kinase activating protein phosphatase",
                    "Effect on Glycogen Phosphorylase": "Inhibits it through dephosphorylation"
                }
            }
        },
        {
            "slug": "organ_fuel_sources",
            "title": "Organ Fuel Sources Across Metabolic States",
            "subtitle": "Match each tissue to its predominant fuel in each metabolic state",
            "categories": ["Well-Fed", "Fasting", "Prolonged Fasting"],
            "data": {
                "Liver": {
                    "Well-Fed": "Predominately glucose",
                    "Fasting": "Fatty acids",
                    "Prolonged Fasting": "Fatty acids"
                },
                "Resting skeletal muscle": {
                    "Well-Fed": "Glucose",
                    "Fasting": "Fatty acids and ketone bodies",
                    "Prolonged Fasting": "More fatty acids, less ketone bodies"
                },
                "Cardiac muscle": {
                    "Well-Fed": "Fatty acids",
                    "Fasting": "Fatty acids and ketone bodies",
                    "Prolonged Fasting": "More fatty acids, less ketone bodies"
                },
                "Brain": {
                    "Well-Fed": "Glucose",
                    "Fasting": "Glucose",
                    "Prolonged Fasting": "Ketone bodies"
                },
                "Adipocytes": {
                    "Well-Fed": "Glucose",
                    "Fasting": "Fatty acids",
                    "Prolonged Fasting": "Fatty acids"
                },
                "Red blood cells": {
                    "Well-Fed": "Glucose",
                    "Fasting": "Glucose",
                    "Prolonged Fasting": "Glucose"
                }
            }
        },
        {
            "slug": "fuel_metabolism_enzymes",
            "title": "Key Enzymes of Fuel Metabolism",
            "subtitle": "Match each enzyme to its tissue, reaction, and regulatory point",
            "categories": ["Tissue", "Reaction / Function", "Key Regulatory Point"],
            "data": {
                "Glucose 6-phosphatase": {
                    "Tissue": "Liver (absent in skeletal muscle)",
                    "Reaction / Function": "Converts glucose 6-phosphate to free glucose",
                    "Key Regulatory Point": "Enables hepatic glucose export via GLUT2; deficient in Von Gierke disease"
                },
                "Glycerol kinase": {
                    "Tissue": "Liver only (absent in adipocytes)",
                    "Reaction / Function": "Reversibly converts glycerol to glycerol 3-phosphate",
                    "Key Regulatory Point": "Lets liver use glycerol for gluconeogenesis or VLDL"
                },
                "Hormone-sensitive lipase": {
                    "Tissue": "Adipocytes",
                    "Reaction / Function": "Hydrolyzes triglycerides to glycerol plus 3 fatty acids",
                    "Key Regulatory Point": "Activated by glucagon/epinephrine (PKA), inhibited by insulin"
                },
                "Glycogen synthase": {
                    "Tissue": "Liver and skeletal muscle",
                    "Reaction / Function": "Builds glycogen from glucose (anabolic)",
                    "Key Regulatory Point": "Activated by insulin (dephosphorylation), inhibited by glucagon (phosphorylation)"
                },
                "Glycogen phosphorylase": {
                    "Tissue": "Liver and skeletal muscle",
                    "Reaction / Function": "Degrades glycogen to glucose (glycogenolysis)",
                    "Key Regulatory Point": "Activated by phosphorylation, AMP, and Ca2+-calmodulin"
                }
            }
        }
    ]
}
