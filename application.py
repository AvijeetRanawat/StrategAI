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
        "The input JSON schema details player coordinates (with precision up to two decimal places within the range -3.2 < X < 3.2 and -4.4 < Y < 4.4), the current score, ball possession, and the match's elapsed time. Manchester City FC owns Y < 0 area throughout the game and tries to goal in the goal post near Y = 4.4. Utilizing player statistics and history from FBRef for both teams, the strategist provides only an output JSON file with optimized positions for all 11 Manchester City FC players, ensuring the suggestions are realistic and achievable within the next minute, hence make sure that the optimized coordinates are within the range of radius of 1.5 from their original coordinates. Also, pay attention to the player who possesses the ball and optimize the coordinates accordingly. The output coordinates are optimized up to two decimal places. The goalkeeper position is fixed throughout the game. The optimized coordinate should also take care that it is not leading to offside. If the input deviates from the specified schema, an error will be prompted for correction, ensuring accuracy in strategic recommendations."
    )

    prompt_part5 = (
        "Output JSON Schema will look like this: "
        "{"
        "    \"ManchesterCity\": {"
        "        \"OptimizedCoordinates\": ["
        "            {"
        "                \"name\": \"Ederson\""
        "                \"Coordinates\": ["
        "                    1.97"
        "                    -3.32"
        "                ]"
        "            }"
        "            {"
        "                \"name\": \"Stefan Ortega\""
        "                \"Coordinates\": ["
        "                    -2.61"
        "                    -3.89"
        "                ]"
        "            }"
        "            {"
        "                \"name\": \"Kyle Walker\""
        "                \"Coordinates\": ["
        "                    -3.04"
        "                    -3.19"
        "                ]"
        "            }"
        "            {"
        "                \"name\": \"Nathan Ake\""
        "                \"Coordinates\": ["
        "                    -3.0"
        "                    -2.57"
        "                ]"
        "            }"
        "            {"
        "                \"name\": \"Phil Foden\""
        "                \"Coordinates\": ["
        "                    0.78"
        "                    -0.58"
        "                ]"
        "            }"
        "            {"
        "                \"name\": \"Bernardo Silva\""
        "                \"Coordinates\": ["
        "                    1.85"
        "                    3.03"
        "                ]"
        "            }"
        "            {"
        "                \"name\": \"Rodri\""
        "                \"Coordinates\": ["
        "                    -0.31"
        "                    -2.86"
        "                ]"
        "            }"
        "            {"
        "                \"name\": \"Mateo Kovacic\""
        "                \"Coordinates\": ["
        "                    -2.31"
        "                    0.8"
        "                ]"
        "            }"
        "            {"
        "                \"name\": \"Erling Haaland\""
        "                \"Coordinates\": ["
        "                    -1.35"
        "                    3.19"
        "                ]"
        "            }"
        "            {"
        "                \"name\": \"Julian Alvarez\""
        "                \"Coordinates\": ["
        "                    0.97"
        "                    3.88"
        "                ]"
        "            }"
        "            {"
        "                \"name\": \"Jeremy Doku\""
        "                \"Coordinates\": ["
        "                    -1.02"
        "                    4.17"
        "                ]"
        "            }"
        "        ]"
        "    }"
        "}"
        " Optimize the team's positions. The output should just be a JSON"
    )

    # Combine all parts to form the final prompt
    prompt = prompt_part1 + prompt_part2 + prompt_part3 + prompt_part4 + prompt_part5

    # messages = [{"role": "user", "content": prompt}]
    # try:
    #     response = openai.ChatCompletion.create(
    #         model="gpt-4-0125-preview",  # Specify the GPT-4 model
    #         messages=messages,
    #         max_tokens=500,
    #         temperature=1,
    #         top_p=1,
    #     )

    #     # Extract the text response and return it in JSON format
    #     response_str = response.choices[0].message.content.strip()
    #     # Remove the code block syntax and correct escaping

    #     text_response = response_str.lstrip("```json").rstrip("```")
    #     text_response = text_response.replace('\n', '')

    #     text_response = json.loads(text_response)


    text_response = {
        "ManchesterCity": {
            "OptimizedCoordinates": [
                {
                    "name": "Bernardo Silva",
                    "Coordinates": [
                        2.2,
                        -0.5
                    ]
                },
                {
                    "name": "Ederson",
                    "Coordinates": [
                        0.0,
                        0.0
                    ]
                },
                {
                    "name": "Erling Haaland",
                    "Coordinates": [
                        -0.5,
                        1.5
                    ]
                },
                {
                    "name": "Jeremy Doku",
                    "Coordinates": [
                        -0.3,
                        2.4
                    ]
                },
                {
                    "name": "Julian Alvarez",
                    "Coordinates": [
                        0.97,
                        3.88
                    ]
                },
                {
                    "name": "Kyle Walker",
                    "Coordinates": [
                        1.1,
                        -1.7
                    ]
                },
                {
                    "name": "Mateo Kovacic",
                    "Coordinates": [
                        -1.5,
                        -1.3
                    ]
                },
                {
                    "name": "Nathan Ake",
                    "Coordinates": [
                        -0.8,
                        -2.4
                    ]
                },
                {
                    "name": "Phil Foden",
                    "Coordinates": [
                        0.45,
                        -1.2
                    ]
                },
                {
                    "name": "Rodri",
                    "Coordinates": [
                        0.2,
                        -2.1
                    ]
                },
                {
                    "name": "Stefan Ortega",
                    "Coordinates": [
                        -2.61,
                        -3.89
                    ]
                }
            ]
        }
    }


    return jsonify(text_response)

    # except Exception as e:
    #     return jsonify({"error": str(e)})

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=5000)