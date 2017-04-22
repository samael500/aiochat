Simple asyncio chat
===================

Simple async websocket chat written on python [aiohttp](http://aiohttp.readthedocs.io/en/stable/)

About blog post `ru` [Простой чат на AioHTTP](https://maks.live/articles/python/prostoi-chat-na-aiohttp/)

### Try it yourself
With [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

#### Pre Requirements

```shell
$ sudo apt-get install fabric
$ vagrant plugin install vagrant-fabric
```

#### Run project

```
$ git clone git@github.com:Samael500/aiochat.git
$ cd aiochat
$ vagrant up
```

### Example result

Open in browser http://10.1.1.111/

### How to use this simple chat?
- Login or create new user
- Join any chat room, or create new
- Send any text messages in room
- Use chat commands by send message with text /help
- Ready, you are awesome ;)
