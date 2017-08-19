import requests

url = 'https://apps.fedoraproject.org/datagrepper/raw'

def grep(tries=0, **kwargs):
    response = requests.get(url, params=kwargs)
    if not bool(response):
        if tries > 7:
            raise IOError("Failed to %r %r" % (response.url, response))
        for item in grep(tries=tries + 1, **kwargs):
            yield item

    data = response.json()
    pages = data['pages']

    for message in data['raw_messages']:
        yield message

    for page in range(1, pages):
        for attempt in range(20):
            try:
                kwargs['page'] = page
                response = requests.get(url, params=kwargs)
                try:
                    data = response.json()
                except Exception as e:
                    if "Expecting value" in str(e):
                        continue
                    else:
                        raise
            except ValueError as error:
                print "Value Error in json.. retrying %s" % (attempt)
                print error
            else:
                break
        else:
            raise ValueError("Ran out of retries")
        for message in data.get('raw_messages', []):
            yield message


