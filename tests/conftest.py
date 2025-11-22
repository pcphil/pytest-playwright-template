"""Shared pytest configuration and fixtures for playwright tests.

Best practices:
- Fixture scope: session for browser, function for page/context to ensure isolation.
- Context per test: avoid shared mutable state; each test gets fresh context.
- Failure handling: screenshots and traces captured on test failure.
- Markers: use @pytest.mark.slow, @pytest.mark.flaky for categorization.
- Secrets: use environment variables (see .env.example); never hardcode credentials.

Supports both:
- Async tests: use @pytest.mark.asyncio with async def test_*
- Sync tests (Page Objects): use sync_api fixtures with def test_*
"""
import os
import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright, Browser as SyncBrowser, BrowserContext as SyncContext, Page as SyncPage
from playwright.async_api import async_playwright, Browser, BrowserContext, Page
from dotenv import load_dotenv

load_dotenv()

# Synchronous fixtures for Page Object tests (sync_api)
@pytest.fixture(scope="session")
def browser_sync():
    """Create a synchronous browser instance for sync tests.
    
    Used with Page Object pattern and sync_api.
    """
    headless = os.getenv("HEADLESS", "true").lower() == "true"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context_sync(browser_sync):
    """Create a new sync browser context for each test."""
    context = browser_sync.new_context()
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context_sync, request):
    """Create a new sync page for each test with failure handling.
    
    Used by Page Object tests. Captures screenshots on failure.
    """
    page = context_sync.new_page()
    
    yield page
    
    # Capture screenshot on test failure
    if hasattr(request, "node") and hasattr(request.node, "rep_call"):
        if request.node.rep_call.failed:
            screenshots_dir = Path("test-screenshots")
            screenshots_dir.mkdir(exist_ok=True)
            page.screenshot(path=screenshots_dir / f"{request.node.name}.png")
    
    page.close()
