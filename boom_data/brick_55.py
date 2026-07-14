BRICK = {
    "brick_num": 55,
    "brick_title": "Molecular Biology Techniques (2 of 3), DNA analysis",
    "games": [
        {
            "slug": "dna_analysis_techniques",
            "title": "DNA Analysis Techniques",
            "subtitle": "Match each molecular technique to its approach, what it best detects, and its key limitation",
            "categories": ["Approach", "Best detects", "Key limitation"],
            "data": {
                "SNP-microarray": {
                    "Approach": "Targeted probe-based genotyping panel",
                    "Best detects": "Known common SNPs, CNVs, and loss of heterozygosity",
                    "Key limitation": "Misses rare or novel variants lacking a probe"
                },
                "RFLP (restriction digestion)": {
                    "Approach": "Targeted, limited to a single known site",
                    "Best detects": "Known mutations that alter a restriction site",
                    "Key limitation": "Only works if the mutation changes a restriction site"
                },
                "Sanger sequencing": {
                    "Approach": "Targeted, reads one region base by base",
                    "Best detects": "Novel point mutations and small indels",
                    "Key limitation": "Low throughput, one region at a time"
                },
                "Next-generation sequencing (NGS)": {
                    "Approach": "Unbiased, high-throughput, millions of fragments at once",
                    "Best detects": "Rare and low-frequency variants across exome or genome",
                    "Key limitation": "Generates massive data needing complex bioinformatics"
                }
            }
        },
        {
            "slug": "pcr_components",
            "title": "PCR Components",
            "subtitle": "Match each PCR reagent to its function, key feature, and copy-machine analogy",
            "categories": ["Function in reaction", "Key feature", "Copy-machine analogy"],
            "data": {
                "Taq polymerase": {
                    "Function in reaction": "Synthesizes the new complementary DNA strand",
                    "Key feature": "Heat-stable enzyme purified from Thermus aquaticus",
                    "Copy-machine analogy": "The copy machine itself"
                },
                "DNA sample (template)": {
                    "Function in reaction": "Provides the target sequence to be amplified",
                    "Key feature": "Extracted from blood, tissues, or cultured cells",
                    "Copy-machine analogy": "The book containing the information"
                },
                "Primers": {
                    "Function in reaction": "Flank and define the fragment to be amplified",
                    "Key feature": "Short ~20-nucleotide oligos, one forward and one reverse",
                    "Copy-machine analogy": "The first and last words of the page"
                },
                "dNTPs": {
                    "Function in reaction": "Serve as building blocks of the new strand",
                    "Key feature": "Mix of dATP, dTTP, dCTP, and dGTP",
                    "Copy-machine analogy": "The ink used to copy the page"
                }
            }
        },
        {
            "slug": "reading_the_results",
            "title": "Reading the Results",
            "subtitle": "Match each technique to how its output is read, what it reveals, and an example finding",
            "categories": ["Result readout", "What it reveals", "Example finding"],
            "data": {
                "Sanger sequencing": {
                    "Result readout": "Electropherogram of colored peaks, one per base",
                    "What it reveals": "The exact base-by-base DNA sequence",
                    "Example finding": "Overlapping peaks indicate a heterozygous variant"
                },
                "RFLP gel electrophoresis": {
                    "Result readout": "Bands separated by size on an agarose gel",
                    "What it reveals": "Whether a restriction site is present or absent",
                    "Example finding": "A single uncut band marks a homozygous sickle (HbSS) allele"
                },
                "SNP-microarray": {
                    "Result readout": "Data plots or heatmaps with genotype tables",
                    "What it reveals": "Genotype, copy number, and allele dosage",
                    "Example finding": "Uniparental disomy detected in a relapsed leukemia"
                },
                "NGS": {
                    "Result readout": "FASTQ files summarized in a variant table",
                    "What it reveals": "Thousands of variants compared to a reference genome",
                    "Example finding": "20,000 to 50,000 variants identified per exome"
                }
            }
        },
        {
            "slug": "technique_for_the_scenario",
            "title": "Choosing the Right Technique",
            "subtitle": "Match each clinical scenario to the best technique, the rationale, and the approach type",
            "categories": ["Best technique", "Rationale", "Approach type"],
            "data": {
                "Detect a novel point mutation": {
                    "Best technique": "Sanger or NGS sequencing",
                    "Rationale": "Only sequencing can read previously unknown bases",
                    "Approach type": "Targeted or unbiased sequencing"
                },
                "Common known mutation, clear phenotype": {
                    "Best technique": "SNP-microarray",
                    "Rationale": "Cheap, quick screen for well-characterized common variants",
                    "Approach type": "Targeted (a priori)"
                },
                "Disease mutation after negative SNP-array": {
                    "Best technique": "Genome or exome sequencing",
                    "Rationale": "An uncommon or novel variant is now likely",
                    "Approach type": "Unbiased (no a priori)"
                },
                "Genotype known sickle-cell mutation": {
                    "Best technique": "PCR plus restriction (RFLP) digestion",
                    "Rationale": "The HBB point mutation abolishes a DdeI site",
                    "Approach type": "Targeted to a known site"
                },
                "Lynch syndrome hereditary cancer": {
                    "Best technique": "NGS mismatch-repair gene panel",
                    "Rationale": "Sequences MLH1, MSH2, MSH6, PMS2, and EPCAM together",
                    "Approach type": "Targeted multigene panel"
                }
            }
        }
    ]
}
