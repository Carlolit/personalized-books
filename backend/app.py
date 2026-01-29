
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Разрешаем запросы с других доменов (GitHub Pages)

@app.route('/api/create-story', methods=['POST'])
def create_story():
    hero_name = request.form.get('heroName')
    hero_photo = request.files.get('heroPhoto')

    if not hero_name or not hero_photo:
        return jsonify({"error": "Имя или фото не предоставлены"}), 400

    # Пока вместо ИИ просто создаём тестовую историю
    story_text = f"Это история про героя {hero_name}. Фото загружено: {hero_photo.filename}"

    return jsonify({"story": story_text})

if __name__ == '__main__':
    app.run(debug=True)
