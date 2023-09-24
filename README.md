一个可以ping爆zkitefly的bot

邀请链接：https://www.kookapp.cn/app/oauth2/authorize?id=22573&permissions=137216&client_id=VrornoWM_xO9rmGz&redirect_uri=&scope=bot

Token：你在想P吃

你可以自行在bot的根目录下新建一个config文件夹，然后在config文件夹里新建config.json，里面填

```
{
    "token": "webhook/websocket bot token",
    "verify_token": "webhook verify token",
    "encrypt_token": "webhook encrypt token",
    "webhook_port": 50000,
    "using_ws": true
}

```

把 webhook/websocket bot token 换成你的 bot 的 token

"using_ws" 的值如果是 true 则使用 Websocket，如果是 false 则使用 Webhook，使用 Webhook 还需还要填入 verify_token 和 encrypt_token

在 config 文件夹下还增加了 config.json.example，你可以把文件名改成 config.json 并填入必要的信息以快速配置 Bot