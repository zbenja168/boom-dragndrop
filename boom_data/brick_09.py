BRICK = {
    "brick_num": 9,
    "brick_title": "DNA Structure",
    "games": [
        {
            "slug": "nucleotide_building_blocks",
            "title": "Nucleotide Building Blocks",
            "subtitle": "Match each nitrogenous base to its ring class, complementary partner, and hydrogen bonds in that pair",
            "categories": ["Ring Class", "Complementary Base", "Hydrogen Bonds in Pair"],
            "data": {
                "Adenine": {
                    "Ring Class": "Purine (two-ring base)",
                    "Complementary Base": "Thymine",
                    "Hydrogen Bonds in Pair": "Two hydrogen bonds"
                },
                "Guanine": {
                    "Ring Class": "Purine (two-ring base)",
                    "Complementary Base": "Cytosine",
                    "Hydrogen Bonds in Pair": "Three hydrogen bonds"
                },
                "Cytosine": {
                    "Ring Class": "Pyrimidine (one-ring base)",
                    "Complementary Base": "Guanine",
                    "Hydrogen Bonds in Pair": "Three hydrogen bonds"
                },
                "Thymine": {
                    "Ring Class": "Pyrimidine (one-ring base)",
                    "Complementary Base": "Adenine",
                    "Hydrogen Bonds in Pair": "Two hydrogen bonds"
                },
                "Uracil": {
                    "Ring Class": "Pyrimidine (one-ring base)",
                    "Complementary Base": "Adenine (in RNA, replaces thymine)",
                    "Hydrogen Bonds in Pair": "Two hydrogen bonds"
                }
            }
        },
        {
            "slug": "molecular_features_dna",
            "title": "Molecular Features of the Double Helix",
            "subtitle": "Match each structural feature to what it is and why it matters",
            "categories": ["What It Is", "Bond or Force Involved", "Functional Significance"],
            "data": {
                "Phosphodiester bond": {
                    "What It Is": "Covalent link joining adjacent nucleotides in a strand",
                    "Bond or Force Involved": "Covalent bond between 5' phosphate and 3' hydroxyl",
                    "Functional Significance": "Forms the sugar-phosphate backbone and gives each strand a 5' and 3' end"
                },
                "Base pairing": {
                    "What It Is": "A-T and G-C pairing across the two strands",
                    "Bond or Force Involved": "Hydrogen bonds between complementary bases",
                    "Functional Significance": "Holds the two antiparallel strands together and stores complementary information"
                },
                "Antiparallel orientation": {
                    "What It Is": "3' end of one strand pairs with 5' end of the other",
                    "Bond or Force Involved": "Geometry required for correct base-pair hydrogen bonding",
                    "Functional Significance": "Allows strands to fit and be read by replication and transcription machinery"
                },
                "Sugar-phosphate backbone": {
                    "What It Is": "Deoxyribose sugars linked by phosphate groups on strand exterior",
                    "Bond or Force Involved": "Exposed negatively charged phosphate groups",
                    "Functional Significance": "Gives DNA an overall negative charge and lets histones bind"
                },
                "Major and minor grooves": {
                    "What It Is": "Two grooves created by the natural twist of the helix",
                    "Bond or Force Involved": "Surface contacts for DNA-binding proteins",
                    "Functional Significance": "Sites where proteins access bases for transcription and replication"
                }
            }
        },
        {
            "slug": "dna_packaging_levels",
            "title": "Levels of DNA Packaging",
            "subtitle": "Match each packaging structure to its composition and place in the condensation pathway",
            "categories": ["Composition", "Key Proteins", "Condensation Level"],
            "data": {
                "Nucleosome": {
                    "Composition": "DNA wound twice around a core of eight histones",
                    "Key Proteins": "Two each of H2A, H2B, H3, and H4",
                    "Condensation Level": "First step; gives 'beads on a string' appearance"
                },
                "Chromatosome": {
                    "Composition": "Nucleosome plus a linker histone securing the DNA",
                    "Key Proteins": "H1 linker histone added to the core octamer",
                    "Condensation Level": "Locks DNA onto the histone core"
                },
                "Chromatin fiber": {
                    "Composition": "Coiled string of nucleosomes forming a solenoid tube",
                    "Key Proteins": "Histone core plus H1 stabilizing the coil",
                    "Condensation Level": "Solenoid (~30 nm) fiber, more condensed"
                },
                "Chromatid": {
                    "Composition": "Chromatin fiber looped and further supercoiled",
                    "Key Proteins": "Histones plus scaffolding and supercoiling proteins",
                    "Condensation Level": "Highly condensed single DNA molecule"
                },
                "Metaphase chromosome": {
                    "Composition": "Two sister chromatids joined at the centromere",
                    "Key Proteins": "Cohesins hold chromatids; spindle attaches at centromere",
                    "Condensation Level": "Most condensed 'X-shaped' form seen in mitosis"
                }
            }
        },
        {
            "slug": "chromatin_states_regulation",
            "title": "Chromatin States and Epigenetic Control",
            "subtitle": "Match each chromatin state or modification to its condensation and effect on transcription",
            "categories": ["Condensation State", "Chemical Modification", "Effect on Transcription"],
            "data": {
                "Euchromatin": {
                    "Condensation State": "Loosely condensed, open chromatin",
                    "Chemical Modification": "Low DNA methylation; histone tail acetylation",
                    "Effect on Transcription": "Accessible to polymerases; transcriptionally active"
                },
                "Heterochromatin": {
                    "Condensation State": "Highly condensed, closed chromatin",
                    "Chemical Modification": "High DNA methylation of specific sequences",
                    "Effect on Transcription": "Inaccessible to polymerases; transcriptionally inactive"
                },
                "DNA methylation": {
                    "Condensation State": "Promotes tighter condensation into heterochromatin",
                    "Chemical Modification": "Methyl groups added to specific DNA sequences (CpG)",
                    "Effect on Transcription": "Recruits repressor proteins; decreases gene expression"
                },
                "Histone acetylation": {
                    "Condensation State": "Decondenses and opens the chromatin",
                    "Chemical Modification": "Acetyl groups added to histone tails, reducing positive charge",
                    "Effect on Transcription": "Relaxes coil; increases gene expression"
                },
                "Histone methylation": {
                    "Condensation State": "Alters tail contact with DNA depending on level",
                    "Chemical Modification": "Methyl groups added to histone tails (Lys/Arg)",
                    "Effect on Transcription": "May increase or decrease expression depending on the mark"
                }
            }
        }
    ]
}
