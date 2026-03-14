import pandas as pd
import os
from data_loader import load_datasets, merge_datasets


OUTPUT_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "processed",
    "player_innings.csv",
)


def create_batsman_innings_dataset():

    print("Creating batsman innings dataset...\n")

    matches, deliveries = load_datasets()

    merged_data = merge_datasets(matches, deliveries)

    innings = merged_data.groupby(
        ['match_id', 'batsman', 'bowling_team', 'venue']
    )['batsman_runs'].sum().reset_index()

    innings.rename(columns={
        'bowling_team': 'opposition',
        'batsman_runs': 'runs'
    }, inplace=True)

    print("Innings dataset shape:", innings.shape)

    return innings


if __name__ == "__main__":

    innings_df = create_batsman_innings_dataset()

    print("\nSample Data:\n")
    print(innings_df.head())

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    innings_df.to_csv(OUTPUT_PATH, index=False)

    print(f"\nDataset saved to {OUTPUT_PATH}")
