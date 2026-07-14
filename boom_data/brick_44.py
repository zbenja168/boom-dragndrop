BRICK = {
    "brick_num": 44,
    "brick_title": "Mosaicism",
    "games": [
        {
            "slug": "types_of_mosaicism",
            "title": "Types of Genetic Mosaicism",
            "subtitle": "Match each type of mosaicism to the tissues involved, its effect on the individual, and the transmission risk",
            "categories": ["Tissues Involved", "Effect on Individual", "Transmission Risk to Offspring"],
            "data": {
                "Confined Placental Mosaicism": {
                    "Tissues Involved": "Extraembryonic (placental) tissue only, not the embryo proper",
                    "Effect on Individual": "Normal pregnancy outcome or delayed fetal growth",
                    "Transmission Risk to Offspring": "None; embryo and gametes are unaffected"
                },
                "Pure Somatic Mosaicism": {
                    "Tissues Involved": "Some somatic tissues (e.g., skin, blood); gametes spared",
                    "Effect on Individual": "Phenotype affects the individual",
                    "Transmission Risk to Offspring": "Not transmitted; germline is not affected"
                },
                "Pure Germline (Gonadal) Mosaicism": {
                    "Tissues Involved": "Gamete (germ cell) lineage only",
                    "Effect on Individual": "Individual is unaffected, with no somatic disease",
                    "Transmission Risk to Offspring": "At risk of transmitting the mutation to offspring"
                },
                "Somatic + Germline Combination": {
                    "Tissues Involved": "Both somatic lineages and the germline",
                    "Effect on Individual": "Phenotype affects the individual",
                    "Transmission Risk to Offspring": "Affected AND at risk of transmitting the mutation"
                }
            }
        },
        {
            "slug": "x_inactivation",
            "title": "X Chromosome Inactivation",
            "subtitle": "Match each concept to what it is, its location or mechanism, and its significance",
            "categories": ["What It Is", "Location or Mechanism", "Significance"],
            "data": {
                "XIST": {
                    "What It Is": "Non-coding RNA gene that is the master regulator of inactivation",
                    "Location or Mechanism": "Expressed from the allele on the inactive X",
                    "Significance": "Long ncRNA coats and epigenetically silences the inactive X"
                },
                "X Inactivation Center (XIC)": {
                    "What It Is": "Complex regulatory locus that contains XIST",
                    "Location or Mechanism": "Region on the X chromosome controlling inactivation",
                    "Significance": "Required for normal X chromosome inactivation"
                },
                "Barr Body": {
                    "What It Is": "Condensed heterochromatic mass of the inactive X",
                    "Location or Mechanism": "Visible in the interphase nucleus of somatic cells",
                    "Significance": "Cytologic marker of an inactivated X chromosome"
                },
                "Escape Genes": {
                    "What It Is": "About 15% of X genes expressed from both active and inactive X",
                    "Location or Mechanism": "Preferentially located near the distal Xp region",
                    "Significance": "Not fully silenced, so expressed to some extent biallelically"
                },
                "Skewed X Inactivation": {
                    "What It Is": "The same X inactivated in a high proportion of cells",
                    "Location or Mechanism": "Due to a structurally abnormal X or occurring by chance",
                    "Significance": "Can unmask X-linked disease in a female carrier"
                }
            }
        },
        {
            "slug": "mosaic_conditions",
            "title": "Mosaic Clinical Conditions",
            "subtitle": "Match each condition to its underlying genetic event, its karyotype or gene, and a clinical clue",
            "categories": ["Underlying Genetic Event", "Karyotype or Gene", "Clinical Clue"],
            "data": {
                "Mosaic Down Syndrome": {
                    "Underlying Genetic Event": "Mitotic nondisjunction of chromosome 21 in the early embryo",
                    "Karyotype or Gene": "Mixture of disomy 21 and trisomy 21 cell lines",
                    "Clinical Clue": "Typically a less severe phenotype than full trisomy 21"
                },
                "Mosaic Turner Syndrome": {
                    "Underlying Genetic Event": "Mitotic nondisjunction or loss of an X early in development",
                    "Karyotype or Gene": "Mixture of 46,XX and 45,X cell lines",
                    "Clinical Clue": "Delayed onset of puberty in a phenotypic female"
                },
                "Segmental Neurofibromatosis (NF1)": {
                    "Underlying Genetic Event": "Post-zygotic NF1 mutation during embryogenesis",
                    "Karyotype or Gene": "Mosaic pathogenic variant in the NF1 gene",
                    "Clinical Clue": "Pigmentation and neurofibromas confined to one body region"
                },
                "Manifesting DMD Carrier": {
                    "Underlying Genetic Event": "Skewed X inactivation silencing the normal X in key tissue",
                    "Karyotype or Gene": "Heterozygous X-linked DMD pathogenic variant",
                    "Clinical Clue": "Muscle weakness and elevated creatine kinase in a female"
                }
            }
        },
        {
            "slug": "recurrence_risk_counseling",
            "title": "Recurrence Risk and Counseling",
            "subtitle": "Match each family scenario to its most likely explanation and the key counseling point",
            "categories": ["Family Scenario", "Most Likely Explanation", "Counseling Point"],
            "data": {
                "Two children, same AD mutation, negative parents": {
                    "Family Scenario": "Two children share an FBN1 (Marfan) mutation; parents test negative",
                    "Most Likely Explanation": "Germline (gonadal) mosaicism in one parent",
                    "Counseling Point": "Future offspring have an increased recurrence risk"
                },
                "Child with somatic mosaicism, unaffected parents": {
                    "Family Scenario": "Child has patchy somatic disease; both parents are unaffected",
                    "Most Likely Explanation": "Post-zygotic mutation during embryonic development",
                    "Counseling Point": "Parents' recurrence risk equals the population risk"
                },
                "Mosaic individual planning children": {
                    "Family Scenario": "Individual with somatic mosaicism for an autosomal dominant disorder",
                    "Most Likely Explanation": "Germline involvement cannot be excluded",
                    "Counseling Point": "At increased risk of having fully affected offspring"
                },
                "Female heterozygote with partial disease": {
                    "Family Scenario": "Carrier female with partial expression of an X-linked disease",
                    "Most Likely Explanation": "Skewed X inactivation (manifesting heterozygote)",
                    "Counseling Point": "Phenotype varies with the X-inactivation pattern across tissues"
                }
            }
        }
    ]
}
