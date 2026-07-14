BRICK = {
    "brick_num": 17,
    "brick_title": "Biotechniques: Protein Detection",
    "games": [
        {
            "slug": "detection_techniques",
            "title": "Protein Detection Techniques Compared",
            "subtitle": "Match each antibody-based technique to its principle, unique output, and clinical use",
            "categories": ["Principle / Sample", "Unique Information Provided", "Clinical Application"],
            "data": {
                "Western blot": {
                    "Principle / Sample": "Denatured proteins separated by size, blotted to membrane, antibody-stained",
                    "Unique Information Provided": "Molecular weight (size) of the target antigen",
                    "Clinical Application": "Confirmatory test for HIV and Lyme disease"
                },
                "ELISA": {
                    "Principle / Sample": "Immobilized antigen, sample added, labeled anti-human antibody plus substrate",
                    "Unique Information Provided": "Relative abundance of an antibody or antigen",
                    "Clinical Application": "Hepatitis B titer to confirm vaccine response"
                },
                "Flow cytometry": {
                    "Principle / Sample": "Intact cells run one at a time past a light source",
                    "Unique Information Provided": "Antigen abundance on intact cells and cell counts",
                    "Clinical Application": "CBC/WBC differential and CD4+ T-cell counts"
                },
                "Immunohistochemistry / IF": {
                    "Principle / Sample": "Antibody-stained tissue biopsy examined by microscopy",
                    "Unique Information Provided": "Relative localization of an antigen within tissue",
                    "Clinical Application": "Staging cancer or identifying syphilis and chlamydia"
                },
                "Enzymatic assay": {
                    "Principle / Sample": "Substrate conversion measured against a standard, no protein visualized",
                    "Unique Information Provided": "Activity level of a specific enzyme",
                    "Clinical Application": "ALT and AST measured in liver panels"
                }
            }
        },
        {
            "slug": "scd_gene_to_cell",
            "title": "Sickle Cell Disease: Gene to Cell",
            "subtitle": "Order the molecular change, its consequence, and the clinical or detection note",
            "categories": ["Molecular Change", "Consequence", "Clinical / Detection Note"],
            "data": {
                "Point mutation in beta-globin": {
                    "Molecular Change": "Single change in the beta-globin chain gene",
                    "Consequence": "Glutamate replaced by valine at position 6",
                    "Clinical / Detection Note": "Classified as a point (missense) mutation"
                },
                "Neutral valine substitution": {
                    "Molecular Change": "Negatively charged glutamate becomes neutral nonpolar valine",
                    "Consequence": "HbS carries a less negative (more positive) overall charge",
                    "Clinical / Detection Note": "Basis for separation on hemoglobin electrophoresis"
                },
                "Deoxygenation of HbS": {
                    "Molecular Change": "Hydrophobic pocket forms and exposes the valine",
                    "Consequence": "Valine binds an adjacent deoxy-Hb tetramer",
                    "Clinical / Detection Note": "Low-oxygen states favor sickling"
                },
                "Hemoglobin polymerization": {
                    "Molecular Change": "Hb polymers are far less soluble",
                    "Consequence": "RBC membrane distorts into a rigid sickle shape",
                    "Clinical / Detection Note": "Reoxygenation restores biconcave morphology"
                },
                "Sickled RBC rigidity": {
                    "Molecular Change": "Inflexible sickled RBCs cannot deform",
                    "Consequence": "Vaso-occlusion of small vasculature",
                    "Clinical / Detection Note": "Painful crises damaging the spleen and brain"
                },
                "Sickle cell crisis management": {
                    "Molecular Change": "Increase hemoglobin oxygen saturation",
                    "Consequence": "Shifts Hb toward the soluble oxygenated form",
                    "Clinical / Detection Note": "Supplemental O2 by nasal cannula plus reduced exertion"
                }
            }
        },
        {
            "slug": "choosing_the_assay",
            "title": "Choosing the Right Assay",
            "subtitle": "Match each clinical need to the best protein detection technique and the reason",
            "categories": ["Clinical Need", "Best Technique", "Reason"],
            "data": {
                "Confirm HIV or Lyme disease": {
                    "Clinical Need": "Confirm a reactive infectious-disease screen",
                    "Best Technique": "Western blot",
                    "Reason": "Provides confirmatory antigen size information"
                },
                "Count CD4+ T-cells": {
                    "Clinical Need": "Quantify cells expressing a surface marker",
                    "Best Technique": "Flow cytometry",
                    "Reason": "Quantifies antigens on intact cells one at a time"
                },
                "Check hepatitis B immunity": {
                    "Clinical Need": "Confirm antibody response after vaccination",
                    "Best Technique": "ELISA titer",
                    "Reason": "Measures relative antibody abundance by serial dilution"
                },
                "Distinguish sickle trait from disease": {
                    "Clinical Need": "Identify which hemoglobin variants are present",
                    "Best Technique": "Hemoglobin electrophoresis",
                    "Reason": "Separates HbA and HbS by their difference in charge"
                },
                "Stage a cancer from a biopsy": {
                    "Clinical Need": "Localize an antigen within a tissue section",
                    "Best Technique": "Immunohistochemistry",
                    "Reason": "Shows antigen localization and staining pattern by microscopy"
                },
                "Measure liver enzyme activity": {
                    "Clinical Need": "Quantify activity of a specific enzyme",
                    "Best Technique": "Enzymatic assay",
                    "Reason": "Quantifies ALT and AST activity referenced to a standard"
                }
            }
        },
        {
            "slug": "flow_cytometry_signals",
            "title": "Flow Cytometry Signals",
            "subtitle": "Match each flow cytometry parameter or marker to what it detects and how it is read",
            "categories": ["Parameter / Marker", "What It Detects", "Interpretation"],
            "data": {
                "Forward scatter (FSC)": {
                    "Parameter / Marker": "Light scattered forward as a cell crosses the laser",
                    "What It Detects": "The physical size of the cell",
                    "Interpretation": "Larger cells produce greater forward scatter"
                },
                "Side scatter (SSC)": {
                    "Parameter / Marker": "Light scattered to the side",
                    "What It Detects": "Internal granularity and density of the cell",
                    "Interpretation": "Granulocytes show high side scatter"
                },
                "CD4 antibody signal": {
                    "Parameter / Marker": "Binding of a labeled anti-CD4 antibody",
                    "What It Detects": "Cells expressing the CD4 surface marker",
                    "Interpretation": "Used to count helper T-cells, which fall in HIV"
                },
                "CD8 antibody signal": {
                    "Parameter / Marker": "Binding of a labeled anti-CD8 antibody",
                    "What It Detects": "Cells expressing the CD8 surface marker",
                    "Interpretation": "Marks the single-positive CD8 cytotoxic T-cell quadrant"
                },
                "Double-positive quadrant": {
                    "Parameter / Marker": "Both CD4 and CD8 signals on the same cell",
                    "What It Detects": "Cells co-expressing two markers",
                    "Interpretation": "Falls in the upper-right double-positive region"
                },
                "Double-negative quadrant": {
                    "Parameter / Marker": "Neither CD4 nor CD8 signal detected",
                    "What It Detects": "Cells lacking both markers",
                    "Interpretation": "Falls in the lower-left double-negative region"
                }
            }
        }
    ]
}
