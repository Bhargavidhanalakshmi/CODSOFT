<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Calculator</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        body {
            background: linear-gradient(135deg, #4facfe, #00f2fe);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .calculator {
            background: white;
            width: 350px;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
            text-align: center;
        }

        .calculator h1 {
            margin-bottom: 20px;
            color: #333;
        }

        input,
        select {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
        }

        input:focus,
        select:focus {
            border-color: #4facfe;
            outline: none;
        }

        button {
            width: 48%;
            padding: 12px;
            margin-top: 15px;
            border: none;
            border-radius: 8px;
            background: #4facfe;
            color: white;
            font-size: 16px;
            cursor: pointer;
            transition: 0.3s;
        }

        button:hover {
            background: #007bff;
        }

        h2 {
            margin-top: 20px;
            color: #222;
        }
    </style>
</head>

<body>

    <div class="calculator">
        <h1>Simple Calculator</h1>

        <input type="number" id="num1" placeholder="Enter First Number">

        <select id="operator">
            <option value="+">Addition (+)</option>
            <option value="-">Subtraction (-)</option>
            <option value="*">Multiplication (*)</option>
            <option value="/">Division (/)</option>
        </select>

        <input type="number" id="num2" placeholder="Enter Second Number">

        <button onclick="calculate()">Calculate</button>
        <button onclick="clearFields()">Clear</button>

        <h2 id="result">Result:</h2>
    </div>

    <script>
        function calculate() {

            let num1 = parseFloat(document.getElementById("num1").value);
            let num2 = parseFloat(document.getElementById("num2").value);
            let operator = document.getElementById("operator").value;

            let result;

            if (isNaN(num1) || isNaN(num2)) {
                document.getElementById("result").innerHTML = "Result: Please enter both numbers.";
                return;
            }

            switch (operator) {
                case "+":
                    result = num1 + num2;
                    break;

                case "-":
                    result = num1 - num2;
                    break;

                case "*":
                    result = num1 * num2;
                    break;

                case "/":
                    if (num2 === 0) {
                        document.getElementById("result").innerHTML = "Result: Cannot divide by zero.";
                        return;
                    }
                    result = num1 / num2;
                    break;

                default:
                    document.getElementById("result").innerHTML = "Result: Invalid operation.";
                    return;
            }

            document.getElementById("result").innerHTML = "Result: " + result;
        }

        function clearFields() {
            document.getElementById("num1").value = "";
            document.getElementById("num2").value = "";
            document.getElementById("operator").value = "+";
            document.getElementById("result").innerHTML = "Result:";
        }
    </script>

</body>
</html>