BRICK = {
    "brick_num": 61,
    "brick_title": "Pharmacogenetics: An Introduction",
    "games": [
        {
            "slug": "metabolizer_phenotypes",
            "title": "Metabolizer Phenotypes and Dosing",
            "subtitle": "Match each metabolizer phenotype to its enzyme function, drug breakdown rate, and dosing implication",
            "categories": ["Enzyme Function", "Drug Breakdown Rate", "Dosing Implication"],
            "data": {
                "Ultra-rapid metabolizer": {
                    "Enzyme Function": "Increased enzyme activity (eg, CYP2C19*17)",
                    "Drug Breakdown Rate": "Fast breakdown; drug cleared before it can act",
                    "Dosing Implication": "Needs more drug or a different drug"
                },
                "Normal (extensive) metabolizer": {
                    "Enzyme Function": "Typical enzyme activity",
                    "Drug Breakdown Rate": "Normal breakdown of the drug",
                    "Dosing Implication": "Needs the standard dose"
                },
                "Intermediate metabolizer": {
                    "Enzyme Function": "Reduced enzyme activity (eg, CYP2D6 *4/*10)",
                    "Drug Breakdown Rate": "Somewhat slowed breakdown of the drug",
                    "Dosing Implication": "May need a lower dose; higher risk of adverse effects"
                },
                "Poor metabolizer": {
                    "Enzyme Function": "Little to no enzyme activity",
                    "Drug Breakdown Rate": "Slow breakdown; drug accumulates in the body",
                    "Dosing Implication": "Needs less drug; high risk of toxicity"
                }
            }
        },
        {
            "slug": "gpcr_receptor_variants",
            "title": "GPCR Receptor Variants and Drug Response",
            "subtitle": "Match each receptor gene variant to its receptor type, associated drug, and clinical effect",
            "categories": ["Receptor Type", "Associated Drug(s)", "Effect of the Variant"],
            "data": {
                "ADRB1 R389G": {
                    "Receptor Type": "Beta-1 adrenergic receptor",
                    "Associated Drug(s)": "Metoprolol, carvedilol, bisoprolol",
                    "Effect of the Variant": "Decreased antihypertensive response"
                },
                "ADRB2 R16G": {
                    "Receptor Type": "Beta-2 adrenergic receptor",
                    "Associated Drug(s)": "Long-acting beta agonists (LABA)",
                    "Effect of the Variant": "Increased risk of asthma exacerbation"
                },
                "ADRA2C Del322-325": {
                    "Receptor Type": "Alpha-2C adrenergic receptor",
                    "Associated Drug(s)": "Clonidine",
                    "Effect of the Variant": "Increased efficacy"
                },
                "OPRM1 N40D": {
                    "Receptor Type": "Mu-opioid receptor",
                    "Associated Drug(s)": "Buprenorphine, endogenous opioids",
                    "Effect of the Variant": "Decreased efficacy for buprenorphine"
                },
                "DRD2 -141C Ins/Del": {
                    "Receptor Type": "Dopamine D2 receptor",
                    "Associated Drug(s)": "Antipsychotics",
                    "Effect of the Variant": "Decreased efficacy and increased weight gain"
                },
                "HTR2A rs6313": {
                    "Receptor Type": "Serotonin 2A receptor",
                    "Associated Drug(s)": "Risperidone",
                    "Effect of the Variant": "Increased adverse cardiovascular events"
                }
            }
        },
        {
            "slug": "metabolizing_enzymes",
            "title": "Phase I and Phase II Metabolizing Enzymes",
            "subtitle": "Match each drug-metabolizing enzyme to its metabolic phase, a key drug substrate, and the consequence of a variant",
            "categories": ["Metabolic Phase", "Key Drug Substrate", "Consequence of Variant"],
            "data": {
                "CYP2D6": {
                    "Metabolic Phase": "Phase I (oxidation)",
                    "Key Drug Substrate": "Venlafaxine and many antidepressants/antipsychotics",
                    "Consequence of Variant": "*4/*10 intermediate metabolizer; reduced metabolism and adverse effects"
                },
                "CYP2C19": {
                    "Metabolic Phase": "Phase I (oxidation)",
                    "Key Drug Substrate": "Proton pump inhibitors",
                    "Consequence of Variant": "*17 ultra-rapid metabolizer; loss of drug effectiveness"
                },
                "CYP3A4": {
                    "Metabolic Phase": "Phase I (oxidation)",
                    "Key Drug Substrate": "Cyclosporine and tacrolimus",
                    "Consequence of Variant": "Decreased function (*8, *11, *13); drug toxicity"
                },
                "TPMT": {
                    "Metabolic Phase": "Phase II (methylation)",
                    "Key Drug Substrate": "Azathioprine and 6-mercaptopurine",
                    "Consequence of Variant": "Deficiency causes myelosuppression and bone marrow toxicity"
                }
            }
        },
        {
            "slug": "snp_variant_classification",
            "title": "SNP and Variant Classification",
            "subtitle": "Match each variant type to its location, effect on protein, and clinical significance",
            "categories": ["Location", "Effect on Protein", "Clinical Significance"],
            "data": {
                "Linked SNP": {
                    "Location": "Outside the gene",
                    "Effect on Protein": "No effect on protein production or function",
                    "Clinical Significance": "Indicative marker that may correlate with drug response or disease"
                },
                "Coding SNP": {
                    "Location": "Coding region of the gene",
                    "Effect on Protein": "Changes the amino acid sequence",
                    "Clinical Significance": "Causative; can directly alter protein structure or activity"
                },
                "Noncoding SNP": {
                    "Location": "Non-coding region of the gene",
                    "Effect on Protein": "Changes the amount of protein produced",
                    "Clinical Significance": "Causative; may alter expression and treatment response"
                },
                "Pathogenic variant": {
                    "Location": "Within a gene",
                    "Effect on Protein": "Impairs or alters protein function",
                    "Clinical Significance": "Increases risk of a condition, disorder, or disease"
                },
                "Benign variant": {
                    "Location": "Within a gene",
                    "Effect on Protein": "Little to no effect on protein function",
                    "Clinical Significance": "No increased disease risk"
                }
            }
        }
    ]
}
