BRICK = {
    "brick_num": 45,
    "brick_title": "Molecular Biology Techniques (1 of 3) - Cytogenetics",
    "games": [
        {
            "slug": "technique_overview",
            "title": "Four Cytogenetic Techniques Compared",
            "subtitle": "Match each technique to its resolution, approach, and classic use",
            "categories": ["Resolution / Detection Limit", "Approach", "Classic Application"],
            "data": {
                "G-banded Karyotype": {
                    "Resolution / Detection Limit": "Low; only abnormalities ~5-10 megabases or larger",
                    "Approach": "Unbiased, genome-wide visualization of all chromosomes",
                    "Classic Application": "Aneuploidy and large translocations (e.g., trisomy 21)"
                },
                "FISH": {
                    "Resolution / Detection Limit": "High; resolves submicroscopic microdeletions",
                    "Approach": "Targeted 'a priori' probe for a suspected locus",
                    "Classic Application": "22q11 microdeletion (DiGeorge syndrome)"
                },
                "Array CGH": {
                    "Resolution / Detection Limit": "High; detects CNVs as small as ~50-200 kilobases",
                    "Approach": "Unbiased, untargeted genome-wide copy number screen",
                    "Classic Application": "Williams syndrome 7q11.23 deletion; developmental delay"
                },
                "Southern Blot": {
                    "Resolution / Detection Limit": "Moderate; sizes long repeats but needs abundant DNA",
                    "Approach": "Targeted; restriction digest plus labeled DNA probe",
                    "Classic Application": "Triplet repeat expansions (Friedreich ataxia, fragile X)"
                }
            }
        },
        {
            "slug": "reading_signals",
            "title": "Reading the Signals",
            "subtitle": "Match each laboratory observation to its technique and interpretation",
            "categories": ["Technique", "Observation", "Interpretation"],
            "data": {
                "Single red TUPLE1 dot": {
                    "Technique": "FISH",
                    "Observation": "One red 22q11 signal with normal green ARSA control",
                    "Interpretation": "Heterozygous 22q11 deletion (DiGeorge)"
                },
                "Green-dominant well": {
                    "Technique": "Array CGH",
                    "Observation": "Green (reference) fluorescence stronger than red",
                    "Interpretation": "Deletion in the patient DNA at that locus"
                },
                "Red-dominant well": {
                    "Technique": "Array CGH",
                    "Observation": "Red (test) fluorescence stronger than green",
                    "Interpretation": "Duplication in the patient DNA at that locus"
                },
                "Yellow well": {
                    "Technique": "Array CGH",
                    "Observation": "Equal red and green fluorescence (most wells)",
                    "Interpretation": "No copy number variation; normal dosage"
                },
                "Three copies of chromosome 21": {
                    "Technique": "G-banded Karyotype",
                    "Observation": "An extra whole chromosome 21 in the spread",
                    "Interpretation": "Trisomy 21 (47,XX,+21), Down syndrome"
                },
                "Segments swapped between 9 and 22": {
                    "Technique": "G-banded Karyotype",
                    "Observation": "Material exchanged between chromosomes 9 and 22",
                    "Interpretation": "Balanced translocation t(9;22)"
                }
            }
        },
        {
            "slug": "acgh_dosage",
            "title": "Array CGH Dosage Scores",
            "subtitle": "Match each DNA-dosage value to its copy number and meaning",
            "categories": ["aCGH Dosage Score", "Copy Number", "Interpretation"],
            "data": {
                "Score -2": {
                    "aCGH Dosage Score": "Strong green shift, most negative value",
                    "Copy Number": "Zero copies",
                    "Interpretation": "Homozygous deletion; both alleles lost"
                },
                "Score -1": {
                    "aCGH Dosage Score": "Moderate green shift",
                    "Copy Number": "One copy",
                    "Interpretation": "Heterozygous deletion; one allele lost"
                },
                "Score 0": {
                    "aCGH Dosage Score": "Balanced yellow signal at baseline",
                    "Copy Number": "Two copies",
                    "Interpretation": "Normal dosage; no CNV"
                },
                "Score +1": {
                    "aCGH Dosage Score": "Moderate red shift",
                    "Copy Number": "Three copies",
                    "Interpretation": "Duplication; a single extra copy"
                },
                "Score +2": {
                    "aCGH Dosage Score": "Strong red shift, most positive value",
                    "Copy Number": "Four copies",
                    "Interpretation": "Duplication; two extra copies"
                }
            }
        },
        {
            "slug": "match_disorder",
            "title": "Match the Genetic Disorder",
            "subtitle": "Match each disorder to its lesion, clinical clue, and best test",
            "categories": ["Molecular / Chromosomal Lesion", "Key Clinical Clue", "Best Diagnostic Technique"],
            "data": {
                "Down syndrome": {
                    "Molecular / Chromosomal Lesion": "Trisomy 21 (extra whole chromosome 21)",
                    "Key Clinical Clue": "Flat facial profile with atrioventricular septal defect",
                    "Best Diagnostic Technique": "G-banded karyotype"
                },
                "DiGeorge syndrome": {
                    "Molecular / Chromosomal Lesion": "22q11.2 microdeletion",
                    "Key Clinical Clue": "Conotruncal heart defect, hypocalcemia, T-cell immunodeficiency",
                    "Best Diagnostic Technique": "FISH"
                },
                "Williams syndrome": {
                    "Molecular / Chromosomal Lesion": "~1.5 Mb 7q11.23 deletion",
                    "Key Clinical Clue": "Failure to thrive, VSD, dysmorphism, normal karyotype",
                    "Best Diagnostic Technique": "Array CGH (chromosomal microarray)"
                },
                "Friedreich ataxia": {
                    "Molecular / Chromosomal Lesion": "GAA triplet expansion in FXN intron 1",
                    "Key Clinical Clue": "Progressive gait ataxia, dysarthria, cardiomyopathy",
                    "Best Diagnostic Technique": "Southern blot"
                },
                "Balanced translocation carrier": {
                    "Molecular / Chromosomal Lesion": "Reciprocal or Robertsonian translocation",
                    "Key Clinical Clue": "Recurrent pregnancy loss in a phenotypically normal couple",
                    "Best Diagnostic Technique": "G-banded karyotype"
                }
            }
        }
    ]
}
