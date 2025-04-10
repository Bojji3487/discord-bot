import discord
import os 
import google.genai as genAI

my_secret = os.environ['SECRET_KEY']

class MyClient(discord.Client):
    chat="Message history:\n"
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if  self.user in message.mentions:
            my_prompt=""
            if(message.author!=self):
                self.chat+=(f"Message from {message.author.name}:{message.content}\n")
                my_prompt=f"{self.chat}current prompt:{message.content}\n"
            client= genAI.Client(api_key=os.getenv("GEMINI_API"))

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents="\n"+my_prompt,
            )
            print(my_prompt)
            await message.channel.send(response.text)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(my_secret)