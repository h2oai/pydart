import 'dart:convert';
import 'dart:io';
import 'dart:html';
import 'package:flutter/material.dart';
import 'package:web_socket_channel/web_socket_channel.dart';
import 'package:flutter/foundation.dart' show kIsWeb;
import 'load.dart';
import 'types.dart';

void main() {
  runApp(const NitroApp());
}

String _getWebSocketEndpoint(String path) {
  if (kIsWeb) {
    final location = window.location;
    final protocol = location.protocol == 'https:' ? 'wss' : 'ws';
    return '$protocol://${location.host}$path';
  }
  throw 'unhandled: get ws endpoint for non-web';
}

class NitroApp extends StatefulWidget {
  const NitroApp({Key? key}) : super(key: key);

  @override
  _NitroAppState createState() => _NitroAppState();
}

class _NitroAppState extends State<NitroApp> {
  final _channel = WebSocketChannel.connect(
    Uri.parse('ws://localhost:11111/nitro'),
  );

  Widget _interpret(String code) {
    final commands = jsonDecode(code);
    if (commands is List<dynamic>) {
      for (final command in commands) {
        if (command is List<dynamic> && command.isNotEmpty) {
          final op = command[0];
          if (op is String) {
            switch (op) {
              case '=': // set
                if (command.length == 3) {
                  final query = command[1];
                  final state = command[2];
                  if (query is String && state is Map<String, dynamic>) {
                    final widget = unmarshal(loaders, state);
                    return widget;
                  }
                }
                break;
              case '~': // del
                break;
            }
          }
        }
      }
      return const Text('List');
    }
    return const Text('TBD');
  }

  @override
  Widget build(BuildContext context) {
    const title = 'Nitro App';
    return MaterialApp(
        title: title,
        home: StreamBuilder(
          stream: _channel.stream,
          builder: (BuildContext context, AsyncSnapshot snapshot) {
            if (snapshot.hasError) {
              return Text('Error: ${snapshot.error}');
            } else {
              switch (snapshot.connectionState) {
                case ConnectionState.none:
                  return const Text('Not connected');
                case ConnectionState.waiting:
                  return const Text('Waiting');
                case ConnectionState.active:
                  return _interpret(snapshot.data);
                case ConnectionState.done:
                  return Text('done: ${snapshot.data}');
              }
            }
          },
        ));
  }

  @override
  void dispose() {
    _channel.sink.close();
    super.dispose();
  }
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // Notice that the counter didn't reset back to zero; the application
        // is not restarted.
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;
  final _channel = WebSocketChannel.connect(
    Uri.parse('wss://echo.websocket.org'),
  );

  @override
  void dispose() {
    _channel.sink.close();
    super.dispose();
  }

  void _incrementCounter() {
    _channel.sink.add('$_counter');
    setState(() {
      // This call to setState tells the Flutter framework that something has
      // changed in this State, which causes it to rerun the build method below
      // so that the display can reflect the updated values. If we changed
      // _counter without calling setState(), then the build method would not be
      // called again, and so nothing would appear to happen.
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Scaffold(
      appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(widget.title),
      ),
      body: Center(
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
        child: Column(
          // Column is also a layout widget. It takes a list of children and
          // arranges them vertically. By default, it sizes itself to fit its
          // children horizontally, and tries to be as tall as its parent.
          //
          // Invoke "debug painting" (press "p" in the console, choose the
          // "Toggle Debug Paint" action from the Flutter Inspector in Android
          // Studio, or the "Toggle Debug Paint" command in Visual Studio Code)
          // to see the wireframe for each widget.
          //
          // Column has various properties to control how it sizes itself and
          // how it positions its children. Here we use mainAxisAlignment to
          // center the children vertically; the main axis here is the vertical
          // axis because Columns are vertical (the cross axis would be
          // horizontal).
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'You have pushed the button this many times:',
            ),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headline4,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
