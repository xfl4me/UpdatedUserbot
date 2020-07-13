#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""Per favore vai su my.telegram.org
Effettua l'accesso
Clicca su API development tools
Crea una nuova applicazione, inserendo i dettagli richiesti.""")
APP_ID = int(input("Inserisci l'API ID qui: "))
API_HASH = input("Inserisci l'API HASH qui: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
