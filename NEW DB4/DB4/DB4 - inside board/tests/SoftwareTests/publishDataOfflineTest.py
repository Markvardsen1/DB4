import time

from Systems import components

data = {
                "temp": 5,
                "od": 6,
                }

components.dataPublisher.publishOffline(data)
