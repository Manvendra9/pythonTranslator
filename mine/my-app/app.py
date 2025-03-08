from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)  # ✅ Enable CORS for frontend communication

# 🔹 Python to JavaScript Converter
def python_to_javascript(python_code):
    """Convert Python print statements to JavaScript console.log()"""
    js_code = re.sub(r"print\((.*?)\)", r"console.log(\1);", python_code)
    return f"// Translated JavaScript code\n{js_code}"

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    if not data or "code" not in data or "language" not in data:
        return jsonify({"error": "Invalid request, missing code or language"}), 400

    code = data["code"].strip()
    language = data["language"].strip().lower()

    translations = {
        "javascript": python_to_javascript(code),
        "c": f"#include <stdio.h>\nint main() {{ printf({code}); return 0; }}",
        "c++": f"#include <iostream>\nint main() {{ std::cout << {code}; return 0; }}",
        "java": f"public class Main {{ public static void main(String[] args) {{ System.out.println({code}); }} }}",
        "ruby": f"puts {code}",
        "go": f'package main\nimport "fmt"\nfunc main() {{ fmt.Println({code}) }}',
        "php": f"<?php echo {code}; ?>",
        "swift": f'print({code})',
        "rust": f'fn main() {{ println!({code}); }}',
        "kotlin": f'fun main() {{ println({code}) }}',
        "typescript": f"console.log({code});",
    }

    translated_code = translations.get(language, f"// No translation available for {language}\n{code}")

    return jsonify({"translatedCode": translated_code})

if __name__ == "__main__":
    print("Starting Flask server on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
