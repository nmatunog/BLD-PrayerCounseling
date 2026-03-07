#!/usr/bin/env python3
"""Extract text from PowerPoint .pptx (Office Open XML) files."""
import zipfile
import xml.etree.ElementTree as ET
import re
import sys
from pathlib import Path

# OOXML namespaces
NS = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
}

def extract_text_from_pptx(path):
    path = Path(path)
    if not path.exists():
        return []
    out = []
    try:
        with zipfile.ZipFile(path, 'r') as z:
            slide_files = sorted([n for n in z.namelist() if n.startswith('ppt/slides/slide') and n.endswith('.xml')])
            for name in slide_files:
                with z.open(name) as f:
                    root = ET.parse(f).getroot()
                    texts = []
                    for t in root.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}t'):
                        if t.text:
                            texts.append(t.text)
                        if t.tail and t.tail.strip():
                            texts.append(t.tail)
                    slide_num = re.search(r'slide(\d+)', name)
                    num = slide_num.group(1) if slide_num else name
                    block = ' '.join(texts).strip()
                    if block:
                        out.append((num, block))
    except Exception as e:
        out.append(('error', str(e)))
    return out

if __name__ == '__main__':
    for f in sys.argv[1:]:
        print(f'\n=== {f} ===\n')
        for num, text in extract_text_from_pptx(f):
            print(f'--- Slide {num} ---')
            print(text[:2000] + ('...' if len(text) > 2000 else ''))
            print()
