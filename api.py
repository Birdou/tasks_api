
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

tarefas = []


@app.route("/task/<int:id>", methods=["GET", "PUT", "DELETE"])
def task_view(id):
    if request.method == "GET":
        try:
            return jsonify(tarefas[id])
        except IndexError:
            mensagem = "O índice {} está fora do intervalo".format(id)
            return jsonify({"status": "erro", "mensagem": mensagem})

    elif request.method == "PUT":
        data = json.loads(request.data)
        response = tarefas[id]
        response["status"] = data["status"]

        return jsonify(response)

    elif request.method == "DELETE":
        try:
            tarefas.pop(id)
            mensagem = "Registro de id {} removido".format(id)
            return jsonify({"status": "sucesso", "mensagem": mensagem})
        except IndexError:
            mensagem = "O índice {} está fora do intervalo".format(id)
            return jsonify({"status": "erro", "mensagem": mensagem})


@app.route("/task", methods=["GET", "POST"])
def task():
    if request.method == "GET":
        return jsonify(tarefas)

    elif request.method == "POST":
        response = json.loads(request.data)
        response['id'] = len(tarefas)

        tarefas.append(response)

        return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
