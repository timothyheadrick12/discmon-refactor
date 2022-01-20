import {Client} from 'discord.js'
import ready from './listeners/ready'

const token = 'ODYxOTk4MTEzNzEwOTMxOTY4.YOR8TQ.nkepaU8wSkM_u7EBjXZZqbjd880'

console.log('Bot is starting...')

const client = new Client({
  intents: [],
})

ready(client)

client.login(token)
