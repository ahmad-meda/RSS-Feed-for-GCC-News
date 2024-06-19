import time
import schedule
import feedparser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import google.generativeai as genai

# RSS Feed URL
rss_url = 'https://rss.app/feeds/cFyjvn2nT3BgFBlv.xml'

# Function to parse the RSS feed
def parse_feed(url):
    feed = feedparser.parse(url)
    stories = []
    for entry in feed.entries:
        story = {
            'title': entry.title,
            'link': entry.link,
            'summary': entry.summary,
            'image': entry.get('media_content')[0]['url'] if 'media_content' in entry else None  # Example for getting image URL, adjust based on actual feed structure
        }
        stories.append(story)
    return stories

def gemini_prompt(prompt):
    genai.configure(api_key="AIzaSyAzPLDO1k1eFo4JhewPpcwd4VzQUpIce5I")  # Replace with your actual API key

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

# Main function
def working(article_list):
    stories = parse_feed(rss_url)

    # Sender and receiver email
    email = "gcc.news.update.24@gmail.com"  # Your email
    receiver_email = "ahmad04.meda@gmail.com"  # Receiver email

    # Email subject
    subject = "GCC Headlines Report"

    # Generate a short summary for the top articles
    summary_prompt = "Generate a short, two-line intro to the news articles chosen, and make sure you only give back plain text. Make sure the text goes like this: 'Due to the world of business in turmoil, here are some headlines...' Tailor this statement to look professional and accurate, don't copy the exact same thing, write it like an introduction and make it 2 or 3 sentences and the output should be plain english.\n"
    for index in article_list:
        if len(stories) > index:
            summary_prompt += f"{stories[index]['title']}\n"
    summary_text = gemini_prompt(summary_prompt)

    # Constructing the HTML content for the email
    html_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; color: #000;">
        <h1 style="font-weight: bold; font-size: 30px; color:#000;">GCC Headlines Report</h1>
        <hr style="border: 1px solid #000;">
        <p style="font-size: 15px; color:#000;">{summary_text}</p>
        <table style="width: 100%; border-collapse: collapse;">
    """

    for idx, index in enumerate(article_list):
        if len(stories) > index:
            selected_story = stories[index]  # Get the story at the specified index

            title = selected_story['title']
            summary = gemini_prompt(f"Summarize this text in one paragraph and cut off abruptly to create suspense: {selected_story['summary']}")
            image = selected_story['image']
            link = selected_story['link']
            bg_color = "#f2f2f2" if idx % 2 == 0 else "#ffffff"  # Alternating row colors

            html_content += f"""
            <tr style="background-color: {bg_color};">
                <td style="width: 150px; vertical-align: top; padding: 10px;">
                    <img src="{image}" alt="Story Image" style="width:100%; height:auto; border-radius: 8px;">
                </td>
                <td style="vertical-align: top; padding: 10px 15px;">
                    <h2 style="font-size: 18px; color:#000; margin: 0;"><a href="{link}" style="text-decoration: none; color: #000;">{title}</a></h2>
                    <p style="font-size: 15px; color:#555; margin: 0;">{summary}</p>
                </td>
            </tr>
            """

    html_content += """
        </table>
        <p style="font-size: 15px; color:#000; margin: 20px 0 0 0;"><b>Read more about this:</b> <a href="https://gulfnews.com/business" style="text-decoration: none; color: #000;">https://gulfnews.com/business</a></p>
    </body>
    </html>
    """

    # Print the message for debugging
    print(html_content)

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(html_content, 'html'))

    # Send the email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, "zacltknhfrcteuxg")  # Replace with your actual email password
        server.send_message(msg)
        server.quit()
        print("Email sent successfully to " + receiver_email)
    except Exception as e:
        print(f"Failed to send email: {e}")

def gemini():
    stories = parse_feed(rss_url)
    genai.configure(api_key="AIzaSyAzPLDO1k1eFo4JhewPpcwd4VzQUpIce5I")  # Replace with your actual API key

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(f"""choose 5 story from these {stories} and give the numbers of the stories that 
                                      Highlight Big Numbers/Brands in GCC and and give me an answer in form of a python list,i want that number to be the article number - 1 of what you
                                      chose, Your answer should be only a python list of 5 numbers ,example:[1,2,3,4,5]. that should be your only output.""")
    print(f"Chosen article no: {response.text}")
    return eval(response.text)  # Convert the response text to a Python list

def main():
    article_list = gemini()  # Get the list of article indices
    working(article_list)
    
    
# Run the script
if __name__ == '__main__':
    main()


# # Schedule the job
# schedule.every(24).hours.do(main)

# # Run the scheduler
# while True:
#     schedule.run_pending()
#     time.sleep(1)

