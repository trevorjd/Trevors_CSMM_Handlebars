import discord
# Replace with your server ID and channel ID
server_id = SERV_ID  # Replace with your server's ID
channel_id = CHAN_ID  # Replace with the channel ID you want to read messages from

intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent to read messages

client = discord.Client(intents=intents)

# Function to log messages to a file
def log_message_to_file(message):
    with open('player_login_log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{message.content}\n')

@client.event
async def on_ready():
    print('Hello {0.user} !'.format(client))
    await client.change_presence(activity=discord.Game('_scan help'))
    
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')



    server = client.get_guild(server_id)  # Fetch the server
    if server:
        channel = server.get_channel(channel_id)  # Fetch the channel
        if channel:
            # Get the last 10 messages from the channel
            #messages = [history async for history in channel.history(limit=10)]
            #for message in messages:
            #    print(f'{message.author}: {message.content}')
            #    log_message_to_file(message)  # Log each incoming message to the file
            print("Channel found")
        else:
            print("Channel not found!")
    else:
        print("Server not found!")

@client.event
async def on_message(message):
    # To prevent the bot from reading its own messages
    if message.author == client.user:
        return
    if message.channel.id == channel_id:
        print(f'{message.author}: {message.content}')
        log_message_to_file(message)  # Log each incoming message to the file


# Run the bot with your token
client.run('TOKEN')  # Replace with your bot's token

