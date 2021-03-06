from mako.template import Template
from mako.lookup import TemplateLookup
import users
import mako.exceptions
import web
import os.path

ROOT = os.path.dirname(__file__)

lookup = TemplateLookup(directories=[ROOT],
						cache_enabled = False , 
                        module_directory='/tmp/mako_modules',
                        input_encoding='utf-8',
                        output_encoding='utf-8')

def render(uri, **kwargs):
    if 'user' not in kwargs:
        kwargs['user'] = users.get_user()

    try:
        template = lookup.get_template(uri)
        output = template.render_unicode(**kwargs)
        return output
    except:
        return mako.exceptions.html_error_template().render()
