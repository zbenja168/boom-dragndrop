BRICK = {
    "brick_num": 25,
    "brick_title": "Overview of Cell Signaling",
    "games": [
        {
            "slug": "signaling_paradigms",
            "title": "Five Cell Signaling Paradigms",
            "subtitle": "Match each signaling paradigm to its signal range, transport route, and classic example",
            "categories": ["Signal Range", "Transport Route", "Classic Example"],
            "data": {
                "Juxtacrine": {
                    "Signal Range": "Adjacent, physically contacting cells",
                    "Transport Route": "Gap junctions or membrane-bound ligands",
                    "Classic Example": "Cardiomyocytes coordinating force via gap junctions"
                },
                "Paracrine": {
                    "Signal Range": "Nearby local cells",
                    "Transport Route": "Diffusion through local interstitial space",
                    "Classic Example": "Mast cell histamine causing nearby vasodilation"
                },
                "Autocrine": {
                    "Signal Range": "The secreting cell itself",
                    "Transport Route": "Ligand binds the cell's own receptors",
                    "Classic Example": "Activated T lymphocytes secreting self-acting growth factors"
                },
                "Endocrine": {
                    "Signal Range": "Distant target cells",
                    "Transport Route": "Carried through the bloodstream",
                    "Classic Example": "Luteinizing hormone surge from anterior pituitary"
                },
                "Synaptic": {
                    "Signal Range": "Postsynaptic cell across the cleft",
                    "Transport Route": "Neurotransmitter across the synaptic cleft",
                    "Classic Example": "Acetylcholine released at a neuronal synapse"
                }
            }
        },
        {
            "slug": "hormone_classes",
            "title": "Hormone Classes and Their Properties",
            "subtitle": "Match each hormone class to its solubility, biosynthetic source, receptor type, and examples",
            "categories": ["Solubility", "Synthesized From", "Receptor Type", "Example"],
            "data": {
                "Peptide/Protein hormones": {
                    "Solubility": "Hydrophilic",
                    "Synthesized From": "Prohormones needing further processing",
                    "Receptor Type": "Cell-surface receptors driving second messengers",
                    "Example": "Insulin, prolactin, follicle-stimulating hormone"
                },
                "Catecholamines": {
                    "Solubility": "Hydrophilic",
                    "Synthesized From": "The amino acid tyrosine",
                    "Receptor Type": "Cell-surface membrane receptors",
                    "Example": "Epinephrine, dopamine"
                },
                "Thyroid hormones": {
                    "Solubility": "Lipophilic",
                    "Synthesized From": "Iodinated tyrosine residues",
                    "Receptor Type": "Intracellular nuclear receptors",
                    "Example": "Triiodothyronine (T3), thyroxine"
                },
                "Steroid hormones": {
                    "Solubility": "Lipophilic",
                    "Synthesized From": "Cholesterol",
                    "Receptor Type": "Nuclear ligand-activated transcription factors",
                    "Example": "Cortisol, estrogen, testosterone"
                }
            }
        },
        {
            "slug": "receptor_pathways",
            "title": "Signaling Receptor and Pathway Types",
            "subtitle": "Match each receptor class to its activation mechanism, downstream effector, and typical ligand",
            "categories": ["Activation Mechanism", "Downstream Effector", "Typical Ligand"],
            "data": {
                "G protein-coupled receptor": {
                    "Activation Mechanism": "Seven-transmembrane receptor triggers Ga GDP-to-GTP exchange",
                    "Downstream Effector": "Adenylate cyclase producing cAMP, then PKA",
                    "Typical Ligand": "Epinephrine and glucagon"
                },
                "Ligand-gated ion channel": {
                    "Activation Mechanism": "Ligand binding opens a membrane ion pore",
                    "Downstream Effector": "Ion flux altering membrane potential",
                    "Typical Ligand": "GABA opening chloride channels"
                },
                "Receptor tyrosine kinase": {
                    "Activation Mechanism": "Ligand-induced dimerization and tyrosine autophosphorylation",
                    "Downstream Effector": "Adaptor proteins activating Ras/MAPK and PI3K",
                    "Typical Ligand": "Growth factors and insulin"
                },
                "Nuclear receptor": {
                    "Activation Mechanism": "Intracellular ligand binding with conformational change",
                    "Downstream Effector": "Direct DNA binding to regulate transcription",
                    "Typical Ligand": "Steroid hormones, thyroid hormone, vitamin D3"
                }
            }
        },
        {
            "slug": "second_messengers",
            "title": "Second Messengers",
            "subtitle": "Match each second messenger to how it is generated, its molecular target, and its cellular effect",
            "categories": ["Generated By", "Molecular Target", "Cellular Effect"],
            "data": {
                "cAMP": {
                    "Generated By": "Adenylate cyclase acting on ATP",
                    "Molecular Target": "Protein kinase A (PKA)",
                    "Cellular Effect": "Amplifies epinephrine and glucagon responses"
                },
                "cGMP": {
                    "Generated By": "Guanylate cyclase acting on GTP",
                    "Molecular Target": "Smooth muscle relaxation machinery",
                    "Cellular Effect": "Vasodilation; degraded by PDE-5"
                },
                "IP3": {
                    "Generated By": "Phospholipase C cleaving PIP2 (soluble product)",
                    "Molecular Target": "IP3 receptors on the ER/SR",
                    "Cellular Effect": "Releases intracellular calcium stores"
                },
                "DAG": {
                    "Generated By": "Phospholipase C cleaving PIP2 (membrane-anchored product)",
                    "Molecular Target": "Protein kinase C (PKC)",
                    "Cellular Effect": "Membrane-bound activation of downstream targets"
                },
                "Calcium ions": {
                    "Generated By": "Released from ER/SR stores",
                    "Molecular Target": "Calmodulin and protein kinase C",
                    "Cellular Effect": "Triggers muscle contraction and glycogen breakdown"
                },
                "Nitric oxide": {
                    "Generated By": "NO synthase acting on arginine",
                    "Molecular Target": "Cytosolic guanylate cyclase",
                    "Cellular Effect": "Smooth muscle relaxation and vasodilation"
                }
            }
        }
    ]
}
