BRICK = {
    "brick_num": 46,
    "brick_title": "Pedigrees and Patterns of Monogenic Inheritance",
    "games": [
        {
            "slug": "inheritance_patterns",
            "title": "Patterns of Monogenic Inheritance",
            "subtitle": "Match each inheritance pattern to its genetic location, pedigree clue, and transmission rule",
            "categories": ["Genetic Location", "Signature Pedigree Clue", "Transmission Rule"],
            "data": {
                "Autosomal Dominant": {
                    "Genetic Location": "One of the 22 autosomes (non-sex chromosomes)",
                    "Signature Pedigree Clue": "Affected individuals in every generation with male-to-male transmission",
                    "Transmission Rule": "Only one pathogenic allele is needed to express the phenotype"
                },
                "Autosomal Recessive": {
                    "Genetic Location": "One of the 22 autosomes (non-sex chromosomes)",
                    "Signature Pedigree Clue": "Affected child of unaffected carrier parents; may skip generations; consanguinity",
                    "Transmission Rule": "Two pathogenic alleles (one from each parent) are needed"
                },
                "X-linked Recessive": {
                    "Genetic Location": "The X chromosome",
                    "Signature Pedigree Clue": "Mostly affected males with generations skipping expression",
                    "Transmission Rule": "Males need only one X-variant allele; no male-to-male transmission"
                },
                "X-linked Dominant": {
                    "Genetic Location": "The X chromosome",
                    "Signature Pedigree Clue": "All daughters of an affected male are affected; more females affected",
                    "Transmission Rule": "Fathers transmit to all daughters but never to sons; females often milder"
                },
                "Y-linked": {
                    "Genetic Location": "The Y chromosome",
                    "Signature Pedigree Clue": "Only males affected, passed straight down the paternal line",
                    "Transmission Rule": "Fathers transmit to all sons only"
                },
                "Mitochondrial": {
                    "Genetic Location": "The circular mitochondrial chromosome (37 genes)",
                    "Signature Pedigree Clue": "Both sexes affected; all children of an affected female may be affected",
                    "Transmission Rule": "Maternally inherited; affected males do not transmit"
                }
            }
        },
        {
            "slug": "genetic_terminology",
            "title": "Core Genetics Terminology",
            "subtitle": "Match each term to its definition, what it describes, and a related contrast",
            "categories": ["Definition", "What It Describes", "Related Contrast"],
            "data": {
                "Genotype": {
                    "Definition": "An individual's set of genes, or the two alleles at a locus",
                    "What It Describes": "The underlying genetic makeup inherited from both parents",
                    "Related Contrast": "Contrasts with phenotype"
                },
                "Phenotype": {
                    "Definition": "The physical, clinical, cellular, or biochemical traits from a genotype",
                    "What It Describes": "The observable or testable expression of a genotype",
                    "Related Contrast": "Contrasts with genotype"
                },
                "Locus": {
                    "Definition": "A specific location on a chromosome",
                    "What It Describes": "Where a particular gene resides on a homologous pair",
                    "Related Contrast": "Often used interchangeably with the word gene"
                },
                "Allele": {
                    "Definition": "A variation of a gene or DNA sequence",
                    "What It Describes": "An alternative version of a gene at a given locus",
                    "Related Contrast": "Can be wild-type or a pathogenic variant"
                },
                "Wild-type Allele": {
                    "Definition": "An allele encoding a common natural variant of a gene",
                    "What It Describes": "The typical, non-disease form of the gene",
                    "Related Contrast": "Opposite of a pathogenic variant"
                },
                "Pathogenic Variant": {
                    "Definition": "An allele variation that results in disease",
                    "What It Describes": "A disease-causing form of the gene",
                    "Related Contrast": "Also called a mutation or mutant allele"
                }
            }
        },
        {
            "slug": "zygosity_states",
            "title": "Zygosity and Carrier States",
            "subtitle": "Match each status to its allele composition, a typical example, and its disease expression",
            "categories": ["Allele Composition at Locus", "Typical Example", "Disease Expression"],
            "data": {
                "Homozygote": {
                    "Allele Composition at Locus": "Two identical alleles at a nuclear DNA locus",
                    "Typical Example": "A person with two recessive pathogenic alleles",
                    "Disease Expression": "Expresses a recessive phenotype when both alleles are pathogenic"
                },
                "Heterozygote": {
                    "Allele Composition at Locus": "Two different alleles at a nuclear DNA locus",
                    "Typical Example": "An unaffected carrier parent of an autosomal recessive disease",
                    "Disease Expression": "Expresses dominant conditions but not recessive ones"
                },
                "Hemizygote": {
                    "Allele Composition at Locus": "Only a single allele present for a gene",
                    "Typical Example": "A male considering genes on his single X chromosome",
                    "Disease Expression": "Expresses an X-linked recessive disease with just one variant allele"
                },
                "Carrier": {
                    "Allele Composition at Locus": "One pathogenic allele plus one wild-type allele",
                    "Typical Example": "A mother heterozygous for hemophilia A",
                    "Disease Expression": "Does not display the disease phenotype of the pathogenic allele"
                }
            }
        },
        {
            "slug": "pedigree_symbols",
            "title": "Reading a Pedigree",
            "subtitle": "Match each pedigree symbol or term to its appearance and its significance",
            "categories": ["Symbol or Appearance", "Meaning", "Significance"],
            "data": {
                "Affected Individual": {
                    "Symbol or Appearance": "A fully shaded square or circle",
                    "Meaning": "An individual who expresses the disease phenotype",
                    "Significance": "Marks who in the family is clinically affected"
                },
                "Carrier": {
                    "Symbol or Appearance": "A symbol with a central dot or half-filled shading",
                    "Meaning": "Has one pathogenic allele without displaying disease",
                    "Significance": "Commonly seen among parents in autosomal recessive pedigrees"
                },
                "Marriage or Union": {
                    "Symbol or Appearance": "A horizontal line connecting two partner symbols",
                    "Meaning": "A mating relationship between two reproductive partners",
                    "Significance": "Joins the parents whose offspring are drawn below"
                },
                "Consanguinity": {
                    "Symbol or Appearance": "A double horizontal line between two partners",
                    "Meaning": "The partners are biologically related and share an ancestor",
                    "Significance": "Raises the chance both carry the same recessive allele"
                },
                "Proband": {
                    "Symbol or Appearance": "A shaded symbol with an arrow pointing to it",
                    "Meaning": "The affected person who first brings the family to attention",
                    "Significance": "Serves as the index case for tracing the family history"
                },
                "Deceased": {
                    "Symbol or Appearance": "A symbol with a diagonal slash through it",
                    "Meaning": "An individual in the pedigree who has died",
                    "Significance": "Records mortality while preserving that person's place in the family"
                }
            }
        }
    ]
}
