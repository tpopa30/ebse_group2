# EBSE Group 2 2025 Assignment 1

This repository contains the replication package for the EBSE Group 2 2025 Assignment 1. The purpose of this assignment was to conduct a Rapid Review on a selected research topic. Our chosen title was: "How can we measure and optimize the energy efficiency of containerised software applications in the cloud?". 

The research questions are:

1. Which methods have been used to measure power usage of containerized cloud applications?
2. What are the limitations of the existing methods for measuring power usage of containerized
cloud applications?
3. What techniques are used to manage or reduce power usage in containerized cloud environ-
ments?

## Repository Structure

This repository contains the components required to replicate each step of our rapid review protocol:

- `queries/`: Contains the search queries used for different digital libraries.
- `deduplication/`: Script used data to combine the search results and remove duplicates.
- `charts/`: Contains visualizations and charts generated from the review.

## Data Extraction and Synthesis Data

The data extraction and synthesis data can be found in the following Google Sheets document: https://docs.google.com/spreadsheets/d/1aUp_-yyHUlnr-ZvdusXgXX-UlS2MVr46YGXwOz2sY6M/edit?usp=sharing

The sheet is split into the following main tabs:
1. `initial_paper_list_with_relevance`: Contains the initial list of papers gathered and the relevance for both screening stages.
2. `final_papers`: This tab contains the final list of papers included after the full-text screening along with IDs to match the data extraction sheet.
3. `quality_assessment`: Contains the quality assessment results for each paper.
4. `data_extraction`: Contains the extracted data for each paper based on our data extraction
5. Other paper: There are a number of other tabs which contain synthesised data and notes used to create the charts in our report.

## How to Use

We used Python for our script and used UV for package management. To run the scripts to the following:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using UV:

```bash
uv sync
```

4. Run the deduplication script:

```bash
uv run ./deduplication/deduplicate.py
```

4. Conduct the data extraction and synthesis as per the protocol outlined in our report.

5. Once data has been gathered, add it to the chart script and run it to generate visualizations:

```bash
uv run ./charts/charts.py
```
