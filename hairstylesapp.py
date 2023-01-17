from flask import Flask, jsonify, request
from hairstylesdbutils import get_hairstyle_recommendations

app = Flask(__name__)

@app.route('/hairstyle/<answer>')
def suggested_hairstyle(answer):
    result = get_hairstyle_recommendations(answer)
    jsonifyresult = jsonify(result)
    return jsonifyresult

if __name__ == '__main__':
    app.run(debug=True, port=5001)