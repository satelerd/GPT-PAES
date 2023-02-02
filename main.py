# write the utf-8 encoding at the top of the file
# -*- coding: utf-8 -*-

import os
import time
import json
import openai
import requests

# Variables
# --------------------------
page = 0

# Functions
# --------------------------
def get_prompt(page):
    """Read the txt file and append it to the prompt"""
    prompt = """Lo siguiente es la PAES, la prueba mas importante de transicion universitaria en chile. Tu rol como destacado profesor de lengua española y literatura es conseguir la mejor nota en la prueba de competencia lectora.

La prueba conciste en un texto, seguido de 7 preguntas de seleccion multiple. al final de las preguntas, deberas responder 1  a 1 explicando porque elegiste esa opcion.
###

$$$

###
Las respuestas correctas son las siguientes:
1.
"""

    with open('./PAES/lenguaje/0.txt', 'r', encoding='utf-8') as f:
        prompt = prompt.replace('$$$', f.read())
        # this is giving me the UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 2462: character maps to <undefined>
        # I tried to change the encoding to utf-8 but it didn't work

    return prompt


def gpt3_call(prompt):
    """API call to OpenAI GPT-3"""
    return


def compare_answers():
    """Compare all the answers given by the GPT-3 model with the correct answers"""
    return


# Main
# --------------------------
if __name__ == '__main__':
    for i in range(0, page):
        prompt = get_prompt(i)
        print(prompt)



        # answers = gpt3_call(prompt)
        # corrections = get_corrections()
        # print(answers)
        # print(corrections)
