"""
utils.py — shared display utilities for Lab 3 notebooks.

Keeps notebook cells focused on concepts by housing reusable data,
formatting helpers, and visualisation functions here.
"""

import textwrap
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# ── Representative PubMed QA examples (one per label) ─────────────────────────
# Source: pubmed_qa / pqa_labeled  (see pubmed_qa_eda.ipynb for full EDA)
EXAMPLES = [
    {
        "final_decision": "yes",
        "question": (
            "Is the breast best for children with a family history of atopy?"
        ),
        "context": (
            "Previous studies reported that breast-feeding protects children "
            "against a variety of diseases, but these studies were generally "
            "conducted on 'high-risk' or hospitalised children. This paper "
            "describes the results of our study on the effects of breast-feeding "
            "on rate of illness in normal children with and without a family "
            "history of atopy, recruited from a community-based birth cohort."
        ),
        "long_answer": (
            "Our results suggest a protective effect of breast-feeding among "
            "children with a family history of atopy that is not confined to "
            "the period of breast-feeding itself, and extends through the first "
            "two years of life."
        ),
    },
    {
        "final_decision": "no",
        "question": (
            "Kell alloimmunization in pregnancy: associated with fetal "
            "thrombocytopenia?"
        ),
        "context": (
            "Kell haemolytic disease in pregnancies has been suggested to be "
            "associated with decreased fetal platelet counts. The aim of this "
            "study was to evaluate the incidence and clinical significance of "
            "fetal thrombocytopenia in pregnancies complicated by Kell "
            "alloimmunization. Fetal platelet counts were performed in 42 "
            "pregnancies with severe Kell alloimmunization prior to the first "
            "intrauterine blood transfusion."
        ),
        "long_answer": (
            "In contrast to fetuses with severe anaemia due to RhD "
            "alloimmunization, fetuses with severe anaemia due to Kell "
            "alloimmunization are generally not thrombocytopenic, and "
            "thrombocytopenia is not a clinical concern in the management "
            "of these pregnancies."
        ),
    },
]


def show_examples(examples=None, width=64):
    """Print box-formatted PubMed QA examples. Defaults to the two built-in ones."""
    if examples is None:
        examples = EXAMPLES

    W    = width
    bar  = "═" * W
    thin = "─" * W

    def row(text):
        for line in textwrap.wrap(text, width=W - 4) or [""]:
            print(f"║  {line:<{W-2}}║")

    for ex in examples:
        label = ex["final_decision"]
        print(f"╔{bar}╗")
        print(f"║  EXAMPLE — Expected answer: {label.upper():<{W-28}}║")
        print(f"╠{bar}╣")
        print(f"║  QUESTION{' '*(W-8)}║")
        row(ex["question"])
        print(f"╠{thin}╣")
        print(f"║  CONTEXT  (abstract excerpt){' '*(W-28)}║")
        row(ex["context"])
        print(f"╠{thin}╣")
        print(f"║  LONG ANSWER  (abstract conclusion){' '*(W-35)}║")
        row(ex["long_answer"])
        print(f"╠{bar}╣")
        print(f"║  FINAL DECISION  →  {label.upper():<{W-20}}║")
        print(f"╚{bar}╝")
        print()


def plot_label_distribution(save_path="pubmedqa_distribution.png"):
    """
    Side-by-side bar chart: original PubMed QA distribution vs balanced subset.

    Original counts (pubmed_qa / pqa_labeled, 1,000 examples):
        yes:   552  (55.2 %)  — publication bias toward positive findings
        no:    338  (33.8 %)  — dropped for this yes/maybe subset
        maybe: 110  (11.0 %)

    Balanced subset (220 examples):
        yes: 110, maybe: 110   — yes downsampled to match maybe
    """
    original = {"yes": 552, "no": 338, "maybe": 110}
    balanced = {"yes": 110, "maybe": 110}
    palette  = {"yes": "#4CAF50", "no": "#F44336", "maybe": "#FF9800"}

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    fig.suptitle("PubMed QA — Label Distribution", fontsize=13, fontweight="bold", y=1.02)

    # Left: original distribution
    labels = list(original.keys())
    counts = list(original.values())
    bars = axes[0].bar(labels, counts, color=[palette[l] for l in labels],
                       edgecolor="white", width=0.5)
    for bar, val in zip(bars, counts):
        axes[0].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 8,
                     str(val), ha="center", fontweight="bold", fontsize=11)
    axes[0].set_title("Original Dataset  (1,000 examples)", fontsize=11)
    axes[0].set_xlabel("final_decision")
    axes[0].set_ylabel("Count")
    axes[0].set_ylim(0, 650)
    axes[0].axhline(110, color="grey", linestyle="--", linewidth=0.8, alpha=0.6)

    # Right: balanced subset
    labels = list(balanced.keys())
    counts = list(balanced.values())
    bars = axes[1].bar(labels, counts, color=[palette[l] for l in labels],
                       edgecolor="white", width=0.4)
    for bar, val in zip(bars, counts):
        axes[1].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2,
                     str(val), ha="center", fontweight="bold", fontsize=11)
    axes[1].set_title("Balanced Subset  (220 examples)", fontsize=11)
    axes[1].set_xlabel("final_decision")
    axes[1].set_ylabel("Count")
    axes[1].set_ylim(0, 140)
    axes[1].legend(handles=[
        mpatches.Patch(color=palette["no"],  label="'no' dropped"),
        mpatches.Patch(color=palette["yes"], label="'yes' downsampled to match 'maybe'"),
    ], loc="upper right", fontsize=9)

    plt.tight_layout()
    plt.savefig(save_path, bbox_inches="tight", dpi=120)
    plt.show()

    print(f"Original — yes: {original['yes']}, no: {original['no']}, maybe: {original['maybe']}")
    print(f"Balanced — yes: {balanced['yes']}, maybe: {balanced['maybe']}")
    print(f"Imbalance ratio (original yes/maybe): {original['yes'] / original['maybe']:.2f}x")
