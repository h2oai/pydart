import random

import starlette.routing
import starlette.middleware
import starlette.middleware.cors
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


async def serve(ui: UI):
    ui[''] = build()
    await ui.save()


async def websocket_endpoint(websocket: starlette.websockets.WebSocket):
    await websocket.accept()
    await serve(UI('', websocket.send_text))
    while True:
        await serve(UI(await websocket.receive_text(), websocket.send_text))


app: Any = Starlette(
    debug=True,
    routes=[starlette.routing.WebSocketRoute('/nitro', websocket_endpoint)],
    middleware=[starlette.middleware.Middleware(starlette.middleware.cors.CORSMiddleware, allow_origins=['*'])]
)

if __name__ == '__main__':
    uvicorn.run(app, port=11111)
