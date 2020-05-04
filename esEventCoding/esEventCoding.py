from __future__ import absolute_import, division, print_function
from psychopy import gui  #fetch default gui handler (qt if available)
import os
import sys
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath('__file__'))
os.chdir(_thisDir)
# This alternative uses a gui.Dlg and you manually extract the data.
# This approach gives more control, eg, text color.
expInfo = {'Exp Name': 'esEventCoding', 'SubID': '', 'Gender':'','Age':'',
'Phase(1=Action Segmentation; 2=Action Naming; 3=Goal Segmentation; 4=Goal Naming)':'',
'Movie(0/1/2)':''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title="Segmentation_Naming_Starting") 
sys.argv = ['Seg_Naming_start.py',dlg.dictionary['Exp Name'], dlg.dictionary['SubID'], dlg.dictionary['Gender'], dlg.dictionary['Age'], dlg.dictionary['Phase(1=Action Segmentation; 2=Action Naming; 3=Goal Segmentation; 4=Goal Naming)'], dlg.dictionary['Movie(0/1/2)']]
phase=dlg.dictionary['Phase(1=Action Segmentation; 2=Action Naming; 3=Goal Segmentation; 4=Goal Naming)']
if dlg.OK:
    if phase == '1':
        exec(compile(open('segmentation_action.py', "rb").read(), 'segmentation_action.py', 'exec'))
    elif phase == '2':
        exec(compile(open('action_naming.py', "rb").read(), 'action_naming.py', 'exec'))
    elif phase == '3':
        exec(compile(open('segmentation_goal.py', "rb").read(), 'segmentation_goal.py', 'exec'))
    elif phase == '4':
        exec(compile(open('goal_naming.py', "rb").read(), 'goal_naming.py', 'exec'))
else:
    print('User cancelled')
