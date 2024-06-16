# GCC News Update Email Script

This Python script fetches news stories from an RSS feed, processes the stories, and sends an email with the selected story in a structured format. The script utilizes Google's Gemini AI for generating text content.

## Features

- Fetches news stories from a specified RSS feed.
- Selects a specific story based on criteria provided to Gemini AI.
- Generates a LinkedIn-style post using Gemini AI.
- Sends an email with the structured news story content.

## Requirements

- Python 3.x
- The following Python libraries:
  - `feedparser`
  - `smtplib`
  - `email.mime.multipart`
  - `email.mime.text`
  - `google.generativeai`

## Installation

1. Install Python 3.x from the official website: [Python.org](https://www.python.org/).
2. Install the required Python libraries using pip:

    ```sh
    pip install feedparser smtplib google-generativeai
    ```

## Configuration

1. **RSS Feed URL**: Update the `rss_url` variable with the RSS feed URL you want to use.
2. **Google Gemini API Key**: Replace the placeholder API key with your actual API key from Google Gemini AI.
3. **Email Credentials**: Update the `email` and `receiver_email` variables with the sender and receiver email addresses. Also, replace the email password with your actual password.

## Usage

1. **Main Function**: The `main()` function orchestrates the execution of the script, fetching the news stories, selecting a specific story, generating content, and sending the email.

2. **Parsing the RSS Feed**: The `parse_feed()` function fetches and parses the RSS feed, returning a list of stories.

3. **Generating Content with Gemini AI**: The `gemini_promt()` function interacts with Gemini AI to generate specific content based on the prompt provided.

4. **Selecting an Article**: The `gemini()` function uses Gemini AI to choose an article based on specified criteria.

5. **Constructing and Sending the Email**: The `working()` function constructs the email content and sends it.

## Running the Script

Run the script using the command:

```sh
python main.py
