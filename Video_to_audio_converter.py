{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the video path that you want to convert to audio along with the extension gcp 1.mp4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "chunk:   0%|                                                                       | 0/14879 [00:00<?, ?it/s, now=None]"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MoviePy - Writing audio in output_audio.wav\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "                                                                                                                       "
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MoviePy - Done.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\r"
     ]
    }
   ],
   "source": [
    "import speech_recognition as sr\n",
    "import moviepy.editor as mp\n",
    "clipping =str(input('Enter the video path that you want to convert to audio along with the extension'))\n",
    "print('Hang in there audio extracting from audio')\n",
    "clip = mp.VideoFileClip(clipping)\n",
    "clip.audio.write_audiofile('output_audio.wav')\n",
    "print('hey there your requested audio is saved in the name of Output_audio')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
