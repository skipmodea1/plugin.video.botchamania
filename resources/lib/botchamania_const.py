#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import xbmcaddon

#
# Constants
# 
ADDON = "plugin.video.botchamania"
SETTINGS = xbmcaddon.Addon(id=ADDON)
LANGUAGE = SETTINGS.getLocalizedString
IMAGES_PATH = os.path.join(xbmcaddon.Addon(id=ADDON).getAddonInfo('path'), 'resources', 'images')
DATE = "2016-04-17"
VERSION = "1.1.4-SNAPSHOT"

