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

def gemini_promt(prompt):
    genai.configure(api_key="AIzaSyAzPLDO1k1eFo4JhewPpcwd4VzQUpIce5I")

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return (f"{response.text}")

# Main function
def working(article_index):
    stories = parse_feed(rss_url)
    

    # Check if the specified article index is within the range of available stories
    if len(stories) > article_index:
        selected_story = stories[article_index]  # Get the story at the specified index
        
        # Sender and receiver email
        email = "gcc.news.update.24@gmail.com"  # Your email
        receiver_email = "nexn726@gmail.com"  # Receiver email

        # Email subject
        subject = "GCC News Update"
        

        # Constructing the HTML content for the email with increased normal text size
        html_content = f"""
        <html>
        <body>
            <h1 style="font-weight: bold; font-size: 24px; color:black;">{selected_story.get('title')}</h1>
            <h2 style="font-size: 18px; color:black;">{gemini_promt( f"just give me plain summary without html tags or images,just plain summary from this :{selected_story.get('summary')}.Keep in mind that you shouldn't change a thing from the text given and you should only output the summary without the link or the html tags")}</h2>
            {gemini_promt(f"Give me a 3 paragraph on this topic:{selected_story.get('title')}-keep in mind to mimick the tone of the text as writing a linkedin post about it. -write all paragraph in plain english but put html tags for each paragraphs so that i can use them in code -and include some emojis -include some emojis in each paragraph -You should ONLY Generate paragraph 1,2,3 and nothing more nothing less. -Here is and example: <p>Paragraph 1</p> <p>Paragraph 2</p> <p>Paragraph 3</p> <p>hastags</p> -Your Outputshould be like the example above and include bold where it is needed and keep the font size of the text as 12 and keep hashtags as another paragraph and make this blue color and bold and NOOO hashtags in the first 3 paragraphs and follow the example strictly,nothing more nothing less")}
            <p><b style="font-size: 16px; color:black; ">Read more on this topic:</b><a href="{selected_story.get('link')}" style="font-size: 15px; color:black;">{selected_story.get('link')}</a></p>
            <p style="font-size: 18px; color:black;">{gemini_promt(f"i want to just keep the image of this and remove the text{selected_story.get('summary')}.the out put should be just image and no text")}</p>
            
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
    else:
        print(f"There are less than {article_index + 1} stories in the feed.")

def gemini():
    stories = parse_feed(rss_url)
    genai.configure(api_key="AIzaSyAzPLDO1k1eFo4JhewPpcwd4VzQUpIce5I")

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(f"""choose a story from these {stories} and give the number of the story that 
                                      Highlight Big Numbers/Brands in GCC and and give me an answer of a 
                                      single number,i want that number to be the article number - 1 of what you
                                      chose,Your answer should be no longer than a single digit""")
    print(f"Chosen article no: {response.text}")
    return int(f"{response.text}")

def main():
    article_index = gemini()  # Change this value to choose a different article
    working(article_index)

# Run the script
if __name__ == '__main__':
    main()