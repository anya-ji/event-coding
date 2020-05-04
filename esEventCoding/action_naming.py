from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock, monitors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import math
import string
import csv
import movieHandler
import pandas
import writeData

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath('__file__'))

os.chdir(_thisDir)#change working directory

#Check monitor size 
monitorSize = monitors.Monitor('testMonitor').getSizePix()

#Text settings
textSize = 0.02
allLetters = list(string.ascii_lowercase)#list all letters 

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'action_naming'  # from the Builder filename that created this script
expInfo = {'SubID': '', 'Gender':'','Age':'',
'Phase(1=Action Segmentation; 2=Action Naming; 3=Goal Segmentation; 4=Goal Naming)':'',
'Movie(0/1/2)':''}
expInfo['Exp Name'] = sys.argv[1]
expInfo['SubID'] = sys.argv[2]
expInfo['Gender'] = sys.argv[3]
expInfo['Age'] = sys.argv[4]
expInfo['Phase(1=Action Segmentation; 2=Action Naming; 3=Goal Segmentation; 4=Goal Naming)'] = sys.argv[5]
expInfo['Movie(0/1/2)'] = sys.argv[6]

if expInfo['Movie(0/1/2)'] == '0':
    movie = '3backPrac'
elif expInfo['Movie(0/1/2)'] == '1':
    movie = 'Corn'
else: movie = '3Iron'

moviefile = _thisDir + os.sep + 'Movie' + os.sep + movie + '.mp4'

#Window setup
win = visual.Window(size = tuple(monitorSize),pos=(0,0), fullscr=True,
                    winType='pyglet', allowGUI=False, allowStencil=False,
                    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
                    blendMode='avg', useFBO=True,
                    units='height') #(1366,768)
    
win.mouseVisible = False

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s/%s' % ('Sub_'+ expInfo['SubID'] , expInfo['Exp Name'] + '.' + expInfo ['SubID'] + '.' + expInfo ['Gender'] + '.' + expInfo ['Age'] + '.actionNaming.txt')
headerSave = ('SubID', 'SubExpName', 'movName', 'movOrder', 'pauseFrameTime' , 'recallText', 'recallStartTime', 'recallEndTime')
dataSave = [expInfo['SubID'], 'actionNaming', movie, expInfo['Movie(0/1/2)']]

savedFramesFile = _thisDir + os.sep + u'data/%s/%s/' % ('Sub_'+expInfo['SubID'], 'Movie_' + expInfo['Movie(0/1/2)'])

thisExp = data.ExperimentHandler(name=expName, version='',
extraInfo=expInfo, runtimeInfo=None,
originPath=_thisDir + '/action_naming.py',
savePickle=False, saveWideText=False,
dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False
frameTolerance = 0.001  # how close to onset before 'same' frame

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

##--------------Initializations---------------------

# Initialize components for Routine "Instruction"
instrText = 'Welcome to PHASE 2: action naming!\
            \n\
            \n\
            \nFor this part of the experiment, we would like you to rewatch the movie you just segmented. The movie will pause at the end of each of your segmentation.\
            \n\
            \nOnce the movies pauses, type in what you would describe the action in the segment in a SINGLE VERB. Press RETURN to submit your response.\
            \n\
            \n\
            \nThis is clip: ' + movie

InstructionClock = core.Clock()
instScreen = visual.TextStim(win = win, name = 'instScreen',
                             text = instrText, alignHoriz = 'center',
                             font = 'Arial', height = textSize, wrapWidth = None, ori = 0,
                             color = 'white', colorSpace = 'rgb', opacity = 1,
                             languageStyle = 'LTR');

                         
# Initialize components for Routine "Experiment_end"

endText = 'You have reached the end of clip: ' + movie + '. Press SPACE to quit.'

Experiment_endClock = core.Clock()
endScreen = visual.TextStim(win=win, name='endScreen',
                            text=endText,
                            font='Arial',
                            pos=(0, 0), height=textSize, wrapWidth=None, ori=0,
                            color='white', colorSpace='rgb', opacity=1,
                            languageStyle='LTR',
                            depth=0.0);
                        
                        
# Initialize components for Routine "Recall_Trial"
recall_trialClock = core.Clock()
                        
recall_instr = visual.TextStim(win=win, name='recall_inst',
                               text='Name the previous ACTION with a SINGLE VERB, and press RETURN.',
                               font='Arial',
                               pos = (0,-0.3), height=textSize, wrapWidth=None, ori=0, 
                               color='white', colorSpace='rgb', opacity=1, 
                               languageStyle='LTR');

recall_text = visual.TextStim(win=win, name='recall_text',
                              text= None,
                              font='Arial',
                              pos=(0,-0.4), height=textSize, ori=0,
                              color='white', colorSpace='rgb', opacity=1,
                              languageStyle='LTR');

playback = visual.MovieStim3(
        win=win, name='playback',
        noAudio = False,
        filename=moviefile,
        ori=0, size = win.size/3, pos=(0, 75), opacity=1,
        loop=False,
        depth=0.0,
    )

singleframe = 1 / playback.getFPS()                     
       
# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine


## ------Prepare to start Routine "Instruction"-------
t = 0
InstructionClock.reset()  # clock
frameN = -1
InstcontinueRoutine = True
# update component parameters for each repeat
instkey_resp = keyboard.Keyboard()
# keep track of which components have finished
InstructionComponents = [instScreen, instkey_resp]
for thisComponent in InstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instruction"-------
while InstcontinueRoutine:
# get current time
    t = InstructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
# update/draw components on each frame

# *text* updates
    if t >= 0.0 and instScreen.status == NOT_STARTED:
    # keep track of start time/frame for later
        instScreen.tStart = t  # not accounting for scr refresh
        instScreen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(instScreen, 'tStartRefresh')  # time at next scr refresh
        instScreen.setAutoDraw(True)

# *key_resp* updates
    if t >= 0.0 and instkey_resp.status == NOT_STARTED:
    # keep track of start time/frame for later
        instkey_resp.tStart = t  # not accounting for scr refresh
        instkey_resp.frameNStart = frameN  # exact frame index
        win.timeOnFlip(instkey_resp, 'tStartRefresh')  # time at next scr refresh
        instkey_resp.status = STARTED
    # keyboard checking is just starting
        instkey_resp.clearEvents(eventType='keyboard')
    if instkey_resp.status == STARTED:
       theseKeys = instkey_resp.getKeys(keyList = ['space'], waitRelease = False)
       if len(theseKeys):
          theseKeys = theseKeys[0]  # at least one key was pressed

        # check for quit:
          if "escape" == theseKeys:
             endExpNow = True
        # a response ends the routine
          InstcontinueRoutine = False

# check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        win.close()
        core.quit()

# check if all components have finished
    if not InstcontinueRoutine:  # a component has requested a forced-end of Routine
        break
    InstcontinueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            InstcontinueRoutine = True
            break  # at least one component has not yet finished

# refresh the screen
    if InstcontinueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        win.timeOnFlip(instScreen, 'tStopRefresh')

# -------Ending Routine "Instruction"-------
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instScreen.started', instScreen.tStartRefresh)
thisExp.addData('instScreen.stopped', instScreen.tStopRefresh)
    
# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
win.flip()


## ------Prepare to start Routine "Recall_Trial"-------    
t = 0
recall_trialClock.reset()  # clock
frameN = -1
continueRoutine = True
 #update component parameters for each repeat
modify = False
recall_text.text = ''
event.clearEvents('keyboard')
 #keep track of which components have finished
trialComponents = [recall_instr, recall_text, playback]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
        
 #import lists
eventlist=[]
openfile = _thisDir + os.sep + u'data/%s/%s' % ('Sub_'+ expInfo['SubID'] , expInfo['Exp Name'] + '.' + expInfo ['SubID'] + '.' + expInfo ['Gender'] + '.' + expInfo ['Age'] + '.actionSegmentation.txt')
segmentData = pandas.read_table(openfile, delim_whitespace=True)
eventlist = segmentData.frameTime[(segmentData.movName == movie) & (segmentData.outcome.isin(['play', 'lastFrame']))].tolist()

core.wait(1)

index = 0
namingperiod = False
 #-------Start Routine "trial"-------
while continueRoutine:
    # get current time
    t = recall_trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # get current time
    
    tThisFlip = win.getFutureFlipTime(clock=recall_trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    
    # update/draw components on each frame
        
    # *text* updates
    if t >= 0.0 and recall_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        recall_text.tStart = t  # not accounting for scr refresh
        recall_text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(recall_text, 'tStartRefresh')  # time at next scr refresh
        win.timeOnFlip(recall_instr, 'tStartRefresh')
    
    if playback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        playback.frameNStart = frameN  # exact frame index
        playback.tStart = t  # local t and not account for scr refresh
        playback.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(playback, 'tStartRefresh')  # time at next scr refresh
        playback.setAutoDraw(True)
        
    if index<=len(eventlist)-1 and playback.getCurrentFrameTime() >= round(eventlist[index], len(str(playback.getCurrentFrameTime()).split(".")[1])):
        playback.pause()
        playback.seek(eventlist[index])
        pauseFrameTime = playback.getCurrentFrameTime()
        index=index+1
        recall_instr.setAutoDraw(True)
        recall_text.setAutoDraw(True)
        recallStartTime = recall_trialClock.getTime()
        namingperiod = True
    elif index == len(eventlist)-1 and (abs(playback.getCurrentFrameTime() - eventlist[index])< frameTolerance):
        playback.pause()
        playback.seek(eventlist[index]-singleframe)
        pauseFrameTime = playback.getCurrentFrameTime()
        index=index+1
        recall_instr.setAutoDraw(True)
        recall_text.setAutoDraw(True)
        recallStartTime = recall_trialClock.getTime()
        namingperiod = True
        
    while namingperiod: 
        keys = event.getKeys()
        if len(keys):
            if 'space' in keys:
                recall_text.text = recall_text.text + ' '
            elif 'backspace' in keys:
                recall_text.text = recall_text.text[:-1]
            elif 'period' in keys: 
                recall_text.text = recall_text.text + '.'
            elif 'comma' in keys:
                recall_text.text = recall_text.text + ','
            elif 'exclamation' in keys:
                recall_text.text = recall_text.text + '!'
            elif 'semicolon' in keys: 
                recall_text.text = recall_text.text + ';'
            elif 'apostrophe' in keys: 
                recall_text.text = recall_text.text + "'"
            elif 'lshift' in keys or 'rshift' in keys:
                modify = True
            elif 'return' in keys and recall_text.text != '':
                data = dataSave + [str(pauseFrameTime) + recall_text.text + str(recallStartTime) + str(recall_trialClock.getTime())]
                writeData.writeData(headerSave, data, filename)
                recall_text.text = ''
                recall_instr.setAutoDraw(False)
                recall_text.setAutoDraw(False)
                namingperiod = False
                if index >= len(eventlist):
                    continueRoutine=False
                    break
                else:
                    playback.play()                   
            else:
                if modify:
                    if keys[0] in allLetters:
                        recall_text.text = recall_text.text + keys[0].upper()
                        modify = False
                    elif 'slash' in keys:
                        recall_text.text = recall_text.text + '?'
                        modify = False
                    elif '1' in keys:
                        recall_text.text = recall_text.text + '!'
                        modify = False
                else:
                    if 'slash' in keys: 
                        recall_text.text = recall_text.text + '/'
                    recall_text.text = recall_text.text + keys[0]
                    
        win.flip()
        # check for quit (typically the Esc key)
    if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
        core.quit()
        win.close()
        
    if continueRoutine: 
        win.flip()
        win.timeOnFlip(recall_text, 'tStopRefresh')
    
    # get current time
    endtime = recall_trialClock.getTime()
            
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
        continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
           continueRoutine = True
           break  # at least one component has not yet finished
    
        # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        
 #-------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
        thisExp.addData('recall_text.started', recall_text.tStartRefresh)
        thisExp.addData('recall_text.stopped', recall_text.tStopRefresh)
 #the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
win.flip()

## ------Prepare to start Routine "Experiment_end"-------
t = 0
Experiment_endClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = keyboard.Keyboard()
# keep track of which components have finished
Experiment_endComponents = [endScreen, key_resp_2]
for thisComponent in Experiment_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Experiment_end"-------
while continueRoutine:
    # get current time
    t = Experiment_endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_2* updates
    if t >= 0.0 and endScreen.status == NOT_STARTED:
        # keep track of start time/frame for later
        endScreen.tStart = t  # not accounting for scr refresh
        endScreen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(endScreen, 'tStartRefresh')  # time at next scr refresh
        endScreen.setAutoDraw(True)

    # *key_resp_3* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # not accounting for scr refresh
        key_resp_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        key_resp_2.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed

            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Experiment_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        win.timeOnFlip(endScreen, 'tStopRefresh')
        

# -------Ending Routine "Experiment_end"-------
for thisComponent in Experiment_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('endScreen.started', endScreen.tStartRefresh)
thisExp.addData('endScreen.stopped', endScreen.tStopRefresh)
thisExp.addData('SubID', expInfo['SubID'])
thisExp.addData('Gender', expInfo['Gender'])
thisExp.addData('Age', expInfo['Age'])
thisExp.addData('Phase', expInfo['Phase(1=Action Segmentation; 2=Action Naming; 3=Goal Segmentation; 4=Goal Naming)'])
thisExp.addData('Movie', expInfo['Movie(0/1/2)'])
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()

thisExp.abort()  # or data files will save again on exit
    
    # make sure everything is closed down
win.mouseVisible = True
win.close()
core.quit()

    
    
    
    
    
   