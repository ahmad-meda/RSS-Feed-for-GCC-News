# GCC News Email Automation Project

## Project Overview

This project automates the process of sending GCC news updates via email every 24 hours. The script fetches news articles from an RSS feed, summarizes them using Google's Generative AI, and sends the summarized news to a specified recipient.

## Features

- **Fetches News Articles**: Retrieves news articles from a specified RSS feed URL.
- **Summarizes Articles**: Uses Google's Generative AI to generate concise summaries of the news articles.
- **Email Automation**: Sends the summarized news via email to a specified recipient.
- **Scheduled Execution**: Runs the entire process automatically every 24 hours.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3**: Make sure Python 3 is installed on your system.
- **Required Python Packages**:
  - `feedparser`: Used to parse the RSS feed.
  - `smtplib`: Used to send emails.
  - `email`: Used to construct the email content.
  - `google-generativeai`: Used to access Google's Generative AI for summarizing articles.
  - `schedule`: Used to schedule the script to run every 24 hours.

## Installation

Follow these steps to set up and run the project:

1. **Clone the repository**:
   Clone the project repository to your local machine using the following command:
   ```sh
   git clone <repository_url>
   cd <repository_directory>

    ```

## Configuration

1. **RSS Feed URL**: Update the `rss_url` variable with the RSS feed URL you want to use.
2. **Google Gemini API Key**: Replace the placeholder API key with your actual API key from Google Gemini AI.
3. **Email Credentials**: Update the `email` and `receiver_email` variables with the sender and receiver email addresses. Also, replace the email password with your actual password.

## Usage

1. **Main Function**: The `main()` function orchestrates the execution of the script, fetching the news stories, selecting a specific story, generating content, and sending the email.

2. **Parsing the RSS Feed**: The `parse_feed()` function fetches and parses the RSS feed, returning a list of stories.

3. **Generating Content with Gemini AI**: The `gemini_promt()` function interacts with Gemini AI to generate specific content based on the prompt provided.

4. **Selecting Top 5 Articles with Big Headlines and GCC content**: The `gemini()` function uses Gemini AI to choose an article based on specified criteria.

5. **Constructing and Sending the Email**: The `working()` function constructs the email content and sends it.

## Running the Script

Run the script using the command:

```sh
python main.py
