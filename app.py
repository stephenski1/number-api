import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

NUMBERS_API_URL = "http://numbersapi.com"

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    return sum(int(digit) ** power for digit in num_str) == n

def fetch_fun_fact(n):
    try:
        response = requests.get(f"{NUMBERS_API_URL}/{n}/math", timeout=5)
        if response.status_code == 200:
            return response.text
    except requests.exceptions.RequestException:
        return "No fun fact available at the moment."
    return "No fun fact found."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    num = request.args.get("number")

    if not num or not num.isdigit():
        return jsonify({"number": num, "error": True}), 400

    num = int(num)

    # Determine properties
    properties = []
    if is_armstrong(num):
        properties.append("armstrong")
    properties.append("even" if num % 2 == 0 else "odd")

    response = {
        "number": num,
        "is_prime": is_prime(num),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(num)),
        "fun_fact": fetch_fun_fact(num)
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

