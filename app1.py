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
max_tokens = 4096


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        questions = request.form["search"]
        print("questions:" + questions)
        response = openai.Completion.create(engine="text-davinci-003", prompt=questions, max_tokens=max_tokens)
        str = response.choices[0].text
        # remain = response.usage.total_tokens - response.usage.completion_tokens
        # while remain > 0:
        #     questions = "接着 " + str[-8:]
        #     print("questions:" + questions)
        #     time.sleep(1)
        #     response = openai.Completion.create(engine="text-davinci-003", prompt=questions, max_tokens=max_tokens)
        #     remain -= response.usage.completion_tokens
        #     str += response.choices[0].text
        #     print(response.choices[0].text)
        print("response:" + str)
        # response = openai.Completion.create(
        #     model="text-davinci-003",
        #     prompt=generate_prompt(animal),
        #     temperature=0.6,
        # )
        return redirect(url_for("index", result=str))

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