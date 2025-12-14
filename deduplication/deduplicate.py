import pandas as pd
import bibtexparser

# Loading the data as CSV
df_ieee = pd.read_csv("ieee.csv")
df_scopus = pd.read_csv("scopus.csv")

# Forced to parse bib file as ACM only allows export in BIB format
with open("acm.bib", encoding="utf-8") as f:
    bibdb = bibtexparser.load(f)

df_acm = pd.DataFrame(bibdb.entries)

# Normalizing column names across dataframes
df_ieee = df_ieee.rename(columns={
    "Document Title": "title",
    "Authors": "authors",
    "Publication Year": "year",
    "Publication Title": "source",
    "DOI": "doi"
})

df_scopus = df_scopus.rename(columns={
    "Title": "title",
    "Authors": "authors",
    "Year": "year",
    "Source title": "source",
    "DOI": "doi"
})

df_acm = df_acm.rename(columns={
    "title": "title",
    "author": "authors",
    "year": "year",
    "journal": "source",
    "doi": "doi"
})

df_acm = df_acm[["title", "authors", "year", "source", "doi"]]

# Normalizing title and doi for comparison 
for df in (df_ieee, df_scopus, df_acm):
    df["doi"] = df["doi"].astype(str).str.strip().str.lower()
    df["title"] = df["title"].astype(str).str.strip().str.lower()

# Add source repository for each paper
df_ieee["source_dataset"] = "IEEE"
df_scopus["source_dataset"] = "Scopus"
df_acm["source_dataset"] = "ACM"

# Combine everything into one dataframe
combined = pd.concat(
    [df_ieee, df_scopus, df_acm],
    ignore_index=True
)

# Deduplicate using DOI and then deduplicate again using title
combined = combined.drop_duplicates(subset="doi", keep="first")
combined = combined.drop_duplicates(subset="title", keep="first")

# Keep only relevant columns
final = combined[[
    "title",
    "authors",
    "year",
    "source",
    "source_dataset"
]]

final.to_csv("merged_unique.csv", index=False)