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

    os.chdir("..")
    print(scores)
    return scores


def compare_xlsx(scores):
    # Create a xlsx file with the results
    data = []

    with open("./PAES/lenguaje/puntajes.txt", "r", encoding="utf-8") as f:
        puntajes = f.read().splitlines()

    for prompt_version in scores:
        for i in range(len(scores[prompt_version])):
            data.append(
                [
                    prompt_version,
                    puntajes[scores[prompt_version][i][0]],
                    scores[prompt_version][i][0],
                    scores[prompt_version][i][1],
                    scores[prompt_version][i][0]
                    / (scores[prompt_version][i][0] + scores[prompt_version][i][1]),
                ]
            )

    df = pd.DataFrame(
        data,
        columns=[
            "Prompt",
            "Puntaje",
            "Correct",
            "Incorrecto",
            "Promedio de respuestas correctas",
        ],
    )
    df.to_excel("./Resultados/Comparacion/total.xlsx", index=False)

    print("Excel creado con los resultados")
    print()
    return


if __name__ == "__main__":
    scores = get_scores()
    compare_xlsx(scores)
