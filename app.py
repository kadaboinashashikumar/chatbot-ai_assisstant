from flask import Flask, render_template, request, jsonify
import os
from openai import OpenAI

client = OpenAI()

app = Flask(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Set the key


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_task', methods=['POST'])
def process_task():
    try:
        data = request.get_json()
        task = data.get('task')
        persona = data.get('persona')
        format_ = data.get('format')
        style = data.get('style')
        detail = data.get('detail')
        size = data.get('size')
        additional_instructions = data.get('additional', '')

        prompt = f"""
        You are a highly skilled {persona}, and your goal is to provide a detailed, thoughtful response that aligns with the user's requirements. Please adhere to the following guidelines to ensure the response meets expectations:

        1. **Role**: Your persona for this task is that of a {persona}.
        2. **Output Format**: The response should be in the form of {format_}. Ensure that it is structured according to this format.
        3. **Tone & Style**: Write in a {style} manner, suitable for the given audience and context.
        4. **Level of Explanation**: The level of detail should be {detail}.
        5. **Output Size**: The response should be approximately {size} words in length.
        6. **Additional Instructions**: {additional_instructions}

        User's question: "{task}"
        """
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
        )

        answer = response.choices[0].message.content

        return jsonify({'answer': answer})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
