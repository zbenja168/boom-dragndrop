BRICK = {
    "brick_num": 38,
    "brick_title": "Dyslipidemias, Lipid Storage Disorders, and other defects in Lipid Metabolism",
    "games": [
        {
            "slug": "fredrickson_types",
            "title": "Fredrickson Primary Dyslipidemias",
            "subtitle": "Match each familial dyslipidemia to its lipoprotein defect, elevated lipoprotein(s), and key clinical feature",
            "categories": ["Lipoprotein defect", "Elevated lipoprotein(s)", "Key clinical feature"],
            "data": {
                "Familial hyperchylomicronemia (type I)": {
                    "Lipoprotein defect": "Deficiency of LPL or apolipoprotein C-II",
                    "Elevated lipoprotein(s)": "Chylomicrons",
                    "Key clinical feature": "TGs often >1,000 mg/dL; pancreatitis, no increased heart disease"
                },
                "Familial hypercholesterolemia (type IIa)": {
                    "Lipoprotein defect": "Too few or absent LDL receptors",
                    "Elevated lipoprotein(s)": "LDL",
                    "Key clinical feature": "Very high LDL with normal TGs; early MI, xanthomas, arcus"
                },
                "Familial combined hyperlipidemia (type IIb)": {
                    "Lipoprotein defect": "Increased apo B-100 with decreased LDL receptors",
                    "Elevated lipoprotein(s)": "LDL and VLDL",
                    "Key clinical feature": "Most common primary disorder; high LDL, VLDL, TGs, low HDL"
                },
                "Familial dysbetalipoproteinemia (type III)": {
                    "Lipoprotein defect": "Apolipoprotein E defect",
                    "Elevated lipoprotein(s)": "IDL and chylomicron remnants",
                    "Key clinical feature": "Palmar xanthomas; premature atherosclerotic heart disease"
                },
                "Familial hypertriglyceridemia (type IV)": {
                    "Lipoprotein defect": "Hepatic overproduction of VLDL",
                    "Elevated lipoprotein(s)": "VLDL",
                    "Key clinical feature": "High TGs with low HDL; acute pancreatitis, weak atherosclerosis link"
                }
            }
        },
        {
            "slug": "lipoprotein_functions",
            "title": "Lipoprotein Transport Roles",
            "subtitle": "Match each lipoprotein to where it originates, its main cargo, and its destination or function",
            "categories": ["Origin", "Main cargo", "Destination / function"],
            "data": {
                "Chylomicrons": {
                    "Origin": "Intestinal enterocytes",
                    "Main cargo": "Dietary TGs, cholesterol, fat-soluble vitamins",
                    "Destination / function": "Deliver TGs from the gut to peripheral tissues"
                },
                "VLDL": {
                    "Origin": "Liver (de novo synthesis)",
                    "Main cargo": "Endogenous TGs made in the liver",
                    "Destination / function": "Deliver TGs to tissues including adipocytes"
                },
                "IDL": {
                    "Origin": "Remodeling of VLDL in circulation",
                    "Main cargo": "TGs and cholesterol",
                    "Destination / function": "Transitional form; TGs to tissues, cholesterol to liver"
                },
                "LDL": {
                    "Origin": "Further processing of IDL",
                    "Main cargo": "60%-70% of total cholesterol",
                    "Destination / function": "Deliver cholesterol from liver to tissues; cleared by LDL receptor"
                },
                "HDL": {
                    "Origin": "Liver and intestine",
                    "Main cargo": "Cholesterol and donated apolipoproteins",
                    "Destination / function": "Reverse transport of cholesterol from tissues to liver"
                }
            }
        },
        {
            "slug": "physical_findings",
            "title": "Lipid Deposits and Physical Findings",
            "subtitle": "Match each observable finding to its description and its associated disorder",
            "categories": ["Description / location", "Associated disorder"],
            "data": {
                "Palmar xanthoma": {
                    "Description / location": "Yellow-orange plaques along the palmar creases of the hands",
                    "Associated disorder": "Pathognomonic for familial dysbetalipoproteinemia (type III)"
                },
                "Tendon xanthoma": {
                    "Description / location": "Lipid deposits in tendons of hands, Achilles, and knees",
                    "Associated disorder": "Always indicates a familial lipid disorder"
                },
                "Corneal arcus": {
                    "Description / location": "Faint white ring of lipid deposited within the eye",
                    "Associated disorder": "Seen in familial hypercholesterolemia"
                },
                "Eruptive xanthoma": {
                    "Description / location": "Inflamed, oozing lesions from excess fat under the skin",
                    "Associated disorder": "Severe hypertriglyceridemia"
                },
                "Xanthelasma": {
                    "Description / location": "Xanthomas around the skin of the eyes",
                    "Associated disorder": "May occur even with normal lipid levels"
                },
                "Orange-yellow tonsils": {
                    "Description / location": "Enlarged tonsils with orange-yellow discoloration",
                    "Associated disorder": "Defining feature of Tangier disease"
                }
            }
        },
        {
            "slug": "molecular_players",
            "title": "Molecular Players in Lipid Handling",
            "subtitle": "Match each protein to its normal role, the disease seen when it fails, and the resulting lipid change",
            "categories": ["Normal function", "Disease when defective", "Lipid consequence"],
            "data": {
                "Lipoprotein lipase (LPL)": {
                    "Normal function": "Degrades circulating TGs on the endothelial surface to free fatty acids",
                    "Disease when defective": "Familial hyperchylomicronemia (type I)",
                    "Lipid consequence": "Very high TGs from impaired chylomicron clearance"
                },
                "Apolipoprotein E": {
                    "Normal function": "Donated by HDL to allow hepatic uptake of remnant particles",
                    "Disease when defective": "Familial dysbetalipoproteinemia (type III)",
                    "Lipid consequence": "Accumulation of IDL and chylomicron remnants"
                },
                "LDL receptor": {
                    "Normal function": "Clears LDL particles from the circulation into hepatocytes",
                    "Disease when defective": "Familial hypercholesterolemia (type IIa)",
                    "Lipid consequence": "Very high LDL cholesterol with normal TGs"
                },
                "PCSK9": {
                    "Normal function": "Binds LDL receptors and directs them to lysosomes for degradation",
                    "Disease when defective": "Familial hypercholesterolemia (gain-of-function)",
                    "Lipid consequence": "Fewer recycled receptors, raising circulating LDL"
                },
                "ABC1 transporter": {
                    "Normal function": "Promotes cholesterol efflux from peripheral tissue onto HDL",
                    "Disease when defective": "Tangier disease",
                    "Lipid consequence": "Low HDL and low total cholesterol with intracellular buildup"
                },
                "OCTN2 transporter (SLC22A5)": {
                    "Normal function": "Reabsorbs carnitine needed to import long-chain fatty acids",
                    "Disease when defective": "Primary systemic carnitine deficiency",
                    "Lipid consequence": "Urinary carnitine wasting and impaired beta-oxidation"
                }
            }
        }
    ]
}
