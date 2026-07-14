BRICK = {
    "brick_num": 57,
    "brick_title": "Prenatal Genetic Testing & Neonatal Screening",
    "games": [
        {
            "slug": "screening_tests_timeline",
            "title": "Prenatal Screening Tests",
            "subtitle": "Match each prenatal screening test to its timing, method, and key feature",
            "categories": ["When performed", "What it involves", "Key detection feature"],
            "data": {
                "NIPT (cell-free DNA)": {
                    "When performed": "After ~10 weeks of gestation",
                    "What it involves": "Blood draw analyzing cell-free DNA from maternal serum",
                    "Key detection feature": "Most sensitive aneuploidy screen (trisomy 21 ~99%); no NTD information"
                },
                "First trimester combined screen": {
                    "When performed": "11-14 weeks",
                    "What it involves": "Nuchal translucency ultrasound plus PAPP-A and free beta-hCG",
                    "Key detection feature": "Estimates risk of trisomy 21, 18, and 13"
                },
                "Quad screen": {
                    "When performed": "15-20 weeks",
                    "What it involves": "Blood draw for MSAFP, beta-hCG, estriol, and inhibin A",
                    "Key detection feature": "Screens for trisomies and neural tube defects"
                },
                "Anatomy ultrasound": {
                    "When performed": "18-22 weeks",
                    "What it involves": "Targeted fetal anatomic ultrasound",
                    "Key detection feature": "Detects structural anomalies; best NTD detection (~95%)"
                }
            }
        },
        {
            "slug": "quad_marker_patterns",
            "title": "Quad Screen Marker Patterns",
            "subtitle": "Match each condition to its second-trimester quad screen analyte pattern",
            "categories": ["MSAFP", "Beta-hCG", "Estriol", "Inhibin A"],
            "data": {
                "Down syndrome (trisomy 21)": {
                    "MSAFP": "Low",
                    "Beta-hCG": "High",
                    "Estriol": "Low",
                    "Inhibin A": "High"
                },
                "Edwards syndrome (trisomy 18)": {
                    "MSAFP": "Low",
                    "Beta-hCG": "Low",
                    "Estriol": "Low",
                    "Inhibin A": "Low to normal"
                },
                "Open neural tube defect": {
                    "MSAFP": "High",
                    "Beta-hCG": "Normal",
                    "Estriol": "Normal",
                    "Inhibin A": "Normal"
                },
                "Fetal growth restriction": {
                    "MSAFP": "Normal",
                    "Beta-hCG": "Normal",
                    "Estriol": "Low (isolated)",
                    "Inhibin A": "Normal"
                }
            }
        },
        {
            "slug": "diagnostic_and_sampling",
            "title": "Diagnostic & Preimplantation Testing",
            "subtitle": "Match each testing method to its timing, sample, and purpose",
            "categories": ["When performed", "Sample obtained", "Purpose"],
            "data": {
                "Chorionic villus sampling (CVS)": {
                    "When performed": "10-14 weeks (first trimester)",
                    "Sample obtained": "Biopsy of chorionic villi (placental trophoblast) transcervical or transabdominal",
                    "Purpose": "Diagnostic for fetal trisomies; slight miscarriage risk"
                },
                "Amniocentesis": {
                    "When performed": "16-20 weeks (second trimester)",
                    "Sample obtained": "Amniotic fluid via transabdominal needle",
                    "Purpose": "Diagnoses trisomies; amniotic AFP detects NTDs (>99%)"
                },
                "Preimplantation genetic diagnosis (PGD)": {
                    "When performed": "Before pregnancy, during IVF (day-5 embryo)",
                    "Sample obtained": "3-8 cells biopsied from the blastocyst",
                    "Purpose": "Detects a specific genetic change before implantation"
                },
                "Newborn metabolic screening": {
                    "When performed": "After birth (neonate)",
                    "Sample obtained": "Dried blood collected by heel stick",
                    "Purpose": "Detects metabolic disorders via tandem mass spectrometry"
                }
            }
        },
        {
            "slug": "chromosomal_conditions",
            "title": "Aneuploidies Detected in Screening",
            "subtitle": "Match each karyotype to its eponym and screening note",
            "categories": ["Karyotype", "Eponym", "Screening note"],
            "data": {
                "Trisomy 21": {
                    "Karyotype": "47,XX or XY, +21",
                    "Eponym": "Down syndrome",
                    "Screening note": "Quad shows high beta-hCG and inhibin A with low MSAFP/estriol"
                },
                "Trisomy 18": {
                    "Karyotype": "47,XX or XY, +18",
                    "Eponym": "Edwards syndrome",
                    "Screening note": "All four quad markers low (inhibin A low to normal)"
                },
                "Trisomy 13": {
                    "Karyotype": "47,XX or XY, +13",
                    "Eponym": "Patau syndrome",
                    "Screening note": "Quad screen not sensitive or specific; ultrasound shows midline/renal defects"
                },
                "Monosomy X": {
                    "Karyotype": "45,X",
                    "Eponym": "Turner syndrome",
                    "Screening note": "Sex chromosome aneuploidy assessed on most cfDNA tests, not routine"
                },
                "XXY": {
                    "Karyotype": "47,XXY",
                    "Eponym": "Klinefelter syndrome",
                    "Screening note": "Sex chromosome aneuploidy reported by most cfDNA panels"
                },
                "XXX": {
                    "Karyotype": "47,XXX",
                    "Eponym": "Triple X syndrome",
                    "Screening note": "Sex chromosome aneuploidy reported by most cfDNA panels"
                }
            }
        }
    ]
}
