import os

from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

db = os.environ.get("DB_URL");
adapter = os.environ.get("DB_ADAPTER");
readOnly = os.environ.get("READ_ONLY");
if db is None:
    db = "sqlite:///db.sqlite3"

if adapter is None:
    adapter = "chatterbot.storage.SQLStorageAdapter"
if readOnly is None:
    readOnly = "True"

chinese_bot = ChatBot("Chatterbot", read_only=(readOnly == "True"), storage_adapter=adapter,
                      database_uri=db)
trainer = ListTrainer(chinese_bot)


# trainer = ChatterBotCorpusTrainer(chinese_bot)
# trainer = ChatterBotCorpusTrainer(chinese_bot)
# trainer.train("chatterbot.corpus.chinese")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    responseText = chinese_bot.get_response(userText);
    return jsonify(response=str(responseText))


@app.route("/train", methods=['POST'])
def get_train_response():
    data = request.get_json();
    trainer.train(data)
    return jsonify(response="ok")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
