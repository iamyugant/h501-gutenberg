import pandas as pd


AUTHORS_URL = (
    "https://raw.githubusercontent.com/rfordatascience/"
    "tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
)

METADATA_URL = (
    "https://raw.githubusercontent.com/rfordatascience/"
    "tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv"
)


def load_gutenberg() -> pd.DataFrame:
    """Load and merge Gutenberg authors with metadata.

    Returns
    -------
    pandas.DataFrame
        A merged DataFrame containing author and book metadata
        joined on ``gutenberg_author_id``.
    """
    gutenberg_authors = pd.read_csv(AUTHORS_URL)
    gutenberg_metadata = pd.read_csv(METADATA_URL)

    df = pd.merge(
        gutenberg_authors,
        gutenberg_metadata,
        on="gutenberg_author_id",
        how="inner",
    )

    return df
