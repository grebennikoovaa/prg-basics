import json

def save_voting_data(data):
     file_name = 'voting.json'
     with open(file_name, 'w') as file:
          json.dump(data, file, indent=4) 
          
