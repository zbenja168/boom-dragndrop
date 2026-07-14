BRICK = {
    "brick_num": 24,
    "brick_title": "BOOM: Lipids and Lipid Metabolism Introduction (3 of 3) - Arachidonic Acid and Eicosanoids",
    "games": [
        {
            "slug": "aa_pathway_enzymes",
            "title": "Enzymes of the Arachidonic Acid Pathway",
            "subtitle": "Match each enzyme to the reaction it catalyzes, its product, and how it is regulated",
            "categories": ["Reaction / Substrate", "Product", "Regulation"],
            "data": {
                "Phospholipase A2 (PLA2)": {
                    "Reaction / Substrate": "Cleaves membrane phospholipids at the sn-2 site",
                    "Product": "Releases free arachidonic acid",
                    "Regulation": "Released by neutrophils/macrophages; blocked by glucocorticoids"
                },
                "Cyclooxygenase-1 (COX-1)": {
                    "Reaction / Substrate": "Oxidizes arachidonic acid; constitutively expressed",
                    "Product": "PGH2, then thromboxane A2 and prostaglandins",
                    "Regulation": "Maintains homeostasis; irreversibly acetylated by aspirin"
                },
                "Cyclooxygenase-2 (COX-2)": {
                    "Reaction / Substrate": "Oxidizes arachidonic acid; inducible in inflammation",
                    "Product": "PGH2, then prostaglandins such as PGE2 and PGI2",
                    "Regulation": "Induced by tissue injury; target of selective COX-2 inhibitors"
                },
                "Lipoxygenase (LOX)": {
                    "Reaction / Substrate": "Oxidizes arachidonic acid down the alternative branch",
                    "Product": "Leukotrienes",
                    "Regulation": "Not inhibited by NSAIDs; suppressed indirectly by steroids"
                }
            }
        },
        {
            "slug": "pathway_lipids",
            "title": "Lipid Molecules of the Pathway",
            "subtitle": "Match each lipid molecule to its classification, a defining structural feature, and its source or role",
            "categories": ["Classification", "Structural Feature", "Source or Role"],
            "data": {
                "Arachidonic acid": {
                    "Classification": "Omega-6 polyunsaturated fatty acid",
                    "Structural Feature": "20 carbons; first double bond on the 6th carbon from the methyl end",
                    "Source or Role": "Precursor of eicosanoids; from meat, eggs, fish or linoleic acid"
                },
                "Docosahexaenoic acid (DHA)": {
                    "Classification": "Omega-3 polyunsaturated fatty acid",
                    "Structural Feature": "First double bond on the 3rd carbon from the methyl end",
                    "Source or Role": "Anti-inflammatory; enriched in tuna and salmon"
                },
                "Linoleic acid": {
                    "Classification": "Essential omega-6 fatty acid",
                    "Structural Feature": "Cannot be synthesized by the body, so must be ingested",
                    "Source or Role": "Dietary precursor from which arachidonic acid is made"
                },
                "Eicosanoids": {
                    "Classification": "20-carbon lipid signaling molecules",
                    "Structural Feature": "Ligands for G-protein coupled receptors with a 10 s to 5 min half-life",
                    "Source or Role": "Act locally near their site of synthesis"
                }
            }
        },
        {
            "slug": "aa_pathway_drugs",
            "title": "Agents That Modulate the Pathway",
            "subtitle": "Match each drug or drug class to its enzyme target, its mechanism, and its key clinical feature",
            "categories": ["Enzyme Target", "Mechanism", "Clinical Feature"],
            "data": {
                "Aspirin": {
                    "Enzyme Target": "COX-1 and COX-2 (active-site serine)",
                    "Mechanism": "Irreversible acetylation of the active site (suicide inhibitor)",
                    "Clinical Feature": "Antithrombotic; blocks platelet TXA2 for the platelet's lifespan"
                },
                "Ibuprofen": {
                    "Enzyme Target": "COX-1 and COX-2",
                    "Mechanism": "Reversible competitive inhibition",
                    "Clinical Feature": "Common over-the-counter NSAID for pain and inflammation"
                },
                "Indomethacin": {
                    "Enzyme Target": "COX with higher affinity for COX-1",
                    "Mechanism": "Potent reversible competitive inhibition",
                    "Clinical Feature": "Used for refractory inflammation; greater gastric toxicity"
                },
                "Glucocorticoids (e.g., prednisone)": {
                    "Enzyme Target": "Phospholipase A2 (upstream)",
                    "Mechanism": "Inhibit release of arachidonic acid from membranes",
                    "Clinical Feature": "Dampen both COX and LOX branches; side effects include high glucose and blood pressure"
                },
                "Leukotriene-receptor antagonists": {
                    "Enzyme Target": "Leukotriene receptors / LOX branch",
                    "Mechanism": "Block leukotriene signaling or formation",
                    "Clinical Feature": "Used to treat select forms of asthma"
                }
            }
        },
        {
            "slug": "eicosanoid_mediators",
            "title": "Eicosanoid Mediators and Their Actions",
            "subtitle": "Match each eicosanoid to the pathway that makes it, its main physiological action, and its clinical relevance",
            "categories": ["Source Pathway", "Physiological Action", "Clinical Relevance"],
            "data": {
                "Thromboxane A2 (TXA2)": {
                    "Source Pathway": "COX-1 in platelets",
                    "Physiological Action": "Promotes platelet aggregation, clot formation, and vasoconstriction",
                    "Clinical Relevance": "Blocked by low-dose aspirin for antithrombotic benefit"
                },
                "Prostacyclin (PGI2)": {
                    "Source Pathway": "COX-2 in vascular endothelium",
                    "Physiological Action": "Inhibits platelet aggregation and dilates blood vessels",
                    "Clinical Relevance": "Promotes the desired vasodilatory state in cardiovascular disease"
                },
                "Prostaglandin E2 (PGE2)": {
                    "Source Pathway": "COX pathway",
                    "Physiological Action": "Reduces gastric acid secretion and stimulates uterine contractions",
                    "Clinical Relevance": "Protects gastric mucosa; used for labor induction and postpartum hemorrhage"
                },
                "Prostaglandin F2-alpha (PGF2a)": {
                    "Source Pathway": "COX pathway",
                    "Physiological Action": "Stimulates pain receptors",
                    "Clinical Relevance": "Contributes to inflammatory pain"
                },
                "Leukotrienes": {
                    "Source Pathway": "LOX (lipoxygenase) pathway",
                    "Physiological Action": "Drive neutrophil chemotaxis, adhesion, and bronchoconstriction",
                    "Clinical Relevance": "Slow-reacting substance of anaphylaxis; targeted in asthma therapy"
                }
            }
        }
    ]
}
