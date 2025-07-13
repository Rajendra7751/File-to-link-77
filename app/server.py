from aiohttp import web

async def web_server(bot_token):
    async def handle(request):
        return web.Response(text="✅ File-to-Link Bot is Running!", content_type="text/plain")

    app = web.Application()
    app.router.add_get("/", handle)
    return app
