#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 13:48:43 2019

@author: karen sasmita

Wrapper script for ffmpeg and other video manipulations
    
"""

import subprocess

# to get duration of entire clip
def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)

## top level function to spawn a child process
#def spawn_child(cmds=[]):
#    subprocess.Popen(cmds)

def extract_frame(video_input, image_output, time): 
    """
    Returns: saves single frame from video input at predefined time as image.
    
    Parameter video_input: The video source
    Precondition: string (e.g. 'video.mp4')
    
    Parameter image_output: Image name to save frame as 
    Precondition: string (e.g. 'image.jpg')
    
    Parameter time: Timepoint at which frame is to be extracted
    Precondition: string ('hh:mm:ss')
    """
    cmds = ['ffmpeg', '-i', video_input, '-ss', time, '-frames:v', '1', image_output]
    subprocess.Popen(cmds)
    
def extract_clip(video_input, video_output, time_from, time_to):
    """
    Returns: saves single clips from video input at predefined time interval as video file.
    
    Parameter video_input: The video source
    Precondition: string (e.g. 'video.mp4')
    
    Parameter video_output: Video name to save clip as 
    Precondition: string (e.g. 'video.mp4')
    
    Parameter time_from: Interval start time
    Precondition: string ('hh:mm:ss')
    
    Parameter time_to: Interval end time
    Precondition: string ('hh:mm:ss')
    
    """
    cmds = ['ffmpeg', '-i', video_input, '-ss', time_from, '-to', time_to, '-c', 'copy', video_output]
    subprocess.Popen(cmds)

    
def get_keyframe_time(video_input):
    """
    Returns: list of time points (as string) when keyframes occur.
    
    Parameter video_input: The video source
    Precondition: string (e.g. 'video.mp4')
    
    """
    cmds = ['ffprobe', '-v', 'error', '-skip_frame', 'nokey', '-show_entries', 'frame=pkt_pts_time', '-select_streams', 'v', '-of', 'csv=p=0', video_input]
    p = subprocess.Popen(cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate() #out is the output we want but it is currently in type 'bytes'
    out = out.decode() #decode bytes to string. Out now is a string containing keyframe times with \n delimiter 
    kfTimes = out.split('\n') #split 'out' by delim \n to list. Resultant 'kfTimes is a list of keyframe times. 
    kfTimes.remove('') #remove empty string elements in list -> typically kfTimes end with an empty element ('')
    return kfTimes
    

def double_speed(video_input, video_output):
    cmds = ['ffmpeg', '-i', video_input, '-filter:v', 'setpts=0.5*PTS', video_output]
    subprocess.Popen(cmds)



