import random

import starlette.routing
import starlette.staticfiles
import starlette.websockets
import uvicorn
from starlette.applications import Starlette

from h2o_nitro import *

# Original: https://github.com/flutter/codelabs/blob/master/startup_namer/step4_infinite_list/lib/main.dart

prefixes = ['Great', 'Mass', 'Left', 'Break', 'Hard']
suffixes = ['Edge', 'Crack', 'Jet', 'Cloud', 'Trip']
_biggerFont = TextStyle(font_size=18.0)


def _build_suggestions():
    _suggestions = [random.choice(prefixes) + random.choice(suffixes) for _ in range(10)]
    return ListView(
        padding=EdgeInsets.all(16.0),
        # TODO insert Divider() in between
        children=[ListTile(title=Text(suggestion, style=_biggerFont)) for suggestion in _suggestions],
    )


def build():
    return MaterialApp(
        title='Startup Name Generator',
        home=Scaffold(
            app_bar=AppBar(
                title=Text('Startup Name Generator'),
            ),
            body=_build_suggestions(),
        ),
    )


_ui_lookup = {}


async def handle(client_key: Any, request: str) -> str:
    ui = _ui_lookup.get(client_key)
    if ui is None:
        ui = build()
        _ui_lookup[client_key] = ui
    return marshal(ui)


async def websocket_endpoint(websocket: starlette.websockets.WebSocket):
    await websocket.accept()
    while True:
        request = await websocket.receive_text()
        response = await handle(websocket, request)
        await websocket.send_text(response)


app: Any = Starlette(debug=True, routes=[
    starlette.routing.Mount('/', starlette.staticfiles.StaticFiles(directory="../../client/web", html=True)),
    starlette.routing.WebSocketRoute('/nitro', websocket_endpoint),
])

if __name__ == '__main__':
    uvicorn.run(app, port=8000)
