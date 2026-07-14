BRICK = {
    "brick_num": 10,
    "brick_title": "DNA Replication",
    "games": [
        {
            "slug": "replication_enzymes",
            "title": "Enzymes and Proteins of the Replication Fork",
            "subtitle": "Match each replication protein to its function, target, and board pearl",
            "categories": ["Function", "Acts On", "Key Feature"],
            "data": {
                "Helicase": {
                    "Function": "Severs hydrogen bonds between paired nitrogenous bases",
                    "Acts On": "The double helix at the origin and replication fork",
                    "Key Feature": "Favors A-T rich regions, which have only two hydrogen bonds"
                },
                "Primase": {
                    "Function": "Lays a short RNA primer that provides a free 3'-OH",
                    "Acts On": "The exposed single-stranded parent template",
                    "Key Feature": "Needed because DNA pol cannot start synthesis de novo"
                },
                "DNA polymerase": {
                    "Function": "Adds free nucleotides to the 3' end in a 5' to 3' direction",
                    "Acts On": "The RNA primer and the growing daughter strand",
                    "Key Feature": "High fidelity with proofreading against the template"
                },
                "Ligase": {
                    "Function": "Creates phosphodiester bonds to seal gaps",
                    "Acts On": "Adjacent Okazaki fragments on the lagging strand",
                    "Key Feature": "Performs the final joining step of lagging strand synthesis"
                },
                "Single-stranded binding proteins": {
                    "Function": "Provide a physical barrier to prevent strand reannealing",
                    "Acts On": "Exposed nucleotides of the separated parent strands",
                    "Key Feature": "Easily displaced by DNA polymerase and primase"
                },
                "Topoisomerase": {
                    "Function": "Relieves supercoiling tension introduced by helicase",
                    "Acts On": "The helix downstream, ahead of the replication fork",
                    "Key Feature": "Nicks and reseals the DNA backbone to release strain"
                }
            }
        },
        {
            "slug": "elongation_polymerases",
            "title": "Eukaryotic DNA Polymerases and the Sliding Clamp",
            "subtitle": "Match each elongation factor to its role, distinguishing feature, and processivity note",
            "categories": ["Primary Role", "Distinguishing Feature", "Processivity Note"],
            "data": {
                "DNA Pol alpha": {
                    "Primary Role": "Initiates replication of the leading strand and each Okazaki fragment",
                    "Distinguishing Feature": "Contains a subunit with RNA primase activity",
                    "Processivity Note": "Low processivity; stays attached for only about 20 nucleotides"
                },
                "DNA Pol delta": {
                    "Primary Role": "Completes synthesis of the Okazaki fragments on the lagging strand",
                    "Distinguishing Feature": "Displaces the RNA primer, creating a flap that must be trimmed",
                    "Processivity Note": "High processivity via association with the PCNA sliding clamp"
                },
                "DNA Pol epsilon": {
                    "Primary Role": "Completes synthesis of the leading strand",
                    "Distinguishing Feature": "A primary replicative polymerase with 3' to 5' exonuclease proofreading",
                    "Processivity Note": "High processivity via association with the PCNA sliding clamp"
                },
                "PCNA sliding clamp": {
                    "Primary Role": "Keeps the polymerase physically anchored to the DNA",
                    "Distinguishing Feature": "Forms a ring around the DNA during replication",
                    "Processivity Note": "Source of the high processivity of Pol delta and Pol epsilon"
                }
            }
        },
        {
            "slug": "fork_structures",
            "title": "Structures and Landmarks of Replication",
            "subtitle": "Match each replication structure to its identity, feature, and directional detail",
            "categories": ["What It Is", "Key Feature", "Directional Detail"],
            "data": {
                "Leading strand": {
                    "What It Is": "A new daughter strand synthesized continuously",
                    "Key Feature": "Requires only a single RNA primer",
                    "Directional Detail": "Template bases are exposed 3' to 5' as pol follows the helicase"
                },
                "Lagging strand": {
                    "What It Is": "A new daughter strand built in a semi-discontinuous manner",
                    "Key Feature": "Constructed from many small Okazaki fragments",
                    "Directional Detail": "Template bases are exposed 5' to 3', opposite to fork movement"
                },
                "Okazaki fragment": {
                    "What It Is": "A short polynucleotide segment of the lagging strand",
                    "Key Feature": "Each one begins with its own new RNA primer",
                    "Directional Detail": "20 to 30 million must be initiated to copy a human genome"
                },
                "RNA primer": {
                    "What It Is": "A short stretch of RNA laid down by primase",
                    "Key Feature": "Supplies the 3'-OH that DNA polymerase extends from",
                    "Directional Detail": "Later displaced and removed during fragment processing"
                },
                "Replication bubble": {
                    "What It Is": "The region where the parent strands have been separated",
                    "Key Feature": "Gives replicative enzymes room to associate with each strand",
                    "Directional Detail": "Bounded by a replication fork advancing at each end"
                },
                "Origin of replication": {
                    "What It Is": "The site where duplex opening first occurs",
                    "Key Feature": "Recognized by initiator proteins that recruit helicase",
                    "Directional Detail": "Long eukaryotic chromosomes use multiple ori sites"
                }
            }
        },
        {
            "slug": "tension_and_accuracy",
            "title": "Relieving Tension and Ensuring Accuracy",
            "subtitle": "Match each enzyme or mechanism to what it does and how it works",
            "categories": ["What It Does", "How It Works"],
            "data": {
                "Topoisomerase I": {
                    "What It Does": "Relaxes supercoils by making a transient single-stranded break",
                    "How It Works": "Monomeric and ATP-independent; lets the helix rotate around the intact strand"
                },
                "Topoisomerase II": {
                    "What It Does": "Relaxes supercoils by making a double-stranded break",
                    "How It Works": "Homodimeric or heterotetrameric and ATP-dependent; passes a helix segment through the break"
                },
                "3' to 5' exonuclease proofreading": {
                    "What It Does": "Removes a mismatched nucleotide during synthesis",
                    "How It Works": "Intrinsic activity of Pol delta and Pol epsilon that corrects errors before continuing"
                },
                "Mismatch repair": {
                    "What It Does": "Corrects pairing errors missed by polymerase proofreading",
                    "How It Works": "A separate post-replication safeguard against remaining mispairings"
                },
                "Flap endonuclease": {
                    "What It Does": "Trims the displaced RNA and DNA flap on the lagging strand",
                    "How It Works": "Cuts the flap so that ligase can seal the gap between Okazaki fragments"
                }
            }
        }
    ]
}
