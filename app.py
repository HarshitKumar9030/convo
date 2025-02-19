from flask import Flask, render_template, request, session, jsonify, send_file
from dotenv import load_dotenv
import google.generativeai as genai
import os
import textwrap
import io

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")
app.config['SESSION_TYPE'] = 'filesystem'

model = genai.GenerativeModel('gemini-1.5-flash-latest')

def format_prompt(context):
    prompt_template = textwrap.dedent(f"""
    Generate {context['question_count']} {context['question_type']} questions for a {context['duration']}-month relationship.
    Tone: {context['tone']}
    Complexity: {context['complexity']}
    Interests: {context['interests']}
    Last conversation: {context['last_topic']}
    Custom instructions: {context['custom_prompt']}
    
    Format requirements:
    - Include emojis: {'✅' if context['emojis'] else '❌'}
    - Max question length: {context['max_length']} characters
    - Language: {context['language']}
    
    Make them {context['tone'].lower()} but meaningful. Avoid clichés.
    """)
    return prompt_template

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        context = {
            'duration': request.json.get('duration', 6),
            'tone': request.json.get('tone', 'Playful'),
            'interests': ', '.join(request.json.get('interests', [])),
            'last_topic': request.json.get('last_topic', ''),
            'custom_prompt': request.json.get('custom_prompt', ''),
            'question_count': request.json.get('question_count', 3),
            'question_type': request.json.get('question_type', 'conversational'),
            'complexity': request.json.get('complexity', 'medium'),
            'max_length': request.json.get('max_length', 120),
            'emojis': request.json.get('emojis', True),
            'language': request.json.get('language', 'English')
        }
        
        response = model.generate_content(format_prompt(context))
        result = {
            'questions': response.text,
            'context': context
        }
        
        if 'history' not in session:
            session['history'] = []
        session['history'].append(result)
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    return send_file(
        io.BytesIO(data['text'].encode('utf-8')),
        mimetype='text/plain',
        download_name='conversation_starters.txt',
        as_attachment=True
    )

@app.route('/history', methods=['GET'])
def get_history():
    return jsonify(session.get('history', []))

if __name__ == '__main__':
    app.run(debug=True)