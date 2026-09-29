# SPDX-FileCopyrightText: 2022-present deepset GmbH <info@deepset.ai>
#
# SPDX-License-Identifier: Apache-2.0

from urllib.parse import urlparse


def is_valid_http_url(url: str) -> bool:
    """
    Check if a URL is a valid HTTP/HTTPS URL.

    Returns ``False`` instead of raising when the input cannot be parsed at all:
    ``urlparse`` raises ``ValueError`` for malformed IPv6 literals such as
    ``"http://[::1"``. Callers can therefore treat this as a total predicate.
    """
    try:
        r = urlparse(url)
    except ValueError:
        return False
    return all([r.scheme in ["http", "https"], r.netloc])
