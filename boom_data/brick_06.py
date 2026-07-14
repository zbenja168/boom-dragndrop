BRICK = {
    "brick_num": 6,
    "brick_title": "BOOM: Metabolic Overview III - O2 Delivery (2 of 2): Anemia, MCV Classification, and the B Vitamins",
    "games": [
        {
            "slug": "bvitamins_and_anemia",
            "title": "B Vitamins and the Nutritional Anemias",
            "subtitle": "Match each B vitamin to the anemia it causes, its metabolic defect, and a diagnostic clue",
            "categories": ["MCV Classification", "Underlying Metabolic Defect", "Diagnostic / Key Clue"],
            "data": {
                "Riboflavin (B2)": {
                    "MCV Classification": "Normocytic (macrocytic only if extremely severe)",
                    "Underlying Metabolic Defect": "Impaired maximal iron absorption; riboflavin is the core of FMN/FAD flavoproteins",
                    "Diagnostic / Key Clue": "Erythrocyte glutathione reductase activity ratio above 1.2"
                },
                "Pyridoxine (B6)": {
                    "MCV Classification": "Microcytic",
                    "Underlying Metabolic Defect": "PLP is the coenzyme for the first step of porphyrin (heme) synthesis, limiting Hb",
                    "Diagnostic / Key Clue": "Provoked by isoniazid; classically paired with sensory neuropathy"
                },
                "Folate (B9)": {
                    "MCV Classification": "Macrocytic",
                    "Underlying Metabolic Defect": "One-carbon donor for purine and thymidine synthesis; deficiency stalls DNA production",
                    "Diagnostic / Key Clue": "Elevated homocysteine with NORMAL methylmalonic acid (MMA)"
                },
                "Cobalamin (B12)": {
                    "MCV Classification": "Macrocytic",
                    "Underlying Metabolic Defect": "Recycles methyl-FH4 back to folate (methyl trap) and converts methylmalonyl-CoA to succinyl-CoA",
                    "Diagnostic / Key Clue": "Elevated homocysteine AND elevated MMA, plus peripheral neuropathy"
                }
            }
        },
        {
            "slug": "cobalamin_absorption",
            "title": "Cobalamin (B12) Absorption and Transport",
            "subtitle": "Match each player in the B12 pathway to where it acts, its job, and its clinical link",
            "categories": ["Origin / Location", "Function in B12 Handling", "Clinical Note"],
            "data": {
                "R-binders": {
                    "Origin / Location": "Secreted by gastric mucosa",
                    "Function in B12 Handling": "Shield dietary B12 from the acidic, enzyme-rich stomach environment",
                    "Clinical Note": "Sacrificially degraded so that B12 is preserved"
                },
                "Intrinsic factor (IF)": {
                    "Origin / Location": "Secreted by parietal cells of the stomach",
                    "Function in B12 Handling": "Escorts B12 through the gut for absorption and resists pancreatic proteases",
                    "Clinical Note": "Target of autoantibodies in pernicious anemia"
                },
                "Pancreatic proteases": {
                    "Origin / Location": "Released by the exocrine pancreas",
                    "Function in B12 Handling": "Degrade the R-binder so B12 can be handed off to intrinsic factor",
                    "Clinical Note": "Pancreatic insufficiency can impair B12 release"
                },
                "Transcobalamin II": {
                    "Origin / Location": "Carrier protein in the bloodstream",
                    "Function in B12 Handling": "Transports absorbed B12, roughly 50% to liver and 50% to other tissues",
                    "Clinical Note": "Liver holds a 3-6 year reserve of cobalamin"
                },
                "Terminal ileum": {
                    "Origin / Location": "Distal segment of the small intestine",
                    "Function in B12 Handling": "Site where the IF-B12 complex is actually absorbed",
                    "Clinical Note": "Crohn disease or resection here causes B12 deficiency"
                }
            }
        },
        {
            "slug": "one_carbon_players",
            "title": "One-Carbon Metabolism: Cofactors and Reactions",
            "subtitle": "Match each molecule to the reaction it drives and the effect of losing it",
            "categories": ["Molecular Identity", "Reaction / Role", "Deficiency or Inhibition Effect"],
            "data": {
                "Methyl-cobalamin": {
                    "Molecular Identity": "Methyl form of vitamin B12",
                    "Reaction / Role": "Converts homocysteine to methionine, regenerating FH4 from methyl-FH4",
                    "Deficiency or Inhibition Effect": "Methyl trap: folate stays trapped, homocysteine rises, macrocytic anemia"
                },
                "Deoxyadenosyl-cobalamin": {
                    "Molecular Identity": "Adenosyl form of vitamin B12",
                    "Reaction / Role": "Converts methylmalonyl-CoA to succinyl-CoA, feeding the TCA cycle (folate-independent)",
                    "Deficiency or Inhibition Effect": "Elevated MMA, a marker unique to B12 deficiency"
                },
                "Tetrahydrofolate (FH4)": {
                    "Molecular Identity": "Reduced, active carrier form of folate",
                    "Reaction / Role": "Donates one-carbon units for purine and thymidine (DNA) synthesis",
                    "Deficiency or Inhibition Effect": "Macrocytic anemia with elevated homocysteine and urinary FIGLU"
                },
                "Dihydrofolate reductase (DHFR)": {
                    "Molecular Identity": "Enzyme that reduces folate",
                    "Reaction / Role": "Reduces dietary folate to tetrahydrofolate (FH4), the usable form",
                    "Deficiency or Inhibition Effect": "Blocked by the antifolate methotrexate, halting DNA synthesis"
                }
            }
        },
        {
            "slug": "deficiency_causes",
            "title": "Predisposing Factors for B9 / B12 Deficiency",
            "subtitle": "Match each risk factor to its mechanism, the vitamin at risk, and a key detail",
            "categories": ["Mechanism", "Primary Vitamin at Risk", "Key Detail"],
            "data": {
                "Chronic alcohol use": {
                    "Mechanism": "Denatures GI proteins and damages the gut lining, plus accompanying malnutrition",
                    "Primary Vitamin at Risk": "Folate (B9) first",
                    "Key Detail": "Folate depletes earlier than B12 because of its small body stores"
                },
                "Pernicious anemia": {
                    "Mechanism": "Autoantibodies against parietal cells and/or intrinsic factor block absorption",
                    "Primary Vitamin at Risk": "Cobalamin (B12)",
                    "Key Detail": "Disproportionately affects women, usually after age 60"
                },
                "Nitrous oxide abuse": {
                    "Mechanism": "N2O binds the cobalt ion, rendering cobalamin inert",
                    "Primary Vitamin at Risk": "Cobalamin (B12)",
                    "Key Detail": "Inactivates both dietary and hepatic-stored B12; increasingly seen in clinic"
                },
                "Methotrexate therapy": {
                    "Mechanism": "Structural folate analogue that inhibits DHFR",
                    "Primary Vitamin at Risk": "Folate (B9)",
                    "Key Detail": "Antifolate class emerged from Sidney Farber's leukemia work"
                },
                "Proton pump inhibitor overuse": {
                    "Mechanism": "Low gastric acid leaves B12 bound to dietary protein",
                    "Primary Vitamin at Risk": "Cobalamin (B12)",
                    "Key Detail": "Acid is needed to denature food protein and activate proteases"
                }
            }
        }
    ]
}
