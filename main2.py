import bot
import praw
import openai

if __name__ == '__main__':
     bot.run_discord_bot(token="")

reddit = praw.Reddit(client_id = "",
                    client_secret = "",
                    username = "",
                    password = "",
                    user_agent = "")

openai.api_key = "YOUR_KEY"