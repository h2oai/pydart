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


async def _increment_counter(ui: UI):
    print('button clicked')


async def on_load(ui: UI):
    _suggestions = [random.choice(prefixes) + random.choice(suffixes) for _ in range(10)]
    ui[''] = MaterialApp(
        title='Startup Name Generator',
        home=Scaffold(
            app_bar=AppBar(
                title=Text('Startup Name Generator'),
            ),
            body=ListView(
                padding=EdgeInsets.all(16.0),
                # TODO insert Divider() in between
                children=[ListTile(title=Text(suggestion, style=_biggerFont)) for suggestion in _suggestions],
            ),
            floating_action_button=FloatingActionButton(
                on_pressed=_increment_counter,
                tooltip='Increment',
                child=Icon(icon=Icons.add),
            ),
        ),
    )
    await ui.save()


nitro = Nitro(on_load)


async def websocket_endpoint(websocket: starlette.websockets.WebSocket):
    host = websocket.client.host
    port = websocket.client.port
    await websocket.accept()
    await nitro.load(websocket.send_text)
    while True:
        await nitro.handle(await websocket.receive_text(), websocket.send_text)


app: Any = Starlette(
    debug=True,
    routes=[starlette.routing.WebSocketRoute('/nitro', websocket_endpoint)],
    middleware=[starlette.middleware.Middleware(starlette.middleware.cors.CORSMiddleware, allow_origins=['*'])]
)

if __name__ == '__main__':
    uvicorn.run(app, port=11111)
