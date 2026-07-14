BRICK = {
    "brick_num": 52,
    "brick_title": "Multifactorial Disorders",
    "games": [
        {
            "slug": "factors_complex_disease",
            "title": "Factors in Complex Disease",
            "subtitle": "Match each factor to its domain, example mechanism, and nature of change",
            "categories": ["Domain", "Example Mechanism", "Nature of Change"],
            "data": {
                "SNPs / point mutations": {
                    "Domain": "Genetics",
                    "Example Mechanism": "Single-nucleotide variants in the DNA sequence",
                    "Nature of Change": "Alteration of the DNA sequence itself"
                },
                "CpG methylation": {
                    "Domain": "Epigenetics",
                    "Example Mechanism": "Methyl groups added at CpG sites",
                    "Nature of Change": "Reversible mark; no change in DNA sequence"
                },
                "Histone modification": {
                    "Domain": "Epigenetics",
                    "Example Mechanism": "Chemical tags altering chromatin packing",
                    "Nature of Change": "Shifts gene expression without sequence change"
                },
                "Toxins and pathogens": {
                    "Domain": "Environment",
                    "Example Mechanism": "Nutrition, drugs, toxins, and infections",
                    "Nature of Change": "External exposures acting on the host"
                },
                "Non-coding RNAs (miRNA/ncRNA)": {
                    "Domain": "Genetics-Epigenetics overlap",
                    "Example Mechanism": "Regulatory RNAs fine-tuning gene expression",
                    "Nature of Change": "Post-transcriptional regulation of genes"
                }
            }
        },
        {
            "slug": "threshold_model_risk",
            "title": "Risk Concepts in the Threshold Model",
            "subtitle": "Match each concept to its definition, key relationship, and brick example",
            "categories": ["Definition", "Key Relationship", "Brick Example"],
            "data": {
                "Occurrence risk": {
                    "Definition": "Chance of being affected without a family history",
                    "Key Relationship": "Reflects baseline population liability",
                    "Brick Example": "Risk of Alzheimer's with no affected relative"
                },
                "Recurrence risk": {
                    "Definition": "Chance of being affected when a relative already has it",
                    "Key Relationship": "Rises with the number of shared risk factors",
                    "Brick Example": "2-5% in future pregnancies after a neural tube defect"
                },
                "Liability threshold": {
                    "Definition": "Cutoff dividing unaffected from affected on the liability curve",
                    "Key Relationship": "Higher threshold means lower population prevalence",
                    "Brick Example": "Neural tube defects in ~1 in 1,500 live births"
                },
                "Higher threshold in less-affected sex": {
                    "Definition": "Affected member of the resistant sex carries a greater genetic load",
                    "Key Relationship": "Raises recurrence risk among that person's relatives",
                    "Brick Example": "Affected female with pyloric stenosis (male-to-female 4:1)"
                }
            }
        },
        {
            "slug": "study_methods",
            "title": "Comparing Study Methods",
            "subtitle": "Match each method to its core approach, what it reveals, and a brick example",
            "categories": ["Core Approach", "What It Reveals", "Brick Example"],
            "data": {
                "Twin studies": {
                    "Core Approach": "Compare disease concordance in monozygotic vs dizygotic twins",
                    "What It Reveals": "Genetic versus environmental contribution",
                    "Brick Example": "Oral cleft 50% MZ vs 8% DZ concordance"
                },
                "GWAS": {
                    "Core Approach": "Scan many genomes for SNPs more frequent in cases than controls",
                    "What It Reveals": "Susceptibility loci and common risk variants",
                    "Brick Example": "~75 susceptibility loci for type 2 diabetes"
                },
                "Manhattan plot": {
                    "Core Approach": "Plot -log10(p) of variants across the chromosomes",
                    "What It Reveals": "Genomic regions crossing the significance threshold",
                    "Brick Example": "12 significant loci in an ADHD meta-analysis"
                },
                "Linkage analysis": {
                    "Core Approach": "Track co-inheritance of markers within families",
                    "What It Reveals": "Familial, higher-penetrance monogenic loci",
                    "Brick Example": "Monogenic IBD genes IL10RA, XIAP, CYBB"
                }
            }
        },
        {
            "slug": "genes_and_pharmacogenomics",
            "title": "Genes, Drugs, and Multifactorial Traits",
            "subtitle": "Match each theme to its associated gene(s), molecular role, and clinical link",
            "categories": ["Associated Gene(s)", "Molecular Role", "Clinical / Phenotype Link"],
            "data": {
                "Warfarin sensitivity": {
                    "Associated Gene(s)": "VKORC1",
                    "Molecular Role": "Alters expression of vitamin K epoxide reductase (the drug target)",
                    "Clinical / Phenotype Link": "Changes body's sensitivity to warfarin, guiding dose"
                },
                "Warfarin metabolism": {
                    "Associated Gene(s)": "CYP2C9",
                    "Molecular Role": "Encodes the liver enzyme that breaks down warfarin",
                    "Clinical / Phenotype Link": "Slow-metabolizer variants raise drug levels and bleeding risk"
                },
                "Migraine drug targets": {
                    "Associated Gene(s)": "CALCA/CALCB, HTR1F",
                    "Molecular Role": "Encode CGRP and the serotonin 5-HT1F receptor",
                    "Clinical / Phenotype Link": "Targets of gepants/monoclonal antibodies and ditans"
                },
                "Addiction / stress resilience": {
                    "Associated Gene(s)": "MAOA, SLC6A4, COMT",
                    "Molecular Role": "Modulate stress response and resilience",
                    "Clinical / Phenotype Link": "Different alleles influence addiction susceptibility"
                },
                "Cocaine dependence": {
                    "Associated Gene(s)": "HIST1H2BD",
                    "Molecular Role": "Histone-gene variant affecting chromatin",
                    "Clinical / Phenotype Link": "Associated specifically with cocaine dependence"
                }
            }
        }
    ]
}
