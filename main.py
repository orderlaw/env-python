# First install the dotenv via terminal
# Also install os via terminal
# Then import the them as follows-
import os
from dotenv import load_dotenv, find_dotenv

# Now use the code given below to find the .env file in your project folder.
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Now finally call the TOKEN you put inside the .env file.
token = os.getenv("TOKEN")

# In my case I'm giving an example of discord bot so you can use the token as follows-
client.run(token)
