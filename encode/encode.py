import base64


def encode(data):
    encoded_bytes = base64.b64encode(data.encode('utf-8'))
    encoded_string = str(encoded_bytes, 'utf-8')
    return encoded_string


def url_safe_encode(data):
    urlsafe_encoded_bytes = base64.urlsafe_b64encode(data.encode('utf-8'))
    urlsafe_encoded_string = str(urlsafe_encoded_bytes, 'utf-8')
    return urlsafe_encoded_string

