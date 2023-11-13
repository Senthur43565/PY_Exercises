from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the Flask Web App"

@app.route("/run-python")
def run_python():
    try:
        import random
        import pyautogui as pg
        import time

        time.sleep(1)
        animal = ('hello', 'how', 'are', 'you')

        for _ in range(5):
            a = random.choice(animal)
            pg.write(f"you are a {a}")
            pg.press("enter")

        return "Python script executed successfully."
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    app.run()
