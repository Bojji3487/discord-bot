import discord
import os 

my_secret = os.environ['SECRET_KEY']

appId= 1359529744479162643
publicKey= "e0ecfbac052930657eb33356661b5ec06330f6c0452ca624feb367c3f64ee32f"

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if "tellme" in message.content:
            import google.generativeai as genai
            my_prompt=message.content
            genai.configure(api_key=os.getenv("GEMINI_API"))

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=my_prompt,
            )
            await message.channel.send(response.text)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(my_secret)