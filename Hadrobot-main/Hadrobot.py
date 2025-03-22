#Setup
import re
import os
import discord
import random 

#Safe token storage
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

#What can this bad boy work with
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.guilds = True
client = discord.Client(intents=intents)

#Global variables
lastSentMessageID = None
lastMessagedChannelID = None

#Bot has booted message
@client.event
async def on_ready():
    print('Hadrobot, Ready to Rock')


#Observes sent messages
@client.event
async def on_message(message):
    #safety measure for testing
    #if message.author.id != 255040778592583681:
       # return

    #ignores own messages except for id
    if message.author == client.user:
        global lastSentMessageID
        global lastMessagedChannelID
        lastSentMessageID = message.id
        lastMessagedChannelID = message.channel
        return
    
    if re.search('trilobite', message.content.lower()):
        await message.channel.send('shoe')
        return
    
    #quiet, my love
    if re.search(r'(?=.*hadro)((?=.*quiet)|(?=.*hush))', message.content.lower()):
        msg = await lastMessagedChannelID.fetch_message(lastSentMessageID)
        if re.search('(?=.*shoe)(?=.*thesaurus)', msg.content.lower()):
            await message.channel.send('nuh uh')
        else:
            await msg.delete()
        return

    #THE FINAL. IS NOT. OPEN. NOTE!!!!
    if re.search('(?=.*open)(?=.*note)', message.content.lower()):
        await message.channel.send('The midterms and the final are not open note! \nHowever, weekly quizzes are.')
        return
    
    #That's a no-no word
    if re.search('asshole|bastard|bitch|cock|cunt|dick|fuck|goddamn|piss|retard|shit|slut', message.content.lower()):
        await message.channel.send('Language!')
                                   # \n \n 1. Keep everything "work-safe".  That means no profanity, ' \
                                   #'no insults, nothing "adult".  Don\'t post or say anything here that ' \
                                   #'you wouldn\'t want Dr. Martin (or your parents) to see.')
        return
        
    #Prints exam date info
    if re.search('((?=.*when)|(?=.*date))((?=.*final)|(?=.*midterm)|(?=.*exam))', message.content.lower()):
        whenexam = ''
        with open('examdates.txt') as datesFile:
            for line in datesFile:
                whenexam = whenexam + line
        await message.channel.send(whenexam)
        return

    #Pulls up the FAQ
    if re.search(r'(midterm|final|exam).*\?|.*\?(midterm|final|exam)|faq', message.content.lower()):
        await message.channel.send('FAQ for exams:')
        faq = ''
        with open('FAQ.txt') as faqFile:
            for line in faqFile:
                faq = faq + line
        await message.channel.send(faq)
        return
    
    #Prints out capabilities
    if message.content == 'hadro help':
        capabilities = ''
        with open('functions.txt') as functionsFile:
            for line in functionsFile:
                capabilities = capabilities + line
        await message.channel.send(capabilities)
        return
    
    #Prints out study guide directions. Link volatile, not included
    if message.content == 'hadro study help':
        instructions = ''
        with open('guideInstructions.txt') as instructionsFile:
            for line in instructionsFile:
                instructions = instructions + line
        await message.channel.send(instructions)
        return
    
    #Prints out extension details
    if re.search('(?=.*quiz)(?=.*extension)', message.content.lower()):
        await message.channel.send('Quiz extensions may be available if the quiz was missed due to '
                                   'an emergency or illness, in which case you should message Dr. Martin '
                                   'on Canvas. There are no extensions otherwise')
        return

    #gossip
    if re.search(r'(?=.*hadro)((?=.*controversy)|(?=.*tea)|(?=.*gossip)|(?=.*spill))', message.content.lower()):
        await message.channel.send(random.choice(list(open('gossip.txt'))))
        return
    
    #Hadrobot has feelings too!!
    if re.search('(?=.*hate)((?=.*dino)|(?=.*hadro))', message.content.lower()):
        await message.channel.send(':(')
        return
    
    if re.search('(?=.*love)((?=.*dino)|(?=.*hadro))', message.content.lower()):
        await message.channel.send(':)')
        return
    
    #HADROBOT CONGRATS
    if re.search('(?=.*hadro)(?=.*did it)', message.content.lower()):
        await message.channel.send('WOOHOO!!!!')
        return
    
    #Hadjokebot silly
    if re.search('(?=.*hadro)((?=.*joke)|(?=.*funny)|(?=.*funni)|(?=.*silly)|(?=.*goof))', message.content.lower()):
        await message.channel.send(random.choice(list(open('the_funnies.txt'))))
        return
    
    # if re.search('(?=.*hadro)(?=.*skibidi)', message.content.lower()):
    #     await message.channel.send('https://cdn.discordapp.com/attachments/357699039011274754/1298024344261365772/Screenshot_2024-10-21_at_1.45.14_PM.png?ex=67180edf&is=6716bd5f&hm=f4557a93eb1ce09121e66ad4dc018d253e4a28cc96c3dc26cd60041620ea1ce9&')
    #     return
    if re.search('(?=.*eat chicken)', message.content.lower()):
        await message.channel.send('would you still love me if i was a chicken?')
        return

    #he hoo funny misc responses
    if re.search('(?=.*hadro)', message.content.lower()):
        await message.channel.send(random.choice(list(open('magic_8_bot.txt'))).replace('\\n','\n'))
        return

#run the bot
client.run(DISCORD_TOKEN)