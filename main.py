# write the utf-8 encoding at the top of the file
# -*- coding: utf-8 -*-

import os
import time
import json
import openai
import requests

# Variables
# --------------------------
page = 8
answers = []

openai.api_key = os.getenv("OPENAI_API_KEY")


# Functions
# --------------------------
def get_prompt(page):
    """Read the txt file and append it to the prompt"""
    prompt = """Lo siguiente es la PAES, la prueba mas importante de transicion universitaria en chile. Tu rol como destacado profesor de lengua española y literatura es conseguir la mejor nota en la prueba de competencia lectora.

La prueba conciste en un texto, seguido de 7 preguntas de seleccion multiple. Al final de las preguntas, deberas crear un objeto en formato json con las respuestas correspodientes. (ejemplo: {"0": "a", "1": "b", "2": "c", "3": "d", "4": "e", "5": "f", "6": "g"})
###

$$$

###
Las respuestas correctas (en formato json) son las siguientes:
{"""
#     :"""

    with open(f'./PAES/lenguaje/{page}.txt', 'r', encoding='utf-8') as f:
        prompt = prompt.replace('$$$', f.read())

    # print("get_prompt ready")
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
        max_tokens=70,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    answers += response.choices[0].text
    print(answers)
    answers = json.loads(answers)
    print()
    

    print("gpt3_call ready")
    print()
    return answers


def compare_answers(gpt3_answers):
    """Compare all the answers given by the GPT-3 model with the correct answers"""
    correct = 0
    incorrect = 0
    with open('./PAES/lenguaje/clavijero.txt', 'r', encoding='utf-8') as f:
        # get the correct answer and make it a list of strings separated by \n
        correct_answer = f.read().splitlines()

    for i in range(0, len(gpt3_answers)):
        print(i, " GPT-3 answer: ", gpt3_answers[str(i)])
        print(i, " Correct answer: ", correct_answer[i+23])
        print()
        if gpt3_answers[str(i)] == correct_answer[i+23]:
            correct += 1 
            gpt3_answers[str(i)] = gpt3_answers[str(i)] + " (correct)"
        else:
            incorrect += 1
            gpt3_answers[str(i)] = gpt3_answers[str(i)] + " (incorrect)"

    print()
    print("compare_answers ready")
    print("Correct: ", correct)
    print("Incorrect: ", incorrect)
    print()
    return


# Main
# --------------------------
if __name__ == '__main__':
    print ("Comenzando GPT-PAES Comprension Lectora")
    print()
    
    for i in range(0, page):
        print("Respondiendo texto: ", i+1)
        print()

        # getting the prompt
        if i == 1:
            continue
            for j in range(1, 3):
                prompt = get_prompt(f"{i}.{j}")

        elif i == 3:
            for j in range(1, 3):
                prompt = get_prompt(f"{i}.{j}")
                gpt3_answers = gpt3_call(prompt)
                answers += gpt3_answers
        else:
            prompt = get_prompt(i)
            gpt3_answers = gpt3_call(prompt)
            answers += gpt3_answers

        # results = compare_answers(gpt3_answers)

