BRICK = {
    "brick_num": 42,
    "brick_title": "Sex Chromosome Aneuploidy",
    "games": [
        {
            "slug": "aneuploidy_syndromes",
            "title": "Sex Chromosome Aneuploidy Syndromes",
            "subtitle": "Match each syndrome to its karyotype, gonadal/endocrine finding, and somatic hallmark",
            "categories": ["Karyotype", "Gonadal / Endocrine Finding", "Somatic Hallmark"],
            "data": {
                "Turner syndrome": {
                    "Karyotype": "45,X (also written 45,XO)",
                    "Gonadal / Endocrine Finding": "Ovarian dysgenesis with low estrogen and primary amenorrhea",
                    "Somatic Hallmark": "Short stature, webbed neck, and cubitus valgus"
                },
                "Klinefelter syndrome": {
                    "Karyotype": "47,XXY",
                    "Gonadal / Endocrine Finding": "Small fibrotic testes, low testosterone, and gynecomastia",
                    "Somatic Hallmark": "Tall body with long limbs (macroskelia)"
                },
                "Triple X syndrome": {
                    "Karyotype": "47,XXX",
                    "Gonadal / Endocrine Finding": "Normal ovarian function with preserved fertility",
                    "Somatic Hallmark": "Tall stature with epicanthal folds and hypertelorism"
                },
                "XYY (Jacobs) syndrome": {
                    "Karyotype": "47,XYY",
                    "Gonadal / Endocrine Finding": "Normal testosterone and normal male genitalia",
                    "Somatic Hallmark": "Tall stature with flat feet and severe acne"
                }
            }
        },
        {
            "slug": "nondisjunction_outcomes",
            "title": "Nondisjunction and Gamete Outcomes",
            "subtitle": "Match each meiotic error to the abnormal gametes it makes and an example zygote",
            "categories": ["Meiotic Error", "Abnormal Gamete(s) Produced", "Example Resulting Zygote"],
            "data": {
                "Paternal nondisjunction in meiosis I": {
                    "Meiotic Error": "Homologs fail to separate in the first male division",
                    "Abnormal Gamete(s) Produced": "XY sperm or sperm with no sex chromosome",
                    "Example Resulting Zygote": "XY sperm plus X egg gives 47,XXY (Klinefelter)"
                },
                "Paternal nondisjunction in meiosis II": {
                    "Meiotic Error": "Sister chromatids fail to separate in the second male division",
                    "Abnormal Gamete(s) Produced": "XX sperm, YY sperm, or nullisomic sperm",
                    "Example Resulting Zygote": "YY sperm plus X egg gives 47,XYY (Jacobs)"
                },
                "Maternal nondisjunction": {
                    "Meiotic Error": "Failed separation during either female meiotic division",
                    "Abnormal Gamete(s) Produced": "XX egg or egg with no sex chromosome",
                    "Example Resulting Zygote": "XX egg plus X sperm gives 47,XXX (Triple X)"
                },
                "Loss producing a nullisomic gamete": {
                    "Meiotic Error": "Nondisjunction leaves a gamete lacking any sex chromosome",
                    "Abnormal Gamete(s) Produced": "Empty gamete carrying zero sex chromosomes",
                    "Example Resulting Zygote": "Empty gamete plus X gamete gives 45,X (Turner)"
                }
            }
        },
        {
            "slug": "sex_chromosome_genetics",
            "title": "Sex Chromosome Genetics Essentials",
            "subtitle": "Match each element or process to where it acts and its key role",
            "categories": ["Element / Process", "Location or Trigger", "Key Role"],
            "data": {
                "SRY gene": {
                    "Element / Process": "Master sex-determination gene",
                    "Location or Trigger": "Found on the Y chromosome",
                    "Key Role": "Encodes testis-determining factor driving male differentiation"
                },
                "Pseudoautosomal region": {
                    "Element / Process": "Region of X-Y homology",
                    "Location or Trigger": "Present on both the X and Y chromosomes",
                    "Key Role": "Lets X and Y pair and recombine during male meiosis"
                },
                "X-inactivation": {
                    "Element / Process": "Dosage-compensation mechanism",
                    "Location or Trigger": "Occurs in cells carrying two or more X chromosomes",
                    "Key Role": "Silences extra X genes to prevent overexpression"
                },
                "X chromosome": {
                    "Element / Process": "Larger sex chromosome",
                    "Location or Trigger": "One of the 23rd-pair chromosomes",
                    "Key Role": "Carries about 900 genes, most unique to X"
                },
                "Y chromosome": {
                    "Element / Process": "Smaller sex chromosome",
                    "Location or Trigger": "One of the 23rd-pair chromosomes",
                    "Key Role": "Carries fewer than 100 genes, including SRY"
                }
            }
        },
        {
            "slug": "fertility_and_complications",
            "title": "Fertility and Complications by Syndrome",
            "subtitle": "Match each syndrome to its fertility status and a major associated risk",
            "categories": ["Syndrome", "Fertility Status", "Major Associated Risk"],
            "data": {
                "Turner (45,X)": {
                    "Syndrome": "Monosomy X in a female",
                    "Fertility Status": "Infertile from premature ovarian failure; IVF sometimes possible",
                    "Major Associated Risk": "Bicuspid aortic valve, coarctation, and aortic dissection"
                },
                "Klinefelter (47,XXY)": {
                    "Syndrome": "Extra X in a male",
                    "Fertility Status": "Infertile from germ cell degeneration and low testosterone",
                    "Major Associated Risk": "Gynecomastia, learning disability, and anxiety disorders"
                },
                "Triple X (47,XXX)": {
                    "Syndrome": "Extra X in a female",
                    "Fertility Status": "Normal fertility; most can have children",
                    "Major Associated Risk": "Increased risk of learning disabilities"
                },
                "XYY / Jacobs (47,XYY)": {
                    "Syndrome": "Extra Y in a male",
                    "Fertility Status": "Normal fertility with normal testosterone",
                    "Major Associated Risk": "ADHD, autism spectrum, and impulsive behavior"
                }
            }
        }
    ]
}
