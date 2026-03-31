from flask import Blueprint, request, jsonify
from app.services.calculadora_service import CalculadoraService


calculadora_bp = Blueprint("calculadora", __name__, url_prefix='/calculadora')


@calculadora_bp.route("/adicao", methods=["POST"])
def adicao():
    data = request.get_json()
    
    resultado = CalculadoraService.adicao(data["a"], data["b"])
    return jsonify({"resultado": resultado})


@calculadora_bp.route("/subtracao", methods=["POST"])
def subtracao():
    data = request.get_json()
    resultado = CalculadoraService.subtracao(data["a"], data["b"])
    return jsonify({"resultado": resultado})


@calculadora_bp.route("/multiplicacao", methods=["POST"])
def multiplicacao():
    data = request.get_json()
    resultado = CalculadoraService.multiplicacao(data["a"], data["b"])
    return jsonify({"resultado": resultado})


@calculadora_bp.route("/divisao", methods=["POST"])
def divisao():
    data = request.get_json()
    try:
        resultado = CalculadoraService.divisao(data["a"], data["b"])
        return jsonify({"resultado": resultado})
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@calculadora_bp.route("/potenciacao", methods=["POST"])
def potenciacao():
    data = request.get_json()
    resultado = CalculadoraService.potenciacao(data["a"], data["b"])
    return jsonify({"resultado": resultado})


@calculadora_bp.route("/raiz-quadrada", methods=["POST"])
def raiz_quadrada():
    data = request.get_json()
    try:
        resultado = CalculadoraService.raiz_quadrada(data["a"])
        return jsonify({"resultado": resultado})
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@calculadora_bp.route("/porcentagem", methods=["POST"])
def porcentagem():
    data = request.get_json()
    try:
        resultado = CalculadoraService.porcentagem(
            data["tipo"],
            data["porcentagem"],
            data["valor"]
        )
        return jsonify({"resultado": resultado})
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400