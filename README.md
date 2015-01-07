# Django Galaxy Datasource

Simple django module to make it easier to integrate your home built genomic
databases (because everyone rolls their own...) with Galaxy!

This is in **ALPHA** and has a **LOT** of code which will be removed before release.

# Installation

Add the middleware:

```python
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    ...
    'galaxy_datasource.middleware.session',
)
```

Add it to your install apps:

```python
INSTALLED_APPS = (
    ...
    'galaxy_datasource',
    ...
)
```

# Use

Here's an example template. First we load the tag library, then we store a URL
to some data resource as the parameter `data`. This `data` URL variable is then
linked to directly for the raw downloads, or it's passed to the `gx_url` function
for generating a Galaxy link. 

```
{% load galaxy_datasource %}
{% url 'galaxy_datasource:data' as data %}

<a href="{{ data }}">Data (Raw)</a>
<a href="{% gx_url target=data name="Exported Data" type="tabular" %}">Data (Galaxy)</a>
```

## `gx_url`

There are three parameters for the `gx_url` template tag:

| Parameter   | Use/Meaning/Values                                                                                    |
| ----------- | ----------------------------------------------------------------------------------                    |
| `target`    | The url which Galaxy will use to fetch the dataset with just a GET or POST request                    |
| `name`      | Filename, used in Galaxy dataset                                                                      |
| `type`      | Galaxy filetype. This frees you from having to do parameter translation in Galaxy, unless you want to |
