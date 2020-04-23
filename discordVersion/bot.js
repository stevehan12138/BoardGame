require('dotenv').config();

const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});

client.login('NzAyNjgwNDg0OTU3NjUxMDE3.XqDuiA.inCIPKrPq9x6kb3vv7zbFH3EJxQ');