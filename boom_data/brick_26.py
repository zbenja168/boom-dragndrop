BRICK = {
    "brick_num": 26,
    "brick_title": "Overview of Cell Signaling (2 of 2)",
    "games": [
        {
            "slug": "receptor_pathways",
            "title": "Receptor Signaling Pathways",
            "subtitle": "Match each signaling system to its ligand, core mechanism, and gene-activating effector",
            "categories": ["Ligand / Trigger", "Core Mechanism", "Gene-Activating Effector"],
            "data": {
                "Receptor tyrosine kinase (RTK)": {
                    "Ligand / Trigger": "Epidermal growth factor (EGF)",
                    "Core Mechanism": "Ligand dimerizes monomers; intrinsic kinase autophosphorylates receptor",
                    "Gene-Activating Effector": "Grb2 activates Ras, driving MAPK/Erk gene expression"
                },
                "Serine/threonine receptor kinase": {
                    "Ligand / Trigger": "Transforming growth factor-beta (TGF-beta)",
                    "Core Mechanism": "Ligand heterodimerizes subunits, activating receptor kinase",
                    "Gene-Activating Effector": "Phosphorylated SMAD proteins translocate to nucleus"
                },
                "JAK-STAT pathway": {
                    "Ligand / Trigger": "Cytokines such as erythropoietin (EPO)",
                    "Core Mechanism": "Receptor lacks intrinsic kinase; associated JAK phosphorylates it",
                    "Gene-Activating Effector": "Dimerized STAT translocates to nucleus as transcription factor"
                },
                "NF-kB pathway": {
                    "Ligand / Trigger": "Tumor necrosis factor-alpha (TNF-alpha)",
                    "Core Mechanism": "IKK phosphorylates IkB, marking it for proteasomal degradation",
                    "Gene-Activating Effector": "Liberated NF-kB (p50/p65) translocates to nucleus"
                },
                "Wnt / Frizzled pathway": {
                    "Ligand / Trigger": "Wnt glycoprotein binding the Frizzled GPCR",
                    "Core Mechanism": "Dishevelled inhibits the Axin/APC/GSK-3beta destruction complex",
                    "Gene-Activating Effector": "Stabilized beta-catenin enters nucleus to promote transcription"
                }
            }
        },
        {
            "slug": "signaling_diseases",
            "title": "When Signaling Goes Awry",
            "subtitle": "Match each disease to its molecular defect, affected gene/protein, and clinical feature",
            "categories": ["Molecular Defect", "Affected Gene / Protein", "Clinical Feature"],
            "data": {
                "Polycythemia vera": {
                    "Molecular Defect": "Activating mutation constitutively turns on the kinase",
                    "Affected Gene / Protein": "JAK2 (V617F)",
                    "Clinical Feature": "RBC overproduction with pruritus after a hot shower"
                },
                "Chronic myeloid leukemia": {
                    "Molecular Defect": "t(9;22) fusion yields a constitutively active kinase",
                    "Affected Gene / Protein": "BCR-ABL fusion (Philadelphia chromosome)",
                    "Clinical Feature": "Immune-cell cancer treated effectively with imatinib"
                },
                "McCune-Albright syndrome": {
                    "Molecular Defect": "Constitutive activation overstimulates adenylate cyclase and cAMP",
                    "Affected Gene / Protein": "GNAS encoding G-alpha-s",
                    "Clinical Feature": "Precocious puberty, cafe-au-lait spots, and fibrous dysplasia"
                },
                "Achondroplasia": {
                    "Molecular Defect": "Activating mutation causes autophosphorylation without ligand",
                    "Affected Gene / Protein": "FGFR-3 receptor tyrosine kinase",
                    "Clinical Feature": "Short-limbed dwarfism with rhizomelic shortening, normal intelligence"
                },
                "HER2-positive breast cancer": {
                    "Molecular Defect": "Gene amplification/duplication overexpresses a pro-growth receptor",
                    "Affected Gene / Protein": "HER2 receptor tyrosine kinase",
                    "Clinical Feature": "Aggressive breast tumor targeted by monoclonal antibody therapy"
                }
            }
        },
        {
            "slug": "adhesion_receptors",
            "title": "Cell Surface Adhesion Receptors",
            "subtitle": "Match each adhesion molecule to its source cell, binding partner, and key role or disease",
            "categories": ["Source / Expressing Cell", "Binding Partner", "Key Role or Disease"],
            "data": {
                "Integrin (LFA-1 / CD18)": {
                    "Source / Expressing Cell": "Leukocytes",
                    "Binding Partner": "Extracellular matrix and vascular endothelium",
                    "Key Role or Disease": "Defect causes leukocyte adhesion deficiency (LAD)"
                },
                "L-selectin": {
                    "Source / Expressing Cell": "Leukocytes ('L' for leukocyte)",
                    "Binding Partner": "Ligands on inflamed endothelium",
                    "Key Role or Disease": "Lets leukocytes hook onto vessels near inflammation"
                },
                "E-selectin": {
                    "Source / Expressing Cell": "Endothelial cells ('E' for endothelial)",
                    "Binding Partner": "Circulating leukocytes",
                    "Key Role or Disease": "Expressed near inflammatory reactions to recruit cells"
                },
                "P-selectin": {
                    "Source / Expressing Cell": "Platelets ('P') and endothelial cells",
                    "Binding Partner": "Passing leukocytes in blood vessels",
                    "Key Role or Disease": "Enables leukocyte extravasation into inflamed tissue"
                },
                "E-cadherin": {
                    "Source / Expressing Cell": "Epithelial cells",
                    "Binding Partner": "Cadherin on the neighboring cell (transbinding)",
                    "Key Role or Disease": "Sequesters beta-catenin; its loss drives EMT in cancer"
                }
            }
        },
        {
            "slug": "nfkb_tnf",
            "title": "NF-kB / TNF-alpha Cascade and Therapeutics",
            "subtitle": "Match each component or drug to its identity, cascade role, and clinical note",
            "categories": ["Identity", "Role in the Cascade", "Clinical Note"],
            "data": {
                "TNF-alpha": {
                    "Identity": "Trimeric pro-inflammatory cytokine",
                    "Role in the Cascade": "Binds TNFR-1 to initiate NF-kB activation",
                    "Clinical Note": "Excess in synovial joints drives rheumatoid arthritis"
                },
                "IkB": {
                    "Identity": "Inhibitor of kappa-B protein",
                    "Role in the Cascade": "Sequesters NF-kB in the cytoplasm until degraded",
                    "Clinical Note": "Ubiquitinated and destroyed by the proteasome after IKK acts"
                },
                "IKK complex": {
                    "Identity": "IkB kinase (IKK-alpha, -beta, -gamma)",
                    "Role in the Cascade": "Phosphorylates IkB upon receptor activation",
                    "Clinical Note": "Post-translational mark that frees NF-kB for signaling"
                },
                "NF-kB (p50/p65)": {
                    "Identity": "Heterodimeric transcription factor",
                    "Role in the Cascade": "p50 binds DNA; p65 provides transactivation domain",
                    "Clinical Note": "Regulates immune response, inflammation, and cell survival"
                },
                "Adalimumab (Humira)": {
                    "Identity": "Monoclonal antibody",
                    "Role in the Cascade": "Binds soluble circulating TNF-alpha with high affinity",
                    "Clinical Note": "Immunosuppression raises risk of common infections"
                },
                "Etanercept (Enbrel)": {
                    "Identity": "Recombinant soluble decoy receptor",
                    "Role in the Cascade": "Mimics shed TNFR-1 to intercept TNF-alpha before the cell",
                    "Clinical Note": "Not membrane-bound, so it dampens the inflammatory response"
                }
            }
        }
    ]
}
