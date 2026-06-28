from backend.models.web_page import WebPage

page = WebPage(
    url="https://www.apple.com",
    source_domain="apple.com",
    title="Apple",
    html="<html><body>Hello</body></html>"
)

print(page)