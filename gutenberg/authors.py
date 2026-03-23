from gutenberg.data import load_gutenberg


def list_authors(by_languages: bool = True, alias: bool = True) -> list:
    """
    Return a list of author aliases sorted by number of appearances.

    The function loads the Gutenberg dataset, removes rows with missing
    alias or language values, groups by alias, and returns the aliases
    sorted from most frequent to least frequent.

    Returns
    -------
    list
        A list of author aliases sorted by frequency (descending).
    """
    df = load_gutenberg()

    alias_counts = (
        df.dropna(subset=["alias", "language"])
        .groupby("alias")
        .size()
        .sort_values(ascending=False)
    )

    return alias_counts.index.tolist()




