# -*- coding: utf-8 -*-

PLUGIN_NAME = u"Search SoundtrackCollector for Release (codebase 4.1)"
PLUGIN_AUTHOR = u"Brian Schweitzer"
PLUGIN_DESCRIPTION = "Search SoundtrackCollector"
PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10"]

from PyQt4 import QtCore
from picard.cluster import Cluster
from picard.util import webbrowser2
from picard.ui.itemviews import BaseAction, register_cluster_action
from picard.ui.itemviews import BaseAction, register_album_action


class SearchSoundtrackCollector(BaseAction):
    NAME = "Search with SoundtrackCollector"
    def callback(self, objs):
        cluster = objs[0]
        url = "http://www.soundtrackcollector.com/catalog/search.php?searchon=all&searchtext="
        url += QtCore.QUrl.toPercentEncoding(cluster.metadata["album"])
        webbrowser2.open(url)
register_cluster_action(SearchSoundtrackCollector())
register_album_action(SearchSoundtrackCollector())
