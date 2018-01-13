#!/usr/bin/bash
# -*- coding: utf-8 -*-

import sys
import json
import requests



def put_req(token, url, payload):

    headers = dict()
    headers['Accept'] = 'application/json'
    headers['Content-Type'] = 'application/json'
    headers['Authorization'] = 'Bearer {0}'.format(token)

    try:
        response = requests.put(url, headers=headers, data=json.dumps(payload))
    except Exception as e:
        print e
        sys.exit('Error in put_request')
    content = response
    return response



def get_req(token, url):

    headers = dict()
    headers['Accept'] = 'application/json'
    headers['Content-Type'] = 'application/json'
    headers['Authorization'] = 'Bearer {0}'.format(token)

    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        print e
        sys.exit('Error in put_request')
    content = response.json()
    print content
    return response