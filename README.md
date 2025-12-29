# Financial-Sentiment-Analysis-Pipeline
Financial News Sentiment Pipeline: FinBERT vs. Market Data

## Project Overview

This project builds an end-to-end NLP pipeline to analyse financial news sentiment using Deep Learning. It ingests live news data from the Alpha Vantage API, processes it using Data Engineering best practices, and analyses it using the FinBERT Transformer model from Hugging Face.

The goal was to audit the performance of semantic sentiment models (FinBERT) against market-grade sentiment labels provided by financial APIs.

## Architecture

The system follows a standard ETL (Extract, Transform, Load) & Inference pattern:

Ingestion Layer: Fetches raw JSON data for multi-sector stocks (Reliance, TCS, HDFC, etc.) via Alpha Vantage.

Processing Layer: Parses nested JSON structures into clean, structured Pandas DataFrames (Silver Layer).

Inference Layer: Implements the "L.P.L.S" pattern to feed news summaries into ProsusAI/finbert.

Validation Layer: Compares the AI's semantic predictions against the API's market labels to calculate an "Agreement Score."

##  Tech Stack

Language: Python

Data Engineering: Pandas, JSON

Deep Learning: Hugging Face Transformers (pipeline), PyTorch

Model: ProsusAI/finbert (BERT fine-tuned on Financial PhraseBank)

API: Alpha Vantage (News & Sentiment Endpoint)

##  Key Results & Insights

We analysed news across multiple sectors (Energy, Tech, Banking).

Agreement Rate: 56%

Insight: The disparity suggests a divergence between Literal Text Sentiment (what FinBERT sees) and Market Context Sentiment (what Alpha Vantage sees).

Conclusion: While FinBERT accurately captures the tone of the text, it lacks the broader market context (e.g., "beating estimates" might be positive even if profits are down). A hybrid approach is recommended for production trading systems.

## Future Improvements

Price Correlation: Merge sentiment data with historical stock prices to test predictive power.

Fine-Tuning: Fine-tune FinBERT on the Alpha Vantage labels to bridge the 44% disagreement gap.

Containerization: Dockerize the pipeline for scheduled runs.
