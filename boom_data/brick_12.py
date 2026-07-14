BRICK = {
    "brick_num": 12,
    "brick_title": "DNA Point Mutations",
    "games": [
        {
            "slug": "point_mutation_types",
            "title": "Point Mutations by Effect",
            "subtitle": "Match each point mutation to its amino-acid outcome, protein impact, and class",
            "categories": ["Amino Acid Outcome", "Protein Function Impact", "Classification"],
            "data": {
                "Silent Mutation": {
                    "Amino Acid Outcome": "Same amino acid encoded (no change)",
                    "Protein Function Impact": "No effect on protein structure or function",
                    "Classification": "Synonymous / silent"
                },
                "Conservative Missense": {
                    "Amino Acid Outcome": "Different amino acid with similar properties",
                    "Protein Function Impact": "Usually mild; little effect on folding",
                    "Classification": "Nonsynonymous missense (conservative)"
                },
                "Non-conservative Missense": {
                    "Amino Acid Outcome": "Different amino acid with different charge or size",
                    "Protein Function Impact": "Often greater effect on protein function",
                    "Classification": "Nonsynonymous missense (non-conservative)"
                },
                "Nonsense Mutation": {
                    "Amino Acid Outcome": "Premature stop codon replaces an amino acid",
                    "Protein Function Impact": "Truncated, usually non-functional protein",
                    "Classification": "Nonsynonymous nonsense"
                }
            }
        },
        {
            "slug": "protein_level_effects",
            "title": "Protein-Level Mutation Effects",
            "subtitle": "Match each mechanism to its definition, effect on gene product, and key note",
            "categories": ["Definition", "Effect on Gene Product", "Inheritance or Example"],
            "data": {
                "Gain-of-function": {
                    "Definition": "Product expressed inappropriately or acquires new abnormal function",
                    "Effect on Gene Product": "Excess, mistimed, or novel activity",
                    "Inheritance or Example": "Typically acts as a dominant condition"
                },
                "Loss-of-function": {
                    "Definition": "Reduces gene activity by lowering production or activity",
                    "Effect on Gene Product": "Decreased amount of functional product",
                    "Inheritance or Example": "Recessive or dominant depending on the gene"
                },
                "Null Mutation": {
                    "Definition": "Loss-of-function causing complete absence of functional product",
                    "Effect on Gene Product": "Zero product from that allele (~50% total)",
                    "Inheritance or Example": "Cause: whole-gene deletion or early stop codon"
                },
                "Haploinsufficiency": {
                    "Definition": "One functional allele (50% product) is not enough for normal phenotype",
                    "Effect on Gene Product": "50% of product is insufficient",
                    "Inheritance or Example": "Williams syndrome (7q11.23)"
                },
                "Dominant-negative": {
                    "Definition": "Abnormal product interferes with function of the normal protein",
                    "Effect on Gene Product": "Function ends up far below 50%",
                    "Inheritance or Example": "Acts as if both alleles are defective"
                }
            }
        },
        {
            "slug": "coding_reading_frame_terms",
            "title": "Coding Region and Reading-Frame Terms",
            "subtitle": "Match each term to what it is, its distinguishing feature, and its value or location",
            "categories": ["What It Is", "Distinguishing Feature", "Value or Location"],
            "data": {
                "Coding Sequence (CDS)": {
                    "What It Is": "Contiguous sequence confirmed to code for a protein",
                    "Distinguishing Feature": "Backed by experimental evidence or annotation",
                    "Value or Location": "Has AUG start plus stop; found in transcribed mRNA"
                },
                "Open Reading Frame (ORF)": {
                    "What It Is": "Potential protein-coding region in DNA or RNA",
                    "Distinguishing Feature": "May or may not actually code a protein",
                    "Value or Location": "Identified by sequence features; may not be transcribed"
                },
                "Reading Frames": {
                    "What It Is": "The possible frames a ribosome could use",
                    "Distinguishing Feature": "Three on the (+)-strand and three on the (-)-strand",
                    "Value or Location": "Six total per DNA segment"
                },
                "In-frame": {
                    "What It Is": "The single frame the ribosome uses to translate",
                    "Distinguishing Feature": "Must stay in one frame for the correct protein",
                    "Value or Location": "Chosen from among the six frames"
                },
                "Splice Donor Site": {
                    "What It Is": "Start sequence of an intron",
                    "Distinguishing Feature": "Altering it can cause an intron to be retained",
                    "Value or Location": "5'-GU at the intron start"
                },
                "Splice Acceptor Site": {
                    "What It Is": "End sequence of an intron",
                    "Distinguishing Feature": "Altering it can cause an exon to be skipped",
                    "Value or Location": "AG-3' at the intron end"
                }
            }
        },
        {
            "slug": "mutation_origin_indels",
            "title": "Mutation Origin, Indels, and Examples",
            "subtitle": "Match each mutation to its mechanism, consequence, and clinical example or note",
            "categories": ["Mechanism", "Consequence", "Example or Note"],
            "data": {
                "Somatic Mutation": {
                    "Mechanism": "Occurs in non-reproductive tissue, not inherited",
                    "Consequence": "Affects only the individual; can be a patchy region",
                    "Example or Note": "McCune-Albright syndrome (bone, skin, endocrine)"
                },
                "Germline Mutation": {
                    "Mechanism": "Occurs in ova or sperm and is heritable",
                    "Consequence": "Present in every cell; passed to offspring",
                    "Example or Note": "Neurofibromatosis type 1 (NF-1 gene)"
                },
                "Frameshift Mutation": {
                    "Mechanism": "Insertion or deletion of non-triplet bases in coding region",
                    "Consequence": "Distorts every downstream codon",
                    "Example or Note": "Can generate a premature stop codon"
                },
                "In-frame Indel": {
                    "Mechanism": "Insertion or deletion of a multiple of three bases",
                    "Consequence": "Adds or removes a few amino acids but stays in frame",
                    "Example or Note": "Frameshift is avoided"
                },
                "Nonsense (PTC) Disease": {
                    "Mechanism": "Point mutation creating a premature termination codon",
                    "Consequence": "Truncated, dysfunctional protein",
                    "Example or Note": "Cystic fibrosis (CFTR)"
                }
            }
        }
    ]
}
