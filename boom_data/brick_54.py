BRICK = {
    "brick_num": 54,
    "brick_title": "Molecular Biology Techniques (1 of 3) - Cytogenetics",
    "games": [
        {
            "slug": "techniques_compared",
            "title": "Cytogenetic Techniques at a Glance",
            "subtitle": "Match each technique to its approach, resolution, and best clinical use",
            "categories": ["Approach", "Resolution / Detection Limit", "Best Clinical Use"],
            "data": {
                "Karyotyping (G-banding)": {
                    "Approach": "Unbiased whole-chromosome visualization",
                    "Resolution / Detection Limit": "Low; detects abnormalities >5-10 megabases",
                    "Best Clinical Use": "Aneuploidy and balanced translocations"
                },
                "FISH": {
                    "Approach": "Targeted; requires prior knowledge of the sequence",
                    "Resolution / Detection Limit": "High; detects known microdeletions/duplications",
                    "Best Clinical Use": "Confirm a suspected microdeletion (e.g. 22q11)"
                },
                "Array CGH": {
                    "Approach": "Unbiased, genome-wide copy number scan",
                    "Resolution / Detection Limit": "High; detects CNVs as small as 50-200 kilobases",
                    "Best Clinical Use": "Unexplained developmental delay or intellectual disability"
                },
                "Southern Blot": {
                    "Approach": "Targeted; restriction digest then labeled probe",
                    "Resolution / Detection Limit": "Moderate; needs large DNA input, radiolabeled probe",
                    "Best Clinical Use": "Size large repeat expansions (e.g. FXN GAA)"
                }
            }
        },
        {
            "slug": "how_it_works",
            "title": "How Each Technique Works",
            "subtitle": "Match each technique to its first step, label/stain, and readout",
            "categories": ["Sample / First Step", "Label or Stain", "Readout"],
            "data": {
                "Karyotyping (G-banding)": {
                    "Sample / First Step": "Cultured cells arrested at metaphase with colchicine",
                    "Label or Stain": "Giemsa stain after trypsin digestion",
                    "Readout": "Chromosomes paired 1-22 plus X and Y by size and bands"
                },
                "FISH": {
                    "Sample / First Step": "Metaphase or interphase DNA denatured to single strands",
                    "Label or Stain": "Fluorescent DNA probe with DAPI counterstain",
                    "Readout": "Presence, absence, or location of a fluorescent signal"
                },
                "Array CGH": {
                    "Sample / First Step": "Patient and reference DNA extracted and compared",
                    "Label or Stain": "Test DNA red (Cy5), reference DNA green (Cy3)",
                    "Readout": "Red-to-green fluorescence ratio at each microarray well"
                },
                "Southern Blot": {
                    "Sample / First Step": "DNA cut by restriction enzyme, separated by gel electrophoresis",
                    "Label or Stain": "Radioactive-labeled DNA probe on a membrane",
                    "Readout": "Size of the band bound by the probe"
                }
            }
        },
        {
            "slug": "signals_interpreted",
            "title": "Bands, Signals, and Ratios",
            "subtitle": "Match each observed result to its technique and correct interpretation",
            "categories": ["Result / Signal", "Technique", "Interpretation"],
            "data": {
                "Dark band": {
                    "Result / Signal": "Dark (G-positive) band",
                    "Technique": "G-banded karyotype",
                    "Interpretation": "AT-rich, gene-poor heterochromatin"
                },
                "Light band": {
                    "Result / Signal": "Light (G-negative) band",
                    "Technique": "G-banded karyotype",
                    "Interpretation": "GC-rich, gene-rich euchromatin"
                },
                "Single red probe signal": {
                    "Result / Signal": "One red (TUPLE1) signal instead of two",
                    "Technique": "FISH with control and target probes",
                    "Interpretation": "Heterozygous 22q11 deletion"
                },
                "Green-dominant ratio": {
                    "Result / Signal": "Green signal stronger than red",
                    "Technique": "Array CGH",
                    "Interpretation": "Deletion in the patient DNA at that locus"
                },
                "Red-dominant ratio": {
                    "Result / Signal": "Red signal stronger than green",
                    "Technique": "Array CGH",
                    "Interpretation": "Duplication in the patient DNA at that locus"
                },
                "Yellow ratio": {
                    "Result / Signal": "Equal red and green (yellow)",
                    "Technique": "Array CGH",
                    "Interpretation": "Normal copy number, no CNV"
                }
            }
        },
        {
            "slug": "syndrome_to_test",
            "title": "Match Syndrome to Lesion and Best Test",
            "subtitle": "Match each disorder to its molecular lesion and the optimal diagnostic technique",
            "categories": ["Chromosomal / Molecular Lesion", "Key Clinical Features", "Optimal Diagnostic Technique"],
            "data": {
                "Down syndrome": {
                    "Chromosomal / Molecular Lesion": "Trisomy 21 (47,XX,+21)",
                    "Key Clinical Features": "Flat facial profile, AV septal defect, protruding tongue",
                    "Optimal Diagnostic Technique": "Karyotype (G-banding)"
                },
                "DiGeorge syndrome": {
                    "Chromosomal / Molecular Lesion": "22q11.2 microdeletion",
                    "Key Clinical Features": "Conotruncal heart defect, T-cell immunodeficiency, hypocalcemia",
                    "Optimal Diagnostic Technique": "FISH with TUPLE1 probe"
                },
                "Williams syndrome": {
                    "Chromosomal / Molecular Lesion": "7q11.23 microdeletion (~1.5 Mb)",
                    "Key Clinical Features": "Failure to thrive, VSD, dysmorphism, normal karyotype",
                    "Optimal Diagnostic Technique": "Array CGH"
                },
                "Friedreich ataxia": {
                    "Chromosomal / Molecular Lesion": "GAA trinucleotide repeat expansion in FXN intron 1",
                    "Key Clinical Features": "Gait and limb ataxia, dysarthria, cardiomyopathy, diabetes",
                    "Optimal Diagnostic Technique": "Southern blot to size the expansion"
                },
                "Reciprocal translocation": {
                    "Chromosomal / Molecular Lesion": "t(9;22)(q11;p11), two chromosomes involved",
                    "Key Clinical Features": "Balanced rearrangement in a male 46,XY patient",
                    "Optimal Diagnostic Technique": "Karyotype (G-banding)"
                }
            }
        }
    ]
}
