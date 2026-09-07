import math
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculator():
  result = None
  error = None
  num1 = None
  num2 = None

  if request.method == "POST":
    try:
      num1 = float(request.form.get("num1", 0))
      num2 = float(request.form.get("num2", 0))
      operation = request.form.get("operation")

      if operation == "+":
        result = num1 + num2
      elif operation == "-":
        result = num1 - num2
      elif operation == "*":
        result = num1 * num2
      elif operation == "/":
        if num2 != 0:
          result = num1 / num2
        else:
          error = "Error: Division by zero is not allowed."
      elif operation == "^":
        result = num1**num2
      elif operation == "sqrt":
        if num1 >= 0:
          result = math.sqrt(num1)
        else:
          error = "Error: Square root of a negative number is not defined."
      elif operation == "log":
        if num1 > 0:
          result = math.log(num1)
        else:
          error = "Error: Logarithm of a non-positive number is not defined."
      elif operation == "sin":
        result = math.sin(num1)
      elif operation == "cos":
        result = math.cos(num1)
      elif operation == "tan":
        result = math.tan(num1)
      else:
        error = "Invalid operation selected."
    except Exception as e:
      error = f"An error occurred: {e}"

  return render_template(
      "index.html", result=result, error=error, num1=num1, num2=num2
  )


if __name__ == "__main__":
  app.run(debug=True)