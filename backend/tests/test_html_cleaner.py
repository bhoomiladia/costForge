from backend.models.web_page import WebPage
from backend.services.cleaner.html_cleaner import HTMLCleaner

html = html = """
<html>

<head>

<style>
.hidden {display:none;}
</style>

<script>
alert("hello");
</script>

</head>

<body>

<h1>Dell XPS 13</h1>

<p>
Intel      Core      Ultra      7
</p>

<p>

16GB RAM

</p>

<!-- Hidden -->

<svg>
...
</svg>

</body>

</html>
"""

page = WebPage(
    url="https://example.com",
    source_domain="example.com",
    title="Demo",
    html=html,
)

cleaner = HTMLCleaner()

print(cleaner.clean(page))