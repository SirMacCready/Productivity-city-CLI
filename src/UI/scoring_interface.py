from score.score_checker import score_checking

def display_score():
    total_score, normalized = score_checking()

    print("+----------------------+--------------------------+")
    print("|      Score Type      |          Valeur          |")
    print("+----------------------+--------------------------+")
    print(f"|Raw Score             | {total_score:>24.2f} |")
    print(f"|Normalized Score (/10)| {normalized:>24.2f} |")
    print("+----------------------+--------------------------+")
