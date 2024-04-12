TOKEN = "Token here"

# import discord things to create the bot
import discord # main package
from discord.ext import commands # package for the commands

# import to create data model
from pydantic import BaseModel
# import to get requests/posts
import requests
# import json to read data from ai
import json
# import log to create logs
import logging


log = logging.getLogger(__name__)
 
# function to initialize the bot
def init_bot ():
    # create bot and set ! for the commands prefixes
    client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

    # create a event
    @client.event
    async def on_ready () : # when bot is ready
        # set bot status
        await client.change_presence(
            activity=discord.activity.Game(name="nothing"), 
            status=discord.Status.online
        )
        # print the bot is on
        print("started bot")

    # create a command
    @client.command()
    async def ask(ctx, *arg): # on tap "!ask something" do 

        # create a model to data
        class GenerateRequest(BaseModel):
            model: str = "llama2"
            prompt: str
            stream: bool = False

        # url to make a post to get data
        url = 'http://localhost:11434/api/generate'
        # data to send to ai
        data = GenerateRequest(prompt=" ".join(arg))

        # data receibt
        response_dict = requests.post(url, json=data.dict())
        print ("asked to ai")
        # get on ai response in json
        response_string = json.loads(response_dict.text)["response"]
        print("received info from ai")
        # send to discord the answer from ai
        await ctx.send(response_string)
        print("sended to discord ")

    # run bot
    client.run (TOKEN)
    pass
