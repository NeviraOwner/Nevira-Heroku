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
            print('Start Nevira(/start 1)        View version(/version)')
            print('Start AeroBot(/start 2)       Quit(/exit)')
            print('Start shell(/start 3)')
            action = input('>')
            if action=='/start 1':
                import Nevira
            elif action=='/start 2':
                import Aerobot
            elif action=='/start 3':
                print('')
                break
            elif action=='/version':
                print('Nevira.py Interactive V1.1')
            elif action=='/exit':
                quit()
            else:
                print('Unknown command, check if command is available')
                print('')
    elif cmd=='/start':
        try:
            print('Importing Nevira.py...')
            import Nevira
        except:
            print('No default file detected! Specify code file you want to run.')
            script = input('/start:')
            try:
                execfile('python',script)
            except:
                print('[**]Failed startup, script not detected')
