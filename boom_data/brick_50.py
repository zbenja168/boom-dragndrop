BRICK = {
    "brick_num": 50,
    "brick_title": "Mitochondrial Diseases",
    "games": [
        {
            "slug": "mito_syndromes",
            "title": "Mitochondrial Disease Syndromes",
            "subtitle": "Match each disorder to its clinical features, genetic basis, and distinguishing fact",
            "categories": ["Key Clinical Features", "Genetic Basis", "Distinguishing Fact"],
            "data": {
                "MELAS": {
                    "Key Clinical Features": "Encephalomyopathy, lactic acidosis, and stroke-like episodes",
                    "Genetic Basis": "mtDNA mutation; maternal (mitochondrial) inheritance",
                    "Distinguishing Fact": "Presents within the first decade; ragged-red fibers on biopsy"
                },
                "MERRF": {
                    "Key Clinical Features": "Myoclonus, seizures, myopathy, and cerebellar ataxia",
                    "Genetic Basis": "tRNA lysine gene MT-TK mutation (e.g., A8344G)",
                    "Distinguishing Fact": "High muscle mutation load (80-90%) correlates with severity"
                },
                "Leber hereditary optic neuropathy (LHON)": {
                    "Key Clinical Features": "Sudden, painless bilateral vision loss in the 2nd-3rd decade",
                    "Genetic Basis": "MT-ND1, MT-ND4, MT-ND4L, or MT-ND6; usually homoplasmic",
                    "Distinguishing Fact": "About 90% of affected patients are male"
                },
                "Friedreich ataxia (FRDA)": {
                    "Key Clinical Features": "Progressive gait ataxia, frequent falls, and cardiomyopathy",
                    "Genetic Basis": "FXN gene GAA trinucleotide repeat; autosomal recessive",
                    "Distinguishing Fact": "Nuclear-encoded frataxin defect, not maternally inherited"
                }
            }
        },
        {
            "slug": "mtdna_vs_nuclear",
            "title": "Mitochondrial DNA vs Nuclear DNA",
            "subtitle": "Match each feature of mtDNA to its value, its nuclear-DNA contrast, and its significance",
            "categories": ["mtDNA Feature", "Contrast with Nuclear DNA", "Significance"],
            "data": {
                "Genome shape": {
                    "mtDNA Feature": "Circular double-stranded DNA in the matrix",
                    "Contrast with Nuclear DNA": "Nuclear genome is linear",
                    "Significance": "Reflects bacterial endosymbiotic origin"
                },
                "Genome size": {
                    "mtDNA Feature": "16,569 base pairs encoding only 37 genes",
                    "Contrast with Nuclear DNA": "Nuclear genome is about 3.3 billion base pairs",
                    "Significance": "Most mitochondrial proteins are nuclear-encoded"
                },
                "Gene content": {
                    "mtDNA Feature": "13 OXPHOS proteins, 22 tRNAs, and 2 rRNAs",
                    "Contrast with Nuclear DNA": "Nuclear DNA encodes the ~1100 other mito proteins",
                    "Significance": "Nuclear-encoded proteins are imported from the cytoplasm"
                },
                "Histone packaging": {
                    "mtDNA Feature": "mtDNA has no histones",
                    "Contrast with Nuclear DNA": "Nuclear DNA is wrapped around histones",
                    "Significance": "Contributes to higher mtDNA vulnerability and mutation"
                },
                "Codon usage": {
                    "mtDNA Feature": "UGA codes for tryptophan; AGA and AGG are stop codons",
                    "Contrast with Nuclear DNA": "In nuclear DNA UGA is a stop and AGA/AGG code arginine",
                    "Significance": "mtDNA uses a slightly different genetic code"
                },
                "Mutation rate": {
                    "mtDNA Feature": "About 10 times higher than the nuclear genome",
                    "Contrast with Nuclear DNA": "Nuclear DNA has robust repair mechanisms",
                    "Significance": "Poor repair plus ROS damage drives disease"
                }
            }
        },
        {
            "slug": "mito_genetics_concepts",
            "title": "Concepts of Mitochondrial Genetics",
            "subtitle": "Match each concept to its definition, its consequence, and a supporting detail",
            "categories": ["Definition", "Consequence", "Supporting Detail"],
            "data": {
                "Maternal inheritance": {
                    "Definition": "Mutations transmitted only through the mother",
                    "Consequence": "Both sexes are affected but only females transmit",
                    "Supporting Detail": "Only oocytes contribute mitochondria to offspring"
                },
                "Homoplasmy": {
                    "Definition": "Uniform mtDNA, either all normal or all mutant",
                    "Consequence": "Cell is either fully normal or fully affected",
                    "Supporting Detail": "LHON risk requires homoplasmy or very high mutant load"
                },
                "Heteroplasmy": {
                    "Definition": "A cell containing both normal and mutant mtDNA",
                    "Consequence": "Variable expressivity and disease severity",
                    "Supporting Detail": "Proportion of mutant mtDNA sets the severity"
                },
                "Threshold effect": {
                    "Definition": "Symptoms appear only after a critical mutant level",
                    "Consequence": "Disease manifests when ATP falls below organ needs",
                    "Supporting Detail": "Respiratory complexes tolerate partial inhibition"
                },
                "Endosymbiotic theory": {
                    "Definition": "Mitochondrion arose from an engulfed aerobic microbe",
                    "Consequence": "Explains the two mitochondrial membranes",
                    "Supporting Detail": "Outer membrane from host, inner from the bacterium"
                },
                "Binary fission": {
                    "Definition": "Prokaryote-like division of mitochondria",
                    "Consequence": "Division is independent of cell division",
                    "Supporting Detail": "Mitochondria fuse and divide with energy needs"
                }
            }
        },
        {
            "slug": "organ_involvement",
            "title": "Organ Systems in Mitochondrial Disease",
            "subtitle": "Match each affected organ to its manifestation and an associated disorder",
            "categories": ["Affected Organ", "Characteristic Manifestation", "Associated Disorder"],
            "data": {
                "Eye": {
                    "Affected Organ": "Optic nerve and retina",
                    "Characteristic Manifestation": "Optic neuropathy, ophthalmoplegia, retinopathy",
                    "Associated Disorder": "Leber hereditary optic neuropathy (LHON)"
                },
                "Skeletal muscle": {
                    "Affected Organ": "Voluntary muscle fibers",
                    "Characteristic Manifestation": "Weakness, fatigue, and myopathy",
                    "Associated Disorder": "MELAS and MERRF with ragged-red fibers"
                },
                "Brain / CNS": {
                    "Affected Organ": "Central nervous system",
                    "Characteristic Manifestation": "Seizures, stroke, ataxia, and dementia",
                    "Associated Disorder": "MELAS (stroke-like episodes)"
                },
                "Heart": {
                    "Affected Organ": "Cardiac muscle and conduction system",
                    "Characteristic Manifestation": "Cardiomyopathy and conduction disorders",
                    "Associated Disorder": "Friedreich ataxia and MERRF"
                },
                "Blood": {
                    "Affected Organ": "Bone marrow / hematologic system",
                    "Characteristic Manifestation": "Marrow cell dysfunction",
                    "Associated Disorder": "Pearson syndrome"
                },
                "Pancreas": {
                    "Affected Organ": "Endocrine pancreas",
                    "Characteristic Manifestation": "Impaired glucose control",
                    "Associated Disorder": "Diabetes mellitus"
                }
            }
        }
    ]
}
