# write the utf-8 encoding at the top of the file
# -*- coding: utf-8 -*-

import os
import time
import json
import openai
import requests

# Variables
# --------------------------
page = 1
answers = []

openai.api_key = os.getenv("OPENAI_API_KEY")


# Functions
# --------------------------
def get_prompt(page):
    """Read the txt file and append it to the prompt"""
    prompt = """Lo siguiente es la PAES, la prueba mas importante de transicion universitaria en chile. Tu rol como destacado profesor de lengua española y literatura es conseguir la mejor nota en la prueba de competencia lectora.

La prueba conciste en un texto, seguido de 7 preguntas de seleccion multiple. al final de las preguntas, deberas crear un objeto en formato json con las respuestas correspodientes. (ejemplo: {"0": "a", "1": "b", "2": "c", "3": "d", "4": "e", "5": "f", "6": "g"})
###

$$$

###
Las respuestas correctas (en formato json) son las siguientes:
{"""

    with open('./PAES/lenguaje/-0.txt', 'r', encoding='utf-8') as f:
        prompt = prompt.replace('$$$', f.read())

    print("get_prompt ready")
    print()
    return prompt


def gpt3_call(prompt):
    """API call to OpenAI GPT-3"""
    answers = "{"

    response = openai.Completion.create(
        model="text-davinci-003",
        # model="text-ada-001",
        prompt= prompt,
        temperature=0.7,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    answers += response.choices[0].text
    answers = json.loads(answers)
    print()
    print(answers)
    

    print("gpt3_call ready")
    print()
    return answers


def compare_answers(gpt3_answers):
    """Compare all the answers given by the GPT-3 model with the correct answers"""
    with open('./PAES/lenguaje/clavijero.txt', 'r', encoding='utf-8') as f:
        # get the correct answer and make it a list of strings separated by \n
        correct_answer = f.read().splitlines()
    for answer in gpt3_answers:
        if answer == correct_answer:
            print("Correct answer")
        else:
            print("Wrong answer")
    return


# Main
# --------------------------
if __name__ == '__main__':
    for i in range(0, page):
        prompt = get_prompt(i)
        gpt3_answers = gpt3_call(prompt)
        results = compare_answers(gpt3_answers)

        # answers.append(gpt3_answers)

