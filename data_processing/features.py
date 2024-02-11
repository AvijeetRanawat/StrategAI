import pandas as pd

# Load the datasets
mc_stats = pd.read_csv('manchester_city_stats.csv')
liverpool_stats = pd.read_csv('liverpool_stats.csv')

# Feature Engineering: Simplify player positions
def simplify_position(pos):
    if 'GK' in pos:
        return 'Goalkeeper'
    elif any(def_pos in pos for def_pos in ['DF', 'LB', 'RB', 'CB']):
        return 'Defender'
    elif 'MF' in pos:
        return 'Midfielder'
    elif any(att_pos in pos for att_pos in ['FW', 'ST', 'LW', 'RW']):
        return 'Forward'
    else:
        return 'Unknown'

mc_stats['Simplified Pos'] = mc_stats['Pos'].apply(simplify_position)
liverpool_stats['Simplified Pos'] = liverpool_stats['Pos'].apply(simplify_position)

# Since detailed defensive metrics and pressures are not available, we focus on the provided metrics
# For advanced metrics like xG and xA, we use 'Expected xG' and 'Expected xA' directly from the data

# Select relevant features for final output
relevant_features = ['Player', 'Simplified Pos', 'Performance Gls', 'Performance Ast', 'Performance PK', 'Performance PKatt', 'Per 90 Minutes Gls', 'Expected xG', 'Per 90 Minutes Ast', 'Per 90 Minutes xG']

# Save the processed data to new CSV files
mc_stats[relevant_features].to_csv('processed_manchester_city_stats.csv', index=False)
liverpool_stats[relevant_features].to_csv('processed_liverpool_stats.csv', index=False)

# Output file paths for download
processed_mc_file_path = 'processed_manchester_city_stats.csv'
processed_liverpool_file_path = 'processed_liverpool_stats.csv'

processed_mc_file_path, processed_liverpool_file_path
