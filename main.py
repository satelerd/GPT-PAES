# -*- coding: utf-8 -*-

import os
import time
import json
import openai
import requests


# Functions
# --------------------------
def get_prompt(section):
    """Read the txt file and append it to the prompt"""
    
    with open('./prompt.txt', 'r', encoding='utf-8') as f:
        prompt = f.read()

    with open(f'./PAES/lenguaje/{section}.txt', 'r', encoding='utf-8') as f:
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
    # Variables
    start_time = time.time()
    sections = 8
    answers = []
    openai.api_key = os.getenv("OPENAI_API_KEY")


    print ("Comenzando GPT-PAES Comprension Lectora")
    print()
    
    for i in range(0, sections):
        print("Respondiendo texto: ", i)

        # the function calls depend on the sections number
        if i == 1:
            for j in range(1, 3):
                prompt = get_prompt(f"{i}.{j}")
                gpt3_answers = gpt3_call(prompt)
                answers += list(gpt3_answers.values())

        elif i == 3:
            for j in range(1, 3):
                prompt = get_prompt(f"{i}.{j}")
                gpt3_answers = gpt3_call(prompt)
                answers += list(gpt3_answers.values())
        
        elif i == 7:
            for j in range(1, 3):
                prompt = get_prompt(f"{i}.{j}")
                gpt3_answers = gpt3_call(prompt)
                answers += list(gpt3_answers.values())

        else:
            prompt = get_prompt(i)
            gpt3_answers = gpt3_call(prompt)
            answers += list(gpt3_answers.values())

        print(answers)
        print()

        # results = compare_answers(gpt3_answers)
    
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
