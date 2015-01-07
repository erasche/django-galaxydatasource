import urlparse
import urllib

def export_redirect(request, fetch_url, file_format='tabular', file_name='Export'):

    params = {
        'URL': fetch_url,
        'type': file_format,
        'name': file_name,
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

    # When done, we need to clear galaxy url
    #del(request.session['GALAXY_URL'])
    return redir

def galaxy_export_available(request):
    return 'GALAXY_URL' in request.session
