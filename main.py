from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def game():
    game_url = "https://vseigru.net/igry-dlya-devochek-10-let/45085-igra-remont-velosipeda-dlya-devochek-stiralnyj-salon.html"
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Гра: Ремонт велосипедів</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f0f0f0;
                font-family: Arial, sans-serif;
            }
            h1 {
                margin-bottom: 20px;
                font-size: 24px;
                color: #333;
            }
            iframe {
                width: 80%;
                height: 80%;
                border: 2px solid #ccc;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }
        </style>
    </head>
    <body>
        <h1>Вітаємо в грі: Ремонт велосипедів</h1>
        <iframe src="{{ game_url }}"></iframe>
    </body>
    </html>
    ''', game_url=game_url)

if __name__ == "__main__":
    app.run(debug=True)