from bs4 import BeautifulSoup, Comment

from backend.models.web_page import WebPage

class HTMLCleaner:
    """
    Cleans raw HTML and extracts visible text.
    """
    REMOVABLE_TAGS = (
    "script",
    "style",
    "noscript",
    "svg",
    "iframe",
    "canvas",
    )

    def clean(self, page: WebPage) -> str:
        """
        Convert raw HTML into clean text.
        """
        soup = BeautifulSoup(page.html, "html.parser")

        for tag in soup(self.REMOVABLE_TAGS):
            tag.decompose()
        for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
            comment.extract()
        text = soup.get_text(separator="\n")

        cleaned_lines = []

        for line in text.splitlines():
            line = " ".join(line.split())

            if line:
                cleaned_lines.append(line)

        return "\n".join(cleaned_lines)