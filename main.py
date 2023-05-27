# -*- coding: utf-8 -*-

import os
import time
import json
import openai
import requests
import pandas as pd
from compare import get_scores, compare_xlsx


# Changeable variables
# --------------------------
prompt_version = "1"  # check the number txt file in the Prompts folder
sections = 8  # between 1 and 8
model_type = "system" # "system" or ""

# Functions
# --------------------------
def create_prompt(section):
    """Read the txt file and append it to the messages_history list"""

    with open(f"./Prompts/{model_type}V{prompt_version}.txt", "r", encoding="utf-8") as f:
        system = f.read()
    with open(f"./PAES/lenguaje/{section}.txt", "r", encoding="utf-8") as f:
        paes_fragment = f.read()

    messages_history = [
        {"role": "system", "content": system},
        {"role": "user", "content": paes_fragment}
    ]
    return messages_history


def gpt_call(messages_history):
    """API call to OpenAI GPT-4"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            # model="gpt-3.5-turbo",
            messages=messages_history,
        )

        answers = response.choices[0].message.content
        print("Respuesta: ", answers)

    except openai.error.RateLimitError:
        print("Modelo sobrecargado. Esperando 5 segundos antes de volver a intentar.")
        time.sleep(5)
        gpt_call(messages_history)

    answers = response.choices[0].message.content
    print("Respuesta: ", answers)
    answers = json.loads(answers)
    print("Respuesta JSON: ", answers)
    print(answers)
    print()

    return answers


def dir_manipulation():
    """Create and manage the directories to store all the results"""

    os.chdir("./Resultados")
    len_dir = len(os.listdir()) - 1  # -1 to ignore the test folder
    xlsx_name = f"{model_type}V{prompt_version}_{len_dir+1}.xlsx"

    # muy dudosa ejecucion de codigo, pero funciona (ojala algun dia pueda mejorar esto :v (jasjaj copilot me recomendo poner ":v"))
    if xlsx_name in os.listdir():
        repeted = True
        while repeted:
            len_dir += 1
            xlsx_name = f"V{prompt_version}_{len_dir+1}.xlsx"
            if xlsx_name not in os.listdir():
                repeted = False
    xlsx_path = "./Resultados/" + xlsx_name
    os.chdir("..")

    return xlsx_path


def upload_answers(gpt_answers):
    """Compare all the answers given by the GPT-3 model with the correct answers and then create a xlsx file with the results"""

    with open("./PAES/lenguaje/clavijero.txt", "r", encoding="utf-8") as f:
        correct_answer = f.read().splitlines()

    final_answers = []
    correct = 0
    incorrect = 0
    for i in range(min(len(gpt_answers), len(correct_answer))):
        if gpt_answers[i] == correct_answer[i]:
            final_answers.append([i + 1, gpt_answers[i], True])
            correct += 1
        else:
            final_answers.append([i + 1, gpt_answers[i], False])
            incorrect += 1

    print()
    print("Respuestas")
    print("--------------------------------------------------------------")
    print(gpt_answers)
    print("--------------------------------------------------------------")
    print("Correctas:   ", correct)
    print("Incorrectas: ", incorrect)
    print()

    # create a xlsx file to post the answers
    data = list(zip(correct_answer, gpt_answers))
    df = pd.DataFrame(data, columns=["Clavijero", "GPT-PAES"])
    for i in range(len(final_answers)):
        x_pos = 1
        y_pos = 1
        if final_answers[i][2]:
            df.iloc[y_pos, x_pos] = final_answers[i][1]

        else:
            df.iloc[y_pos, x_pos] = final_answers[i][1]

    # it could be awesome to change the color of the cell if the answer is correct or incorrect, or at least a cell with the number of correct and incorrect answers

    df.to_excel(dir_manipulation(), index=False)

    print("Excel actualizado con las respuestas")
    print()
    return


# Main
# --------------------------
if __name__ == "__main__":
    # Variables
    start_time = time.time()
    answers = []
    openai.api_key = os.getenv("OPENAI_API_KEY")

    print("Comenzando GPT-PAES Comprension Lectora")
    print()

    for i in range(0, sections):

        if i == 1 or i == 3 or i == 7:  # special naming cases
            for j in range(1, 3):
                print("Respondiendo texto: ", i, ".", j)

                messages_history = create_prompt(f"{i}.{j}")
                gpt3_answers = gpt_call(messages_history)
                answers += list(gpt3_answers.values())

        else:
            print("Respondiendo texto: ", i)

            messages_history = create_prompt(str(i))
            gpt3_answers = gpt_call(messages_history)
            answers += list(gpt3_answers.values())
    upload_answers(answers)

    scores = get_scores()
    compare_xlsx(scores)
    print("Estadisticas actualizadas")

    time_elapsed = time.time() - start_time
    print("Fin GPT-PAES Comprension Lectora")
    print("Se demoro", round(time_elapsed, 2), "segundos en completar la prueba")
    print()
