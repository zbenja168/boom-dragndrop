BRICK = {
    "brick_num": 11,
    "brick_title": "The Central Dogma: DNA to RNA to Proteins",
    "games": [
        {
            "slug": "gene_regulatory_elements",
            "title": "Gene Regulatory Elements",
            "subtitle": "Match each DNA regulatory element to its location, function, and key detail",
            "categories": ["Location", "Function", "Key Detail"],
            "data": {
                "CAAT box": {
                    "Location": "About 70-80 nucleotides upstream of the start site",
                    "Function": "Proximal promoter element that recruits transcription factors",
                    "Key Detail": "One of the core RNA polymerase II promoter boxes"
                },
                "TATA box": {
                    "Location": "About 25-30 nucleotides upstream of the start site",
                    "Function": "Proximal promoter element that positions the transcription machinery",
                    "Key Detail": "Sits just upstream of the transcription start site (+1)"
                },
                "Enhancer": {
                    "Location": "Thousands of base pairs upstream or downstream of the gene",
                    "Function": "Distal sequence that upregulates gene expression",
                    "Key Detail": "Recruits activating transcription factors"
                },
                "Silencer": {
                    "Location": "Thousands of base pairs distant from the gene",
                    "Function": "Distal sequence that downregulates gene expression",
                    "Key Detail": "Recruits repressor factors that inhibit transcription"
                },
                "Polyadenylation signal": {
                    "Location": "Near the 3' end of the pre-mRNA",
                    "Function": "Signals a downstream cleavage site for poly(A) tail addition",
                    "Key Detail": "Consensus sequence 5'-AAUAAA-3'"
                }
            }
        },
        {
            "slug": "mrna_anatomy",
            "title": "Anatomy of a Mature mRNA",
            "subtitle": "Match each mRNA feature to its location, function, and defining feature",
            "categories": ["Location on mRNA", "Function", "Defining Feature"],
            "data": {
                "5' cap": {
                    "Location on mRNA": "The extreme 5' end",
                    "Function": "Aids nuclear export, blocks 5' exonucleases, and initiates translation",
                    "Defining Feature": "A 7-methylguanosine linked by a 5'-to-5' triphosphate bridge"
                },
                "5' UTR": {
                    "Location on mRNA": "Between the cap and the start codon",
                    "Function": "Untranslated leader region that is scanned before translation",
                    "Defining Feature": "All nucleotides upstream of the AUG start codon"
                },
                "Start codon": {
                    "Location on mRNA": "The beginning of the coding segment",
                    "Function": "Sets the reading frame and codes the first amino acid",
                    "Defining Feature": "AUG, which codes for methionine"
                },
                "Stop codon": {
                    "Location on mRNA": "The end of the coding segment",
                    "Function": "Signals translation termination via a release factor",
                    "Defining Feature": "UAA, UGA, or UAG"
                },
                "3' UTR": {
                    "Location on mRNA": "Downstream of the stop codon",
                    "Function": "Untranslated trailing region",
                    "Defining Feature": "Nucleotides after the stop codon before the tail"
                },
                "Poly(A) tail": {
                    "Location on mRNA": "The extreme 3' end",
                    "Function": "Stabilizes the mRNA and shields it from 3' exonucleases",
                    "Defining Feature": "40-250 adenosine nucleotides bound by PABP"
                }
            }
        },
        {
            "slug": "splicing_components",
            "title": "Splicing and the Spliceosome",
            "subtitle": "Match each splicing component to its identity, role, and key feature",
            "categories": ["Identity", "Role in Splicing", "Key Feature"],
            "data": {
                "5' donor site": {
                    "Identity": "The 5' start of an intron",
                    "Role in Splicing": "Cut first, generating the lariat intermediate",
                    "Key Feature": "Contains the sequence 5'-GU"
                },
                "3' acceptor site": {
                    "Identity": "The 3' end of an intron",
                    "Role in Splicing": "Second cleavage site where the two exons are joined",
                    "Key Feature": "Contains the sequence AG-3'"
                },
                "Branch point": {
                    "Identity": "An internal adenine within the intron",
                    "Role in Splicing": "Forms a 5'-2' bond that creates the lariat",
                    "Key Feature": "A single adenine base"
                },
                "Spliceosome": {
                    "Identity": "A complex of small nuclear ribonucleoproteins",
                    "Role in Splicing": "Removes introns and joins exons, then disassembles",
                    "Key Feature": "Built from snRNPs such as U1 and U2"
                },
                "Exon": {
                    "Identity": "A coding segment retained in the mRNA",
                    "Role in Splicing": "Kept and translated into protein",
                    "Key Feature": "Joined to adjacent exons after intron removal"
                },
                "Intron": {
                    "Identity": "An intervening non-coding segment",
                    "Role in Splicing": "Removed from pre-mRNA before translation",
                    "Key Feature": "Released folded into a lariat"
                }
            }
        },
        {
            "slug": "dogma_enzymes",
            "title": "Central-Dogma Enzymes and Exceptions",
            "subtitle": "Match each enzyme to its template, product, and where it is seen",
            "categories": ["Template / Substrate", "Product", "Where Seen / Key Detail"],
            "data": {
                "RNA polymerase II": {
                    "Template / Substrate": "The DNA template (antisense) strand",
                    "Product": "Pre-mRNA (protein-coding transcript)",
                    "Where Seen / Key Detail": "Reads DNA 3' to 5' while building RNA 5' to 3'"
                },
                "Reverse transcriptase": {
                    "Template / Substrate": "RNA",
                    "Product": "A DNA strand",
                    "Where Seen / Key Detail": "Retroviruses (HIV) and Hepatitis B; a central-dogma exception"
                },
                "RNA-dependent RNA polymerase": {
                    "Template / Substrate": "RNA",
                    "Product": "More RNA",
                    "Where Seen / Key Detail": "SARS-CoV-2 and positive-sense single-stranded RNA viruses"
                },
                "Aminoacyl-tRNA synthetase": {
                    "Template / Substrate": "An amino acid and its cognate tRNA",
                    "Product": "A charged (aminoacyl) tRNA",
                    "Where Seen / Key Detail": "Uses ATP; one specific enzyme for each of the 20 amino acids"
                },
                "Poly(A) polymerase": {
                    "Template / Substrate": "ATP as the substrate",
                    "Product": "The 3' poly(A) tail",
                    "Where Seen / Key Detail": "Adds 40-250 adenosines after cleavage of the pre-mRNA"
                }
            }
        }
    ]
}
