"""
ViewHandler.py
Parent class for all views

My standard Boiler plate code
"""
import webapp2
import Tools


class Handler(webapp2.RequestHandler):
    """Helper class to make handling easier"""
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = Tools.jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
