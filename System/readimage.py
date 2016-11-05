from ImageProccessing import DesktopParser, Watcher

bbox = DesktopParser.getGameView()
Watcher.displayGameFeed(bbox)
