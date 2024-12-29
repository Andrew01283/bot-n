import discord
import os
from model import get_class
import random
import requests
import settings
import webserver 
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='*', intents=intents)
#Funciones
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
def get_pokemon_image_url():    
    url = 'https://pokeapi.co'
    res = requests.get(url)
    data = res.json()
    return data['url']
def get_pokemon_image_url():    
    url = 'https://pokeapi.co'
    res = requests.get(url)
    data = res.json()
    return data['url']

#ni idea
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
#Comandos 
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

    
@bot.command()
async def ignorancia(ctx):
    await ctx.send(f"""Hola, soy un bot {bot.user}!
Te explicaré el problema de la ignorancia globalizada y sus peligros
para nuestra sociedad""")
    await ctx.send(f"""La globalización de la ignoracia y su normalización es un problema
que ataca a nuestra sociedad y más que todo a nuestra juventud 
el peligro de esto es que cada vez son más suceptibles a la manipulación y en un
sentido más filosófico perdemos nuestro valor al perder parte de nuestra voluntad
entonces ¿Cómo podemos mejorar este problema?""")
    await ctx.send(f"""¿Quieres saber más?""")
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['Si', 'si', 'no', 'No']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content in ['Si', 'si']:
            await ctx.send(f"""Vale me alegra que te interese. Para convatir este problema
lo mejor es desarrollar un criterio propio y critico, pero ¿Cómo hacemos esto?
La mejor manera de hacerlo es mediante la educación pues la mejor manera
de combatir la ignorancia y el hedonismo es mediante la educación. Ejemplos: 
Leyendo. Leer sobre todo es una gran manera de educarse pues en un libro
no vemos solo su contenido si no parte de la visión del autor y a partir de las 
diferentes opiniones se puede debatir y formar unn criterio propio... Y bueno Master
hasta aquí, no sé que más decirte. """)
        elif response.content in ['No', 'no']:
            await ctx.send(f"""Pos me da igual man el. hedonismo es lo peor. Para combatir este problema
lo mejor es desarrollar un criterio propio y critico, pero ¿Cómo hacemos esto?
La mejor manera de hacerlo es mediante la educación pues la mejor manera
de combatir la ignorancia y el hedonismo es mediante la educación. Ejemplos: 
Leyendo. Leer sobre todo es una gran manera de educarse pues en un libro
no vemos solo su contenido si no parte de la visión del autor y a partir de las 
diferentes opiniones se puede debatir y formar unn criterio propio... Y bueno Master
hasta aquí, no sé que más decirte. """)
        else:
            await ctx.send(f"""Lo siento no entiendo tu mensaje""")

@bot.command()
async def mem(ctx):
    imagenes = os.listdir('images')
    with open(f'images/{random.choice(imagenes)}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)
@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)
@bot.command('pokemon')
async def pokemon(ctx):
    image_url = get_pokemon_image_url()
    await ctx.send(image_url)
#@bot.command()
#async def check(ctx):
    #if ctx.message.attachments:
        #for attachment in ctx.message.attachments:
            #file_name = attachment.filename
            #file_url = attachment.url
            #await attachment.save(f"./{attachment.filename}")
            #await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    #else:
       # await ctx.send("You forgot to upload the image :(")

webserver.keep_alive()
bot.run("DISCORD TOKEN")
