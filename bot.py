import discord
import openai

openai.api_key = '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'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/gpt'):
        user_input = message.content[5:]
        response = await generate_response(user_input)
        await message.channel.send(response)

async def generate_response(user_input):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        temperature=0.7,
        max_tokens=900
    )
    return response.choices[0].text.strip()

client.run("MTEyNTUyMzE5NTIyNzc5OTcxNg.GpLc5W.sL2Yx3h0qdQCHa8dTfsNOEFVyh1uuvVBFCdKfs")