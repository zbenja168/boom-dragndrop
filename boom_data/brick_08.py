BRICK = {
    "brick_num": 8,
    "brick_title": "DNA Damage and DNA Repair Mechanism",
    "games": [
        {
            "slug": "damage_sources",
            "title": "Sources of DNA Damage",
            "subtitle": "Match each source to whether it is endogenous or exogenous, its characteristic lesion, and the repair pathway that corrects it",
            "categories": ["Endogenous or Exogenous", "Characteristic Lesion", "Primary Repair Pathway"],
            "data": {
                "Ultraviolet light": {
                    "Endogenous or Exogenous": "Exogenous (environmental)",
                    "Characteristic Lesion": "Pyrimidine (thymine) dimers that kink the helix",
                    "Primary Repair Pathway": "Nucleotide excision repair"
                },
                "Ionizing radiation (X-rays)": {
                    "Endogenous or Exogenous": "Exogenous (physical)",
                    "Characteristic Lesion": "Double-strand breaks",
                    "Primary Repair Pathway": "Homologous recombination or nonhomologous end joining"
                },
                "Spontaneous methylation": {
                    "Endogenous or Exogenous": "Endogenous (alkylation)",
                    "Characteristic Lesion": "O6-methylguanine that mispairs",
                    "Primary Repair Pathway": "MGMT direct repair"
                },
                "Reactive oxygen species": {
                    "Endogenous or Exogenous": "Endogenous (oxidative)",
                    "Characteristic Lesion": "Oxidized single bases such as 8-oxoguanine",
                    "Primary Repair Pathway": "Base excision repair"
                },
                "DNA replication error": {
                    "Endogenous or Exogenous": "Endogenous (metabolic)",
                    "Characteristic Lesion": "Base-to-base mismatch on the new strand",
                    "Primary Repair Pathway": "Mismatch repair"
                },
                "Uracil incorporation / deamination": {
                    "Endogenous or Exogenous": "Endogenous (hydrolysis)",
                    "Characteristic Lesion": "Uracil or a deaminated base in DNA",
                    "Primary Repair Pathway": "Base excision repair"
                }
            }
        },
        {
            "slug": "repair_pathways",
            "title": "DNA Repair Pathways",
            "subtitle": "Match each repair pathway to the lesion it handles, its mechanistic highlight, and its preferred cell-cycle timing",
            "categories": ["Lesion Repaired", "Mechanistic Highlight", "Cell-Cycle Timing"],
            "data": {
                "Direct repair (MGMT)": {
                    "Lesion Repaired": "O6-methylguanine from alkylation",
                    "Mechanistic Highlight": "Removes the methyl group without cutting the backbone",
                    "Cell-Cycle Timing": "Any phase"
                },
                "Base excision repair": {
                    "Lesion Repaired": "A single damaged or incorrect base",
                    "Mechanistic Highlight": "Glycosylase creates an AP site; endonuclease and lyase cut, polymerase and ligase finish",
                    "Cell-Cycle Timing": "Any phase"
                },
                "Nucleotide excision repair": {
                    "Lesion Repaired": "Bulky, helix-distorting single-strand lesions",
                    "Mechanistic Highlight": "Removes a whole oligonucleotide stretch using uvr endonucleases",
                    "Cell-Cycle Timing": "Primarily G1 phase"
                },
                "Mismatch repair": {
                    "Lesion Repaired": "Base-base mismatch from replication error",
                    "Mechanistic Highlight": "Mut-class proteins recognize the error and recruit endonucleases",
                    "Cell-Cycle Timing": "Primarily S phase"
                },
                "Homologous recombination": {
                    "Lesion Repaired": "Double-strand break (accurate repair)",
                    "Mechanistic Highlight": "Uses a homologous chromosome as a template so no sequence is lost",
                    "Cell-Cycle Timing": "S and G2 phases"
                },
                "Nonhomologous end joining": {
                    "Lesion Repaired": "Double-strand break (versatile repair)",
                    "Mechanistic Highlight": "A ligase complex directly fuses the two ends; error-prone",
                    "Cell-Cycle Timing": "Any phase"
                }
            }
        },
        {
            "slug": "repair_deficiency_syndromes",
            "title": "DNA Repair Deficiency Syndromes",
            "subtitle": "Match each disorder to the gene(s) affected, the repair mechanism involved, and its hallmark clinical feature",
            "categories": ["Gene(s) Affected", "Repair Mechanism Involved", "Hallmark Clinical Feature"],
            "data": {
                "Xeroderma pigmentosum": {
                    "Gene(s) Affected": "XPA-XPG genes",
                    "Repair Mechanism Involved": "Nucleotide excision repair",
                    "Hallmark Clinical Feature": "Extreme photosensitivity with severe sunburn and skin cancer"
                },
                "Lynch syndrome": {
                    "Gene(s) Affected": "MLH1, MSH2, MSH6, or PMS2",
                    "Repair Mechanism Involved": "Mismatch repair",
                    "Hallmark Clinical Feature": "Early-onset colorectal and endometrial cancer"
                },
                "BRCA-associated cancer": {
                    "Gene(s) Affected": "BRCA1 or BRCA2",
                    "Repair Mechanism Involved": "Homologous recombination",
                    "Hallmark Clinical Feature": "Markedly increased breast and ovarian cancer risk"
                },
                "Ataxia-telangiectasia": {
                    "Gene(s) Affected": "ATM gene",
                    "Repair Mechanism Involved": "Double-strand break signaling / nonhomologous end joining",
                    "Hallmark Clinical Feature": "Ataxia and skin/eye telangiectasias with onset before age 5"
                },
                "Nijmegen breakage syndrome": {
                    "Gene(s) Affected": "NBS1 of the MRN complex",
                    "Repair Mechanism Involved": "Double-strand break sensing",
                    "Hallmark Clinical Feature": "Microcephaly with genomic instability"
                },
                "Severe combined immunodeficiency": {
                    "Gene(s) Affected": "Genes of the NHEJ ligase complex",
                    "Repair Mechanism Involved": "Nonhomologous end joining used in V(D)J recombination",
                    "Hallmark Clinical Feature": "Failure to generate antibodies and receptors"
                }
            }
        },
        {
            "slug": "damaging_agents",
            "title": "DNA-Damaging Agents",
            "subtitle": "Match each agent to its class, its mechanism of DNA damage, and a clinical fact from the brick",
            "categories": ["Class of Agent", "Mechanism of DNA Damage", "Clinical Fact"],
            "data": {
                "Cisplatin / carboplatin": {
                    "Class of Agent": "Platinum crosslinking chemotherapy",
                    "Mechanism of DNA Damage": "Covalent adduct at N7 of guanine forming intra- and interstrand crosslinks",
                    "Clinical Fact": "First-line treatment for epithelial ovarian cancer"
                },
                "Nitrogen mustard": {
                    "Class of Agent": "DNA alkylating agent",
                    "Mechanism of DNA Damage": "Adds an alkyl group to nitrogenous bases, forming adducts and crosslinks",
                    "Clinical Fact": "Structural analog of the warfare agent sulfur mustard"
                },
                "Tobacco smoke": {
                    "Class of Agent": "Complex carcinogen mixture",
                    "Mechanism of DNA Damage": "Aldehyde-driven acrolein/crotonaldehyde-DNA adducts plus reduced repair",
                    "Clinical Fact": "Contains at least 70 different carcinogens"
                },
                "Reactive oxygen species": {
                    "Class of Agent": "Oxidative endogenous agent",
                    "Mechanism of DNA Damage": "Unpaired electrons oxidize bases and sever phosphodiester bonds",
                    "Clinical Fact": "Brain is especially vulnerable given its high oxygen use"
                },
                "Spontaneous methylation": {
                    "Class of Agent": "Endogenous alkylation",
                    "Mechanism of DNA Damage": "Methyl group blocks a hydrogen bond on guanine, causing mispairing",
                    "Clinical Fact": "Becomes a substitution mutation if left unrepaired"
                },
                "Ultraviolet light": {
                    "Class of Agent": "Physical exogenous agent",
                    "Mechanism of DNA Damage": "Covalently links adjacent pyrimidines into cyclobutane dimers",
                    "Clinical Fact": "Tanning beds raise melanoma risk before age 35"
                }
            }
        }
    ]
}
