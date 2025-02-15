import csv
import os
from punt_play2 import punt_play

class lector_data:
    def __init__(self):
        self.data_path = 'c:\\data\\primeraprogramada' if os.name == 'nt' else '/data/primeraprogramada'

    def read_punts(self):
        punt_plays = []
        
        for year in range(2009, 2018):
            filename = os.path.join(self.data_path, f'pbp_{year}.csv')
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    print(f"PROSESSING AÑO-------------------------- {year}...")
                    reader = csv.DictReader(file)
                    for row in reader:
                        if ('punts' in row.get('desc', '').lower() and 
                            'fumble' not in row.get('desc', '').lower()):
                            
                            teams = f"{row.get('AwayTeam', '')}@{row.get('HomeTeam', '')}"
                            
                            punt = punt_play(
                                row.get('GameID'),
                                teams,
                                row.get('Yards.Gained'),
                                row.get('qtr'),
                                row.get('Date'),
                                row.get('time')
                            )
                            punt_plays.append(punt)
                            
            except FileNotFoundError:
                print(f"(ERRRRRRRR) no se encontro archivo para añooo------------ {year}")
                continue
            except Exception as e:
                print(f"(ERRRRRRRR) en leer el año------------------{year}: {str(e)}")
                continue
        
        print(f"TOTAL PUNT ENCONTRADAS--------------------: {len(punt_plays)}")
        return punt_plays