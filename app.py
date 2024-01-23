import os
import time

import openai
from flask import Flask, redirect, render_template, request, url_for
from dotenv import load_dotenv

# 如果存在环境变量的文件，则加载配置到环境变量
if os.path.exists(".env"):
    load_dotenv(".env")

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
max_tokens = 2048


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        search = request.form["search"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=search,
            temperature=0,
            max_tokens=max_tokens,
            top_p=1,
            n=1
        )
        result = ''
        if response.choices[0].finish_reason == 'stop':
            result = response.choices[0].text
            print(result)
        else:
            while(response.choices[0].finish_reason != 'stop'):
                search = "接着 " + result[-8:]
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=search,
                    temperature=1,
                    max_tokens=max_tokens
                )
                print(response.choices[0].text)
                result += response.choices[0].text
        return redirect(url_for("index", result=result))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )
