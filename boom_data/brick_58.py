BRICK = {
    "brick_num": 58,
    "brick_title": "From Bench to Bedside: The Role of Animal Models in Novel Therapeutics",
    "games": [
        {
            "slug": "gene_manip_strategies",
            "title": "Gene Manipulation Strategies",
            "subtitle": "Match each technique to the level it acts on, its permanence, and whether it is targeted",
            "categories": ["Acts at which level", "Permanent or transient", "Targeted or random"],
            "data": {
                "RNA interference (RNAi)": {
                    "Acts at which level": "mRNA (degradation or translation block)",
                    "Permanent or transient": "Transient knock-down, DNA unchanged",
                    "Targeted or random": "Targeted, sequence-specific silencing"
                },
                "Homologous recombination": {
                    "Acts at which level": "Genomic DNA via inserted cassette",
                    "Permanent or transient": "Permanent, heritable modification",
                    "Targeted or random": "Targeted at the gene of interest"
                },
                "CRISPR-Cas9": {
                    "Acts at which level": "Genomic DNA cut 3 bp upstream of PAM",
                    "Permanent or transient": "Permanent edit of the sequence",
                    "Targeted or random": "Targeted by the guide RNA spacer"
                },
                "Chemical mutagenesis": {
                    "Acts at which level": "Random point mutations across the genome",
                    "Permanent or transient": "Permanent, fixed in the genome",
                    "Targeted or random": "Random, forward-genetics approach"
                }
            }
        },
        {
            "slug": "rnai_machinery",
            "title": "RNAi Molecules and Machinery",
            "subtitle": "Match each RNAi player to its category, its role in the pathway, and a key detail",
            "categories": ["Category", "Role in the pathway", "Key detail"],
            "data": {
                "siRNA": {
                    "Category": "Small interfering RNA",
                    "Role in the pathway": "Guides RISC to complementary mRNA",
                    "Key detail": "Double-stranded, ~21-23 nucleotides; short-term knockdown"
                },
                "shRNA": {
                    "Category": "Short hairpin RNA",
                    "Role in the pathway": "Processed into siRNA to silence a gene",
                    "Key detail": "Folds into a hairpin loop; long-term silencing"
                },
                "miRNA": {
                    "Category": "MicroRNA",
                    "Role in the pathway": "Endogenous regulator of gene expression",
                    "Key detail": "Single strand ~22 nt; pri-miRNA to pre-miRNA to mature"
                },
                "Dicer": {
                    "Category": "Endonuclease enzyme",
                    "Role in the pathway": "Cleaves dsRNA into siRNA fragments",
                    "Key detail": "Generates guide and non-guide strands"
                },
                "Argonaute (RISC)": {
                    "Category": "Catalytic protein of RISC",
                    "Role in the pathway": "Cleaves the bound target mRNA",
                    "Key detail": "Retains the guide strand after unwinding"
                }
            }
        },
        {
            "slug": "crispr_components",
            "title": "CRISPR-Cas9 Components",
            "subtitle": "Match each component to what it is, its function, and a defining detail",
            "categories": ["What it is", "Function", "Defining detail"],
            "data": {
                "Cas9 protein": {
                    "What it is": "Nuclease enzyme, molecular scissors",
                    "Function": "Cuts double-stranded DNA 3 bp upstream of PAM",
                    "Defining detail": "Derived from a bacterial adaptive immune system"
                },
                "Guide RNA (sgRNA)": {
                    "What it is": "Synthetic fusion of crRNA and tracrRNA",
                    "Function": "Directs Cas9 to the exact target site",
                    "Defining detail": "20-nt variable spacer plus constant scaffold"
                },
                "PAM sequence": {
                    "What it is": "Short motif such as NGG",
                    "Function": "Required adjacent to target for Cas9 to cut",
                    "Defining detail": "Spacer must sit immediately upstream of it"
                },
                "CRISPR array": {
                    "What it is": "Repeats plus spacers in the bacterial genome",
                    "Function": "Serves as molecular memory of past viruses",
                    "Defining detail": "Spacers are fragments of prior viral DNA"
                },
                "NHEJ repair": {
                    "What it is": "Error-prone cellular repair pathway",
                    "Function": "Rejoins the Cas9 double-strand break",
                    "Defining detail": "Introduces indels causing frameshift knockout"
                }
            }
        },
        {
            "slug": "landmark_examples",
            "title": "Landmark Examples and Applications",
            "subtitle": "Match each example to what it is, its disease or context, and the key takeaway",
            "categories": ["What it is", "Disease or context", "Key takeaway"],
            "data": {
                "Thalidomide": {
                    "What it is": "Sedative once given to pregnant women",
                    "Disease or context": "Phocomelia, severe limb birth defects",
                    "Key takeaway": "Toxic in humans but not rodents; model limitation"
                },
                "Huntington siRNA": {
                    "What it is": "Allele-specific siRNA against mutant HTT",
                    "Disease or context": "Huntington disease, CAG triplet repeat",
                    "Key takeaway": "Spares wild-type allele; CNS delivery is the hurdle"
                },
                "Givlaari": {
                    "What it is": "Approved siRNA drug",
                    "Disease or context": "Acute intermittent porphyria",
                    "Key takeaway": "About $442,000 per year; cost limits siRNA therapy"
                },
                "Casgevy": {
                    "What it is": "First FDA-approved CRISPR-Cas9 therapy",
                    "Disease or context": "Sickle cell disease, ex vivo editing",
                    "Key takeaway": "Edits bone-marrow stem cells; over $2 million per patient"
                },
                "Charpentier and Doudna": {
                    "What it is": "Described CRISPR-Cas9 gene editing in 2012",
                    "Disease or context": "Genome editing in eukaryotic cells",
                    "Key takeaway": "Awarded the Nobel Prize in Chemistry in 2020"
                },
                "He Jiankui (2018)": {
                    "What it is": "Edited human embryos with CRISPR",
                    "Disease or context": "CCR5 targeted for HIV resistance",
                    "Key takeaway": "Germline editing caused mosaicism; stricter rules followed"
                }
            }
        }
    ]
}
