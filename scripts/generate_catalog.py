import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_CATALOG = os.path.join(BASE_DIR, "workflows_catalog.json")

def scan_workflows():
    catalog = []
    exclude = {'.git', '.github', 'node_modules', 'scripts', 'test', 'docs', 'assets'}

    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in exclude]
        rel_dir = os.path.relpath(root, BASE_DIR)
        category = rel_dir.split(os.sep)[0] if rel_dir != '.' else 'Root'

        if rel_dir == '.':
            continue

        for file in files:
            if file.endswith('.json') and file not in ('package.json', 'package-lock.json', 'workflows_catalog.json', 'vercel.json'):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    nodes = data.get('nodes', [])
                    node_types = sorted(list(set(n.get('type', '') for n in nodes if 'type' in n)))
                    workflow_name = data.get('name') or os.path.splitext(file)[0]

                    catalog.append({
                        "name": workflow_name,
                        "file": file,
                        "category": category,
                        "relative_path": os.path.relpath(full_path, BASE_DIR).replace('\\', '/'),
                        "nodes_count": len(nodes),
                        "node_types": node_types[:10],
                        "active": data.get('active', False)
                    })
                except Exception:
                    continue

    catalog.sort(key=lambda x: (x['category'], x['name']))
    return catalog

def main():
    catalog = scan_workflows()
    print(f"Discovered {len(catalog)} valid n8n workflow templates across all categories.")
    with open(OUTPUT_CATALOG, 'w', encoding='utf-8') as f:
        json.dump({
            "total_templates": len(catalog),
            "generated_at": "2026-09-10",
            "categories": sorted(list(set(w['category'] for w in catalog))),
            "templates": catalog
        }, f, indent=2, ensure_ascii=False)
    print(f"Catalog generated successfully at {OUTPUT_CATALOG}")

if __name__ == '__main__':
    main()
