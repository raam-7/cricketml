import pandas as pd

# File paths
MATCHES_PATH = "data/raw/matches.csv"
DELIVERIES_PATH = "data/raw/deliveries.csv"


def load_datasets():

    print("Loading datasets...\n")

    matches = pd.read_csv(MATCHES_PATH)
    deliveries = pd.read_csv(DELIVERIES_PATH)

    print("Matches dataset shape:", matches.shape)
    print("Deliveries dataset shape:", deliveries.shape)

    print("\nMatches Columns:")
    print(matches.columns)

    print("\nDeliveries Columns:")
    print(deliveries.columns)

    return matches, deliveries


def merge_datasets(matches, deliveries):

    print("\nMerging datasets...")

    # Adjust columns depending on dataset
    merged_data = deliveries.merge(
        matches[['id', 'venue', 'date']],  # removed season for now
        left_on='match_id',
        right_on='id',
        how='left'
    )

    print("Merged dataset shape:", merged_data.shape)

    return merged_data


if __name__ == "__main__":

    matches, deliveries = load_datasets()

    merged_data = merge_datasets(matches, deliveries)

    print("\nMerged Data Sample:\n")
    print(merged_data.head())