
"""Testprogram för Inlämningsuppgift "3B - Frekvensanalys"
Kursgenomförande DV1574 HT21 LP1
Skrivet av: Carina Nilsson
Datum: 2021-09-09 uppdaterad 2021-10-04
"""

import sys
import json

from frekvens_analys import *

FUNCTIONS = ["frequency", "most_frequent", "word_count", "unique_words",
             "mean_frequency", "median_frequency", "closest_word"]
TEST_FILES = ["small.txt", "umbrella.txt",
              "text_example.txt", "one.txt", "empty.txt"]
COUNT_INFO = [52, 466, 123930, 1, 0]
UNIQUE_INFO = [5, 151, 11413, 1, 0]
MEAN_INFO = [10.40, 16.20, 3371.10, 1.0, ]
MEDIAN_INFO = [12, 15, 2956.5, 1]
CLOSEST_INFO = ['ghost', 'you', 'of', 'hello']


def compare_dicts(dict1, dict2):
    for key in dict1:
        if dict1[key] != dict2[key.lower()]:
            return False
    return True


def function_present(func_name):
    """Tests that required function is present"""
    present = False
    if func_name in globals():
        present = True
    return present


def run_tests():
    """Test main script"""
    for function in FUNCTIONS:
        if not function_present(function):
            print(f"Funktionen {function} finns inte!")
            sys.exit(1)
    print("Alla funktionerna från kravlistan är är implementerade - OK\n")

    for i, filename in enumerate(TEST_FILES):
        print(f"\nTest körs med filen {filename}")
        with open(filename.split('.')[0] + '_correct.json', 'r') as dict_file:
            correct = json.load(dict_file)
        reference = {}
        for key in correct:
            reference[key.lower()] = correct[key]

        test = frequency(filename)
        if type(test) != dict:
            print(
                "Fel: Din funktion 'frequency' returnerar fel typ. " +
                "Den ska returnera en dictionary!")
            sys.exit(1)

        test_copy = test.copy()

        if compare_dicts(test, reference):
            print(
                f"Korrekt frekvensanalys generad från testfil '{filename}' - OK")
        else:
            print(
                "Fel: Din returnerade dictionary innehåller inte rätt information.")
            if len(correct) < 200:
                print(f"Det förväntade innehållet är :\n{correct}\n\n " +
                      f"men ditt resultat ser ut så här:\n{test}")
            sys.exit(1)

        with open(filename.split('.')[0] + '_correct_top.json', 'r') as top_file:
            correct_top = json.load(top_file)
        top_reference = {}
        for key in correct_top:
            top_reference[key.lower()] = correct_top[key]
        top = most_frequent(test)
        if type(top) != dict:
            print(
                "Fel: Din funktion 'most_frequent' returnerar fel typ. " +
                "Den ska returnera en dictionary!")
            sys.exit(1)

        top_copy = top.copy()

        if compare_dicts(top, top_reference):
            print(
                f"Korrekt topp-10-dict generad från testfil '{filename}' - OK")
        else:
            print(
                "Fel: Din returnerade topp-10-dict innehåller inte rätt information")
            print(
                f"Det förväntade innehållet är :\n{correct_top}\n\n " +
                f"men ditt resultat ser ut så här:\n{top}")
            sys.exit(1)

        if test != test_copy:
            print(
                "Fel: Det är inte meningen att funktionen 'most_frequent' " +
                "ska förändra den inskickade dictionaryn!")
            sys.exit(1)

        if test is top:
            print("Fel: Funktionen 'most_frequent' har inte skapat en ny dictionary!")
            sys.exit(1)

        # test word_count()
        count = word_count(test)
        if type(count) != int:
            print(
                "Fel: Din funktion 'word_count' returnerar fel typ. Den ska returnera ett heltal!")
            sys.exit(1)

        if count != COUNT_INFO[i]:
            print(
                f"Fel: Antalet ord stämmer inte.\nDet förväntade värdet är {COUNT_INFO[i]}, " +
                f"men din kod ger {count}.")
            sys.exit(1)

        if test != test_copy:
            print(
                "Fel: Funktionen 'word_count' ska inte förändra den inskickade dictionaryn!")
            sys.exit(1)

        # test unique_words()
        unique = unique_words(test)
        if type(unique) != int:
            print(
                "Fel: Din funktion 'unique_words' returnerar fel typ. " +
                "Den ska returnera ett heltal!")
            sys.exit(1)

        if unique != UNIQUE_INFO[i]:
            print(
                "Fel: Antalet unika ord stämmer inte.\nDet förväntade värdet är " +
                f"{UNIQUE_INFO[i]}, men din kod ger {unique}.")
            sys.exit(1)

        if test != test_copy:
            print(
                "Fel: Funktionen 'unique_words' ska inteförändra den inskickade dictionaryn!")
            sys.exit(1)

        if correct:
            # test mean_frequency()
            mean = mean_frequency(top)
            if not isinstance(mean, (int, float)):
                print(
                    "Fel: Din funktion 'mean_frequency' returnerar fel typ. " +
                    "Den ska returnera ett tal!")
                sys.exit(1)

            if mean != MEAN_INFO[i]:
                print(
                    f"Fel: Medelvärdet stämmer inte.\nDet förväntade värdet är {MEAN_INFO[i]}, " +
                    f"men din kod ger {mean}.")
                sys.exit(1)

            if top != top_copy:
                print(
                    "Fel: Funktionen 'mean_frequency' ska inte förändra den inskickade dictionaryn!")
                sys.exit(1)

            # test median_frequency()
            median = median_frequency(top)
            if not isinstance(median, (int, float)):
                print(
                    "Fel: Din funktion 'median_frequency' returnerar fel typ. Den ska returnera ett tal!")
                sys.exit(1)

            if median != MEDIAN_INFO[i]:
                print(
                    f"Fel: Medianvärdet stämmer inte.\nDet förväntade värdet är {MEDIAN_INFO[i]}, " +
                    f"men din kod ger {median}.")
                sys.exit(1)

            if top != top_copy:
                print(
                    "Fel: Det är inte meningen att funktionen 'median_frequency' ska förändra den inskickade dictionaryn!")
                sys.exit(1)

            # test closest_word(freq_dict, rate)
            word = closest_word(test, mean)
            if not isinstance(word, str):
                print(
                    "Fel: Din funktion 'closest_word' returnerar fel typ. Den ska returnera en sträng!")
                sys.exit(1)

            if word.lower() != CLOSEST_INFO[i].lower():
                print(
                    "Fel: Funktionen hittar inte rätt ord\nDet förväntade ordet är " +
                    f"'{CLOSEST_INFO[i]}', men din kod ger {word}.")
                sys.exit(1)

            if test != test_copy:
                print(
                    "Fel: Det är inte meningen att funktionen 'closest_word' ska förändra den inskickade dictionaryn!")
                sys.exit(1)

    print("\nOK - Dina funktioner passerade alla tester.")


if __name__ == "__main__":
    run_tests()
