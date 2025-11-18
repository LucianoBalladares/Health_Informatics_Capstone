import pandas as pd

def aggregate_chunk_by_region(df, region_col, expansion_col, poverty_col, income_pc_col, educ_col):
    df = df.dropna(subset=[region_col, expansion_col])
    df[expansion_col] = pd.to_numeric(df[expansion_col], errors="coerce")
    df = df.dropna(subset=[expansion_col])

    df["pobreza_pond"] = df[poverty_col] * df[expansion_col]
    df["ingreso_pc_pond"] = df[income_pc_col] * df[expansion_col]
    df["educ_pond"] = df[educ_col] * df[expansion_col]

    grouped = df.groupby(region_col).apply(
        lambda g: pd.Series({
            "pop_weighted": g[expansion_col].sum(),
            "poverty_rate": g["pobreza_pond"].sum() / g[expansion_col].sum(),
            "income_pc_mean": g["ingreso_pc_pond"].sum() / g[expansion_col].sum(),
            "educ_mean": g["educ_pond"].sum() / g[expansion_col].sum()
        })
    )

    grouped.reset_index(inplace=True)
    return grouped