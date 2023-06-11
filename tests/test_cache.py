def test_default_cache():
    from django_tom_select.cache import cache

    cache.set("key", "value")

    assert cache.get("key") == "value"
