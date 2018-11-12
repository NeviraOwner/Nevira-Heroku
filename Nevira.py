print('[OK]Nevira.py is imported')
print('')
print('Nevira 1.0 Aurora [BETA]')
token = 'Token goes here'
y=1
while True:
    try:
        print('Importing module: discord.py...')
        import discord
        print('[OK]Imported discord.py')
    except:
        print('[**]Failed to import discord.py, startup halted')
        quit()
    try:
        from discord.ext import commands
        print('[OK]Imported commands from discord.ext')
    except:
        print('[**]Failed to import commands from discord.ext, startup halted')
        quit()
    try:
        print('Attempting to set up bot...')
        description = 'Nevira 1.0 Aurora'
        print('[OK]Description of bot defined')
    except:
        print('[**]Failed to define description, startup halted')
        quit()
    try:
        bot = commands.Bot(command_prefix='*', description=description)
        print('[OK]Bot defined along with command_prefix')
    except:
        print('[**]Failed to define bot, startup halted')
        quit()
    try:
        print('Setting up logger...')
        import logging
        print('[OK]Imported logging')
    except:
        print('[* ]Failed to import logging')
    try:
        logger = logging.getLogger('discord')
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)
        print('[OK]Logger set')
    except:
        print('[* ]Failed to set logger')
    cntinue = input('Press Y to continue or any other key to abort.')
    if cntinue=='Y':
        print('')
        break
    else:
        print('[* ]Startup interrupted')
        print('')
        print('NeviraShell 1.0')
        
        x=1
        while True:
            startnum = 0
            cmd = input('>')
            if cmd=='/initialize log':
                print('WARNING: You are about to initialize the log. Are you sure you want to continue? (Y/N)')
                warn = input('/initialize:')
                if warn=='Y':
                    try:
                        print('(0/1 complete)Deleting log data...')
                        logedit = open('discord.log', 'w')
                        logedit.write('Log deleted by bot')
                        logedit.close
                        print('[OK]Log data deleted')
                        print('--------LOG INITIALIZATION SUCCESSFUL--------')
                    except:
                        print('[* ]Failed to delete log data')
                        print('----------LOG INITIALIZATION FAILED----------')
            elif cmd=='/exit':
                x=1
                while True:
                    print('')
                    print('Start Shell(/shell)             View version(/version)')
                    print('                                Quit(/exit)')
                    action = input('>')
                    if action=='/shell':
                        print('')
                        break
                    elif action=='/version':
                        print('Nevira.py Interactive Embedded v1.1')
                    elif action=='/exit':
                        quit()
                    else:
                        print('Unknown command, check if command is available')
                        print('')
            elif startnum==1:
                break
            elif cmd=='/token':
                print('Current token:',token)
                print('Enter the new token to change the token, or enter /cancel to cancel')
                tokenchange = input('/token:')
                if tokenchange=='/cancel':
                    print('Token modification canceled')
                else:
                    token = tokenchange
                    print('Token changed to',token,', this will reset after restart')
            elif cmd=='/continue':
                break

print('Starting bot...')

@bot.event
async def on_ready():
    print('[OK]Bot logged on as:',bot.user.name)
    print('[OK]Startup complete')
    print('----------')
    from random import randint
    status = randint(1,5)
    if status==1:
        return await bot.change_presence(game=discord.Game(name='Nevira 1.0 Aurora'))
    elif status==2:
        return await bot.change_presence(game=discord.Game(name='with Ninjabot'))
    elif status==3:
        return await bot.change_presence(game=discord.Game(name='\'Respond commands 2\''))
    elif status==4:
        return await bot.change_presence(game=discord.Game(name='Use *help for help!'))
    elif status==5:
        return await bot.change_presence(game=discord.Game(name='Official Edition!'))

@bot.event
async def on_message(message):
    if message.content.startswith('*hi'):
        await bot.send_message(message.channel, 'Hi there! Nice to see you!')
    elif message.content.startswith('*help'):
        await bot.send_message(message.author, 'Visit https://docs.google.com/document/d/1kRMcu32z4OfZdnmacFGwzCAnj32YDWVjOrtb3JZfLns to see my commands!')
    elif message.content.startswith('*time_gmt'):
        from time import gmtime, strftime
        time = strftime("%Y.%m.%d %H:%M:%S", gmtime())
        await bot.send_message(message.channel, time)
    elif message.content.startswith('*time_cet'):
        from time import ctime
        time1 = ctime()
        await bot.send_message(message.channel, time1)
    elif message.content.startswith('*dice'):
        from random import randint
        number = randint(1,6)
        output = number
        await bot.send_message(message.channel, output)
    elif message.content.startswith('*emoji'):
        from random import randint
        number6 = randint(1,12)
        if number6==1:
            lol = '（⌒▽⌒）'
        elif number6==2:
            lol = '(͡ ° ͜ʖ ͡ °)'
        elif number6==3:
            lol = '（//･_･//)'
        elif number6==4:
            lol = '(҂-̀_-́)'
        elif number6==5:
            lol = '(⌐■_■)'
        elif number6==6:
            lol = '(⊙_⊙)'
        elif number6==7:
            lol = '“ψ(｀∇´)ψ'
        elif number6==8:
            lol = '╮(╯▽╰)╭'
        elif number6==9:
            lol = '(ღ˘ω˘ღ)'
        elif number6==10:
            lol = '(╯°□°）╯︵ ┻━┻'
        elif number6==11:
            lol = '(－‸ლ)'
        elif number6==12:
            lol = '(¬_¬)ﾉ'
    elif message.content.startswith('*status'):
        if message.author.id=='356456393491873795':
            from random import randint
            stats = randint(1,5)
            if stats==1:
                await bot.send_message(message.channel, 'Changed status to **STATUS_ONE**')
                await bot.change_presence(game=discord.Game(name='Nevira 1.0 Aurora'))
            elif stats==2:
                await bot.send_message(message.channel, 'Changed status to **STATUS_TWO**')
                await bot.change_presence(game=discord.Game(name='with Ninjabot'))
            elif stats==3:
                await bot.send_message(message.channel, 'Changed status to **STATUS_THREE**')
                await bot.change_presence(game=discord.Game(name='\'Respond commands 2\''))
            elif stats==4:
                await bot.send_message(message.channel, 'Changed status to **STATUS_FOUR**')
                await bot.change_presence(game=discord.Game(name='Use *help for help!'))
            elif stats==5:
                await bot.send_message(message.channel, 'Changed status to **STATUS_FIVE**')
                await bot.change_presence(game=discord.Game(name='Official Edition!'))
        else:
            await bot.send_message(message.channel, 'You attempted to change the status. But you weren\'t authorized.')
    elif message.content.startswith('*joke'):
        from random import randint
        number5 = randint(1,5)
        if number5==1:
            await bot.send_message(message.channel, 'What has two banks but doesn\'t give money?')
            time.sleep(5)
            await bot.send_message(message.channel, 'A **river**!')
        elif number5==2:
            await bot.send_message(message.channel,'What do you say to your sister when she\'s crying?')
            time.sleep(5)
            await bot.send_message(message.channel,'Are you having a cri**sis**?')
        elif number5==3:
            await bot.send_message(message.channel,'I put grandma on speed dial...')
            time.sleep(5)
            await bot.send_message(message.channel,'I call it Insta**gram**!')
        elif number5==4:
            await bot.send_message(message.channel, 'What did the big chimney say to the small chimney?')
            time.sleep(5)
            await bot.send_message(message.channel, 'You\'re too young to smoke! :smoking:')
        #elif number5==5:
#            await bot.send_message(message.channel, 'How do you make 7 a even number?
#                                   take away the s
        else:
            await bot.send_message(message.channel,'A man asks a farmer near a field, “Sorry sir, would you mind if I crossed your field instead of going around it? You see, I have to catch the 4:23 train.”')
            time.sleep(5)
            await bot.send_message(message.channel,'The farmer says, “Sure, go right ahead. And if my bull sees you, you’ll even catch the 4:11 one.”')
    elif message.content.startswith('*meme'):
        await bot.send_message(message.channel, 'The *meme function is currently being halted since Heroku does not recognise Python as the main language with the pictures.')
    elif message.content.startswith('*shutdown'):
        if message.author.id=='356456393491873795':
            await bot.send_message(message.channel, 'Shutdown! :mobile_phone_off:')
            await bot.change_presence(game=discord.Game(name='Owner told me to shut down'))
            print('Beginning shutdown process...')
            print('[OK]Shutdown command sent, script execution halted')
            quit()
        else:
            await bot.send_message(message.channel, 'Yeah, like if that\'s going to WORK.')
    elif 'damn' in message.content:
        await bot.delete_message(message)
        await bot.send_message(message.channel, 'You have been caught swearing. Please watch your language.')
    elif 'curse u' in message.content:
        await bot.delete_message(message)
        await bot.send_message(message.channel, 'You have been caught cursing someone. Please watch your language.')

x=1
while True:
    try:
        bot.run(token)
    except:
        print('[* ]Failed to connect, retrying...')
        try:
            bot.run(token)
        except:
            print('[**]Failed to connect to the internet, script execution halted')
            break
