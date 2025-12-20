#!/usr/bin/env python3
"""
Fix PlaceholderImage calls - reduce width, simplify description
"""
import re
import os

def fix_placeholder_images(content):
    """Fix PlaceholderImage calls"""
    
    # Pattern: \PlaceholderImage{description}{filename}{width}
    pattern = r'\\PlaceholderImage\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}'
    
    def replace_func(match):
        desc = match.group(1)
        filename = match.group(2)
        width = match.group(3)
        
        # Shorten description to first 3 words max
        short_desc = ' '.join(desc.split()[:3])
        if len(desc.split()) > 3:
            short_desc = "Img"
        else:
            short_desc = "Img"
        
        # Reduce width
        new_width = width
        if '0.95' in width:
            new_width = '0.7\\textwidth'
        elif '0.9' in width or '0.85' in width:
            new_width = '0.65\\textwidth'
        elif '0.7' in width or '0.6' in width:
            new_width = '0.5\\textwidth'
        
        return f'\\PlaceholderImage{{{short_desc}}}{{{filename}}}{{{new_width}}}'
    
    return re.sub(pattern, replace_func, content)

def main():
    sections_dir = 'sections'
    
    for filename in os.listdir(sections_dir):
        if filename.endswith('.tex') and not filename.endswith('.bak'):
            filepath = os.path.join(sections_dir, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = fix_placeholder_images(content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✓ Fixed: {filename}")
            else:
                print(f"  Skipped: {filename} (no changes)")

if __name__ == '__main__':
    main()
