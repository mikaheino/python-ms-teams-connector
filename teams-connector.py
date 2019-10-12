# Code to write into MS TEAMS using Webhook
#
# Version history
# 1.0 12.10.2019  Mika Heino - First working version

import pymsteams
import os

runtime_env = os.environ['RUNTIME_ENV']
dev_ms_teams_webhook = os.environ['DEV_MS_TEAMS_CHANNEL_WEBHOOK']
uat_ms_teams_webhook = os.environ['UAT_MS_TEAMS_CHANNEL_WEBHOOK']
prod_ms_teams_webhook = os.environ['PROD_MS_TEAMS_CHANNEL_WEBHOOK']
ms_teams_title = os.environ['MS_TEAMS_TITLE']
ms_teams_text = os.environ['MS_TEAMS_TEXT']
ms_teams_link_button = os.environ['MS_WEBLINK']

if runtime_env == 'dev':
       TeamsMessage = pymsteams.connectorcard(dev_ms_teams_webhook)
elif runtime_env == 'uat':
       TeamsMessage = pymsteams.connectorcard(uat_ms_teams_webhook)
elif runtime_env == 'prod':
       TeamsMessage = pymsteams.connectorcard(prod_ms_teams_webhook)
else: 
       raise Exception('Environment should be DEV, UAT or PROD')

TeamsMessage.title(ms_teams_title)
TeamsMessage.text(ms_teams_text)
TeamsMessage.addLinkButton(ms_teams_link_button)
TeamsMessage.send()