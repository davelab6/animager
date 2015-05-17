### main python script

import os, sys, getpass
from genImages import gitGenTempImages
from genVideo import morphImages
from genVideo import genVideo
from profiles import readProfile
from profiles import writeProfile
from profiles import getProfList


def main( argv ):

    userName = getpass.getuser()
    inputImage = ''
    frameRate = '25'
    height = ''
    width = ''
    morph = '2'
    morphSet = False
    vOut = '/home/' + userName + '/animager/'

    if '-p' in argv:
        pName = argv[ argv.index( '-p' ) + 1 ]
        options = readProfile( pName )

        if '-i' in argv:
            inputImage = argv[ argv.index( '-i' ) + 1 ]

        else:
            print( "No input file given" )
            sys.exit( 0 )

        if '-o' in argv:
            vOut = argv[ argv.index( '-o' ) + 1 ] + '/'

        for x in options:
            if '-f' in x:
                i = x.index( '-f' ) + 1
                frameRate = x[ i ]

            elif '-h' in x:
                i = x.index( '-h' ) + 1
                height = x[ i ]

            elif '-w' in x:
                i = x.index( '-w' ) + 1
                width = x[ i ]

    elif '-pnew' in argv:
        writeProfile( argv )
        print( 'Profile created successfully' )
        print( 'enter \"animager -plist all\" to get the profile list' )
        sys.exit( 0 )

    elif '-plist' in argv:
        getProfList( userName )
        sys.exit( 0 )

    else:
        print( 'Invalid input.' )
        print( 'usage: animager -p [profile name] -i [input file] -o [output folder]' )
        print( 'usage: animager -pnew [profile name] -h [height] -w [width] -f [frame rate]' )
        sys.exit( 0 )
        
    #print(options)
    #print(height)
    #print(width)
    #print(frameRate)
    #print(vOut)
    #sys.exit(0)


    crossfade = input( '\nAdd crossfade effect ? (y/n)' )

    if crossfade is 'y':
        value = input( 'Enter crossfade value value (default : 2): ' )
        if value is '':
            value = 2
            
        gitGenTempImages( inputImage, '/home/' + userName + '/animager/' )
        morphImages( '/home/' + userName + '/animager/', value, '.png' )
        genVideo( '/home/' + userName + '/animager/morph-cache/', frameRate,
                  height, width, vOut )
        os.system( 'rm -r /home/' + userName + '/animager/morph-cache/*' )
        
    else:
        gitGenTempImages( inputImage, '/home/' + userName + '/animager/' )
        genVideo( '/home/' + userName + '/animager/', frameRate, height, width, vOut )
        
    keepTemp = input( '\nKeep temporary image files ? (y/n) ' )
    if keepTemp is 'y':
        print( "\nWarning ! keeping temporary images will cost hard drive space."
               + "\nTemporary images are in ~/animager/")
        tempFold = input( 'Enter directory name : ' )
        os.system( 'mkdir -p /home/' + userName + '/animager/' + tempFold )
        os.system( 'mv /home/' + userName + '/animager/*.png /home/'
                   + userName + '/animager/' + tempFold )

    else:
        os.system( 'rm -r /home/' + userName + '/animager/*.png' )


if __name__ == "__main__":
    
    main( sys.argv )
