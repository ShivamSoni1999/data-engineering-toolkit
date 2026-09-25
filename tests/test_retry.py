from data_engineering_toolkit.utils.retry import retry

def test_retry_succeeds_after_transient_failures(monkeypatch):
    calls = {"count": 0}
    monkeypatch.setattr("data_engineering_toolkit.utils.retry.time.sleep", lambda _: None)
    @retry(attempts=3, base_delay=0)
    def flaky():
        calls["count"] += 1
        if calls["count"] < 3:
            raise RuntimeError("temporary")
        return "ok"
    assert flaky() == "ok"
    assert calls["count"] == 3
