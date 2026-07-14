BRICK = {
    "brick_num": 41,
    "brick_title": "Numerical & Structural Chromosomal Alterations (1/3) - Variants in Chromosome Number",
    "games": [
        {
            "slug": "aneuploidy_syndromes",
            "title": "Aneuploidy Syndromes at a Glance",
            "subtitle": "Match each chromosome abnormality to its signature clinical sign and life expectancy",
            "categories": ["Karyotype", "Signature Clinical Sign", "Viability / Prognosis"],
            "data": {
                "Down syndrome": {
                    "Karyotype": "47,XX/XY,+21 (trisomy 21)",
                    "Signature Clinical Sign": "Flat facies, single palmar crease, gap between 1st and 2nd toes",
                    "Viability / Prognosis": "Most common viable trisomy; survives well into adulthood"
                },
                "Edwards syndrome": {
                    "Karyotype": "47,XX/XY,+18 (trisomy 18)",
                    "Signature Clinical Sign": "Micrognathia, clenched hands with overlapping fingers, rocker-bottom feet",
                    "Viability / Prognosis": "50% die by 2 months, 90-95% by 1 year"
                },
                "Patau syndrome": {
                    "Karyotype": "47,XX/XY,+13 (trisomy 13)",
                    "Signature Clinical Sign": "Cutis aplasia, holoprosencephaly, cleft lip/palate, polydactyly",
                    "Viability / Prognosis": "50% die by 1 month, 90% by 1 year"
                },
                "Turner syndrome": {
                    "Karyotype": "45,X (monosomy X)",
                    "Signature Clinical Sign": "Short stature, webbed neck, widely spaced nipples",
                    "Viability / Prognosis": "Only monosomy compatible with life"
                },
                "Trisomy 16": {
                    "Karyotype": "Trisomy 16",
                    "Signature Clinical Sign": "No liveborn phenotype (most commonly occurring trisomy)",
                    "Viability / Prognosis": "Always fatal in utero"
                }
            }
        },
        {
            "slug": "mechanisms_aneuploidy",
            "title": "How Aneuploidy Arises",
            "subtitle": "Match each error to what fails to separate and its genetic outcome",
            "categories": ["Timing / Setting", "What Fails to Separate", "Genetic Outcome"],
            "data": {
                "Nondisjunction in meiosis I": {
                    "Timing / Setting": "Meiosis I during gametogenesis",
                    "What Fails to Separate": "Homologous chromosome pair segregates together",
                    "Genetic Outcome": "n+1 gamete carries both maternal and paternal homologs"
                },
                "Nondisjunction in meiosis II": {
                    "Timing / Setting": "Meiosis II during gametogenesis",
                    "What Fails to Separate": "Sister chromatids fail to separate",
                    "Genetic Outcome": "n+1 gamete carries two identical sister chromatids"
                },
                "Mitotic nondisjunction": {
                    "Timing / Setting": "Mitosis after fertilization",
                    "What Fails to Separate": "Sister chromatids in a somatic cell",
                    "Genetic Outcome": "Mosaicism; only some cells are aneuploid (e.g., 46,XX/47,XX,+21)"
                },
                "Robertsonian translocation segregation": {
                    "Timing / Setting": "Meiosis in a translocation carrier",
                    "What Fails to Separate": "Fused acrocentric long arms cannot pair and segregate normally",
                    "Genetic Outcome": "Unbalanced gametes leading to trisomy or monosomy"
                }
            }
        },
        {
            "slug": "down_associations",
            "title": "Down Syndrome Clinical Associations",
            "subtitle": "Match each affected domain to the associated condition and its mechanism",
            "categories": ["Organ System / Domain", "Associated Condition", "Mechanism / Detail"],
            "data": {
                "Gastrointestinal": {
                    "Organ System / Domain": "Gastrointestinal tract",
                    "Associated Condition": "Duodenal atresia and Hirschsprung disease",
                    "Mechanism / Detail": "Structural bowel malformations seen in trisomy 21"
                },
                "Cardiac": {
                    "Organ System / Domain": "Cardiovascular system",
                    "Associated Condition": "Congenital heart disease (e.g., atrial septal defect)",
                    "Mechanism / Detail": "Most common cause of death in early life"
                },
                "Neurodegenerative": {
                    "Organ System / Domain": "Central nervous system",
                    "Associated Condition": "Early-onset Alzheimer disease",
                    "Mechanism / Detail": "Three copies of the APP gene on chromosome 21"
                },
                "Hematologic": {
                    "Organ System / Domain": "Blood / bone marrow",
                    "Associated Condition": "Increased risk of leukemia (usually AML)",
                    "Mechanism / Detail": "Thought to be due to silencing of PRC2"
                },
                "Cognitive": {
                    "Organ System / Domain": "Neurocognitive development",
                    "Associated Condition": "Mild-to-moderate intellectual disability",
                    "Mechanism / Detail": "No. 1 known genetic cause of intellectual disability"
                }
            }
        },
        {
            "slug": "ploidy_terminology",
            "title": "Ploidy & Aneuploidy Terminology",
            "subtitle": "Match each term to its definition and a representative example",
            "categories": ["Definition", "Count Relative to Haploid (n)", "Example / Note"],
            "data": {
                "Euploid": {
                    "Definition": "Chromosome number that is an exact multiple of the haploid number",
                    "Count Relative to Haploid (n)": "Whole multiples of n (n, 2n, 3n, 4n)",
                    "Example / Note": "Diploid, triploid, tetraploid; triploid/tetraploid fetuses are not viable"
                },
                "Aneuploid": {
                    "Definition": "Chromosome number that is NOT an exact multiple of the haploid number",
                    "Count Relative to Haploid (n)": "One or more extra or missing chromosomes",
                    "Example / Note": "Most common and clinically significant human chromosome disorder"
                },
                "Trisomy": {
                    "Definition": "Three copies of a particular chromosome instead of the normal pair",
                    "Count Relative to Haploid (n)": "2n + 1",
                    "Example / Note": "Trisomy 21, 18, and 13"
                },
                "Monosomy": {
                    "Definition": "Only one representative of a particular chromosome",
                    "Count Relative to Haploid (n)": "2n - 1",
                    "Example / Note": "45,X (Turner) is the only viable monosomy"
                },
                "Mosaicism": {
                    "Definition": "Two cell lineages from a single zygote that differ genetically",
                    "Count Relative to Haploid (n)": "Mixture of normal (2n) and aneuploid cells",
                    "Example / Note": "Denoted with a '/', e.g., 46,XX/47,XX,+21"
                }
            }
        }
    ]
}
