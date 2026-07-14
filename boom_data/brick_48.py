BRICK = {
    "brick_num": 48,
    "brick_title": "Molecular Biology Techniques (2 of 3): DNA Analysis",
    "games": [
        {
            "slug": "dna_analysis_techniques",
            "title": "DNA Analysis Techniques",
            "subtitle": "Match each molecular technique to what it detects best, its scope, and its signature feature",
            "categories": ["Best At Detecting", "Targeted vs Unbiased", "Signature Feature"],
            "data": {
                "SNP-Microarray": {
                    "Best At Detecting": "Known SNPs, copy number variations, and loss of heterozygosity",
                    "Targeted vs Unbiased": "Targeted (only variants with probes on the array)",
                    "Signature Feature": "Cost-effective genotyping panel that misses rare or novel variants"
                },
                "Restriction Enzyme Digestion (RFLP)": {
                    "Best At Detecting": "Known variants that create or eliminate a restriction site",
                    "Targeted vs Unbiased": "Targeted (only already-known site-altering mutations)",
                    "Signature Feature": "Bacterial endonuclease cuts DNA, then gel electrophoresis reveals the pattern"
                },
                "Sanger Sequencing": {
                    "Best At Detecting": "Point mutations and small indels within a single selected gene",
                    "Targeted vs Unbiased": "Targeted (one region amplified first by PCR)",
                    "Signature Feature": "Fluorochrome-labeled ddNTPs terminate the chain to read the sequence base by base"
                },
                "Next-Generation Sequencing (NGS)": {
                    "Best At Detecting": "Rare, novel, and low-frequency variants across many genes at once",
                    "Targeted vs Unbiased": "Unbiased (whole genome/exome) or a targeted gene panel",
                    "Signature Feature": "Millions of DNA fragments sequenced simultaneously, generating big data"
                }
            }
        },
        {
            "slug": "pcr_components",
            "title": "PCR Components (Copy-Machine Analogy)",
            "subtitle": "Match each PCR ingredient to its function, a key detail, and its copy-machine analogy",
            "categories": ["Function", "Key Detail", "Copy-Machine Analogy"],
            "data": {
                "Taq Polymerase": {
                    "Function": "Synthesizes the new complementary DNA strand",
                    "Key Detail": "Heat-stable enzyme purified from Thermus aquaticus, active even at 95 degrees C",
                    "Copy-Machine Analogy": "The copy machine itself"
                },
                "DNA Sample (Template)": {
                    "Function": "Provides the template sequence to be amplified",
                    "Key Detail": "Extracted from sources such as blood, tissue, or cultured cells",
                    "Copy-Machine Analogy": "The book containing the information to be copied"
                },
                "Primers": {
                    "Function": "Flank and define the exact region that gets amplified",
                    "Key Detail": "Short ~20-nucleotide oligonucleotides used as a forward and reverse pair",
                    "Copy-Machine Analogy": "The first and last words of the page you want to copy"
                },
                "Deoxynucleotides (dNTPs)": {
                    "Function": "Serve as the building blocks of the new DNA strand",
                    "Key Detail": "A mix of dATP, dTTP, dCTP, and dGTP",
                    "Copy-Machine Analogy": "The ink used to reproduce the page"
                }
            }
        },
        {
            "slug": "sickle_cell_rflp",
            "title": "Sickle Cell RFLP Genotyping",
            "subtitle": "Match each sample to its DdeI digestion outcome, gel banding pattern, and genotype meaning",
            "categories": ["DdeI Digestion Outcome", "Bands Seen on Gel", "Genotype Meaning"],
            "data": {
                "HbAA": {
                    "DdeI Digestion Outcome": "Fragment is completely cut at the intact CTNAG site",
                    "Bands Seen on Gel": "Two smaller digested fragments",
                    "Genotype Meaning": "Homozygous wild type, normal hemoglobin"
                },
                "HbSS": {
                    "DdeI Digestion Outcome": "Cannot cut because the A-to-T mutation destroys the recognition site",
                    "Bands Seen on Gel": "A single uncut band (~450 bp)",
                    "Genotype Meaning": "Homozygous mutant, affected by sickle cell disease"
                },
                "HbAS": {
                    "DdeI Digestion Outcome": "Only the wild-type allele is cut; the mutant allele stays intact",
                    "Bands Seen on Gel": "Three bands (one undigested plus two digested fragments)",
                    "Genotype Meaning": "Heterozygous carrier of sickle cell disease"
                },
                "Undigested PCR Product": {
                    "DdeI Digestion Outcome": "No enzyme applied, so no cutting occurs",
                    "Bands Seen on Gel": "A single ~450 bp band serving as the reference",
                    "Genotype Meaning": "Confirms successful amplification before digestion"
                }
            }
        },
        {
            "slug": "sequencing_pioneers",
            "title": "Origins of the Techniques",
            "subtitle": "Match each technique or tool to its key figure/origin, its era, and its defining principle",
            "categories": ["Key Figure or Origin", "Era", "Defining Principle"],
            "data": {
                "Polymerase Chain Reaction (PCR)": {
                    "Key Figure or Origin": "Kary Mullis, awarded the Nobel Prize in Chemistry",
                    "Era": "Nobel Prize awarded in 1993",
                    "Defining Principle": "Exponential amplification, with a final ratio of 2 to the power of n cycles"
                },
                "Sanger Sequencing": {
                    "Key Figure or Origin": "Frederick Sanger, one of few to win two Nobel Prizes",
                    "Era": "Developed in 1977",
                    "Defining Principle": "Chain-terminating fluorochrome-labeled ddNTPs that lack a 3-prime hydroxyl group"
                },
                "Taq Polymerase": {
                    "Key Figure or Origin": "Isolated from Thermus aquaticus and reported by Chien et al.",
                    "Era": "Reported in 1976",
                    "Defining Principle": "A heat-stable polymerase that made automating PCR possible"
                },
                "Next-Generation Sequencing (NGS)": {
                    "Key Figure or Origin": "Modern high-throughput sequencing platforms",
                    "Era": "Emerged in recent years",
                    "Defining Principle": "Sequencing by synthesis reading millions of fragments at once"
                }
            }
        }
    ]
}
