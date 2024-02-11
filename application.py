from flask import Flask, request, jsonify
import openai
import pandas as pd
import os

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = os.getenv('OPENAI_API_KEY')

# Load your CSV data into a DataFrame
team1_data = pd.read_csv(os.path.join('.', 'data', 'team1_stats.csv'))
team2_data = pd.read_csv(os.path.join('.', 'data', 'team2_stats.csv'))

@app.route('/generate-prompt', methods=['POST'])
def generate_prompt():
    # Parse the incoming JSON request
    input_data = request.json

    # Optionally, append data from CSV to your input_data or construct a new object
    # This is a simple example; modify according to your CSV structure and requirements
    appended_data = {
        "input": input_data,
        "team1_data": team1_data.to_dict(orient='records'),  # Convert CSV data to a list of dicts
        "team2_data": team2_data.to_dict(orient='records')
    }

    # Construct your prompt based on the appended_data
    # Modify this according to your specific requirements
    prompt = f'''
    Given the input JSON: 
    `{appended_data['input']}`
    and player wise statistics for Manchester City FC:
    `{appended_data['team1_data']}`
     and player wise statistics for Liverpool:
    `{appended_data['team2_data']}`,
    Game State Strategist is designed to optimize the positioning of Manchester City FC players in live football scenarios, aiming to improve their performance with the ultimate goal of winning the game against Liverpool. It processes input data in a specific JSON format that includes player coordinates, the current score for both teams, ball possession details, and the elapsed time in the match, with Manchester City FC as the home team and Liverpool as the opponent.

    The input JSON schema details player coordinates (with precision up to two decimal places within the range -3.2 < X < 3.2 and -4.4 < Y < 4.4), the current score, ball possession, and the match's elapsed time. Manchester City FC owns Y < 0 area throughout the game and tries to goal in the goal post near Y = 4.4. Utilizing player statistics and history from FBRef for both teams, the strategist provides only an output JSON file with optimized positions for all 11 Manchester City FC players, ensuring the suggestions are realistic and achievable within the next minute. The output coordinates are optimized up to two decimal places. The goalkeeper position is fixed throughout the game. The optimized coordinate should also take care that it is not leading to offside. If the input deviates from the specified schema, an error will be prompted for correction, ensuring accuracy in strategic recommendations.
    Output JSON Schema will look like this:
    {
        "ManchesterCity": {
            "OptimizedCoordinates": {
                "Ederson": [1.97, -3.32],
                "Stefan Ortega": [-2.61, -3.89],
                "Kyle Walker": [-3.04, -3.19],
                "Nathan Aké": [-3.0, -2.57],
                "Phil Foden": [0.78, -0.58],
                "Bernardo Silva": [1.85, 3.03],
                "Rodri": [-0.31, -2.86],
                "Mateo Kovačić": [-2.31, 0.8],
                "Erling Haaland": [-1.35, 3.19],
                "Julián Álvarez": [0.97, 3.88],
                "Jeremy Doku": [-1.02, 4.17]
            }
        }
    }
    Optimize the team's positions. The output should just be a JSON
      '''
    
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
