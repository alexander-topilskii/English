import os
import re

header_template = """<!DOCTYPE html>
<html lang=\"ru\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>{TITLE}</title>
    <link href=\"https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap\" rel=\"stylesheet\">
    <link rel=\"stylesheet\" href=\"{CSS}\">
</head>
<body>
    <div class=\"container\">
"""

footer = """
    </div>
</body>
</html>
"""

for root, _, files in os.walk('.'):
    for name in files:
        if name.endswith('.html'):
            path = os.path.join(root, name)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
            content = re.sub(r'^<html><body>\n?', '', content)
            content = re.sub(r'</body></html>$', '', content)
            m = re.search(r'<h3>(.*?)</h3>', content)
            title = m.group(1) if m else 'English Pronunciation'
            css = 'style.css' if root == '.' else '../style.css'
            new_content = header_template.replace('{TITLE}', title).replace('{CSS}', css) + content + footer
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
