from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Flask Calculator</title>
<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background: linear-gradient(135deg, #89f7fe, #66a6ff);
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
    }
    .calculator {
        background: #ffffffdd;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        width: 300px;
    }
    h1 {
        text-align: center;
        color: #333;
        margin-bottom: 20px;
    }
    input {
        width: 88%;
        padding: 15px;
        font-size: 20px;
        border-radius: 10px;
        border: 1px solid #ccc;
        margin-bottom: 10px;
        text-align: right;
    }
    .buttons {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
    }
    button {
        padding: 20px;
        font-size: 18px;
        border-radius: 10px;
        border: none;
        background: #66a6ff;
        color: white;
        cursor: pointer;
        transition: 0.2s;
    }
    button:hover {
        background: #557dd1;
    }
    .result {
        text-align: center;
        font-size: 22px;
        margin-top: 15px;
        color: #333;
    }
</style>
</head>
<body>
<div class="calculator">
    <h1>Calculator</h1>
    <form method="POST">
        <input type="text" name="expression" value="{{ expression or '' }}" placeholder="0" readonly>
        <div class="buttons">
            {% for btn in ['7','8','9','/','4','5','6','*','1','2','3','-','0','.','=','+','C'] %}
                <button type="submit" name="button" value="{{ btn }}">{{ btn }}</button>
            {% endfor %}
        </div>
    </form>
    {% if result is not none %}
        <div class="result">Result: {{ result }}</div>
    {% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    expression = ""
    result = None

    if request.method == "POST":
        button = request.form.get("button")
        expression = request.form.get("expression", "")

        if button:
            if button == "C":
                expression = ""
                result = None
            elif button == "=":
                try:
                    # Safely evaluate the expression
                    result = eval(expression)
                except Exception:
                    result = "Error"
                expression = ""
            else:
                expression += button

    return render_template_string(html, result=result, expression=expression)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)