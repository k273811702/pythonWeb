import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('This is my first project')


class StoryHandler(tornado.web.RequestHandler):
    def get(self, stroy_id):
        self.write("You requested the stroy" + stroy_id)


class BuyHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("buy.wupeiqi.com/index")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler),
         (r"/story/([0-9]+)", IndexHandler)
    ])
    print("123123")
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
