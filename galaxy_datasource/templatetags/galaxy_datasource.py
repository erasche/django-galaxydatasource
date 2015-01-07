from django import template
import urlparse, urllib
from django.core.urlresolvers import reverse
from ..templates import QUOTED_STRING

register = template.Library()


class TestTagNode(template.Node):

    def render(self, context):
        print self.tokens.split_contents()
        request = context['request']
        kwargs = {
                'target': 'http://example.org',
                'name': 'Exported Data',
                'type': 'tabular',
                }

        for param in self.tokens.split_contents()[1:]:
            (a, b) = param.split('=')
            stringval = QUOTED_STRING.search(b)
            if stringval:
                kwargs[a] = stringval.group('noquotes')
            else:
                kwargs[a] = b
        print kwargs

        params = {
            'URL': request.build_absolute_uri(kwargs['target']),
            'type': kwargs['type'],
            'name': kwargs['name'],
            'sk': request.session._get_or_create_session_key(),
        }
        if 'GALAXY_URL' in request.session:
            galaxy_url = request.session['GALAXY_URL']
        else:
            galaxy_url = None

        url_parts = list(urlparse.urlparse(galaxy_url))
        query = dict(urlparse.parse_qsl(url_parts[4]))
        query.update(params)
        url_parts[4] = urllib.urlencode(query)
        redir = urlparse.urlunparse(url_parts)
        return redir

@register.tag
def gx_url(parser, token):
    t = TestTagNode()
    t.tokens = token
    return t
