import pandas as pd

def load_gmn_data(file_path):

    df = pd.read_csv(
        file_path,
        sep=";",
        comment="#",
        engine="python"
    )

    df.columns = [c.strip() for c in df.columns]

    print(df.columns)


    return df