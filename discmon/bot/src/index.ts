import {Channel} from 'diagnostics_channel'
import {
  Interaction,
  MessageActionRow,
  MessageAttachment,
  MessageButton,
  TextBasedChannel,
  TextChannel,
} from 'discord.js'

//require the necessary discord.js classes
const {Client, Intents} = require('discord.js')
const {token} = require('../config.json')
const fetch = require('node-fetch')

console.log('Bot is starting...')

//create a new client instance
const client = new Client({
  intents: [Intents.FLAGS.GUILDS],
})

const row0 = new MessageActionRow().addComponents(
  new MessageButton()
    .setCustomId('blank01')
    .setLabel('     ')
    .setStyle('PRIMARY')
    .setDisabled(true),
  new MessageButton()
    .setCustomId('select')
    .setLabel('select')
    .setStyle('PRIMARY'),
  new MessageButton()
    .setCustomId('blank02')
    .setLabel('     ')
    .setStyle('PRIMARY')
    .setDisabled(true),
  new MessageButton()
    .setCustomId('start')
    .setLabel('start')
    .setStyle('PRIMARY'),
  new MessageButton()
    .setCustomId('blank03')
    .setLabel('     ')
    .setStyle('PRIMARY')
    .setDisabled(true)
)
const row1 = new MessageActionRow().addComponents(
  new MessageButton()
    .setCustomId('blank11')
    .setLabel('     ')
    .setStyle('PRIMARY')
    .setDisabled(true),
  new MessageButton().setCustomId('up').setLabel('  ^   ').setStyle('PRIMARY'),
  new MessageButton()
    .setCustomId('blank12')
    .setLabel('     ')
    .setStyle('PRIMARY')
    .setDisabled(true),
  new MessageButton()
    .setCustomId('blank13')
    .setLabel('     ')
    .setStyle('PRIMARY')
    .setDisabled(true),
  new MessageButton()
    .setCustomId('a_button')
    .setLabel('  A  ')
    .setStyle('PRIMARY')
)
const row2 = new MessageActionRow().addComponents(
  new MessageButton().setCustomId('left').setLabel('  <  ').setStyle('PRIMARY'),
  new MessageButton()
    .setCustomId('blank21')
    .setLabel('      ')
    .setStyle('PRIMARY')
    .setDisabled(true),
  new MessageButton()
    .setCustomId('right')
    .setLabel('  >  ')
    .setStyle('PRIMARY'),
  new MessageButton()
    .setCustomId('blank22')
    .setLabel('     ')
    .setStyle('PRIMARY')
    .setDisabled(true),
  new MessageButton()
    .setCustomId('blank23')
    .setLabel('     ')
    .setStyle('PRIMARY')
    .setDisabled(true)
)
const row3 = new MessageActionRow().addComponents(
  new MessageButton()
    .setCustomId('blank31')
    .setLabel('     ')
    .setStyle('PRIMARY')
    .setDisabled(true),
  new MessageButton()
    .setCustomId('down')
    .setLabel('  v   ')
    .setStyle('PRIMARY'),
  new MessageButton()
    .setCustomId('blank32')
    .setLabel('     ')
    .setStyle('PRIMARY')
    .setDisabled(true),
  new MessageButton()
    .setCustomId('blank33')
    .setLabel('     ')
    .setStyle('PRIMARY')
    .setDisabled(true),
  new MessageButton()
    .setCustomId('b_button')
    .setLabel('  B  ')
    .setStyle('PRIMARY')
)
const buttonRows = [row0, row1, row2, row3]

//When the client is ready, run this code (only once)
client.once('ready', () => {
  console.log('Ready!')
  const row0 = new MessageActionRow().addComponents(
    new MessageButton()
      .setCustomId('blank01')
      .setLabel('     ')
      .setStyle('PRIMARY')
      .setDisabled(true),
    new MessageButton()
      .setCustomId('select')
      .setLabel('select')
      .setStyle('PRIMARY'),
    new MessageButton()
      .setCustomId('blank02')
      .setLabel('     ')
      .setStyle('PRIMARY')
      .setDisabled(true),
    new MessageButton()
      .setCustomId('start')
      .setLabel('start')
      .setStyle('PRIMARY'),
    new MessageButton()
      .setCustomId('blank03')
      .setLabel('     ')
      .setStyle('PRIMARY')
      .setDisabled(true)
  )
  const row1 = new MessageActionRow().addComponents(
    new MessageButton()
      .setCustomId('blank11')
      .setLabel('     ')
      .setStyle('PRIMARY')
      .setDisabled(true),
    new MessageButton()
      .setCustomId('up')
      .setLabel('  ^   ')
      .setStyle('PRIMARY'),
    new MessageButton()
      .setCustomId('blank12')
      .setLabel('     ')
      .setStyle('PRIMARY')
      .setDisabled(true),
    new MessageButton()
      .setCustomId('blank13')
      .setLabel('     ')
      .setStyle('PRIMARY')
      .setDisabled(true),
    new MessageButton()
      .setCustomId('a_button')
      .setLabel('  A  ')
      .setStyle('PRIMARY')
  )
  const row2 = new MessageActionRow().addComponents(
    new MessageButton()
      .setCustomId('left')
      .setLabel('  <  ')
      .setStyle('PRIMARY'),
    new MessageButton()
      .setCustomId('blank21')
      .setLabel('      ')
      .setStyle('PRIMARY')
      .setDisabled(true),
    new MessageButton()
      .setCustomId('right')
      .setLabel('  >  ')
      .setStyle('PRIMARY'),
    new MessageButton()
      .setCustomId('blank22')
      .setLabel('     ')
      .setStyle('PRIMARY')
      .setDisabled(true),
    new MessageButton()
      .setCustomId('blank23')
      .setLabel('     ')
      .setStyle('PRIMARY')
      .setDisabled(true)
  )
  const row3 = new MessageActionRow().addComponents(
    new MessageButton()
      .setCustomId('blank31')
      .setLabel('     ')
      .setStyle('PRIMARY')
      .setDisabled(true),
    new MessageButton()
      .setCustomId('down')
      .setLabel('  v   ')
      .setStyle('PRIMARY'),
    new MessageButton()
      .setCustomId('blank32')
      .setLabel('     ')
      .setStyle('PRIMARY')
      .setDisabled(true),
    new MessageButton()
      .setCustomId('blank33')
      .setLabel('     ')
      .setStyle('PRIMARY')
      .setDisabled(true),
    new MessageButton()
      .setCustomId('b_button')
      .setLabel('  B  ')
      .setStyle('PRIMARY')
  )
  client.channels.fetch('865669995438538756').then((channel: TextChannel) => {
    channel.send({
      content: 'Pokemon Red - Controls!',
      components: buttonRows,
    })
    channel.send({
      content: 'Pokemon Red - Screen!',
    })
  })
})

client.on('interactionCreate', async (interaction: Interaction) => {
  if (!interaction.isButton()) return
  //if one of the button is pressed
  if (
    ['left', 'right', 'up', 'down', 'a_button', 'b_button'].includes(
      interaction.customId
    )
  ) {
    //delete previous messages - this is scuffed
    interaction.channel?.messages.cache.forEach((message) => {
      if (message.content !== 'Pokemon Red - Controls!') {
        message.delete()
      }
    })
    interaction.channel?.messages.cache.clear() //clear cache to not retry deletes
    await interaction.deferReply() //wait for fetch to reply
    const {fileName} = await fetch(
      'http://127.0.0.1:5000/' + interaction.customId.at(0)
    ).then((response: any) => response.json()) //fetch gif from python
    interaction.editReply({
      content: 'Pokemon Red - Screen!',
      files: ['../emulator/' + fileName],
    }) //send message
  }
})

client.login(token)
