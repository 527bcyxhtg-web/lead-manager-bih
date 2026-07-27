#!/usr/bin/env python3
"""Build the complete LeadFlow BiH index.html"""

CSS = open('/Users/maki/.qwenpaw/workspaces/cloud-orchestrator/lead-manager-repo/style.css').read()
HTML_BODY = open('/Users/maki/.qwenpaw/workspaces/cloud-orchestrator/lead-manager-repo/body.html').read()
JS = open('/Users/maki/.qwenpaw/workspaces/cloud-orchestrator/lead-manager-repo/app.js').read()

html = f"""<!DOCTYPE html>
<html lang="bs">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>LeadFlow BiH — Lead Manager</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>
{HTML_BODY}
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
{JS}
</script>
</body>
</html>"""

with open('/Users/maki/.qwenpaw/workspaces/cloud-orchestrator/lead-manager-repo/index.html', 'w') as f:
    f.write(html)
print(f"Wrote {len(html)} bytes")
