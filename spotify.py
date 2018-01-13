#!/usr/bin/bash
# -*- coding: utf-8 -*-

import sys


from ConfigParser import ConfigParser
from random import choice
from request_types import put_req
from request_types import get_req

CONFIG = ConfigParser()
CONFIG.read('config.ini')

CATEGORIES = CONFIG.get('general', 'keywords')

TOKEN = CONFIG.get('general', 'token')

HAPPY = 50
SAD = 30
FOCUED = 30


def start_song(uri):
    print "Trying to start song: {0}".format(uri)
    payload = dict()
    payload['context_uri'] = uri
    payload['offset'] = dict()
    payload['offset']['position'] = 5

    url = 'https://api.spotify.com/v1/me/player/play'
    response = put_req(TOKEN, url, payload)
    print "Request sent"




def get_current_all():
    url = 'https://api.spotify.com/v1/me/player/currently-playing'
    response = get_req(TOKEN, url)
    return response

def get_current_uri(current=get_current_all()):
    try:
        return current['item']['uri']
    except:
        return None


def get_random_song(category):
    songs = CONFIG.get(category,'songs').split(',')
    song = choice(songs)
    song_uri = CONFIG.get(category, song)
    return song_uri

def get_mood_levels():
    moods = dict()
    moods['happy'] = HAPPY
    moods['sad'] = SAD
    moods['focused'] = FOCUSED
    return moods



def process():
    current_song = get_current_all()
    #current_song_uri = current_song['item']['uri']
    current_song_uri = get_current_uri()
    print "Current song URI: {0}".format(current_song_uri)

    print get_random_song('happy')
    
    #print "Get current song"
    #get_current_song()
    #print "Started processing request"
    #start_song("spotify:album:5ht7ItJgpBH7W6vJ5BqpPr")
if __name__ == "__main__":
    process()