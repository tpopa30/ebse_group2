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
