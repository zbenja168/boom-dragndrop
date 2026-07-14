BRICK = {
    "brick_num": 36,
    "brick_title": "Porphyrins and Iron Homeostasis (2 of 2)",
    "games": [
        {
            "slug": "iron_handling_proteins",
            "title": "Iron-Handling Proteins",
            "subtitle": "Match each protein to its function, site of expression, and regulation",
            "categories": ["Function", "Site of Expression", "Regulation"],
            "data": {
                "Duodenal cytochrome B": {
                    "Function": "Reduces non-absorbable Fe3+ to absorbable Fe2+",
                    "Site of Expression": "Apical surface of intestinal enterocytes",
                    "Regulation": "Vitamin C dependent"
                },
                "Hephaestin": {
                    "Function": "Copper-dependent ferroxidase; oxidizes exported Fe2+ back to Fe3+ for transferrin loading",
                    "Site of Expression": "Small-intestine enterocytes; also colon, spleen, kidney",
                    "Regulation": "Upregulated in iron deficiency, downregulated when stores are high"
                },
                "Hepcidin": {
                    "Function": "Degrades ferroportin to reduce iron export from cells",
                    "Site of Expression": "Liver hepatocytes; detectable in serum",
                    "Regulation": "Induced by high iron and IL-6 inflammation; suppressed in anemia and hypoxia"
                },
                "Transferrin": {
                    "Function": "Main plasma protein that binds Fe3+ and delivers it to cells",
                    "Site of Expression": "Synthesized in liver; circulates in plasma",
                    "Regulation": "Inversely related to iron stores; increased in iron deficiency"
                },
                "Transferrin receptor (TfR)": {
                    "Function": "Mediates cellular uptake of iron-loaded transferrin by endocytosis",
                    "Site of Expression": "Ubiquitous but highest on erythroid precursors",
                    "Regulation": "Upregulated in iron deficiency; downregulated by high intracellular iron"
                },
                "Ferritin": {
                    "Function": "Main intracellular iron storage protein",
                    "Site of Expression": "Nearly all cell types, though levels vary",
                    "Regulation": "Appears in serum during times of iron overload"
                }
            }
        },
        {
            "slug": "heme_synthesis_enzymes",
            "title": "Heme Synthesis Pathway Enzymes",
            "subtitle": "Match each enzyme to its reaction, location, and clinical note",
            "categories": ["Reaction Catalyzed", "Subcellular Location", "Clinical Note"],
            "data": {
                "ALA synthase": {
                    "Reaction Catalyzed": "Succinyl-CoA + glycine to aminolevulinic acid (ALA)",
                    "Subcellular Location": "Mitochondria",
                    "Clinical Note": "Induced by alcohol/barbiturates/hypoxia; inhibited by glucose and heme"
                },
                "ALA dehydrase": {
                    "Reaction Catalyzed": "Aminolevulinic acid to porphobilinogen",
                    "Subcellular Location": "Cytosol",
                    "Clinical Note": "Early cytosolic step following ALA formation"
                },
                "Porphobilinogen deaminase": {
                    "Reaction Catalyzed": "Porphobilinogen to hydroxymethylbilane",
                    "Subcellular Location": "Cytosol",
                    "Clinical Note": "Deficiency causes acute intermittent porphyria (AIP)"
                },
                "Uroporphyrinogen III synthase": {
                    "Reaction Catalyzed": "Hydroxymethylbilane to uroporphyrinogen III",
                    "Subcellular Location": "Cytosol",
                    "Clinical Note": "Directs the pathway toward the usable type III isomer"
                },
                "Uroporphyrinogen decarboxylase": {
                    "Reaction Catalyzed": "Uroporphyrinogen III to coproporphyrinogen III",
                    "Subcellular Location": "Cytosol",
                    "Clinical Note": "Deficiency causes porphyria cutanea tarda (PCT)"
                },
                "Ferrochelatase": {
                    "Reaction Catalyzed": "Inserts Fe2+ into protoporphyrin IX to form heme",
                    "Subcellular Location": "Mitochondria",
                    "Clinical Note": "Partial deficiency causes erythropoietic protoporphyria (EPP)"
                }
            }
        },
        {
            "slug": "iron_studies",
            "title": "Reading Iron Studies",
            "subtitle": "Match each iron study to what it measures and its trend in deficiency vs overload",
            "categories": ["What It Measures", "Trend in Iron Deficiency", "Trend in Iron Overload"],
            "data": {
                "Serum iron": {
                    "What It Measures": "Amount of iron circulating in the serum",
                    "Trend in Iron Deficiency": "Decreased",
                    "Trend in Iron Overload": "Increased"
                },
                "Serum ferritin": {
                    "What It Measures": "Ferritin released from cells; reflects tissue iron stores",
                    "Trend in Iron Deficiency": "Decreased",
                    "Trend in Iron Overload": "Increased"
                },
                "Total iron binding capacity (TIBC)": {
                    "What It Measures": "Available non-iron-bound transferrin in blood",
                    "Trend in Iron Deficiency": "Increased",
                    "Trend in Iron Overload": "Decreased"
                },
                "Transferrin saturation": {
                    "What It Measures": "Percentage of transferrin binding sites occupied by iron",
                    "Trend in Iron Deficiency": "Decreased",
                    "Trend in Iron Overload": "Increased"
                }
            }
        },
        {
            "slug": "iron_homeostasis_disorders",
            "title": "Disorders of Iron Homeostasis",
            "subtitle": "Match each disorder to its underlying cause, effect on iron, and hallmark feature",
            "categories": ["Underlying Cause", "Effect on Body Iron", "Hallmark Feature"],
            "data": {
                "Hereditary hemochromatosis": {
                    "Underlying Cause": "HFE gene mutation lowering hepcidin activity",
                    "Effect on Body Iron": "Iron overload from excess dietary absorption",
                    "Hallmark Feature": "Bronze diabetes; classically men in their 40s-50s"
                },
                "Secondary hemochromatosis": {
                    "Underlying Cause": "Repeated transfusions, iron supplementation, or ineffective erythropoiesis",
                    "Effect on Body Iron": "Iron overload with no route for excretion",
                    "Hallmark Feature": "Supplement poisoning is a common cause of death in children under 6"
                },
                "Anemia of chronic disease": {
                    "Underlying Cause": "IL-6 driven inflammation raising hepcidin",
                    "Effect on Body Iron": "Iron trapped in stores with low circulating iron",
                    "Hallmark Feature": "Protective sequestration of iron away from pathogens"
                },
                "DMT-1 (SLC11A2) mutation": {
                    "Underlying Cause": "Inherited mutation trapping iron in endosomal vesicles",
                    "Effect on Body Iron": "Iron cannot reach transferrin; functional deficiency",
                    "Hallmark Feature": "Microcytic anemia from reduced heme and globin synthesis"
                },
                "Hemosiderosis": {
                    "Underlying Cause": "Local bleeding into tissue or abnormal RBC turnover",
                    "Effect on Body Iron": "Insoluble hemosiderin iron deposits build up in tissues",
                    "Hallmark Feature": "Darkened skin localized to the ankles and lower legs"
                }
            }
        }
    ]
}
