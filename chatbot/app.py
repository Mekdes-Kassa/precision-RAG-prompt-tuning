from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__, template_folder='Template')

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

# Import the OpenAI module
import openai
 
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=user_text,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text

if __name__ == "__main__":
    app.run(debug=True)