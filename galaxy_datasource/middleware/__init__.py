import urllib

class session(object):

    def process_request(self, request):
        # TODO: check how this behaves from server side...
        # Check if a new GALAXY_URL key

        # If the user visits this URL and has a GALAXY_URL parameter, this is
        # stuffed into the session data
        if 'GALAXY_URL' in request.GET:
            request.session['GALAXY_URL'] = urllib.unquote(request.GET['GALAXY_URL'])
        # If they haven't come here from a Galaxy portal, GALAXY_URL will be
        # empty in both session/GET

