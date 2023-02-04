# -*- coding: utf-8 -*-

import os
import time
import json
import openai
import requests
import pandas as pd

# Changeable variables
prompt_version = "1"


# Functions
# --------------------------
def create_prompt(section):
    """Read the txt file and append it to the prompt"""

    with open(f"./Prompts/V{prompt_version}.txt", "r", encoding="utf-8") as f:
        prompt = f.read()

    with open(f"./PAES/lenguaje/{section}.txt", "r", encoding="utf-8") as f:
        prompt = prompt.replace("$$$", f.read())

    # print("create_prompt ready")
    # print()
    return prompt


def gpt3_call(prompt):
    """API call to OpenAI GPT-3"""
    answers = "{"

    response = openai.Completion.create(
        model="text-davinci-003",
        # model="text-ada-001",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    answers += response.choices[0].text
    print(answers)
    print()
    answers = json.loads(answers)

    return answers


def dir_manipulation():
    """Create and manage the directories to store all the results"""
    current_dir = os.getcwd()
    current_date = time.strftime("%d_%m_%Y")
    os.chdir(current_dir + "/Resultados")
    len_dir = len(os.listdir()) - 1  # -1 to ignore the test file
    xlsx_name = f"V{prompt_version}_{len_dir+1}.xlsx"

    if (
        xlsx_name in os.listdir()
    ):  # muy dudosa ejecucion de codigo, pero creo que funcionara (ojala algun dia pueda mejorar esto :v (copilot me recomendo poner :v jasjaj))
        repeted = True
        while repeted:
            len_dir += 1
            xlsx_name = f"V{prompt_version}_{len_dir+1}.xlsx"
            if xlsx_name not in os.listdir():
                repeted = False
    xlsx_path = "./Resultados/" + xlsx_name
    print(current_dir)

    os.chdir(current_dir)
    return xlsx_path


def compare_answers(gpt3_answers):
    """Compare all the answers given by the GPT-3 model with the correct answers"""
    final_answers = []
    correct = 0
    incorrect = 0

    with open("./PAES/lenguaje/clavijero.txt", "r", encoding="utf-8") as f:
        correct_answer = f.read().splitlines()

    for i in range(0, len(correct_answer)):
        if gpt3_answers[i] == correct_answer[i]:
            final_answers.append([i + 1, gpt3_answers[i], True])
            correct += 1
        else:
            final_answers.append([i + 1, gpt3_answers[i], False])
            incorrect += 1
    print("Respuestas correctas: ", correct)
    print("Respuestas incorrect: ", incorrect)

    # create a xlsx file to post the answers
    data = list(zip(correct_answer, gpt3_answers))
    df = pd.DataFrame(data, columns=["Clavijero", "GPT-PAES"])
    print(final_answers)
    for i in range(len(final_answers)):
        x_pos = 1
        y_pos = 1
        if final_answers[i][2]:
            df.iloc[y_pos, x_pos] = final_answers[i][1]

        else:
            df.iloc[y_pos, x_pos] = final_answers[i][1]
    # now change the color of all the cells in the column depending on the value. if the value is true, the cell will be green, if not, the cell will be red
    df.style.applymap(
        lambda x: "background-color: green"
        if x == True
        else "background-color: red"
        if x == False
        else "",
        subset=pd.IndexSlice[:, ["Respuesta correcta"]],
    )
    # save the file with the name: ans_cl_dia/hora:minuto
    df.to_excel(dir_manipulation(), index=False)

    # row_finded = False
    # while not row_finded:
    #     # search for the first empty row starting from the E column and the 3nd row
    #     for i in range(2, 100):
    #         if df.iloc[i, 5].isnull():
    #             # write the answers in the xlsx file
    #             for j in range(0, len(gpt3_answers)):
    #                 df.iloc[i, j + 5] =
    #             df.to_excel("./Resultados/comprension_lectora.xlsx", index=False)
    #             row_finded = True
    #             break

    print("Excel actualizado con las respuestas")
    print()
    return


# Main
# --------------------------
if __name__ == "__main__":
    # Variables
    start_time = time.time()
    sections = 8
    answers = []
    openai.api_key = os.getenv("OPENAI_API_KEY")

    print("Comenzando GPT-PAES Comprension Lectora")
    print()

    for i in range(0, sections):

        if i == 1 or i == 3 or i == 7:  # special naming cases
            for j in range(1, 3):
                print("Respondiendo texto: ", i, ".", j)

                prompt = create_prompt(f"{i}.{j}")
                gpt3_answers = gpt3_call(prompt)
                answers += list(gpt3_answers.values())
        else:
            print("Respondiendo texto: ", i)
            prompt = create_prompt(str(i))
            gpt3_answers = gpt3_call(prompt)
            answers += list(gpt3_answers.values())

    print()
    print("Respuestas")
    print("--------------------------------------------------------------")
    print(answers)
    print("--------------------------------------------------------------")
    print()
    compare_answers(answers)

    print("Fin GPT-PAES Comprension Lectora")
    time_elapsed = time.time() - start_time
    print("Se demoro", round(time_elapsed, 2), "segundos en completar la prueba")
    print()
