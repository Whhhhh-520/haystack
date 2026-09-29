# SPDX-FileCopyrightText: 2022-present deepset GmbH <info@deepset.ai>
#
# SPDX-License-Identifier: Apache-2.0

from haystack.utils.url_validation import is_valid_http_url


def test_url_validation_with_valid_http_url():
    url = "http://example.com"
    assert is_valid_http_url(url)


def test_url_validation_with_valid_https_url():
    url = "https://example.com"
    assert is_valid_http_url(url)


def test_url_validation_with_invalid_scheme():
    url = "ftp://example.com"
    assert not is_valid_http_url(url)


def test_url_validation_with_no_scheme():
    url = "example.com"
    assert not is_valid_http_url(url)


def test_url_validation_with_no_netloc():
    url = "http://"
    assert not is_valid_http_url(url)


def test_url_validation_with_empty_string():
    url = ""
    assert not is_valid_http_url(url)


def test_url_validation_with_malformed_ipv6_literal():
    # urlparse raises ValueError on an unterminated IPv6 literal. A predicate
    # must not raise, so this has to be reported as invalid.
    url = "http://[::1"
    assert not is_valid_http_url(url)


def test_url_validation_with_malformed_ipv6_scope():
    url = "http://[fe80::1%25eth0"
    assert not is_valid_http_url(url)


def test_url_validation_does_not_raise_on_any_input():
    # The function is used as a total predicate: no input may escape as an
    # exception, including forms urlparse refuses to parse at all.
    for value in ("http://[", "https://]", "http://[]", "://example.com", "http://a:1:2"):
        assert is_valid_http_url(value) in (True, False)
