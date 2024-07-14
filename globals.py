# most of what's required, and the two env variables to run this

# there are some unused imports from testing, too lazy to go throgh
# and remove them, but they don't hurt anything


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

# import env variables
TWINGATE_DOMAIN = os.getenv('TWINGATE_API_DOMAIN')
TWINGATE_API_KEY = os.getenv('TWINGATE_API_KEY')