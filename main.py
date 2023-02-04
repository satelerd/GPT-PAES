# -*- coding: utf-8 -*-

import os
import time
import json
import openai
import requests
import pandas as pd


# Functions
# --------------------------
def create_prompt(section):
    """Read the txt file and append it to the prompt"""
    
    with open('./prompt.txt', 'r', encoding='utf-8') as f:
        prompt = f.read()

    with open(f'./PAES/lenguaje/{section}.txt', 'r', encoding='utf-8') as f:
        prompt = prompt.replace('$$$', f.read())

    # print("create_prompt ready")
    # print()
    return prompt


def gpt3_call(prompt):
    """API call to OpenAI GPT-3"""
    answers = "{"

    response = openai.Completion.create(
        model="text-davinci-003",
        # model="text-ada-001",
        prompt= prompt,
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    answers += response.choices[0].text
    print(answers)
    print()
    answers = json.loads(answers)
    


    return answers


def compare_answers(gpt3_answers):
    """Compare all the answers given by the GPT-3 model with the correct answers"""
    correct = 0
    incorrect = 0
    with open('./PAES/lenguaje/clavijero.txt', 'r', encoding='utf-8') as f:
        correct_answer = f.read().splitlines()

    for i in range(0, len(gpt3_answers)):
        if gpt3_answers[str(i)] == correct_answer[i]:
            correct += 1 
            gpt3_answers[str(i)] = gpt3_answers[str(i)] + " (correct)"
        else:
            incorrect += 1
            gpt3_answers[str(i)] = gpt3_answers[str(i)] + " (incorrect)"

    # open the xlsx file to post the answers
    df = pd.read_excel('./Resultados/comprension_lectora.xlsx')
    row_finded = False
    while not row_finded:
        # search for the first empty row starting from the E column and the 3nd row
        for i in range(2, 100):
            if df.iloc[i, 5] == "":
                # write the answers in the xlsx file
                for j in range(0, len(gpt3_answers)):
                    df.iloc[i, j+5] = gpt3_answers[str(j)]
                df.to_excel('./Resultados/comprension_lectora.xlsx', index=False)
                row_finded = True
                break

    print("Respuestas correctas: ", correct)
    print("Respuestas incorrect: ", incorrect)
    print("Excel actualizado con las respuestas")
    print()
    return


# Main
# --------------------------
if __name__ == '__main__':
    # Variables
    start_time = time.time()
    sections = 8
    answers = []
    openai.api_key = os.getenv("OPENAI_API_KEY")


    print ("Comenzando GPT-PAES Comprension Lectora")
    print()
    
    for i in range(0, sections):
        print("Respondiendo texto: ", i)

        txt_file_name = str(i)
        if i == 1 or i == 3 or i == 7:      # special naming cases
            for j in range(1, 3):
                txt_file_name = f"{i}.{j}"
        
        prompt = create_prompt(txt_file_name)
        gpt3_answers = gpt3_call(prompt)
        answers += list(gpt3_answers.values())

    compare_answers(answers)


    time.sleep(5.3)
    time_elapsed = time.time() - start_time


    print()
    print("Respuestas")
    print("--------------------------------------------------------------")
    print(answers)
    print("--------------------------------------------------------------")
    print()
    print("Fin GPT-PAES Comprension Lectora")
    print("Se demoro", round(time_elapsed,2), "segundos en completar la prueba")
    print()
