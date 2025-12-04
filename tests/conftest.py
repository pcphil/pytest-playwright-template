"""Shared pytest configuration and fixtures for playwright tests.

Best practices:
- Fixture scope: session for browser, function for page/context to ensure isolation.
- Context per test: avoid shared mutable state; each test gets fresh context.
- Failure handling: screenshots, traces, and videos captured on test failure.
- Markers: use @pytest.mark.slow, @pytest.mark.flaky for categorization.
- Secrets: use environment variables (see .env.example); never hardcode credentials.
- Waits: use Playwright's built-in wait_for_* methods; avoid explicit sleeps.
- Selectors: use robust selectors (role-based > test-id > css); avoid flaky XPath.

Supports both:
- Async tests: use @pytest.mark.asyncio with async def test_*
- Sync tests (Page Objects): use sync_api fixtures with def test_*
"""
import os
import pytest
from pathlib import Path
from datetime import datetime
from playwright.sync_api import sync_playwright, Browser as SyncBrowser, BrowserContext as SyncContext, Page as SyncPage
from playwright.async_api import async_playwright, Browser, BrowserContext, Page
from dotenv import load_dotenv

load_dotenv()

# Artifact directories
ARTIFACTS_DIR = Path("test-artifacts")
SCREENSHOTS_DIR = ARTIFACTS_DIR / "screenshots"
TRACES_DIR = ARTIFACTS_DIR / "traces"
VIDEOS_DIR = ARTIFACTS_DIR / "videos"

for directory in [SCREENSHOTS_DIR, TRACES_DIR, VIDEOS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)


# Synchronous fixtures for Page Object tests (sync_api)
@pytest.fixture(scope="session")
def browser_sync():
    """Create a synchronous browser instance for sync tests.
    
    Used with Page Object pattern and sync_api.
    Scope: session — single browser instance for all tests (faster).
    """
    headless = os.getenv("HEADLESS", "true").lower() == "true"
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=headless,
            args=["--disable-blink-features=AutomationControlled"]
        )
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context_sync(browser_sync, request):
    """Create a new sync browser context for each test with trace recording.
    
    Scope: function — fresh context per test ensures isolation.
    Records traces for failed tests to aid debugging.
    """
    # Enable trace recording for debugging
    context = browser_sync.new_context(
        record_video_dir=str(VIDEOS_DIR) if os.getenv("RECORD_VIDEO") == "true" else None
    )
    context.tracing.start(screenshots=True, snapshots=True)
    
    yield context
    
    # Save trace on test failure
    if request.node.rep_call.failed if hasattr(request.node, "rep_call") else False:
        trace_path = TRACES_DIR / f"{request.node.name}.zip"
        context.tracing.stop(path=str(trace_path))
    else:
        context.tracing.stop()
    
    context.close()


@pytest.fixture(scope="function")
def page(context_sync, request):
    """Create a new sync page for each test with comprehensive failure handling.
    
    Used by Page Object tests. Captures screenshots and videos on failure.
    Scope: function — fresh page per test.
    """
    page = context_sync.new_page()
    
    yield page
    
    # Capture screenshot on test failure
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = SCREENSHOTS_DIR / f"{request.node.name}_{timestamp}.png"
        try:
            page.screenshot(path=str(screenshot_path), full_page=True)
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")
    
    page.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test result outcome for fixture decision-making."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
