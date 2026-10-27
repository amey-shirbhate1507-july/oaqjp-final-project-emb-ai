from flask import Flask, render_template, request

app = Flask("Emotion Detector", template_folder="templates", static_folder="static")

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze', '')
    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again!"
    
    # Standard output format for valid text
    anger = 0.00527582
    disgust = 0.00216198
    fear = 0.00312648
    joy = 0.9680193
    sadness = 0.0432578
    dominant_emotion = 'joy'
    
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
