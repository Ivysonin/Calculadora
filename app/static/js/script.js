let a = "";
let b = "";
let operacao = null;
let isSecond = false;

function updateDisplay() {
    let simbolo = "";

    switch (operacao) {
        case "adicao": simbolo = "+"; break;
        case "subtracao": simbolo = "-"; break;
        case "multiplicacao": simbolo = "*"; break;
        case "divisao": simbolo = "/"; break;
        case "potenciacao": simbolo = "^"; break;
        case "porcentagem": simbolo = "%"; break;
    }

    if (operacao === "raiz-quadrada") {
        document.getElementById("display").value = "√(" + a + ")";
    } else {
        document.getElementById("display").value = a + " " + simbolo + " " + b;
    }
}

function addNumber(num) {
    if (!isSecond) {
        a += num;
    } else {
        b += num;
    }
    updateDisplay();
}

function addDot() {
    if (!isSecond && !a.includes(".")) {
        a += ".";
    } else if (isSecond && !b.includes(".")) {
        b += ".";
    }
    updateDisplay();
}

function setOp(op) {
    if (a === "") return;

    if (b !== "") {
        calcularLocal(); // resolve antes de trocar operador
    }

    operacao = op;
    isSecond = true;
    updateDisplay();
}

function clearDisplay() {
    a = "";
    b = "";
    operacao = null;
    isSecond = false;
    updateDisplay();
}

function calcularLocal() {
    let x = parseFloat(a);
    let y = parseFloat(b);

    if (isNaN(x) || isNaN(y)) return;

    switch (operacao) {
        case "adicao":
            a = (x + y).toString();
            break;

        case "subtracao":
            a = (x - y).toString();
            break;

        case "multiplicacao":
            a = (x * y).toString();
            break;

        case "divisao":
            a = (x / y).toString();
            break;

        case "potenciacao":
            a = (x ** y).toString();
            break;
    }

    b = "";
}

async function calculate() {
    if (!operacao || b === "") return;

    b = b.toString();

    calcularLocal();

    operacao = null;
    isSecond = false;
    updateDisplay();
}

async function raiz() {
    if (a === "") return;

    operacao = "raiz-quadrada";
    updateDisplay();

    try {
        const res = await fetch("/calculadora/raiz-quadrada", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ a: parseFloat(a) })
        });

        const data = await res.json();

        if (data.erro) {
            document.getElementById("display").value = "Erro";
        } else {
            a = data.resultado.toString();
            b = "";
            operacao = null;
            isSecond = false;
            updateDisplay();
        }

    } catch {
        document.getElementById("display").value = "Erro";
    }
}

function porcentagem() {
    if (a === "" || b === "") return;

    let base = parseFloat(a);
    let percent = parseFloat(b);

    let valorPercentual = (base * percent) / 100;

    switch (operacao) {
        case "adicao":
            b = valorPercentual.toString();
            break;

        case "subtracao":
            b = valorPercentual.toString();
            break;

        case "multiplicacao":
            b = (percent / 100).toString();
            break;

        case "divisao":
            b = (percent / 100).toString();
            break;

        default:
            return;
    }

    updateDisplay();
}