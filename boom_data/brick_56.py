BRICK = {
    "brick_num": 56,
    "brick_title": "Molecular Biology Techniques (3 of 3), RNA analysis",
    "games": [
        {
            "slug": "rna_techniques",
            "title": "RNA Analysis Techniques",
            "subtitle": "Match each technique to its core principle, main application, and key feature",
            "categories": ["Core Principle", "Primary Application", "Key Feature"],
            "data": {
                "RT-PCR": {
                    "Core Principle": "Reverse transcriptase converts RNA into complementary DNA (cDNA), then it is amplified",
                    "Primary Application": "Detect RNA from viruses or expressed genes; first step for real-time PCR",
                    "Key Feature": "Endpoint detection that is not inherently quantitative"
                },
                "RT-qPCR (real-time PCR)": {
                    "Core Principle": "Fluorescence is measured each cycle to monitor DNA amplification in real time",
                    "Primary Application": "Precise, targeted quantification of known genes and viral load",
                    "Key Feature": "Requires specific primers; low throughput per run"
                },
                "RNA-Seq": {
                    "Core Principle": "Next-generation sequencing profiles the entire transcriptome",
                    "Primary Application": "Exploratory discovery of novel genes and global expression changes",
                    "Key Feature": "Moderate sensitivity; low-expression genes may be missed"
                },
                "Single-cell RNA-Seq": {
                    "Core Principle": "Next-generation sequencing of RNA from individual cells",
                    "Primary Application": "Identify distinct cell populations in heterogeneous tissue such as the tumor microenvironment",
                    "Key Feature": "Resolves rare cell subtypes that bulk averaging would miss"
                }
            }
        },
        {
            "slug": "qpcr_essentials",
            "title": "qPCR Essentials",
            "subtitle": "Match each qPCR component or concept to what it is, its role, and a key note",
            "categories": ["What It Is", "Role in qPCR", "Key Note"],
            "data": {
                "Reverse transcriptase": {
                    "What It Is": "Enzyme derived from retroviruses such as HIV-1 RT",
                    "Role in qPCR": "Converts extracted RNA into cDNA before amplification",
                    "Key Note": "Essential for replication of retroviruses like HIV and HTLV"
                },
                "Taq polymerase": {
                    "What It Is": "Thermostable DNA polymerase",
                    "Role in qPCR": "Amplifies the cDNA target during repeated cycles",
                    "Key Note": "Also used in conventional PCR"
                },
                "Fluorescent compound": {
                    "What It Is": "Reporter dye or probe added to the reaction",
                    "Role in qPCR": "Emits a signal measured each cycle to track amplification",
                    "Key Note": "Its real-time readout distinguishes qPCR from conventional PCR"
                },
                "Cycle threshold (Ct)": {
                    "What It Is": "Cycle number where fluorescence exceeds the background level",
                    "Role in qPCR": "Inversely proportional to the initial amount of target",
                    "Key Note": "Low Ct means highly expressed; high Ct means poorly expressed"
                },
                "Standard curve": {
                    "What It Is": "Plot of Ct versus log10 of known concentrations",
                    "Role in qPCR": "Allows interpolation of unknown sample concentrations",
                    "Key Note": "Basis of absolute quantification, e.g. HIV viral load in copies/mL"
                },
                "Specific primers": {
                    "What It Is": "Short sequences complementary to the gene of interest",
                    "Role in qPCR": "Define the target and confer reaction specificity",
                    "Key Note": "Make qPCR a targeted method requiring known genes"
                }
            }
        },
        {
            "slug": "transcriptomics",
            "title": "RNA-Seq & Transcriptomics",
            "subtitle": "Match each method or tool to its approach, purpose, and distinguishing feature",
            "categories": ["Approach", "Purpose", "Distinguishing Feature"],
            "data": {
                "Bulk RNA-Seq": {
                    "Approach": "NGS on RNA pooled from a tissue or cell population",
                    "Purpose": "Compare global gene expression between conditions",
                    "Distinguishing Feature": "Averages signal across all cells in the sample"
                },
                "Single-cell RNA-Seq": {
                    "Approach": "NGS on RNA from individual isolated cells",
                    "Purpose": "Resolve distinct cell populations and lineage trajectories",
                    "Distinguishing Feature": "Detects rare subtypes lost to bulk averaging"
                },
                "cDNA synthesis": {
                    "Approach": "Reverse transcription of extracted RNA",
                    "Purpose": "Prepare the template needed for sequencing",
                    "Distinguishing Feature": "Shared first step with RT-qPCR"
                },
                "Volcano plot": {
                    "Approach": "Graph of fold change against statistical significance",
                    "Purpose": "Highlight significantly up- or downregulated genes",
                    "Distinguishing Feature": "Separates upregulated and downregulated genes visually"
                },
                "Heatmap": {
                    "Approach": "Color-coded matrix of expression values",
                    "Purpose": "Observe expression patterns across many samples",
                    "Distinguishing Feature": "Clusters genes and samples by similarity"
                }
            }
        },
        {
            "slug": "qpcr_vs_rnaseq",
            "title": "RT-qPCR vs RNA-Seq",
            "subtitle": "Match each feature to the RT-qPCR and RNA-Seq descriptions",
            "categories": ["RT-qPCR", "RNA-Seq"],
            "data": {
                "Purpose": {
                    "RT-qPCR": "Targeted analysis of specific genes",
                    "RNA-Seq": "Global, exploratory analysis of the entire transcriptome"
                },
                "Sensitivity": {
                    "RT-qPCR": "Very high; can detect low-abundance transcripts",
                    "RNA-Seq": "Moderate; low-expression genes may be missed"
                },
                "Precision": {
                    "RT-qPCR": "High, due to specific primer design",
                    "RNA-Seq": "Lower; depends on sequencing depth and alignment accuracy"
                },
                "Throughput": {
                    "RT-qPCR": "Low; limited to a few genes per run",
                    "RNA-Seq": "High; thousands of genes analyzed simultaneously"
                },
                "Cost": {
                    "RT-qPCR": "Relatively low for small gene sets",
                    "RNA-Seq": "Higher, especially for deep sequencing or many samples"
                },
                "Limitations": {
                    "RT-qPCR": "Requires prior knowledge of the target genes",
                    "RNA-Seq": "May miss low-expression or poorly annotated genes"
                }
            }
        }
    ]
}
