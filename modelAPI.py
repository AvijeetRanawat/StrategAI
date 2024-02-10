from flask import Flask, request, jsonify
import openai
import pandas as pd
import os

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = os.getenv('OPENAI_API_KEY')

# Load your CSV data into a DataFrame
csv_data = pd.read_csv('players.csv')

@app.route('/generate-prompt', methods=['POST'])
def generate_prompt():
    # Parse the incoming JSON request
    input_data = request.json

    # Optionally, append data from CSV to your input_data or construct a new object
    # This is a simple example; modify according to your CSV structure and requirements
    appended_data = {
        "input": input_data,
        "csv_data": csv_data.to_dict(orient='records')  # Convert CSV data to a list of dicts
    }

    # Construct your prompt based on the appended_data
    # Modify this according to your specific requirements
    prompt = f'''Given the input {appended_data['input']} and additional data {appended_data['csv_data']},
      what should be the positions of the players. give results in json format'''
    
    messages = [{"role": "user", "content": prompt}]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-0125-preview",  # Specify the GPT-4 model
            messages=messages,
            max_tokens=60,
            temperature=1,
            top_p=1,
        )

        # Extract the text response and return it in JSON format
        text_response = response.choices[0].message.content.strip()
        return jsonify({"response": text_response})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
