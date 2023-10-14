from playwright.sync_api import sync_playwright

# Create a Playwright browser instance
with sync_playwright() as p:
    # Launch a browser (in this case, Chromium)
    browser = p.chromium.launch()

    # Create a new browser page
    page = browser.new_page()

    # Navigate to a website
    page.goto('https://example.com')

    # Take a screenshot and save it
    page.screenshot(path='screenshot.png')

    # Close the browser
    browser.close()
