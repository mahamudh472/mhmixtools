from mhmixtools import template_sync

template = "tests/template.html"

target_files = [
    'tests/test1.html',
    'tests/test2.html',
    'tests/test3.html'
]
content_id = "content"
template_sync.render_templates(template, target_files, content_id)