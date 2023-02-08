"""The following file will loop throgth the Resultados folder and compare the answers, then it will create a xlsx file with the results."""

import os
import pandas as pd


def get_scores():
    # Variables
    scores = {}

    os.chdir("./Resultados")
    files = os.listdir()

    cont = 0
    for file in files:
        if cont == 0:  # Skip the first folder
            cont += 1
            continue

        prompt_version = file.split("_")[0]
        if prompt_version not in scores:
            scores[prompt_version] = []

        correct = 0
        incorrect = 0
        df = pd.read_excel(file)
        for i in range(len(df)):
            if df.iloc[i, 0] == df.iloc[i, 1]:
                correct += 1
            else:
                incorrect += 1

        scores[prompt_version].append([correct, incorrect])

        cont += 1
    print(scores)
    return scores


def create_xlsx(scores):
    return


if __name__ == "__main__":
    scores = get_scores()
    create_xlsx(scores)
