#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
import writeData
import pandas

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath('__file__'))
os.chdir(_thisDir)

monitorSize = monitors.Monitor('testMonitor').getSizePix()

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'segmentation_action'  # from the Builder filename that created this script
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
    movieName = '3backPrac'
    whichClip = 'Practice'
elif expInfo['Movie(0/1/2)'] == '1':
    movieName = 'Corn'
    whichClip = 'Movie 1'
else: 
    movieName = '3Iron' 
    whichClip = 'Movie 2'

moviefile = _thisDir + os.sep + 'Movie' + os.sep + movieName + '.mp4'

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s/%s' % ('Sub_'+ expInfo['SubID'] , expInfo['Exp Name'] + '.' + expInfo ['SubID'] + '.' + expInfo ['Gender'] + '.' + expInfo ['Age'] + '.actionSegmentation.txt')

headerSave = ('SubID', 'SubExpName', 'movName', 'movOrder', 'keyPress', 'keyPressTime' , 'frameTime', 'outcome')
dataSave = [expInfo['SubID'], 'actionSegmentation', movieName, expInfo['Movie(0/1/2)']]

#An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=_thisDir+'/segmentation_action.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

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
instrText = 'Welcome to Task 1: action identification!\
            \n\
            \n\
            \nFor this part of the experiment, we would like you to watch the movie and press SPACE to pause the clip after you have perceived an action change.\
            \nPressing SPACE will pause the movie. You should use the LEFT ARROW key to rewind the movie to the exact frame that first indicate that the last action had ended and new one had begun. If you need to go forward in frame, press the RIGHT ARROW key.\
            \nOnce you have identified the first frame of the new action, press SPACE to confirm and re-start the movie playback.\
            \nIf you happen to accidentally pause the movie or decided that you have not identified a new action, you can press C key to cancel your selection.\
            \n\
            \nPress any key to begin: ' + whichClip
                
#            \
#            \n\
#            \n\'
#            \nThis is clip: ' + clip

InstructionClock = core.Clock()
instScreen = visual.TextStim(win = win, name = 'instScreen',
                              text = instrText, pos = (0,0),
                              font = 'Arial', height = 0.02, wrapWidth = None, ori = 0,
                              color = 'white', colorSpace = 'rgb', opacity = 1,
                              languageStyle = 'LTR');
                     
#double speed
#input='/Users/anyaji/Desktop/5sec/3Backyard_prac.mp4'
#output='/Users/anyaji/Desktop/5sec/3Backyard_prac2.mp4'
#if not os.path.exists(output):
#    movieHandler.double_speed(input,output)

# Initialize components for Routine "trial"
trialClock = core.Clock()

movie = visual.MovieStim3(
        win=win, name='movie',
        noAudio = False,
        filename= moviefile,
        ori=0, pos=(0, 0), opacity=1,
        loop=False,
        depth=0.0,
        )
    
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

## ------Prepare to start Routine "trial"-------
# update component parameters for each repeat
# keep track of which components have finished
trialComponents = [movie]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# movie single frame duration
singleframe = 1 / movie.getFPS()

#Initialize
actionEnd=0
finishSearch=0

# -------Run Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *movie* updates
    if movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movie.frameNStart = frameN  # exact frame index
        movie.tStart = t  # local t and not account for scr refresh
        movie.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
        movie.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
        else:
            actionEnd = movie.getCurrentFrameTime()
            thisExp.addData("play_ft", actionEnd)
            continueRoutine = False

    # keyboard control
    kb=defaultKeyboard
    keys = kb.getKeys(['space','escape','left','right', 'c'])
    for thisKey in keys:
        if thisKey=='space':
            if movie.status==PLAYING:
                win.callOnFlip(movie.pause)
                timestamp = movie.getCurrentFrameTime()
                startSearch = t
                data = dataSave + [thisKey.name, str(startSearch), str(timestamp), 'pause']
                writeData.writeData(headerSave, data, filename)
    
            elif movie.status==PAUSED:
                finishSearch = t
                actionEnd = movie.getCurrentFrameTime()
                data = dataSave + [thisKey.name, str(finishSearch), str(actionEnd), 'play']
                writeData.writeData(headerSave, data, filename)
                win.callOnFlip(movie.play)
                
        elif thisKey=='left':
            if movie.status==PAUSED:
                timestamp = movie.getCurrentFrameTime()
                movie.seek(timestamp)
                movie.play()
                movie.pause()
                data = dataSave + [thisKey.name, str(t), str(timestamp - (2*singleframe)), 'seek']
                writeData.writeData(headerSave, data, filename)
                
        elif thisKey=='right':
            if movie.status==PAUSED:
                timestamp = movie.getCurrentFrameTime()
                movie.seek(timestamp + singleframe * 2)
                movie.play()
                movie.pause()
                data = dataSave + [thisKey.name, str(t), str(timestamp + singleframe), 'seek']
                writeData.writeData(headerSave, data, filename)
                
        elif thisKey == 'c':
            if movie.status==PAUSED:
                timestamp = movie.getCurrentFrameTime()
                data = dataSave + [thisKey.name, str(t), str(timestamp), 'cancel']
                writeData.writeData(headerSave, data, filename)
                win.callOnFlip(movie.play)
                
                
        elif thisKey=='escape':
            core.quit()
            
            
      # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        win.recordFrameIntervals=True  #check framedrop
        win.timeOnFlip(movie, 'tStopRefresh')

# -------Ending Routine "trial"-------
#save last frame time 
data = dataSave + ['none', str(movie.tStopRefresh), str(movie.getCurrentFrameTime()), 'lastFrame'] 
writeData.writeData(headerSave, data, filename)

for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
        thisExp.addData('segmentation.start', movie.tStartRefresh)
        thisExp.addData('segmentation.end', movie.tStopRefresh)

# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# Initialize components for end "Instruction"
endText = 'You have completed the first task. Please wait while the programme is saving your responses.'
quitText = 'Press SPACE to exit'
endScreen = visual.TextStim(win = win, name = 'instScreen',
                text = endText, alignHoriz = 'right',
                font = 'Arial', height = 0.02, wrapWidth = None, ori = 0,
                color = 'white', colorSpace = 'rgb', opacity = 1,
                languageStyle = 'LTR');
endScreen.draw()
win.flip()

 #import lists
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
if not os.path.exists(savedFramesFile):
  os.mkdir(savedFramesFile)

for ft in midlist:
    movieHandler.extract_frame(moviefile, os.path.abspath(savedFramesFile+u'/%s.png'%ft), str(ft))

quitText = 'Press SPACE to exit'
quitScreen = visual.TextStim(win = win, name = 'instScreen',
                text = quitText, pos = (0,0),
                font = 'Arial', height = 0.02, wrapWidth = None, ori = 0,
                color = 'white', colorSpace = 'rgb', opacity = 1,
                languageStyle = 'LTR');

quitAll = True
quitKey = keyboard.Keyboard()
while quitAll:
    quitScreen.setAutoDraw(True)
    theseKeys = quitScreen.getKeys(keyList = ['space'], waitRelease = False)
    if len(theseKeys):
         theseKeys = theseKeys[0]  # at least one key was pressed
         quitKey = False

win.flip()

core.wait(3)
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
