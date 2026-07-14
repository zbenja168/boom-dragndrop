BRICK = {
    "brick_num": 51,
    "brick_title": "Genomic Imprinting Disorders",
    "games": [
        {
            "slug": "imprinting_disorder_genetics",
            "title": "Imprinting Disorders: Genetic Basis",
            "subtitle": "Match each imprinting disorder to its chromosomal locus, key gene, and genetic mechanism",
            "categories": ["Chromosomal Locus", "Key Gene", "Genetic Mechanism"],
            "data": {
                "Prader-Willi syndrome": {
                    "Chromosomal Locus": "15q11-q13",
                    "Key Gene": "SNRPN",
                    "Genetic Mechanism": "Loss of paternal expression (paternal deletion or maternal UPD)"
                },
                "Angelman syndrome": {
                    "Chromosomal Locus": "15q11-q13",
                    "Key Gene": "UBE3A",
                    "Genetic Mechanism": "Loss of maternal expression (maternal deletion or paternal UPD)"
                },
                "Silver-Russell syndrome": {
                    "Chromosomal Locus": "11p15 (ICR1)",
                    "Key Gene": "IGF2",
                    "Genetic Mechanism": "Hypomethylation of paternal ICR1 lowering IGF2"
                },
                "Beckwith-Wiedemann syndrome": {
                    "Chromosomal Locus": "11p15",
                    "Key Gene": "IGF2 / H19",
                    "Genetic Mechanism": "Hypermethylation of paternal 11p15 region"
                },
                "Transient neonatal diabetes": {
                    "Chromosomal Locus": "6q24",
                    "Key Gene": "PLAGL1",
                    "Genetic Mechanism": "Paternal UPD of chromosome 6 or 6q24 duplication"
                }
            }
        },
        {
            "slug": "imprinting_clinical_features",
            "title": "Imprinting Disorders: Clinical Picture",
            "subtitle": "Match each syndrome to its infancy findings, later findings, and distinctive feature",
            "categories": ["Infancy / Childhood", "Adulthood / Later", "Distinctive Feature"],
            "data": {
                "Prader-Willi syndrome": {
                    "Infancy / Childhood": "Hypotonia, poor suck, failure to thrive",
                    "Adulthood / Later": "Hyperphagia, obesity, type 2 diabetes, hypogonadism",
                    "Distinctive Feature": "Almond-shaped eyes, small hands and feet"
                },
                "Angelman syndrome": {
                    "Infancy / Childhood": "Developmental delay, lack of babbling, seizures",
                    "Adulthood / Later": "Minimal speech and severe intellectual impairment",
                    "Distinctive Feature": "Frequent laughter, happy demeanor, hand-flapping, ataxia"
                },
                "Silver-Russell syndrome": {
                    "Infancy / Childhood": "Intrauterine growth retardation, feeding difficulty, hypoglycemia",
                    "Adulthood / Later": "Severe postnatal short stature (dwarfism)",
                    "Distinctive Feature": "Triangular face, body asymmetry, clinodactyly of fifth finger"
                },
                "Beckwith-Wiedemann syndrome": {
                    "Infancy / Childhood": "Macroglossia, umbilical hernia, hypoglycemia",
                    "Adulthood / Later": "Overgrowth of the body",
                    "Distinctive Feature": "Large tongue with prominent abdominal wall defect"
                }
            }
        },
        {
            "slug": "imprinting_diagnostics",
            "title": "Diagnosing Imprinting Disorders",
            "subtitle": "Match each laboratory technique to what it detects, whether it gives parental origin, and its clinical role",
            "categories": ["What It Detects", "Parental-Origin Information", "Clinical Role"],
            "data": {
                "MS-MLPA": {
                    "What It Detects": "Abnormal methylation, CNVs, and UPD in imprinted regions",
                    "Parental-Origin Information": "Yes; probe-dependent, distinguishes affected allele",
                    "Clinical Role": "Most widely used first-line test"
                },
                "Targeted NGS panel": {
                    "What It Detects": "CNVs, UPDs, and methylation across multiple DMRs",
                    "Parental-Origin Information": "Yes; covers multiple differentially methylated regions",
                    "Clinical Role": "Valuable when WGS/WES are not well-suited"
                },
                "aCGH": {
                    "What It Detects": "Copy number variations across the whole genome",
                    "Parental-Origin Information": "No; requires further analysis for parental origin",
                    "Clinical Role": "Identifies deletions/duplications, not allele parent"
                },
                "Microsatellite analysis": {
                    "What It Detects": "Short polymorphic repeats varying in length between people",
                    "Parental-Origin Information": "Yes; traces inheritance by comparing proband to parents",
                    "Clinical Role": "Detects UPD and parental origin of abnormalities"
                },
                "SNP analysis": {
                    "What It Detects": "Single base-pair polymorphisms across the genome",
                    "Parental-Origin Information": "Yes; determines origin when analyzed with parental genotypes",
                    "Clinical Role": "Confirms parental origin of affected chromosome"
                }
            }
        },
        {
            "slug": "imprinting_molecular_basis",
            "title": "Molecular Basis of Imprinting",
            "subtitle": "Match each concept to its description, its location/timing, and its effect",
            "categories": ["Description", "Location / Timing", "Effect on Expression"],
            "data": {
                "DNA methylation": {
                    "Description": "Epigenetic mark at the 5' cytosine of CpG dinucleotides",
                    "Location / Timing": "At CpG islands, especially within ICRs",
                    "Effect on Expression": "Silences the gene without changing DNA sequence"
                },
                "Imprinting Control Region": {
                    "Description": "cis-acting DNA sequence governing imprinted expression",
                    "Location / Timing": "Within CpG islands near gene promoters",
                    "Effect on Expression": "Directs parent-of-origin-specific expression"
                },
                "Gametogenesis reprogramming": {
                    "Description": "Genome-wide demethylation then sex-specific rewriting of imprints",
                    "Location / Timing": "In primordial germ cells before fertilization",
                    "Effect on Expression": "Sets new maternal versus paternal imprints"
                },
                "Uniparental disomy": {
                    "Description": "Both chromosome copies inherited from one parent",
                    "Location / Timing": "Arises from rescue of aneuploidy during division",
                    "Effect on Expression": "Abnormal gene dosage leading to disease"
                },
                "Epimutation": {
                    "Description": "Epigenetic change with no alteration of DNA sequence",
                    "Location / Timing": "A switch in ICR methylation pattern (biparental alleles)",
                    "Effect on Expression": "Changes parent-of-origin expression pattern"
                },
                "ZFP57": {
                    "Description": "Methylation-sensitive transcription factor",
                    "Location / Timing": "Binds methylated ICR alleles, recruits co-repressor",
                    "Effect on Expression": "Maintains imprints; loss causes MLID in cancer"
                }
            }
        }
    ]
}
