BRICK = {
    "brick_num": 53,
    "brick_title": "Population Genetics",
    "games": [
        {
            "slug": "hardy_weinberg_terms",
            "title": "Hardy-Weinberg Equation Terms",
            "subtitle": "Match each term of p2 + 2pq + q2 = 1 to its symbol, meaning, and value in the Laron syndrome example",
            "categories": ["Symbol", "What It Represents", "Value in Laron Example"],
            "data": {
                "Dominant allele frequency": {
                    "Symbol": "p",
                    "What It Represents": "frequency of the dominant (A) allele in the population",
                    "Value in Laron Example": "0.978"
                },
                "Recessive allele frequency": {
                    "Symbol": "q",
                    "What It Represents": "frequency of the recessive (a) allele in the population",
                    "Value in Laron Example": "0.022"
                },
                "Homozygous dominant": {
                    "Symbol": "p-squared",
                    "What It Represents": "frequency of unaffected AA individuals",
                    "Value in Laron Example": "0.956 (9560 people)"
                },
                "Heterozygous carriers": {
                    "Symbol": "2pq",
                    "What It Represents": "frequency of Aa carriers with one of each allele",
                    "Value in Laron Example": "0.043 (430 people)"
                },
                "Homozygous recessive": {
                    "Symbol": "q-squared",
                    "What It Represents": "frequency of affected aa individuals with the disease",
                    "Value in Laron Example": "5/10,000 (5 people)"
                }
            }
        },
        {
            "slug": "forces_altering_frequencies",
            "title": "Forces That Change Allele Frequencies",
            "subtitle": "Match each population-genetics force to its mechanism, effect on diversity, and example",
            "categories": ["Mechanism", "Effect on Genetic Diversity", "Example / Key Feature"],
            "data": {
                "Genetic drift": {
                    "Mechanism": "random chance fluctuations in allele frequency, unrelated to fitness",
                    "Effect on Genetic Diversity": "decreases it; alleles are eventually lost or fixed",
                    "Example / Key Feature": "strongest in small populations"
                },
                "Founder effect": {
                    "Mechanism": "a small group separates from a larger source population",
                    "Effect on Genetic Diversity": "decreases it within the new subpopulation",
                    "Example / Key Feature": "Afrikaner Huntington disease; Ashkenazi disorders"
                },
                "Bottleneck effect": {
                    "Mechanism": "a disaster sharply reduces population size and allele number",
                    "Effect on Genetic Diversity": "decreases it, potentially lowering fitness",
                    "Example / Key Feature": "famine, earthquake, flood, fire, disease, drought"
                },
                "Gene flow": {
                    "Mechanism": "transfer of alleles between populations by migration and mating",
                    "Effect on Genetic Diversity": "increases it by sharing gene pools",
                    "Example / Key Feature": "falling thalassemia minor rate in the mixing town"
                },
                "Natural selection": {
                    "Mechanism": "alleles favored when they confer a reproductive advantage",
                    "Effect on Genetic Diversity": "shifts frequency toward the fitter allele",
                    "Example / Key Feature": "HbS heterozygote resists severe malaria"
                },
                "Assortative mating": {
                    "Mechanism": "individuals preferentially mate with similar partners",
                    "Effect on Genetic Diversity": "reduces random mating within the population",
                    "Example / Key Feature": "attraction to partners with similar facial features"
                }
            }
        },
        {
            "slug": "population_disease_patterns",
            "title": "Genetic Diseases and Population Patterns",
            "subtitle": "Match each disorder to its molecular defect, clinical or testing feature, and population association",
            "categories": ["Molecular Defect / Gene", "Clinical or Testing Feature", "Population Association"],
            "data": {
                "Tay-Sachs disease": {
                    "Molecular Defect / Gene": "deficiency of the hexosaminidase A enzyme",
                    "Clinical or Testing Feature": "seizures, cherry-red macula, neurologic decline",
                    "Population Association": "Ashkenazi Jews (ACOG screening recommended)"
                },
                "Cystic fibrosis": {
                    "Molecular Defect / Gene": "mutated CFTR chloride transporter",
                    "Clinical or Testing Feature": "screening sensitivity depends on ancestry",
                    "Population Association": "71.9% sensitivity white-American vs 23.4% Asian-American"
                },
                "Sickle cell disease": {
                    "Molecular Defect / Gene": "homozygous HbS mutation of the beta-globin chain",
                    "Clinical or Testing Feature": "disease in HbS/HbS; trait in HbA/HbS carriers",
                    "Population Association": "regions with high malaria prevalence"
                },
                "Gaucher disease": {
                    "Molecular Defect / Gene": "autosomal recessive founder-effect disorder",
                    "Clinical or Testing Feature": "spectrum of Types 1, 2, and 3 severity",
                    "Population Association": "carrier ~1 in 10 Jewish vs ~1 in 100 non-Jewish"
                },
                "Huntington disease": {
                    "Molecular Defect / Gene": "disease gene carried by a few original founders",
                    "Clinical or Testing Feature": "unusually high frequency by chance spread",
                    "Population Association": "Afrikaners of South Africa"
                },
                "Thalassemia minor": {
                    "Molecular Defect / Gene": "inherited hemoglobin disorder",
                    "Clinical or Testing Feature": "incidence falling as gene flow raises variation",
                    "Population Association": "southern European ancestry"
                }
            }
        },
        {
            "slug": "hardy_weinberg_assumptions",
            "title": "Hardy-Weinberg Assumptions and Their Violations",
            "subtitle": "Match each equilibrium assumption to the real-world force that violates it and the resulting consequence",
            "categories": ["Equilibrium Assumption", "Violating Force", "Consequence of Violation"],
            "data": {
                "No selection": {
                    "Equilibrium Assumption": "no allele provides a reproductive advantage",
                    "Violating Force": "natural selection",
                    "Consequence of Violation": "the favored allele increases, e.g., HbS where malaria is endemic"
                },
                "No mutation": {
                    "Equilibrium Assumption": "alleles do not mutate from generation to generation",
                    "Violating Force": "mutation",
                    "Consequence of Violation": "new deleterious alleles are introduced into the pool"
                },
                "Large population": {
                    "Equilibrium Assumption": "one new birth does not shift allele proportions",
                    "Violating Force": "genetic drift and bottleneck effect",
                    "Consequence of Violation": "random loss or fixation of alleles by chance"
                },
                "Random mating": {
                    "Equilibrium Assumption": "mating occurs at random within the population",
                    "Violating Force": "assortative mating",
                    "Consequence of Violation": "mates chosen for similar traits, skewing genotype ratios"
                },
                "No migration": {
                    "Equilibrium Assumption": "there is no immigration or emigration",
                    "Violating Force": "gene flow",
                    "Consequence of Violation": "alleles transferred between populations, raising variation"
                }
            }
        }
    ]
}
