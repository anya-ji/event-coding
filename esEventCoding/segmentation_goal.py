#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Mon Jan 27 17:07:12 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, monitors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard
import movieHandler
import csv
import pandas
import writeData


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

monitorSize = monitors.Monitor('testMonitor').getSizePix()

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'segmentation_goal'  # from the Builder filename that created this script
expInfo = {'SubID': '', 'Gender':'','Age':'',
'Phase(1=Action Segmentation; 2=Action Naming; 3=Goal Segmentation; 4=Goal Naming)':'',
'Movie(1/2)':''}
expInfo['Exp Name'] = sys.argv[1]
expInfo['SubID'] = sys.argv[2]
expInfo['Gender'] = sys.argv[3]
expInfo['Age'] = sys.argv[4]
expInfo['Phase(1=Action Segmentation; 2=Action Naming; 3=Goal Segmentation; 4=Goal Naming)'] = sys.argv[5]
expInfo['Movie(0/1/2)'] = sys.argv[6]
    
if expInfo['Movie(0/1/2)'] == '0':
    movieName = '3backPrac'
elif expInfo['Movie(0/1/2)'] == '1':
    movieName = 'Corn'
else: movieName = '3Iron'

textSize = 0.02

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s/%s' % ('Sub_'+ expInfo['SubID'] , expInfo['Exp Name'] + '.' + expInfo ['SubID'] + '.' + expInfo ['Gender'] + '.' + expInfo ['Age'] + '.goalSegmentation.txt')
savedFramesFile = _thisDir + os.sep + u'data/%s/%s' % ('Sub_'+expInfo['SubID'], 'Movie_' + expInfo['Movie(0/1/2)'])

headerSave = ('SubID', 'SubExpName', 'movName', 'movOrder', 'keyPress', 'keyPressTime' , 'frameTime', 'endActionframeTime', 'outcome')
dataSave = [expInfo['SubID'], 'goalSegmentation', movieName, expInfo['Movie(0/1/2)']]

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=_thisDir+'/segmentation_goal.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window

win = visual.Window(
    size=tuple(monitorSize), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
    

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instruction"
instrText = 'Welcome to PHASE 3: goal segmentation!\
            \n\
            \n\
            \nFor this part of the experiment, we would like you to flip through some screenshots of the movie and press SPACE when you identified that a goal is reached on this screenshot.\
            \nPress ESC when finished identifying all goals.\
            \n\
            \n\
            \nThis is clip: ' + movieName

InstructionClock = core.Clock()
instScreen = visual.TextStim(win = win, name = 'instScreen',
                             text = instrText, alignHoriz = 'center',
                             font = 'Arial', height = 0.02, wrapWidth = None, ori = 0,
                             color = 'white', colorSpace = 'rgb', opacity = 1,
                             languageStyle = 'LTR');
                         

# Initialize components for Routine "Goal_segmentation"
image = visual.ImageStim(
    win = win, 
    size = [1, 0.5625],
    pos = [0, 0]
    )

confirmText = visual.TextStim(win = win, name = 'confirmText',
                              text = 'Confirm selection? (y/n)',
                              pos = (0, -0.4), height = textSize, ori = 0,
                              color = 'white', colorSpace = 'rgb', opacity = 1,
                              languageStyle = 'LTR')


lastFrameText = visual.TextStim(win = win, name = 'lastFrameText',
                              text = 'This is the last frame. End task? (y/n)',
                              pos = (0, -0.4), height = textSize, ori = 0,
                              color = 'white', colorSpace = 'rgb', opacity = 1,
                              languageStyle = 'LTR')
    
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

## ------Prepare to start Routine "Goal_segmentation"-------
# reset timers
t = 0
trialClock=core.Clock()
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True
confirm_resp = keyboard.Keyboard()
goalSegmentComponent = [image, confirmText]
for thisComponent in goalSegmentComponent:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# Create eventlist: list of all timestamps of identified action changes
eventlist=[]
openfile = _thisDir + os.sep + u'data/%s/%s' % ('Sub_'+ expInfo['SubID'] , expInfo['Exp Name'] + '.' + expInfo ['SubID'] + '.' + expInfo ['Gender'] + '.' + expInfo ['Age'] + '.actionSegmentation.txt')
segmentData = pandas.read_table(openfile, delim_whitespace=True)
eventlist = segmentData.frameTime[(segmentData.movName == movieName) & segmentData.outcome.isin(['play', 'lastFrame'])].tolist()

midlist=[eventlist[0]/2]
i=1
while i<len(eventlist):
    midlist.append((eventlist[i]+eventlist[i-1])/2)
    i=i+1
    
savedFramesFile = _thisDir + os.sep + u'data/%s/%s' % ('Sub_'+expInfo['SubID'], 'Movie_' + expInfo['Movie(0/1/2)'])

# -------Run Routine "trial"-------
index = 0
while continueRoutine:
    t=trialClock.getTime()
    # add keyboard
    kb=defaultKeyboard    
    
    # *image* updates
    if  image.status == NOT_STARTED and t >= 0.0:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
        
    image.image = savedFramesFile + u'/%s.png'%(midlist[index])
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    keys = kb.getKeys(['space','escape','left','right','return'])
    for thisKey in keys:
        if thisKey=='left':
            if index >= 1:
                index = index - 1
                image.image = savedFramesFile + u'/%s.png'%(midlist[index])
                data = dataSave + [thisKey.name, str(trialClock.getTime()), str(midlist[index]), str(eventlist[index]), 'seek']
                writeData.writeData(headerSave, data, filename)
                win.flip()
        elif thisKey=='right':
            if index < len(eventlist)-1:
                index = index + 1
                image.image = savedFramesFile + u'/%s.png'%(midlist[index])
                data = dataSave + [thisKey.name, str(trialClock.getTime()), str(midlist[index]), str(eventlist[index]), 'seek']
                writeData.writeData(headerSave, data, filename)
                win.flip()
            elif index >= len(eventlist) - 1:
                data = dataSave + [thisKey.name, str(trialClock.getTime()), str(midlist[index]), str(eventlist[index]), 'lastFrame']
                writeData.writeData(headerSave, data, filename)
                lastFrameText.setAutoDraw(True)
                lastFrame = True
                while lastFrame:
                    keys = event.getKeys(keyList = ['y', 'n'])
                    if len(keys):
                        data = dataSave + [thisKey.name, str(trialClock.getTime()), str(midlist[index]), str(eventlist[index]), keys[0]]
                        writeData.writeData(headerSave, data, filename)
                        lastFrameText.setAutoDraw(False)
                        lastFrame = False
                        continueRoutine = False
                    win.flip()                
        elif thisKey=='space':
            data = dataSave + [thisKey.name, str(trialClock.getTime()), str(midlist[index]), str(eventlist[index]), 'select']
            writeData.writeData(headerSave, data, filename)
            confirmText.setAutoDraw(True)
            confirm = True
            while confirm:
                keys = event.getKeys(keyList = ['y', 'n'])
                if len(keys):
                    data = dataSave + [thisKey.name, str(trialClock.getTime()), str(midlist[index]), str(eventlist[index]), keys[0]]
                    writeData.writeData(headerSave, data, filename)
                    confirmText.setAutoDraw(False)
                    confirm = False
                win.flip()

    if continueRoutine:
        win.flip()
        win.timeOnFlip(image, 'tStopRefresh')
        
        
# -------Ending Routine "trial"-------
thisExp.addData('SubID', expInfo['SubID'])
thisExp.addData('Gender', expInfo['Gender'])
thisExp.addData('Age', expInfo['Age'])
thisExp.addData('Phase', expInfo['Phase(1=Action Segmentation; 2=Action Naming; 3=Goal Segmentation; 4=Goal Naming)'])
thisExp.addData('Movie', expInfo['Movie(1/2)'])
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
