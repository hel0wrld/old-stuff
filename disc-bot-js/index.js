//including necessary classes
const fs = require('fs');
const { Client, Collection, Intents } = require('discord.js');
const { token } = require('./config.json');

//create client instance 
const client = new Client({intents: [Intents.FLAGS.GUILDS]});

client.commands = new Collection();

//indicating when client is ready
client.once('ready', () => {
    console.log('Ready!');
});

client.on('interactionCreate', async interaction =>{
    if(!interaction.isCommand()){
        await interaction.reply('Invalid Command!');
        return;
    }

    const { commandName } = interaction;

    if(commandName === 'ping') {
        await interaction.reply('Pong!');
    } else if(commandName === 'server')	{
        await interaction.reply(`Server name: ${interaction.guild.name}\nTotal members: ${interaction.guild.memberCount}`);
	} else if (commandName === 'user') {
		await interaction.reply({
            content:`Your tag: ${interaction.user.tag}\nYour id: ${interaction.user.id}`,
            ephemeral: true
        });
    }
});

client.login(token);