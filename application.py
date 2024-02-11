from flask import Flask, request, jsonify
import openai
import pandas as pd
import os
import json

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/generate-prompt', methods=['POST'])
def generate_prompt():
    # Parse the incoming JSON request

    # Construct your prompt based on the appended_data
    # Modify this according to your specific requirements
    
    input_json = request.json
    # Load your CSV data into a DataFrame
    team1_data = pd.read_csv(os.path.join('.', 'data', 'team1_stats.csv'))
    team2_data = pd.read_csv(os.path.join('.', 'data', 'team2_stats.csv'))
    team1_data = team1_data.to_dict(orient='records')
    team2_data = team2_data.to_dict(orient='records')

    # Constructing the prompt in parts
    prompt_part1 = (
        "Given the input JSON: "
        f"`{input_json}` "
        "and player wise statistics for Manchester City FC: "
    )

    prompt_part2 = f"`{team1_data}` and player wise statistics for Liverpool: `{team2_data}`, "

    prompt_part3 = (
        "Game State Strategist is designed to optimize the positioning of Manchester City FC players in live football scenarios, aiming to improve their performance with the ultimate goal of winning the game against Liverpool. It processes input data in a specific JSON format that includes player coordinates, the current score for both teams, ball possession details, and the elapsed time in the match, with Manchester City FC as the home team and Liverpool as the opponent."
    )

    prompt_part4 = (
        "The input JSON schema details player coordinates (with precision up to two decimal places within the range -3.2 < X < 3.2 and -4.4 < Y < 4.4), the current score, ball possession, and the match's elapsed time. Manchester City FC owns Y < 0 area throughout the game and tries to goal in the goal post near Y = 4.4. Utilizing player statistics and history from FBRef for both teams, the strategist provides only an output JSON file with optimized positions for all 11 Manchester City FC players, ensuring the suggestions are realistic and achievable within the next minute. The output coordinates are optimized up to two decimal places. The goalkeeper position is fixed throughout the game. The optimized coordinate should also take care that it is not leading to offside. If the input deviates from the specified schema, an error will be prompted for correction, ensuring accuracy in strategic recommendations."
    )

    prompt_part5 = (
        "Output JSON Schema will look like this: "
        "{"
        "    \"ManchesterCity\": {"
        "        \"OptimizedCoordinates\": {"
        "            \"Ederson\": [1.97, -3.32],"
        "            \"Stefan Ortega\": [-2.61, -3.89],"
        "            \"Kyle Walker\": [-3.04, -3.19],"
        "            \"Nathan Ake\": [-3.0, -2.57],"
        "            \"Phil Foden\": [0.78, -0.58],"
        "            \"Bernardo Silva\": [1.85, 3.03],"
        "            \"Rodri\": [-0.31, -2.86],"
        "            \"Mateo Kovacic\": [-2.31, 0.8],"
        "            \"Erling Haaland\": [-1.35, 3.19],"
        "            \"Julian Alvarez\": [0.97, 3.88],"
        "            \"Jeremy Doku\": [-1.02, 4.17]"
        "        }"
        "    }"
        "}"
        " Optimize the team's positions. The output should just be a JSON"
    )

    # Combine all parts to form the final prompt
    prompt = prompt_part1 + prompt_part2 + prompt_part3 + prompt_part4 + prompt_part5

    messages = [{"role": "user", "content": prompt}]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-0125-preview",  # Specify the GPT-4 model
            messages=messages,
            max_tokens=500,
            temperature=1,
            top_p=1,
        )

        # Extract the text response and return it in JSON format
        response_str = response.choices[0].message.content.strip()
        # Remove the code block syntax and correct escaping

        text_response = response_str.lstrip("```json").rstrip("```")
        text_response = text_response.replace('\n', '')

        text_response = json.loads(text_response)

        return jsonify(text_response)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
