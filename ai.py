from flask import Flask, request, jsonify
import wikipedia
import speech_recognition as sr
import pyttsx3

app = Flask(__name__)

def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return "Multiple results found. Please provide more specific query."
    except wikipedia.exceptions.PageError as e:
        return "Sorry, the requested page does not exist."

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

@app.route('/query', methods=['POST'])
def process_query():
    query = request.json['query']
    result = search_wikipedia(query)
    text_to_speech(result)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
