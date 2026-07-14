BRICK = {
    "brick_num": 40,
    "brick_title": "Chromosomes",
    "games": [
        {
            "slug": "chromatin_packaging",
            "title": "Chromosome Anatomy and Packaging",
            "subtitle": "Match each structure to what it is, its composition/location, and its key feature",
            "categories": ["What it is", "Composition / location", "Key feature"],
            "data": {
                "Nucleosome": {
                    "What it is": "Basic repeating unit of chromatin",
                    "Composition / location": "DNA wrapped around a histone octamer (H2A, H2B, H3, H4 x2)",
                    "Key feature": "Packages and condenses genomic DNA"
                },
                "H1 histone": {
                    "What it is": "Linker histone",
                    "Composition / location": "Sits on DNA between adjacent nucleosomes",
                    "Key feature": "Further compacts the chromatin fiber"
                },
                "Centromere": {
                    "What it is": "Constricted region of a chromosome",
                    "Composition / location": "Point where the two sister chromatids are joined",
                    "Key feature": "Attachment site for the mitotic spindle"
                },
                "Euchromatin": {
                    "What it is": "Loosely packed chromatin",
                    "Composition / location": "Less condensed DNA dispersed during interphase",
                    "Key feature": "Open, extended form of chromatin"
                },
                "Heterochromatin": {
                    "What it is": "Densely packed chromatin",
                    "Composition / location": "Highly condensed, supercoiled DNA",
                    "Key feature": "Compact form leading toward the metaphase chromosome"
                }
            }
        },
        {
            "slug": "cell_division",
            "title": "Mitosis, Meiosis, and Fertilization",
            "subtitle": "Match each process to its product, the ploidy of the resulting cells, and its defining event",
            "categories": ["Number of daughter cells", "Ploidy of resulting cells", "Distinguishing event"],
            "data": {
                "Mitosis": {
                    "Number of daughter cells": "Two",
                    "Ploidy of resulting cells": "Diploid (46), genetically identical",
                    "Distinguishing event": "Somatic division; sister chromatids separate to each daughter"
                },
                "Meiosis I": {
                    "Number of daughter cells": "Two",
                    "Ploidy of resulting cells": "Haploid (23), each chromosome still has 2 chromatids",
                    "Distinguishing event": "Homologous chromosomes pair, cross over, then segregate"
                },
                "Meiosis II": {
                    "Number of daughter cells": "Four total",
                    "Ploidy of resulting cells": "Haploid (23), single chromatid each",
                    "Distinguishing event": "Sister chromatids finally separate to form gametes"
                },
                "Fertilization": {
                    "Number of daughter cells": "One (zygote)",
                    "Ploidy of resulting cells": "Diploid (46) restored",
                    "Distinguishing event": "Two haploid gametes fuse into a conceptus"
                }
            }
        },
        {
            "slug": "structural_variants",
            "title": "Structural Chromosome Variants",
            "subtitle": "Match each rearrangement to its definition, its effect on genetic material, and its karyotype abbreviation",
            "categories": ["Definition", "Effect on genetic material", "Karyotype abbreviation"],
            "data": {
                "Balanced reciprocal translocation": {
                    "Definition": "Two segments of nonhomologous chromosomes exchange places",
                    "Effect on genetic material": "Equal exchange with no net gain or loss",
                    "Karyotype abbreviation": "t, e.g. t(12;14)(q13;q32)"
                },
                "Robertsonian translocation": {
                    "Definition": "Fusion of long arms of two acrocentric chromosomes with loss of the short arms",
                    "Effect on genetic material": "Considered balanced; carrier has only 45 chromosomes",
                    "Karyotype abbreviation": "rob, e.g. rob(14;21)(q10;q10)"
                },
                "Deletion": {
                    "Definition": "Loss of a chromosome segment, terminal or interstitial",
                    "Effect on genetic material": "Net loss of genetic material",
                    "Karyotype abbreviation": "del, e.g. del(5)(p15)"
                },
                "Duplication": {
                    "Definition": "An abnormal extra copy of a portion of a chromosome",
                    "Effect on genetic material": "Gain of material causing partial trisomy",
                    "Karyotype abbreviation": "dup, e.g. dup(5)(q31q42)"
                },
                "Inversion": {
                    "Definition": "A chromosomal segment is flipped end to end",
                    "Effect on genetic material": "Rearrangement only, no loss or gain",
                    "Karyotype abbreviation": "Notation not emphasized in this brick"
                }
            }
        },
        {
            "slug": "cytogenetic_notation",
            "title": "Cytogenetic Notation Decoder",
            "subtitle": "Match each karyotype description to the chromosomes involved, the type of abnormality, and its meaning",
            "categories": ["Chromosome(s) involved", "Type of abnormality", "Meaning"],
            "data": {
                "47,XY,+21": {
                    "Chromosome(s) involved": "One extra chromosome 21",
                    "Type of abnormality": "Numerical (aneuploidy, trisomy)",
                    "Meaning": "Three copies of chromosome 21 (Down syndrome)"
                },
                "46,XX,del(4)(p15.1p15.32)": {
                    "Chromosome(s) involved": "Short arm of chromosome 4",
                    "Type of abnormality": "Interstitial deletion",
                    "Meaning": "Loss of a 4p segment; linked to fetal growth restriction"
                },
                "46,XY,t(9;22)(p22;q13)": {
                    "Chromosome(s) involved": "Chromosomes 9 and 22",
                    "Type of abnormality": "Balanced reciprocal translocation",
                    "Meaning": "9p and 22q segments swapped with no material lost"
                },
                "45,XY,rob(14;21)(q10;q10)": {
                    "Chromosome(s) involved": "Chromosomes 14 and 21",
                    "Type of abnormality": "Robertsonian translocation",
                    "Meaning": "Long arms fused, short arms lost, only 45 chromosomes"
                },
                "46,XY,dup(5)(q31q42)": {
                    "Chromosome(s) involved": "Long arm of chromosome 5",
                    "Type of abnormality": "Duplication (partial trisomy)",
                    "Meaning": "Extra copy of the q31 to q42 segment"
                }
            }
        }
    ]
}
