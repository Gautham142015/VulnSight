from flask import Flask, jsonify, request
from scanner.scanner import Scanner

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    scanner = Scanner(url)
    vulnerabilities = scanner.scan()
    return jsonify({'vulnerabilities': vulnerabilities})

if __name__ == '__main__':
    app.run(debug=True)
