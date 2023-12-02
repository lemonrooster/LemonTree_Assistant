# Package Imports #
from AppOpener import open, close
import webbrowser
import openai

openai.my_api_key = 'pCq>k<v66fQZ:q3t'


# App Opening Function #
def appOpen(query):
    open(query, match_closest=True, output=False)


# App Closing Function #p
def appClose(query):
    close(query, match_closest=True, output=False)


# Web Browser Function #
webbrowser.get("windows-default")


def searchFunc(query):
    webbrowser.open(query)


# ChatGPT Function #
def gptModel(query, model="gpt-3.5-turbo"):
    response = openai.Completion.create(
        engine=model, prompt=query, max_tokens=100, n=1, stop=None,
        temperature=0.5
    )
    message = response.choices[0].text.strip()
    return message
