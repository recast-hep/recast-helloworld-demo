from flask import Blueprint, render_template, jsonify, request
blueprint = Blueprint('susyhiggs_analysis', __name__, template_folder='templates')

RECAST_ANALYSIS_ID = '19c471ff-2514-eb44-0d82-59563cc38dab'

import json
import requests
import requests
import os
from zipfile import ZipFile
import glob

@blueprint.route('/result/<requestId>/<parameter_pt>')
def result_view(requestId,parameter_pt):
  return render_template('result.html',analysisId = RECAST_ANALYSIS_ID,requestId=requestId,parameter_pt=parameter_pt)
