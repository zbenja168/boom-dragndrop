BRICK = {
    "brick_num": 22,
    "brick_title": "Lipids and Lipid Metabolism Introduction",
    "games": [
        {
            "slug": "plasma_lipoproteins",
            "title": "Plasma Lipoproteins",
            "subtitle": "Match each lipoprotein to its origin, relative lipid content, and main function",
            "categories": ["Origin", "Relative Lipid Content", "Main Function"],
            "data": {
                "Chylomicron": {
                    "Origin": "Small intestine (enterocytes)",
                    "Relative Lipid Content": "Highest triglyceride, lowest cholesterol",
                    "Main Function": "Delivers dietary triglycerides from gut to peripheral tissues"
                },
                "VLDL": {
                    "Origin": "Liver",
                    "Relative Lipid Content": "High triglyceride, low cholesterol",
                    "Main Function": "Delivers endogenous hepatic triglycerides to peripheral tissues"
                },
                "LDL": {
                    "Origin": "Formed in circulation from VLDL",
                    "Relative Lipid Content": "Low triglyceride, highest cholesterol",
                    "Main Function": "Delivers hepatic cholesterol to peripheral tissues"
                },
                "HDL": {
                    "Origin": "Liver and intestine",
                    "Relative Lipid Content": "Lowest triglyceride, high cholesterol",
                    "Main Function": "Reverse cholesterol transport from peripheral tissues to liver"
                }
            }
        },
        {
            "slug": "apolipoproteins",
            "title": "Apolipoproteins",
            "subtitle": "Match each apolipoprotein to the particles it associates with, its origin, and its function",
            "categories": ["Lipoprotein Association", "Origin", "Function"],
            "data": {
                "apoA-I": {
                    "Lipoprotein Association": "HDL, chylomicrons",
                    "Origin": "Liver and intestine",
                    "Function": "Activates lecithin-cholesterol acyltransferase (LCAT) on HDL"
                },
                "apoB-48": {
                    "Lipoprotein Association": "Chylomicrons only",
                    "Origin": "Intestine",
                    "Function": "Structural protein obligate for chylomicron assembly and exit"
                },
                "apoB-100": {
                    "Lipoprotein Association": "VLDL and LDL",
                    "Origin": "Liver",
                    "Function": "Structural protein containing the LDL-receptor binding domain"
                },
                "apoC-II": {
                    "Lipoprotein Association": "HDL, VLDL, chylomicrons",
                    "Origin": "Liver (stored on HDL)",
                    "Function": "Activates extrahepatic lipoprotein lipase (LPL)"
                },
                "apoE": {
                    "Lipoprotein Association": "HDL, VLDL, chylomicrons",
                    "Origin": "Liver (stored on HDL)",
                    "Function": "Mediates hepatic uptake of chylomicron and IDL remnants"
                }
            }
        },
        {
            "slug": "lipid_enzymes",
            "title": "Enzymes of Lipid Digestion and Transport",
            "subtitle": "Match each enzyme to its site of action, substrate, and product or role",
            "categories": ["Site of Action", "Substrate", "Product or Key Role"],
            "data": {
                "Lingual and gastric lipase": {
                    "Site of Action": "Mouth and stomach",
                    "Substrate": "Dietary triglycerides (milk fats)",
                    "Product or Key Role": "Release SCFAs and MCFAs; minor role in TG digestion"
                },
                "Pancreatic lipase": {
                    "Site of Action": "Small intestine lumen",
                    "Substrate": "Dietary triglycerides",
                    "Product or Key Role": "Free LCFAs plus 2-monoacylglycerol; major role in TG digestion"
                },
                "ACAT": {
                    "Site of Action": "Inside enterocytes (intracellular, ER)",
                    "Substrate": "Dietary (intracellular) cholesterol",
                    "Product or Key Role": "Forms cholesteryl esters for packing into lipoproteins"
                },
                "LCAT": {
                    "Site of Action": "Plasma, on circulating HDL",
                    "Substrate": "Endogenous circulating cholesterol",
                    "Product or Key Role": "Forms cholesteryl esters; activated by apoA-I"
                },
                "Lipoprotein lipase (LPL)": {
                    "Site of Action": "Extrahepatic capillary endothelium",
                    "Substrate": "Chylomicron and VLDL triglycerides",
                    "Product or Key Role": "Frees fatty acids for tissue uptake; activated by apoC-II"
                },
                "CETP": {
                    "Site of Action": "Plasma, between VLDL and HDL",
                    "Substrate": "VLDL triglycerides and HDL cholesteryl esters",
                    "Product or Key Role": "Swaps the two lipids and promotes LDL formation from VLDL"
                }
            }
        },
        {
            "slug": "fa_synthesis_degradation",
            "title": "Fatty Acid Synthesis and Degradation",
            "subtitle": "Match each process to its cellular location, key enzyme, and cofactor or regulation",
            "categories": ["Cellular Location", "Key Enzyme", "Cofactor or Regulation"],
            "data": {
                "Fatty acid synthesis": {
                    "Cellular Location": "Cytosol of hepatocytes",
                    "Key Enzyme": "Acetyl-CoA carboxylase (rate-limiting), then fatty acid synthase",
                    "Cofactor or Regulation": "Biotin cofactor; activated by insulin and citrate, inhibited by palmitoyl-CoA"
                },
                "Citrate shuttle": {
                    "Cellular Location": "Mitochondrial matrix to cytosol",
                    "Key Enzyme": "Citrate lyase (regenerates cytosolic acetyl-CoA)",
                    "Cofactor or Regulation": "Exports acetyl-CoA units for fatty acid biosynthesis"
                },
                "Carnitine shuttle": {
                    "Cellular Location": "Inner mitochondrial membrane",
                    "Key Enzyme": "Carnitine acyltransferase / palmitoyltransferase (CPT1 and CPT2)",
                    "Cofactor or Regulation": "Transports LCFAs inward; CPT1 inhibited by malonyl-CoA"
                },
                "Beta-oxidation": {
                    "Cellular Location": "Mitochondrial matrix",
                    "Key Enzyme": "Acyl-CoA dehydrogenases (SCAD, MCAD, LCAD)",
                    "Cofactor or Regulation": "Cleaves two carbons per cycle yielding acetyl-CoA"
                },
                "Very-long-chain FA oxidation": {
                    "Cellular Location": "Peroxisome (initial rounds)",
                    "Key Enzyme": "Peroxisomal fatty acyl-CoA dehydrogenase for VLCFAs",
                    "Cofactor or Regulation": "Shortens chains of 22+ carbons before mitochondrial oxidation"
                },
                "Odd-chain FA finishing": {
                    "Cellular Location": "Mitochondrial matrix",
                    "Key Enzyme": "Methylmalonyl-CoA mutase",
                    "Cofactor or Regulation": "Cobalamin (B12) converts propionyl-CoA to succinyl-CoA"
                }
            }
        }
    ]
}
