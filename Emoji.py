import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

EMOJI_UPWARD_TREND = os.getenv('UPWARD_TREND')
EMOJI_DOWNWARD_TREND = os.getenv('DOWNWARD_TREND')

def get_trend(change):
    if change > 0:
        return EMOJI_UPWARD_TREND
    else:
        return EMOJI_DOWNWARD_TREND

