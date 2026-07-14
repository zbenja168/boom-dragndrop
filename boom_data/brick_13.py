BRICK = {
    "brick_num": 13,
    "brick_title": "Proteins, Enzymatic Machines and Introduction to Protein-based Disorders I",
    "games": [
        {
            "slug": "amino_acid_classes",
            "title": "Classifying the Proteogenic Amino Acids",
            "subtitle": "Match each amino acid to its side-chain chemistry, its charge in blood, and its board-relevant role",
            "categories": ["Side-chain chemistry", "Charge at blood pH (~7.4)", "Board-relevant role"],
            "data": {
                "Glutamate": {
                    "Side-chain chemistry": "Carboxylic acid (acidic side chain)",
                    "Charge at blood pH (~7.4)": "Negatively charged",
                    "Board-relevant role": "Forms ionic salt bridge with protonated histidine"
                },
                "Lysine": {
                    "Side-chain chemistry": "Amine (basic side chain)",
                    "Charge at blood pH (~7.4)": "Positively charged",
                    "Board-relevant role": "Epsilon-amino group is the target for ubiquitination"
                },
                "Histidine": {
                    "Side-chain chemistry": "Imidazole with pKa near physiological pH",
                    "Charge at blood pH (~7.4)": "Near neutral, readily gains or loses a proton",
                    "Board-relevant role": "Physiologic buffer; protonation drives the Bohr effect"
                },
                "Serine": {
                    "Side-chain chemistry": "Alcohol (hydroxyl) group",
                    "Charge at blood pH (~7.4)": "Neutral (uncharged)",
                    "Board-relevant role": "Hydroxyl accepts phosphate during phosphorylation"
                },
                "Leucine": {
                    "Side-chain chemistry": "Nonpolar hydrocarbon",
                    "Charge at blood pH (~7.4)": "Neutral (uncharged)",
                    "Board-relevant role": "Neutral amino acid lost in urine in Hartnup disease"
                },
                "Cysteine": {
                    "Side-chain chemistry": "Thiol (sulfur-containing)",
                    "Charge at blood pH (~7.4)": "Neutral (uncharged)",
                    "Board-relevant role": "Two oxidized cysteines form a disulfide bond"
                }
            }
        },
        {
            "slug": "protein_structure_levels",
            "title": "Four Levels of Protein Structure",
            "subtitle": "Match each level to its description, its main stabilizing force, and an example",
            "categories": ["Description", "Stabilizing force", "Example"],
            "data": {
                "Primary": {
                    "Description": "Linear sequence of amino acids from N- to C-terminus",
                    "Stabilizing force": "Covalent peptide bonds",
                    "Example": "The ordered chain of residues in a polypeptide"
                },
                "Secondary": {
                    "Description": "Local 3D folds of the backbone, not combinations thereof",
                    "Stabilizing force": "Hydrogen bonds (backbone dipole interactions)",
                    "Example": "Alpha-helix and beta-pleated sheet"
                },
                "Tertiary": {
                    "Description": "All secondary elements on a single polypeptide (one N- and C-terminus)",
                    "Stabilizing force": "R-group interactions: salt bridges, van der Waals, disulfides",
                    "Example": "Fully folded myoglobin with eight alpha-helices"
                },
                "Quaternary": {
                    "Description": "Multiple subunits with multiple N- and C-termini assembled together",
                    "Stabilizing force": "Interactions between separate polypeptide subunits",
                    "Example": "Hemoglobin with its four globin subunits"
                }
            }
        },
        {
            "slug": "post_translational_mods",
            "title": "Post-Translational Modifications",
            "subtitle": "Match each modification to the group added, the residue targeted, and its functional consequence",
            "categories": ["Group added", "Target residue(s)", "Functional consequence"],
            "data": {
                "Phosphorylation": {
                    "Group added": "Phosphate group (PO4)",
                    "Target residue(s)": "Serine, threonine, or tyrosine (hydroxyl side chains)",
                    "Functional consequence": "Activates or inhibits the protein in cell signaling"
                },
                "O-linked glycosylation": {
                    "Group added": "Carbohydrate linked to an oxygen",
                    "Target residue(s)": "Serine, threonine, or tyrosine hydroxyl group",
                    "Functional consequence": "Aids cellular routing and folding via O-linkage"
                },
                "N-linked glycosylation": {
                    "Group added": "Carbohydrate linked to a nitrogen",
                    "Target residue(s)": "Asparagine only",
                    "Functional consequence": "Directs trafficking; defective in I-cell disease"
                },
                "Ubiquitination": {
                    "Group added": "Ubiquitin, a 76-amino-acid protein",
                    "Target residue(s)": "Epsilon-amino group of lysine",
                    "Functional consequence": "Polyubiquitin tags proteins for proteasomal turnover"
                },
                "Hydroxylation": {
                    "Group added": "Hydroxyl group (-OH)",
                    "Target residue(s)": "Proline (yielding hydroxyproline in collagen)",
                    "Functional consequence": "Enhances collagen stability; impaired in scurvy"
                }
            }
        },
        {
            "slug": "helpers_and_turnover",
            "title": "Protein Helpers and Cellular Turnover",
            "subtitle": "Match each concept to its definition, an example, and a key distinguishing feature",
            "categories": ["Definition", "Example", "Key distinguishing feature"],
            "data": {
                "Cofactor": {
                    "Definition": "Inorganic or organic molecule a protein requires for activity",
                    "Example": "Metal ions such as Zn++, Mg++, or Ca++",
                    "Key distinguishing feature": "Easily removed by chelators like EDTA to block activity"
                },
                "Coenzyme": {
                    "Definition": "An organic (carbon-containing) cofactor",
                    "Example": "NADH and FADH2 derived from B vitamins",
                    "Key distinguishing feature": "A carbon-based subset of cofactors, not all cofactors"
                },
                "Prosthetic group": {
                    "Definition": "A cofactor covalently linked to the protein",
                    "Example": "Heme within a hemoglobin subunit",
                    "Key distinguishing feature": "Its removal disrupts structure and denatures the protein"
                },
                "Lysosomal turnover": {
                    "Definition": "Degradation route for internalized extracellular proteins",
                    "Example": "Acidic single-bilayer organelle at pH 4.5-5.0",
                    "Key distinguishing feature": "Uses acid-activated enzymes and drives autophagy"
                },
                "Ubiquitin-proteasome pathway": {
                    "Definition": "Degradation route for intracellular cytosolic proteins",
                    "Example": "Multi-subunit proteasome inhibited by bortezomib",
                    "Key distinguishing feature": "ATP-dependent unfolding of polyubiquitin-tagged proteins"
                }
            }
        }
    ]
}
