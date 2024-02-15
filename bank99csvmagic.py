import pandas as pd
import sys

def process_csv(input_csv, output_csv):

    df = pd.read_csv(input_csv, sep=';', encoding='cp1252')
    
    df['Soll'] = df['Soll'].astype(str).str.replace('.', '')
    df['Haben'] = df['Haben'].astype(str).str.replace('.', '')
    
    df['Soll'] = df['Soll'].astype(str).str.replace(',', '.')    
    df['Haben'] = df['Haben'].astype(str).str.replace(',', '.')
    
    df['Soll'] = pd.to_numeric(df['Soll'], errors='coerce').fillna(0)
    df['Haben'] = pd.to_numeric(df['Haben'], errors='coerce').fillna(0)
    
    df['Betrag'] =  df['Haben'] - df['Soll'] 
    df['Betrag'] =  df['Betrag'].astype(str).str.replace('.',',')

    df.to_csv(output_csv, index=False, sep=';', encoding='cp1252')
    print(f"ouput saved as '{output_csv}'")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_csv_path> <output_csv_path>")
        sys.exit(1)
    
    input_csv = sys.argv[1]
    output_csv = sys.argv[2]
    process_csv(input_csv, output_csv)
