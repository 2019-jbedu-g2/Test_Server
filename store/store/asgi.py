import os
from channels.asgi import *

os.environ.setdefault("DJANGO_SETTINGS_MODLUE","store.settings")
channel_layer = get_channel_layer()