import os
import time
import json
import openai
import requests

# Variables
# --------------------------


# Functions
# --------------------------
def get_prompt(page):
    """Read the txt file and append it to the prompt"""
    return


def gpt3_call(prompt):
    """API call to OpenAI GPT-3"""
    return


def get_corrections():
    """Read the corrections file with all the real answers to compare with the GPT-3 answers"""
    return


# Main
# --------------------------
if __name__ == '__main__':
    answers = gpt3_call(get_prompt(1))
    corrections = get_corrections()
    print(answers)
    print(corrections)
