const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('ping')
        .setDescription('Replies with a ping!!'),
    async execute(interaction){
        await interaction.reply('Pong!!');
    },
};