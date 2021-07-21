# Python Mercure (pymercure)

The goal of this library is to provide a quick way to publish and consume messages on Mercure. 
If you don't know what Mercure is, take a look here: (https://github.com/dunglas/mercure).

This library is currently under development, 
so if you find any bug or chance of improvement, please open an issue to us. :)

## Installing the library

The library is available on PyPi, so you can install using pip:

     pip3 install pymercure

## Publishing Messages

As mentioned before, the goal is to provide a quick way to publish messages.
And to do so, it's provided the Sync and Async classes.
 
### Sync publisher

```python
import json
from pymercure.publisher.sync import SyncPublisher
from pymercure.message import Message

data = json.dumps({'status': 'test'})
msg = Message(['mytopicname'], data)
publisher = SyncPublisher(
     'http://127.0.0.1:3000/hub',
     'your.Token.Here'
)
publisher.publish(msg)
```

### Async publisher

```python
import json
from pymercure.publisher.async import AsyncPublisher
from pymercure.message import Message

data = json.dumps({'status': 'test'})
msg = Message(['mytopicname'], data)
publisher = AsyncPublisher(
     'http://127.0.0.1:3000/.well-known/mercure',
     'your.Token.Here'
)
publisher.publish(msg)
```

In the async case, the request will be done using the gevent library.

## Consuming messages

To consume messages it's also pretty straight forward. as the consumer runs in a new thread
you don't have to worry about it, you just need to pass a callback function to it:

```python
from pymercure.consumer import Consumer

def callback(message):
    print(message.data)


c = Consumer('http://127.0.0.1:3000/.well-known/mercure', ['mytopicname'], callback, optional_jwt_token)
c.start_consumption()
```

In your callback you will always receive the `Message` object, with the message data and metadata.

## Credits

Created and maintained by Vitor Villar <vitor.luis98@gmail.com>
