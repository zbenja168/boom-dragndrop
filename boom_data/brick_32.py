BRICK = {
    "brick_num": 32,
    "brick_title": "Amino Acid Metabolism I: Nitrogen Balance and Urea Cycle",
    "games": [
        {
            "slug": "nitrogen_enzymes",
            "title": "Nitrogen-Handling Enzymes",
            "subtitle": "Match each enzyme to the reaction it catalyzes, its cofactor/cosubstrate, and its key feature or site",
            "categories": ["Reaction Catalyzed", "Cofactor / Cosubstrate", "Key Feature or Site"],
            "data": {
                "Transaminase (aminotransferase)": {
                    "Reaction Catalyzed": "Swaps the amino group of an amino acid onto an alpha-keto acid",
                    "Cofactor / Cosubstrate": "PLP, a vitamin B6 derivative",
                    "Key Feature or Site": "ALT and AST serve as liver-function biomarkers"
                },
                "Glutamate dehydrogenase (GDH)": {
                    "Reaction Catalyzed": "Reversibly adds free ammonia to alpha-ketoglutarate forming glutamate",
                    "Cofactor / Cosubstrate": "NAD(P)+ / NAD(P)H",
                    "Key Feature or Site": "Loads nitrogen peripherally; liberates it for urea in liver"
                },
                "Glutamine synthetase": {
                    "Reaction Catalyzed": "Adds a second ammonia onto glutamate to form glutamine",
                    "Cofactor / Cosubstrate": "ATP (hydrolyzed to ADP + Pi)",
                    "Key Feature or Site": "Irreversible; enriched around the hepatic portal vein"
                },
                "Glutaminase": {
                    "Reaction Catalyzed": "Uses water to cleave ammonia from glutamine, yielding glutamate",
                    "Cofactor / Cosubstrate": "Water (H2O)",
                    "Key Feature or Site": "Mitochondrial; liver urea and kidney acid-base balance"
                }
            }
        },
        {
            "slug": "protein_digestion",
            "title": "Protein Digestion in the Gut",
            "subtitle": "Match each digestive player to where it originates, where it acts, and its distinguishing role",
            "categories": ["Origin / Produced As", "Site of Action", "Distinguishing Role"],
            "data": {
                "Pepsin": {
                    "Origin / Produced As": "Secreted as the zymogen pepsinogen",
                    "Site of Action": "Stomach",
                    "Distinguishing Role": "Acid-activated with broad specificity to fragment diverse proteins"
                },
                "Pancreatic proteases (trypsin, chymotrypsin, carboxypeptidase)": {
                    "Origin / Produced As": "Secreted by the pancreas",
                    "Site of Action": "Small intestine",
                    "Distinguishing Role": "Enter with bicarbonate that neutralizes the acidic chyme"
                },
                "Aminopeptidases": {
                    "Origin / Produced As": "Produced by intestinal brush border cells",
                    "Site of Action": "Brush border of the small intestine",
                    "Distinguishing Role": "Complete digestion into single amino acids or small peptides"
                },
                "Amino acid transporters": {
                    "Origin / Produced As": "Expressed in intestinal epithelium and kidney",
                    "Site of Action": "Portal circulation to the liver",
                    "Distinguishing Role": "Active transport drives absorption and reabsorption of amino acids"
                }
            }
        },
        {
            "slug": "ammonia_sources",
            "title": "Sources of Ammonia in the Body",
            "subtitle": "Match each ammonia source to its site, its mechanism, and a representative example",
            "categories": ["Source / Site", "Mechanism", "Representative Example"],
            "data": {
                "Nucleotide metabolism": {
                    "Source / Site": "Purine and pyrimidine breakdown",
                    "Mechanism": "Deamination reactions release ammonia",
                    "Representative Example": "Adenosine deaminase (ADA) activity"
                },
                "Gut metabolism": {
                    "Source / Site": "Intestinal lumen and gut bacteria",
                    "Mechanism": "Amino acid degradation and bacterial urease",
                    "Representative Example": "Urease: urea + H2O yields 2 NH3 + CO2"
                },
                "Glutamate dehydrogenase activity": {
                    "Source / Site": "Peripheral tissues and liver",
                    "Mechanism": "Oxidative deamination of glutamate",
                    "Representative Example": "Glutamate + NAD(P)+ yields alpha-KG + NAD(P)H + NH4+"
                },
                "Amino acid deamination": {
                    "Source / Site": "Direct deamination of select amino acids",
                    "Mechanism": "Removal of the amino group as free ammonia",
                    "Representative Example": "Histidine, threonine, glutamine, asparagine"
                }
            }
        },
        {
            "slug": "ammonia_neurotoxicity",
            "title": "Ammonia Neurotoxicity and Hepatic Encephalopathy",
            "subtitle": "Match each disturbance to the enzyme/trigger, its metabolic consequence, and its clinical effect",
            "categories": ["Trigger / Enzyme Involved", "Metabolic Consequence", "Clinical Effect"],
            "data": {
                "Excess glutamine synthetase activity": {
                    "Trigger / Enzyme Involved": "Ammonia drives glutamine synthetase, consuming glutamate and ATP",
                    "Metabolic Consequence": "Depletion of glutamate and ATP",
                    "Clinical Effect": "Impaired neurotransmission from loss of glutamate and GABA"
                },
                "Glutamine accumulation": {
                    "Trigger / Enzyme Involved": "Glutamine builds up as an active osmolyte in astrocytes",
                    "Metabolic Consequence": "Water influx and osmotic swelling of astrocytes",
                    "Clinical Effect": "Cerebral edema and increased intracranial pressure"
                },
                "Excess glutamate dehydrogenase activity": {
                    "Trigger / Enzyme Involved": "Rising ammonia stimulates GDH, consuming alpha-ketoglutarate",
                    "Metabolic Consequence": "Falling OAA slows the TCA cycle and OXPHOS",
                    "Clinical Effect": "Worsened ATP depletion in the CNS"
                },
                "Brainstem respiratory center effect": {
                    "Trigger / Enzyme Involved": "Ammonia compromises brainstem respiratory centers",
                    "Metabolic Consequence": "Hyperventilation exhales excess CO2, lowering arterial pCO2",
                    "Clinical Effect": "Respiratory alkalosis"
                },
                "Hepatic urea failure": {
                    "Trigger / Enzyme Involved": "Impaired hepatocytes cannot convert ammonia to urea",
                    "Metabolic Consequence": "Systemic hyperammonemia reaching the CNS",
                    "Clinical Effect": "Asterixis (flapping tremor), confusion, and lethargy"
                }
            }
        }
    ]
}
