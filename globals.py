#import all of the main libraries needed to access files, environment variables, and run the app, generate uuids, deal with collections and API requests, graphql queries, and json objects, and access the docker daemon


import os, random, json, collections, requests, sys, uuid
from datetime import date, datetime, timedelta
from math import floor
from flask import Flask, render_template, request, url_for, flash, redirect, make_response, send_file
from werkzeug.exceptions import abort,HTTPException
from werkzeug.utils import secure_filename
from waitress import serve
import traceback
import graphql
from ariadne import *

#import env variables
TWINGATE_DOMAIN = os.getenv('TWINGATE_API_DOMAIN')
TWINGATE_API_KEY = os.getenv('TWINGATE_API_KEY')