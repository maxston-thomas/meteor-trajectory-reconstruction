import pandas as pd
import glob

files = glob.glob("Data/New folder/traj_summary_*.txt")

dfs = []

for f in files:
    df = pd.read_csv(f, delimiter=";", comment="#")
    dfs.append(df)

combined = pd.concat(dfs)

combined.to_csv("Data/gmn_combined.txt", index=False)

print("Total meteors:", len(combined))