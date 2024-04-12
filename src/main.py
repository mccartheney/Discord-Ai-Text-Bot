import click
from bot import init_bot

@click.group()
def functionalities () :
    pass

@functionalities.group()
def bot () :
    init_bot()

@bot.command() 
def start () :    
    pass


if __name__ == "__main__" :
    functionalities()
