import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('This is my first project')
        self.render("html/index.html", list_info={11, 22, 33})


settings = {
    'template_path': 'template',
    'static_path': 'static',
    'static_url_prefix': '/static/',
}

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ], **settings)

    app.listen(80)
    tornado.ioloop.IOLoop.instance().start()
