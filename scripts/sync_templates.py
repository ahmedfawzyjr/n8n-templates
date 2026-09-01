import os
import sys
import json
import re
import urllib.parse
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CATEGORY_CONFIG = [
    {
        "folder": "Gmail and Email Automation",
        "slug": "gmail-email-automation",
        "name": "Gmail & Email Automation",
        "icon": "✉️",
        "color": "#EA4335",
        "heading": "What n8n templates are available for Gmail and email automation?",
        "intro": "This collection includes email automation templates for n8n covering Gmail, Outlook, and IMAP. Templates range from AI-powered email labeling and categorization with OpenAI to phishing detection, auto-reply drafting, and daily financial news delivery. Ideal for operations, security, and executive teams looking to streamline email management.",
        "short_desc": "AI email labeling, phishing detection, auto-reply drafts, and Outlook automation."
    },
    {
        "folder": "Telegram",
        "slug": "telegram-bots",
        "name": "Telegram",
        "icon": "✈️",
        "color": "#229ED9",
        "heading": "How can I automate Telegram bots with n8n?",
        "intro": "These n8n templates help you build AI-powered Telegram bots for voice-to-text transcription in 55+ languages, document Q&A, customer support, audio streaming, and personal assistants. Perfect for support teams, content creators, and developers deploying interactive chatbots.",
        "short_desc": "AI chatbots with LangChain, voice-to-text in 55 languages, PDF chat, and Spotify integration."
    },
    {
        "folder": "Google Drive and Google Sheets",
        "slug": "google-drive-sheets",
        "name": "Google Drive & Google Sheets",
        "icon": "📁",
        "color": "#0F9D58",
        "heading": "What are the best n8n templates for Google Drive and Google Sheets?",
        "intro": "Automate Google Workspace with n8n templates for Google Drive and Google Sheets. Workflows include RAG chatbots for Google Docs, automated fine-tuning of OpenAI models, lead qualification, and dynamic data syncing between spreadsheets and third-party tools.",
        "short_desc": "RAG chatbots for documents, OpenAI fine-tuning, lead qualification, and HR screening."
    },
    {
        "folder": "WordPress",
        "slug": "wordpress",
        "name": "WordPress",
        "icon": "🌐",
        "color": "#21759B",
        "heading": "How do I automate WordPress with n8n?",
        "intro": "Streamline content management and publishing with these WordPress automation templates for n8n. Includes AI-driven blog post categorization, SEO content generation with DeepSeek and OpenAI, and embedding AI chatbots directly on WordPress sites.",
        "short_desc": "AI blog categorization, content generation with DeepSeek, and chatbot embedding."
    },
    {
        "folder": "PDF and Document Processing",
        "slug": "pdf-document-processing",
        "name": "PDF & Document Processing",
        "icon": "📄",
        "color": "#DC2626",
        "heading": "What n8n templates exist for PDF and document processing?",
        "intro": "Process documents at scale using n8n workflows for PDF parsing, OCR, and AI-driven data extraction. Templates cover conversational PDF chatbots with source citations, invoice parsing with LlamaParse and Mistral, and study note generation.",
        "short_desc": "PDF Q&A with source quoting, resume parsing, invoice extraction, and OCR pipelines."
    },
    {
        "folder": "Discord",
        "slug": "discord",
        "name": "Discord",
        "icon": "💬",
        "color": "#5865F2",
        "heading": "How can I automate Discord with n8n?",
        "intro": "Connect n8n to Discord for automated community management and content delivery. Templates include AI bot routing, scheduled sports match notifications, daily comic translations, and automated video summary sharing.",
        "short_desc": "AI Discord bot routing, daily comic translations, and YouTube summary sharing."
    },
    {
        "folder": "Database and Storage",
        "slug": "database-storage",
        "name": "Database & Storage",
        "icon": "🗄️",
        "color": "#3B82F6",
        "heading": "What are the best n8n database and storage automation templates?",
        "intro": "Bridge n8n with SQL and NoSQL databases. These templates include conversational interfaces for PostgreSQL and MongoDB, automated SQL query generation from schemas, and storage management workflows.",
        "short_desc": "Natural language SQL generation, PostgreSQL chat, and MongoDB recommendation engines."
    },
    {
        "folder": "DevOps",
        "slug": "devops-server-automation",
        "name": "DevOps / Server Automation",
        "icon": "⚙️",
        "color": "#6366F1",
        "heading": "What n8n templates are available for DevOps and server automation?",
        "intro": "Automate infrastructure monitoring and maintenance tasks with n8n. Templates include disk space watchdogs, Docker Compose controller webhooks, Linux remote updates, and scheduled server health checks.",
        "short_desc": "Disk space monitoring, Docker controller webhooks, Linux updates, and server health checks."
    },
    {
        "folder": "Airtable",
        "slug": "airtable",
        "name": "Airtable",
        "icon": "📊",
        "color": "#F59E0B",
        "heading": "How do I automate Airtable with n8n?",
        "intro": "Leverage Airtable as a flexible backend for your automations. These n8n templates enable AI agents to chat with Airtable bases, synchronize project management and meeting notes from Fireflies.ai, and sync with Obsidian.",
        "short_desc": "AI agents querying Airtable, meeting notes sync from Fireflies, and Obsidian integration."
    },
    {
        "folder": "Notion",
        "slug": "notion",
        "name": "Notion",
        "icon": "📝",
        "color": "#64748B",
        "heading": "What are the best n8n templates for Notion?",
        "intro": "Turn Notion into an automated knowledge hub. Workflows include archiving customer feedback, summarizing Hugging Face research papers, automating competitor intelligence with Exa.ai, and converting emails into tasks.",
        "short_desc": "Customer feedback logging, AI paper summaries, competitor research, and task generation."
    },
    {
        "folder": "Slack",
        "slug": "slack",
        "name": "Slack",
        "icon": "💼",
        "color": "#4A154B",
        "heading": "How can I automate Slack with n8n?",
        "intro": "Enhance team communication and operations with Slack automation workflows for n8n. Includes Gemini-powered Slack bots, automated customer support ticketing with Linear, information monitoring, and automated daily digest delivery.",
        "short_desc": "Gemini AI Slack bots, Linear ticketing sync, info monitoring, and daily digests."
    },
    {
        "folder": "OpenAI and LLMs",
        "slug": "openai-llms",
        "name": "OpenAI & LLMs",
        "icon": "🧠",
        "color": "#10A37F",
        "heading": "What n8n templates are available for OpenAI, LLMs, and AI agents?",
        "intro": "This comprehensive collection features n8n templates for OpenAI, Anthropic Claude, Google Gemini, Mistral, Ollama, DeepSeek, and LangChain agents. Covers autonomous agents, multi-agent evaluation, tool calling, lead enrichment, image generation, audio transcription, and specialized assistants.",
        "short_desc": "Autonomous agents, LangChain tool calling, multi-agent evaluation, lead scoring, and vision pipelines."
    },
    {
        "folder": "WhatsApp",
        "slug": "whatsapp",
        "name": "WhatsApp",
        "icon": "📱",
        "color": "#25D366",
        "heading": "How do I build WhatsApp chatbots with n8n?",
        "intro": "Build business automations and chatbots for WhatsApp using n8n. Templates cover automated sales meeting preparation with Apify, customer inquiry handling, multilingual lead capture, and escalating invoice reminders.",
        "short_desc": "WhatsApp chatbots, meeting prep with Apify, lead capture, and payment reminders."
    },
    {
        "folder": "Instagram Twitter Social Media",
        "slug": "social-media",
        "name": "Instagram, Twitter, Social Media",
        "icon": "📢",
        "color": "#E1306C",
        "heading": "What are the best n8n templates for social media automation?",
        "intro": "Automate social media marketing across Instagram, X (Twitter), LinkedIn, YouTube, TikTok, and Pinterest. Templates include AI content repurposing engines, Instagram DM inboxes with ManyChat, competitor engagement analysis, and scheduled auto-posting.",
        "short_desc": "Omnichannel repurposing, Instagram DM AI inbox, YouTube transcription, and competitor monitoring."
    },
    {
        "folder": "Other Integrations and Use Cases",
        "slug": "other-integrations",
        "name": "Other Integrations & Use Cases",
        "icon": "🔌",
        "color": "#8B5CF6",
        "heading": "What other n8n integration templates are available?",
        "intro": "Explore diverse n8n workflows covering specialized APIs, web scraping, e-commerce, weather alerts, financial analysis, uptime monitoring, and multi-service connectors like Mattermost, Linear, AWS, and Stripe.",
        "short_desc": "Web scraping, e-commerce workflows, Mattermost integration, AWS analysis, and webhook pipelines."
    },
    {
        "folder": "Forms and Surveys",
        "slug": "forms-surveys",
        "name": "Forms & Surveys",
        "icon": "📋",
        "color": "#06B6D4",
        "heading": "How do I automate forms and surveys with n8n?",
        "intro": "Create interactive and conversational form automations using n8n Forms. Templates feature conversational AI interviews, lead qualification with appointment booking, email subscription flows with Airtable, and automated survey feedback analysis.",
        "short_desc": "Conversational AI interviews, appointment qualification, and automated survey analysis."
    },
    {
        "folder": "AI Research RAG and Data Analysis",
        "slug": "ai-research-rag",
        "name": "AI Research, RAG & Data Analysis",
        "icon": "🔬",
        "color": "#EC4899",
        "heading": "What n8n templates exist for AI research, RAG, and data analysis?",
        "intro": "Advanced AI research and data analysis workflows utilizing vector databases (Qdrant, Pinecone, Milvus), autonomous research agents (Apify, o3, Perplexity, Tavily), financial document analyzers, Hacker News aggregators, and Google Analytics AI reporters.",
        "short_desc": "Deep research agents, vector database RAG, financial document analysis, and web scraping pipelines."
    },
    {
        "folder": "HR and Recruitment",
        "slug": "hr-recruitment",
        "name": "HR & Recruitment",
        "icon": "👥",
        "color": "#14B8A6",
        "heading": "What n8n templates are available for HR and recruitment automation?",
        "intro": "Streamline talent acquisition and employee operations with HR automation templates for n8n. Features automated CV screening with OpenAI, BambooHR policy and benefits chatbots, job posting generation, and employee helpdesk bots with voice transcription.",
        "short_desc": "AI CV screening, BambooHR policy chatbots, job description generation, and IT helpdesk bots."
    }
]

FRIENDLY_NODE_NAMES = {
    'n8n-nodes-base.openAi': 'OpenAI',
    '@n8n/n8n-nodes-langchain.agent': 'AI Agent',
    '@n8n/n8n-nodes-langchain.lmChatOpenAi': 'OpenAI Chat',
    '@n8n/n8n-nodes-langchain.lmChatAnthropic': 'Claude',
    '@n8n/n8n-nodes-langchain.lmChatGoogleGemini': 'Gemini',
    '@n8n/n8n-nodes-langchain.lmChatOllama': 'Ollama',
    '@n8n/n8n-nodes-langchain.lmChatMistral': 'Mistral',
    '@n8n/n8n-nodes-langchain.vectorStoreQdrant': 'Qdrant',
    '@n8n/n8n-nodes-langchain.vectorStorePinecone': 'Pinecone',
    '@n8n/n8n-nodes-langchain.memoryBufferWindow': 'Buffer Memory',
    '@n8n/n8n-nodes-langchain.toolHttpRequest': 'HTTP Tool',
    '@n8n/n8n-nodes-langchain.toolCode': 'Code Tool',
    'n8n-nodes-base.gmail': 'Gmail',
    'n8n-nodes-base.gmailTrigger': 'Gmail Trigger',
    'n8n-nodes-base.googleSheets': 'Google Sheets',
    'n8n-nodes-base.googleSheetsTrigger': 'Google Sheets Trigger',
    'n8n-nodes-base.googleDrive': 'Google Drive',
    'n8n-nodes-base.googleDriveTrigger': 'Google Drive Trigger',
    'n8n-nodes-base.googleDocs': 'Google Docs',
    'n8n-nodes-base.telegram': 'Telegram',
    'n8n-nodes-base.telegramTrigger': 'Telegram Trigger',
    'n8n-nodes-base.slack': 'Slack',
    'n8n-nodes-base.slackTrigger': 'Slack Trigger',
    'n8n-nodes-base.discord': 'Discord',
    'n8n-nodes-base.discordTrigger': 'Discord Trigger',
    'n8n-nodes-base.airtable': 'Airtable',
    'n8n-nodes-base.airtableTrigger': 'Airtable Trigger',
    'n8n-nodes-base.notion': 'Notion',
    'n8n-nodes-base.notionTrigger': 'Notion Trigger',
    'n8n-nodes-base.httpRequest': 'HTTP Request',
    'n8n-nodes-base.webhook': 'Webhook',
    'n8n-nodes-base.code': 'Code (JS/Python)',
    'n8n-nodes-base.scheduleTrigger': 'Schedule',
    'n8n-nodes-base.postgres': 'PostgreSQL',
    'n8n-nodes-base.mySql': 'MySQL',
    'n8n-nodes-base.mongoDb': 'MongoDB',
    'n8n-nodes-base.redis': 'Redis',
    'n8n-nodes-base.wordpress': 'WordPress',
    'n8n-nodes-base.set': 'Edit Fields',
    'n8n-nodes-base.if': 'IF Filter',
    'n8n-nodes-base.switch': 'Switch',
    'n8n-nodes-base.splitInBatches': 'Loop / Batch',
    'n8n-nodes-base.readWriteFile': 'File Operations',
    'n8n-nodes-base.respondToWebhook': 'Webhook Response',
    'n8n-nodes-base.hubspot': 'HubSpot',
    'n8n-nodes-base.stripe': 'Stripe',
    'n8n-nodes-base.jira': 'Jira',
    'n8n-nodes-base.github': 'GitHub',
    'n8n-nodes-base.gitlab': 'GitLab',
    'n8n-nodes-base.whatsapp': 'WhatsApp'
}

def get_friendly_node_name(node_type):
    if not node_type:
        return 'Node'
    if node_type in FRIENDLY_NODE_NAMES:
        return FRIENDLY_NODE_NAMES[node_type]
    raw = node_type.split('.')[-1]
    clean = re.sub(r'([A-Z])', r' \1', raw).strip().capitalize()
    return clean

def clean_title(fname):
    base = os.path.splitext(fname)[0]
    base = re.sub(r'^\s*-\s*💻\s*', '', base)
    base = re.sub(r'\s*-\s*-\s*', ' - ', base)
    base = re.sub(r'\s*–\s*', ' - ', base)
    base = re.sub(r'\s*—\s*', ' - ', base)
    base = re.sub(r'\s*-\s*S\s*', "'s ", base)
    base = re.sub(r'\s+', ' ', base).strip()
    return base

def infer_dept(cat, fname, json_data):
    fn_lower = fname.lower()
    cat_lower = cat.lower()
    
    if 'hr' in cat_lower or 'recruitment' in fn_lower or 'cv ' in fn_lower or 'bamboohr' in fn_lower or 'job' in fn_lower:
        return 'HR'
    if 'security' in fn_lower or 'phishing' in fn_lower or 'siem' in fn_lower or 'hmac' in fn_lower or 'guard' in fn_lower or 'audit' in fn_lower or 'vulnerability' in fn_lower:
        return 'Security'
    if 'sales' in fn_lower or 'lead' in fn_lower or 'crm' in fn_lower or 'cold email' in fn_lower or 'pipedrive' in fn_lower or 'hubspot' in fn_lower or 'deal' in fn_lower or 'invoice' in fn_lower or 'meeting' in fn_lower:
        return 'Sales'
    if 'marketing' in fn_lower or 'social' in cat_lower or 'instagram' in fn_lower or 'twitter' in fn_lower or 'seo' in fn_lower or 'content' in fn_lower or 'blog' in fn_lower or 'pinterest' in fn_lower or 'youtube' in fn_lower:
        return 'Marketing'
    if 'support' in fn_lower or 'ticket' in fn_lower or 'helpdesk' in fn_lower or 'customer' in fn_lower or 'feedback' in fn_lower or 'faq' in fn_lower or 'review' in fn_lower:
        return 'Support'
    if 'devops' in cat_lower or 'docker' in fn_lower or 'linux' in fn_lower or 'database' in cat_lower or 'postgres' in fn_lower or 'sql' in fn_lower or 'api' in fn_lower or 'github' in fn_lower or 'gitlab' in fn_lower:
        return 'Engineering'
    if 'executive' in fn_lower or 'ceo' in fn_lower or 'report' in fn_lower or 'kpi' in fn_lower or 'market news' in fn_lower or 'insights' in fn_lower:
        return 'Executive'
    if 'finance' in fn_lower or 'expense' in fn_lower or 'payment' in fn_lower or 'accounting' in fn_lower or 'rent' in fn_lower:
        return 'Finance'
    return 'Operations'

def generate_desc(cat, fname, json_data):
    title = clean_title(fname)
    nodes = json_data.get('nodes', [])
    node_types = [n.get('type', '') for n in nodes]
    node_names = [n.get('name', '') for n in nodes]
    
    integrations = []
    if any('openAi' in t or 'OpenAI' in n for t, n in zip(node_types, node_names)):
        integrations.append('OpenAI')
    if any('google' in t.lower() or 'Google' in n for t, n in zip(node_types, node_names)):
        integrations.append('Google Workspace')
    if any('qdrant' in t.lower() or 'Qdrant' in n for t, n in zip(node_types, node_names)):
        integrations.append('Qdrant')
    if any('telegram' in t.lower() or 'Telegram' in n for t, n in zip(node_types, node_names)):
        integrations.append('Telegram')
    if any('slack' in t.lower() or 'Slack' in n for t, n in zip(node_types, node_names)):
        integrations.append('Slack')
    if any('airtable' in t.lower() or 'Airtable' in n for t, n in zip(node_types, node_names)):
        integrations.append('Airtable')
    if any('notion' in t.lower() or 'Notion' in n for t, n in zip(node_types, node_names)):
        integrations.append('Notion')
    if any('agent' in t.lower() or 'Agent' in n for t, n in zip(node_types, node_names)):
        integrations.append('AI Agent')
    
    int_str = f" using {', '.join(integrations[:3])}" if integrations else ""
    return f"Automated workflow for {title.lower()}{int_str}, streamlining execution and data processing."

def load_curated_metadata():
    meta = {}
    readme_path = os.path.join(ROOT, 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip().startswith('|') and '[' in line and ']' in line and not line.strip().startswith('| Title') and not line.strip().startswith('|---'):
                    parts = [p.strip() for p in line.strip().split('|')[1:-1]]
                    if len(parts) >= 4:
                        t, d, dep, link_md = parts[0], parts[1], parts[2], parts[3]
                        m = re.search(r'\(([^)]+)\)', link_md)
                        if m:
                            path = urllib.parse.unquote(m.group(1)).replace('/', os.sep)
                            fname = os.path.basename(path)
                            meta[fname] = {'title': t, 'desc': d, 'dept': dep}
    
    docs_cat = os.path.join(ROOT, 'docs', 'categories')
    if os.path.exists(docs_cat):
        for cf in os.listdir(docs_cat):
            if cf.endswith('.md'):
                with open(os.path.join(docs_cat, cf), 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.strip().startswith('|') and '[' in line and not line.strip().startswith('| Template') and not line.strip().startswith('|---'):
                            parts = [p.strip() for p in line.strip().split('|')[1:-1]]
                            if len(parts) >= 3:
                                tmpl_md, d, dep = parts[0], parts[1], parts[2]
                                m = re.search(r'\[([^\]]+)\]\(([^)]+)\)', tmpl_md)
                                if m:
                                    t = m.group(1)
                                    path = urllib.parse.unquote(m.group(2)).replace('/', os.sep)
                                    fname = os.path.basename(path)
                                    if fname not in meta:
                                        meta[fname] = {'title': t, 'desc': d, 'dept': dep}
    return meta

def main():
    curated = load_curated_metadata()
    
    all_categories_data = []
    flat_templates_list = []
    total_templates = 0
    node_counter = Counter()
    
    for cfg in CATEGORY_CONFIG:
        folder = cfg['folder']
        cat_dir = os.path.join(ROOT, folder)
        if not os.path.exists(cat_dir):
            print(f"Warning: directory not found: {cat_dir}")
            continue
            
        json_files = sorted([f for f in os.listdir(cat_dir) if f.endswith('.json')])
        templates_in_cat = []
        
        for f in json_files:
            total_templates += 1
            fpath = os.path.join(cat_dir, f)
            with open(fpath, 'r', encoding='utf-8') as jf:
                data = json.load(jf)
            
            nodes = data.get('nodes', [])
            unique_nodes_in_file = set()
            for node in nodes:
                ntype = node.get('type')
                if ntype:
                    node_counter[ntype] += 1
                    unique_nodes_in_file.add(ntype)
            
            clean_name = clean_title(f)
            
            if f in curated:
                t_info = curated[f]
                title = t_info['title'] or clean_name
                desc = t_info['desc']
                dept = t_info['dept']
            else:
                title = clean_name
                desc = generate_desc(folder, f, data)
                dept = infer_dept(folder, f, data)
            
            desc = desc.replace('|', '/').replace('\n', ' ').strip()
            title = title.replace('|', '/').replace('\n', ' ').strip()
            
            enc_folder = urllib.parse.quote(folder)
            enc_file = urllib.parse.quote(f)
            readme_table_link = f"[Link to Template]({enc_folder}/{enc_file})"
            gh_link = f"https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/{enc_folder}/{enc_file}"
            raw_gh_link = f"https://raw.githubusercontent.com/ahmedfawzyjr/N8N-Templates/main/{enc_folder}/{enc_file}"
            
            # Format node tags
            node_names = [get_friendly_node_name(nt) for nt in unique_nodes_in_file]
            # sort unique friendly node names
            node_names = sorted(list(set(node_names)))
            
            tmpl_id = re.sub(r'[^a-z0-9\-]', '', f.lower().replace(' ', '-').replace('.json', ''))
            
            template_obj = {
                'id': tmpl_id,
                'filename': f,
                'title': title,
                'desc': desc,
                'description': desc,
                'dept': dept,
                'department': dept,
                'category': cfg['name'],
                'category_slug': cfg['slug'],
                'category_icon': cfg['icon'],
                'category_color': cfg['color'],
                'readme_link': readme_table_link,
                'gh_link': gh_link,
                'github_url': gh_link,
                'raw_github_url': raw_gh_link,
                'node_count': len(nodes),
                'node_names': node_names,
                'clean_name': clean_name
            }
            
            templates_in_cat.append(template_obj)
            flat_templates_list.append(template_obj)
            
        templates_in_cat.sort(key=lambda x: x['title'].lower())
        
        all_categories_data.append({
            'config': cfg,
            'templates': templates_in_cat,
            'count': len(templates_in_cat)
        })

    print(f"Total Categories: {len(all_categories_data)}, Total Templates: {total_templates}")

    generate_json_and_js_registry(all_categories_data, flat_templates_list, total_templates)
    generate_readme(all_categories_data, total_templates)
    generate_docs_index(all_categories_data, total_templates)
    generate_docs_categories(all_categories_data)
    generate_unique_nodes_txt(node_counter, total_templates)
    generate_static_html(all_categories_data, total_templates)
    
    print("All documentation, interactive registries, and category files synchronized successfully!")

def generate_static_html(categories_data, total_templates):
    # Read layout
    layout_path = os.path.join(ROOT, 'docs', '_layouts', 'default.html')
    if not os.path.exists(layout_path):
        return
    with open(layout_path, 'r', encoding='utf-8') as f:
        layout = f.read()

    # Read docs/index.md
    index_md_path = os.path.join(ROOT, 'docs', 'index.md')
    with open(index_md_path, 'r', encoding='utf-8') as f:
        index_content = f.read()

    # Strip frontmatter
    parts = index_content.split('---', 2)
    body = parts[2] if len(parts) >= 3 else index_content

    # Convert simple markdown headers/formatting in body if any
    body_html = body
    body_html = re.sub(r'## (.*?)\n', r'<h2>\1</h2>\n', body_html)
    body_html = re.sub(r'### (.*?)\n', r'<h3>\1</h3>\n', body_html)
    body_html = body_html.replace('{{ site.baseurl }}', '.')

    # Inject into layout
    page_html = layout
    page_html = page_html.replace('{{ site.baseurl }}', '.')
    page_html = page_html.replace('{{ page.title | default: site.title }}', f'Awesome n8n Templates - {total_templates}+ Workflow Automations')
    page_html = page_html.replace('{{ page.description | default: site.description }}', f'Curated collection of {total_templates}+ n8n automation templates.')
    page_html = page_html.replace('{% seo %}', '<meta name="description" content="Curated collection of 350+ n8n workflow templates.">')
    page_html = page_html.replace('{% include head-custom.html %}', '')
    page_html = page_html.replace('{{ content }}', body_html)
    page_html = page_html.replace("{{ site.time | date: '%Y' }}", '2026')

    static_index_path = os.path.join(ROOT, 'docs', 'index.html')
    with open(static_index_path, 'w', encoding='utf-8') as f:
        f.write(page_html)
    print("docs/index.html static compiled successfully")

    # Also compile categories into .html for standalone local viewing
    docs_cat_dir = os.path.join(ROOT, 'docs', 'categories')
    for cat in categories_data:
        cfg = cat['config']
        md_file = os.path.join(docs_cat_dir, f"{cfg['slug']}.md")
        if os.path.exists(md_file):
            with open(md_file, 'r', encoding='utf-8') as f:
                c_content = f.read()
            c_parts = c_content.split('---', 2)
            c_body = c_parts[2] if len(c_parts) >= 3 else c_content
            c_body_html = c_body
            c_body_html = re.sub(r'## (.*?)\n', r'<h2>\1</h2>\n', c_body_html)
            c_body_html = re.sub(r'### (.*?)\n', r'<h3>\1</h3>\n', c_body_html)
            c_body_html = c_body_html.replace('{{ site.baseurl }}', '..')

            cat_html = layout
            cat_html = cat_html.replace('{{ site.baseurl }}', '..')
            cat_html = cat_html.replace('{{ page.title | default: site.title }}', f'{cfg["name"]} Templates for n8n | Awesome n8n Templates')
            cat_html = cat_html.replace('{{ page.description | default: site.description }}', f'{cat["count"]} n8n {cfg["name"].lower()} templates. {cfg["short_desc"]}')
            cat_html = cat_html.replace('{% seo %}', f'<meta name="description" content="{cat["count"]} n8n {cfg["name"].lower()} templates.">')
            cat_html = cat_html.replace('{% include head-custom.html %}', '')
            cat_html = cat_html.replace('{{ content }}', c_body_html)
            cat_html = cat_html.replace("{{ site.time | date: '%Y' }}", '2026')

            cat_html_path = os.path.join(docs_cat_dir, f"{cfg['slug']}.html")
            with open(cat_html_path, 'w', encoding='utf-8') as f:
                f.write(cat_html)
    print("docs/categories/*.html static compiled successfully")


def generate_json_and_js_registry(categories_data, flat_templates, total_templates):
    # 1. Output templates.json in docs/
    json_path = os.path.join(ROOT, 'docs', 'templates.json')
    cats_summary = []
    for c in categories_data:
        cfg = c['config']
        cats_summary.append({
            'name': cfg['name'],
            'slug': cfg['slug'],
            'icon': cfg['icon'],
            'color': cfg['color'],
            'short_desc': cfg['short_desc'],
            'count': c['count']
        })
        
    full_data = {
        'total': total_templates,
        'categories': cats_summary,
        'templates': flat_templates
    }
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(full_data, f, indent=2, ensure_ascii=False)
    print(f"docs/templates.json generated ({len(flat_templates)} templates)")
    
    # 2. Output templates-data.js in docs/assets/js/
    js_path = os.path.join(ROOT, 'docs', 'assets', 'js', 'templates-data.js')
    os.makedirs(os.path.dirname(js_path), exist_ok=True)
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write('/**\n * n8n Templates Data Store - Auto-generated\n */\n')
        f.write('window.N8N_CATEGORIES = ' + json.dumps(cats_summary, indent=2, ensure_ascii=False) + ';\n\n')
        f.write('window.N8N_TEMPLATES = ' + json.dumps(flat_templates, indent=2, ensure_ascii=False) + ';\n')
    print(f"docs/assets/js/templates-data.js generated")

def generate_readme(categories_data, total_templates):
    readme_path = os.path.join(ROOT, 'README.md')
    lines = []
    
    lines.append('# Awesome n8n Templates [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)')
    lines.append('')
    lines.append(f'> A curated collection of **{total_templates}+** production-ready n8n automation workflow templates, AI agents, RAG pipelines, and enterprise integrations.')
    lines.append('')
    lines.append('Workflows are ready-to-import `.json` files. Download or copy any template and import it directly into your n8n instance (Cloud or self-hosted). Always review and test imported templates before deploying them in production.')
    lines.append('')
    lines.append(f'[![Templates](https://img.shields.io/badge/Templates-{total_templates}+-blue.svg?style=flat-square)](#categories--template-list)')
    lines.append(f'[![Categories](https://img.shields.io/badge/Categories-18-green.svg?style=flat-square)](#categories--template-list)')
    lines.append('[![n8n](https://img.shields.io/badge/n8n-Compatible-FF6D5A.svg?style=flat-square&logo=n8n)](https://n8n.partnerlinks.io/h1pwwf5m4toe)')
    lines.append('[![Interactive Directory](https://img.shields.io/badge/Interactive_Directory-Live-success.svg?style=flat-square)](https://ahmedfawzyjr.github.io/N8N-Templates/)')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('<p align="center">')
    lines.append('  <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe">')
    lines.append('    <img src="https://img.shields.io/badge/n8n_Cloud-Start_Trial-orange?style=for-the-badge" alt="Start an n8n Cloud trial" />')
    lines.append('  </a>')
    lines.append('  <br />')
    lines.append('  <small>* Referral link — this project receives a commission on eligible purchases.</small>')
    lines.append('</p>')
    lines.append('')
    lines.append('## Table of Contents')
    lines.append('')
    lines.append('- [Interactive Web Directory](https://ahmedfawzyjr.github.io/N8N-Templates/)')
    lines.append('- [Categories & Template List](#categories--template-list)')
    for cat in categories_data:
        cfg = cat['config']
        anchor = re.sub(r'[^a-z0-9\- ]', '', cfg['heading'].lower()).replace(' ', '-')
        lines.append(f"  - [{cfg['icon']} {cfg['name']} ({cat['count']})](#{anchor})")
    lines.append('- [Unique Nodes Reference](#unique-nodes-reference)')
    lines.append('- [FAQ](#faq)')
    lines.append('- [Contributing](#contributing)')
    lines.append('- [Sponsors](#sponsors)')
    lines.append('- [Star History](#star-history)')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## Categories & Template List')
    lines.append('')
    
    for cat in categories_data:
        cfg = cat['config']
        lines.append(f"### {cfg['heading']}")
        lines.append('')
        lines.append(f"{cfg['intro']}")
        lines.append('')
        lines.append('| Title | Description | Department | Link |')
        lines.append('|---|---|---|---|')
        for t in cat['templates']:
            lines.append(f"| {t['title']} | {t['desc']} | {t['dept']} | {t['readme_link']} |")
        lines.append('')
        lines.append('---')
        lines.append('')
    
    lines.append('### Unique Nodes Reference')
    lines.append('')
    lines.append('For a complete inventory of all 200+ distinct n8n node types and node packages utilized across these templates, refer to [ALL_unique_nodes.txt](ALL_unique_nodes.txt).')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## FAQ')
    lines.append('')
    lines.append('### How do I import an n8n template from this repository?')
    lines.append('')
    lines.append('Download the `.json` file for any template you want to use. Open your n8n instance (either self-hosted or on [n8n Cloud](https://n8n.partnerlinks.io/h1pwwf5m4toe)), navigate to Workflows, click "Import from File," and select the downloaded JSON file. Or use the [Interactive Web Directory](https://ahmedfawzyjr.github.io/N8N-Templates/) to click "Copy JSON" and paste (Ctrl+V) directly into your n8n canvas!')
    lines.append('<br />')
    lines.append('<small>* Referral link — this project receives a commission on eligible purchases.</small>')
    lines.append('')
    lines.append('### What is n8n and why should I use it for automation?')
    lines.append('')
    lines.append('[n8n](https://n8n.partnerlinks.io/h1pwwf5m4toe) is a fair-code, source-available workflow automation platform that gives you total control over your data and infrastructure. Unlike proprietary alternatives, n8n can be self-hosted on your own servers, supports 400+ native integrations, and includes advanced features like LangChain AI agents, custom JavaScript/Python execution, and sub-workflows.')
    lines.append('<br />')
    lines.append('<small>* Referral link — this project receives a commission on eligible purchases.</small>')
    lines.append('')
    lines.append('### Are these templates free to use?')
    lines.append('')
    lines.append('Yes, all templates in this repository are free and open-source under the MIT license. You are free to download, modify, and use them in both personal and commercial projects.')
    lines.append('')
    lines.append('### Can I contribute my own templates?')
    lines.append('')
    lines.append('Contributions are welcome! If you have built an n8n workflow that solves a useful problem, please submit a pull request. Make sure to export your workflow without credentials or sensitive data, place it in the appropriate category folder, and run the sync script.')
    lines.append('')
    lines.append('### What AI models are supported in these templates?')
    lines.append('')
    lines.append('The AI templates in this collection support a wide range of LLM providers including OpenAI (GPT-4o, GPT-4, o3-mini), Anthropic (Claude 3.5 Sonnet, Claude 3 Opus), Google (Gemini 1.5 Pro/Flash, Gemini 2.0), Mistral AI, DeepSeek, and locally hosted models via Ollama. You can easily swap the model provider in any template by changing the LLM sub-node.')
    lines.append('')
    lines.append('### How often is this repository updated?')
    lines.append('')
    lines.append('This repository is actively maintained with new templates added regularly. Star and watch the repository to stay updated with the latest community workflows.')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## Contributing')
    lines.append('')
    lines.append('Contributions are welcome! Please read the contribution guidelines before submitting a pull request:')
    lines.append('')
    lines.append('1. Export your workflow from n8n as a `.json` file.')
    lines.append('2. **Remove all credentials, API keys, and sensitive data** before committing.')
    lines.append('3. Place the file in the appropriate category directory.')
    lines.append('4. Submit a pull request with a clear description of what the workflow does.')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('### **Sponsors**')
    lines.append('')
    lines.append('Support this project and get your company or tool featured here.')
    lines.append('')
    lines.append('<a href="https://github.com/sponsors/ahmedfawzyjr">')
    lines.append('  <img src="https://img.shields.io/badge/Sponsor-Awesome_n8n_Templates-ea4aaa?style=for-the-badge&logo=github-sponsors" alt="Sponsor this project" />')
    lines.append('</a>')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## Star History')
    lines.append('')
    lines.append('If you find these templates helpful, please consider giving this repository a star!')
    lines.append('')
    lines.append('[![Star History Chart](https://api.star-history.com/svg?repos=ahmedfawzyjr/N8N-Templates&type=Date)](https://star-history.com/#ahmedfawzyjr/N8N-Templates&Date)')
    lines.append('')
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"README.md written successfully ({len(lines)} lines)")

def generate_docs_index(categories_data, total_templates):
    index_path = os.path.join(ROOT, 'docs', 'index.md')
    lines = []
    
    lines.append('---')
    lines.append('layout: default')
    lines.append(f'title: "Awesome n8n Templates - {total_templates}+ Production-Ready Workflows"')
    lines.append(f'description: "Curated directory of {total_templates}+ n8n automation templates. Instant copy-and-paste workflows for AI agents, RAG, Gmail, Telegram, Slack, and DevOps."')
    lines.append('---')
    lines.append('')
    
    # Hero Section
    lines.append('<section class="hero-section">')
    lines.append('  <div class="hero-eyebrow">')
    lines.append('    <span>✨</span>')
    lines.append(f'    <span>Curated Collection of {total_templates}+ Production-Ready n8n Automations</span>')
    lines.append('  </div>')
    lines.append('  <h1 class="hero-title">')
    lines.append('    Supercharge Your Automations with <span class="text-gradient">Awesome n8n Templates</span>')
    lines.append('  </h1>')
    lines.append('  <p class="hero-subtitle">')
    lines.append('    Instant copy-and-paste workflows for AI agents, RAG document intelligence, multi-channel customer bots, CRM syncs, and DevOps monitoring.')
    lines.append('  </p>')
    lines.append('  <div class="hero-actions">')
    lines.append('    <a href="#explorer" class="btn-primary">⚡ Browse 350+ Templates</a>')
    lines.append('    <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe" target="_blank" rel="noopener" class="btn-secondary">🚀 Start n8n Cloud Trial</a>')
    lines.append('    <a href="https://github.com/ahmedfawzyjr/N8N-Templates" target="_blank" rel="noopener" class="btn-secondary">⭐ Star on GitHub</a>')
    lines.append('  </div>')
    lines.append('  <small style="color: var(--text-muted); font-size: 0.8rem; display: block; margin-top: -24px; margin-bottom: 32px;">* Referral link — this project receives a commission on eligible purchases.</small>')
    lines.append('</section>')
    lines.append('')
    
    # Hero Stats Bento
    lines.append('<div class="stats-bento">')
    lines.append('  <div class="stat-box">')
    lines.append('    <div class="stat-icon">⚡</div>')
    lines.append(f'    <div class="stat-number">{total_templates}+</div>')
    lines.append('    <div class="stat-label">Production Workflows</div>')
    lines.append('  </div>')
    lines.append('  <div class="stat-box">')
    lines.append('    <div class="stat-icon">⭐</div>')
    lines.append('    <div class="stat-number">19k+</div>')
    lines.append('    <div class="stat-label">GitHub Stars</div>')
    lines.append('  </div>')
    lines.append('  <div class="stat-box">')
    lines.append('    <div class="stat-icon">📁</div>')
    lines.append(f'    <div class="stat-number">{len(categories_data)}</div>')
    lines.append('    <div class="stat-label">Specialized Hubs</div>')
    lines.append('  </div>')
    lines.append('  <div class="stat-box">')
    lines.append('    <div class="stat-icon">🔌</div>')
    lines.append('    <div class="stat-number">400+</div>')
    lines.append('    <div class="stat-label">Node Integrations</div>')
    lines.append('  </div>')
    lines.append('</div>')
    lines.append('')
    
    # Interactive Explorer Section
    lines.append('<section id="explorer" class="explorer-section">')
    lines.append('  <div class="explorer-header">')
    lines.append('    <div class="search-command-bar">')
    lines.append('      <div class="search-input-wrapper">')
    lines.append('        <span class="search-icon-left">🔍</span>')
    lines.append('        <input type="text" id="template-search-input" class="search-input" placeholder="Search templates by name, integration (OpenAI, Gmail, Qdrant), or keyword..." aria-label="Search templates">')
    lines.append('        <button id="search-clear-btn" class="search-clear-btn" title="Clear search">✕</button>')
    lines.append('        <span class="search-shortcut-hint">Ctrl + K</span>')
    lines.append('      </div>')
    lines.append('    </div>')
    lines.append('')
    lines.append('    <!-- Category Filter Pills -->')
    lines.append('    <div class="filter-pills-scroll" id="category-pills-container">')
    lines.append('      <!-- Injected dynamically by app.js -->')
    lines.append('    </div>')
    lines.append('')
    lines.append('    <!-- Secondary Filters & View Controls -->')
    lines.append('    <div class="filter-controls-row">')
    lines.append('      <div class="filter-secondary-group">')
    lines.append('        <div class="custom-select-wrapper">')
    lines.append('          <select id="department-filter-select" class="custom-select" aria-label="Filter by department">')
    lines.append('            <option value="all">🏢 All Departments</option>')
    lines.append('            <option value="marketing">📢 Marketing</option>')
    lines.append('            <option value="sales">💼 Sales</option>')
    lines.append('            <option value="engineering">⚙️ Engineering</option>')
    lines.append('            <option value="security">🛡️ Security</option>')
    lines.append('            <option value="hr">👥 HR & Recruiting</option>')
    lines.append('            <option value="support">💬 Support</option>')
    lines.append('            <option value="finance">💰 Finance</option>')
    lines.append('            <option value="executive">👔 Executive</option>')
    lines.append('            <option value="operations">⚡ Operations</option>')
    lines.append('          </select>')
    lines.append('        </div>')
    lines.append('')
    lines.append('        <div class="custom-select-wrapper">')
    lines.append('          <select id="sort-by-select" class="custom-select" aria-label="Sort templates">')
    lines.append('            <option value="title-asc">Sort: Name (A to Z)</option>')
    lines.append('            <option value="title-desc">Sort: Name (Z to A)</option>')
    lines.append('            <option value="nodes-desc">Sort: Node Count (High to Low)</option>')
    lines.append('          </select>')
    lines.append('        </div>')
    lines.append('      </div>')
    lines.append('')
    lines.append('      <div class="filter-secondary-group">')
    lines.append('        <div class="view-toggle-btns">')
    lines.append('          <button id="view-grid-btn" class="view-btn active" title="Grid View">🔲 Grid</button>')
    lines.append('          <button id="view-table-btn" class="view-btn" title="Table View">☰ Table</button>')
    lines.append('        </div>')
    lines.append('      </div>')
    lines.append('    </div>')
    lines.append('')
    lines.append('    <div class="results-status-bar">')
    lines.append(f'      <span id="results-counter-text" class="results-counter">Showing <strong>{total_templates}</strong> of <strong>{total_templates}</strong> templates</span>')
    lines.append('      <button id="reset-filters-btn" class="reset-filters-btn">✕ Reset Filters</button>')
    lines.append('    </div>')
    lines.append('  </div>')
    lines.append('')
    lines.append('  <!-- Dynamic Template Cards Grid Container -->')
    lines.append('  <div id="templates-grid-container" class="templates-grid">')
    lines.append('    <!-- Cards rendered via JavaScript -->')
    lines.append('  </div>')
    lines.append('')
    lines.append('  <!-- Dynamic Template Table Container -->')
    lines.append('  <div id="templates-table-wrapper" class="templates-table-container">')
    lines.append('    <table class="modern-table">')
    lines.append('      <thead>')
    lines.append('        <tr>')
    lines.append('          <th>Workflow Name</th>')
    lines.append('          <th>Category</th>')
    lines.append('          <th>Dept</th>')
    lines.append('          <th>Description</th>')
    lines.append('          <th>Actions</th>')
    lines.append('        </tr>')
    lines.append('      </thead>')
    lines.append('      <tbody id="templates-table-tbody">')
    lines.append('        <!-- Rows rendered via JavaScript -->')
    lines.append('      </tbody>')
    lines.append('    </table>')
    lines.append('  </div>')
    lines.append('</section>')
    lines.append('')
    
    # Categories Directory Bento Grid
    lines.append('<section id="categories" style="margin-top: 64px;">')
    lines.append('  <h2>Browse by Category Hub</h2>')
    lines.append('  <p>Deep-dive into 18 dedicated collections categorized for specific tools, platforms, and use-cases.</p>')
    lines.append('  <div class="categories-bento-grid">')
    for cat in categories_data:
        cfg = cat['config']
        lines.append(f'    <a href="{{{{ site.baseurl }}}}/categories/{cfg["slug"]}" class="category-bento-card" style="--cat-accent: {cfg["color"]};">')
        lines.append('      <div class="cat-card-header">')
        lines.append(f'        <span class="cat-card-icon">{cfg["icon"]}</span>')
        lines.append(f'        <span class="cat-card-count">{cat["count"]} templates</span>')
        lines.append('      </div>')
        lines.append(f'      <div class="cat-card-title">{cfg["name"]}</div>')
        lines.append(f'      <div class="cat-card-desc">{cfg["short_desc"]}</div>')
        lines.append('    </a>')
    lines.append('  </div>')
    lines.append('</section>')
    lines.append('')
    
    # Quickstart Guide
    lines.append('<section id="how-it-works" style="margin-top: 64px;">')
    lines.append('  <h2>Quickstart: Import Workflows in 4 Simple Steps</h2>')
    lines.append('  <p>How to use and customize any workflow template from this library inside n8n:</p>')
    lines.append('  <div class="steps-container">')
    lines.append('    <div class="step-card">')
    lines.append('      <div class="step-number">01</div>')
    lines.append('      <div class="step-title">Choose Template</div>')
    lines.append('      <div class="step-text">Search the directory and select the workflow that fits your business goal.</div>')
    lines.append('    </div>')
    lines.append('    <div class="step-card">')
    lines.append('      <div class="step-number">02</div>')
    lines.append('      <div class="step-title">Copy or Download</div>')
    lines.append('      <div class="step-text">Click "⚡ Copy JSON" for direct canvas clipboard import or download the .json file.</div>')
    lines.append('    </div>')
    lines.append('    <div class="step-card">')
    lines.append('      <div class="step-number">03</div>')
    lines.append('      <div class="step-title">Paste into n8n</div>')
    lines.append('      <div class="step-text">Open your n8n canvas (Cloud or self-hosted) and press Ctrl+V to paste the workflow.</div>')
    lines.append('    </div>')
    lines.append('    <div class="step-card">')
    lines.append('      <div class="step-number">04</div>')
    lines.append('      <div class="step-title">Connect & Deploy</div>')
    lines.append('      <div class="step-text">Attach your API credentials to the nodes, run a test execution, and activate!</div>')
    lines.append('    </div>')
    lines.append('  </div>')
    lines.append('</section>')
    lines.append('')
    
    # Why n8n Bento Section
    lines.append('<section style="margin-top: 64px;">')
    lines.append('  <h2>Why Automate with n8n?</h2>')
    lines.append('  <p>n8n is the premier source-available workflow automation engine for modern technical teams:</p>')
    lines.append('  <div class="features-bento">')
    lines.append('    <div class="feature-box">')
    lines.append('      <div class="feature-box-icon">🔓</div>')
    lines.append('      <div class="feature-box-title">Self-Hostable & Private</div>')
    lines.append('      <p>Host on your own VPC, Docker, or Kubernetes clusters. Total control over your proprietary data and API keys.</p>')
    lines.append('    </div>')
    lines.append('    <div class="feature-box">')
    lines.append('      <div class="feature-box-icon">🤖</div>')
    lines.append('      <div class="feature-box-title">Native AI & LangChain</div>')
    lines.append('      <p>Built-in nodes for Autonomous Agents, LLM tool calling, Vector Stores (Qdrant, Pinecone), and Memory.</p>')
    lines.append('    </div>')
    lines.append('    <div class="feature-box">')
    lines.append('      <div class="feature-box-icon">🔌</div>')
    lines.append('      <div class="feature-box-title">400+ Native Integrations</div>')
    lines.append('      <p>Connect seamlessly to Slack, Google Workspace, GitHub, Postgres, HubSpot, Discord, Telegram, and custom APIs.</p>')
    lines.append('    </div>')
    lines.append('    <div class="feature-box">')
    lines.append('      <div class="feature-box-icon">💻</div>')
    lines.append('      <div class="feature-box-title">Custom JS & Python Code</div>')
    lines.append('      <p>Execute custom JavaScript and Python scripts directly within nodes for advanced data transformations.</p>')
    lines.append('    </div>')
    lines.append('  </div>')
    lines.append('</section>')
    lines.append('')
    
    # FAQ Section
    lines.append('<section id="faq" style="margin-top: 64px;">')
    lines.append('  <h2>Frequently Asked Questions</h2>')
    lines.append('  <p>Everything you need to know about importing and executing these templates.</p>')
    lines.append('  <div class="faq-container">')
    lines.append('    <div class="faq-item">')
    lines.append('      <div class="faq-question">')
    lines.append('        <span>How do I import a workflow directly into n8n?</span>')
    lines.append('        <span class="faq-chevron">▼</span>')
    lines.append('      </div>')
    lines.append('      <div class="faq-answer">')
    lines.append('        Click the "⚡ Copy JSON" button on any template card. Then open your n8n workflow canvas in your browser and press <code>Ctrl + V</code> (or <code>Cmd + V</code> on macOS). The nodes and connections will appear immediately on your canvas!')
    lines.append('      </div>')
    lines.append('    </div>')
    lines.append('    <div class="faq-item">')
    lines.append('      <div class="faq-question">')
    lines.append('        <span>Are these templates compatible with n8n Cloud and self-hosted?</span>')
    lines.append('        <span class="faq-chevron">▼</span>')
    lines.append('      </div>')
    lines.append('      <div class="faq-answer">')
    lines.append('        Yes, all 350+ templates in this repository are standard n8n JSON exports compatible with n8n Cloud and self-hosted n8n (Docker / npm / Kubernetes) running version 1.x or later.')
    lines.append('      </div>')
    lines.append('    </div>')
    lines.append('    <div class="faq-item">')
    lines.append('      <div class="faq-question">')
    lines.append('        <span>Do I need to enter my own API keys?</span>')
    lines.append('        <span class="faq-chevron">▼</span>')
    lines.append('      </div>')
    lines.append('      <div class="faq-answer">')
    lines.append('        Yes. All templates in this repository are completely sanitized with zero hardcoded API keys or sensitive credentials. After importing, open the credential dropdown on each node (e.g. OpenAI, Telegram, Gmail) and attach your own credentials.')
    lines.append('      </div>')
    lines.append('    </div>')
    lines.append('    <div class="faq-item">')
    lines.append('      <div class="faq-question">')
    lines.append('        <span>Can I use these templates in commercial client projects?</span>')
    lines.append('        <span class="faq-chevron">▼</span>')
    lines.append('      </div>')
    lines.append('      <div class="faq-answer">')
    lines.append('        Yes! All templates in this repository are released under the open-source MIT license. You can freely use, modify, and integrate them into internal systems or client solutions.')
    lines.append('      </div>')
    lines.append('    </div>')
    lines.append('    <div class="faq-item">')
    lines.append('      <div class="faq-question">')
    lines.append('        <span>What AI models and providers can I use?</span>')
    lines.append('        <span class="faq-chevron">▼</span>')
    lines.append('      </div>')
    lines.append('      <div class="faq-answer">')
    lines.append('        The AI templates support OpenAI (GPT-4o, o3-mini), Anthropic (Claude 3.5 Sonnet), Google Gemini, DeepSeek, Mistral, and local Ollama models. Simply swap the Model sub-node to connect any provider you prefer.')
    lines.append('      </div>')
    lines.append('    </div>')
    lines.append('  </div>')
    lines.append('</section>')
    lines.append('')
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print("docs/index.md written successfully")

def generate_docs_categories(categories_data):
    docs_cat_dir = os.path.join(ROOT, 'docs', 'categories')
    os.makedirs(docs_cat_dir, exist_ok=True)
    
    for cat in categories_data:
        cfg = cat['config']
        cat_file = os.path.join(docs_cat_dir, f"{cfg['slug']}.md")
        lines = []
        
        lines.append('---')
        lines.append('layout: default')
        lines.append(f'title: "{cfg["name"]} Templates for n8n | Awesome n8n Templates"')
        lines.append(f'description: "{cat["count"]} n8n {cfg["name"].lower()} templates. {cfg["short_desc"]}"')
        lines.append('---')
        lines.append('')
        
        # Breadcrumbs
        lines.append('<nav style="margin-bottom: 24px; font-size: 0.9rem; color: var(--text-muted);">')
        lines.append('  <a href="{{ site.baseurl }}/" style="color: var(--text-secondary);">Home</a> / ')
        lines.append('  <a href="{{ site.baseurl }}/#categories" style="color: var(--text-secondary);">Categories</a> / ')
        lines.append(f'  <span style="color: var(--n8n-coral);">{cfg["name"]}</span>')
        lines.append('</nav>')
        lines.append('')
        
        # Category Hero Banner
        lines.append('<div style="background: var(--surface-glass-card); border: 1px solid var(--border-glass); border-radius: var(--radius-xl); padding: 36px 32px; box-shadow: var(--shadow-glass); position: relative; overflow: hidden; margin-bottom: 40px;">')
        lines.append(f'  <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: {cfg["color"]};"></div>')
        lines.append('  <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px; margin-bottom: 16px;">')
        lines.append('    <div style="display: flex; align-items: center; gap: 14px;">')
        lines.append(f'      <span style="font-size: 2.5rem;">{cfg["icon"]}</span>')
        lines.append(f'      <h1 style="margin: 0; font-size: clamp(1.8rem, 4vw, 2.6rem);">{cfg["name"]}</h1>')
        lines.append('    </div>')
        lines.append(f'    <span class="nav-badge-pill" style="font-size: 0.85rem; padding: 6px 14px;">{cat["count"]} Workflows</span>')
        lines.append('  </div>')
        lines.append(f'  <p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 820px; line-height: 1.6; margin-bottom: 24px;">{cfg["intro"]}</p>')
        lines.append('  <div style="display: flex; gap: 12px; flex-wrap: wrap;">')
        lines.append('    <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe" target="_blank" rel="noopener" class="btn-primary">🚀 Start n8n Cloud Trial</a>')
        lines.append(f'    <a href="{{{{ site.baseurl }}}}/?cat={cfg["slug"]}#explorer" class="btn-secondary">⚡ Filter in Explorer</a>')
        lines.append('  </div>')
        lines.append('  <small style="color: var(--text-muted); font-size: 0.75rem; display: block; margin-top: 10px;">* Referral link — this project receives a commission on eligible purchases.</small>')
        lines.append('</div>')
        lines.append('')
        
        # Category Templates Grid & Table View
        lines.append(f'<h2>All {cat["count"]} {cfg["name"]} Workflows</h2>')
        lines.append(f'<p>Download JSON files or copy directly to your clipboard for instant n8n canvas import.</p>')
        lines.append('')
        
        lines.append('<div class="templates-grid" style="margin-top: 24px;">')
        for t in cat['templates']:
            node_pills = ''.join([f'<span class="node-tag">{n}</span>' for n in t['node_names'][:3]])
            more_nodes = f'<span class="node-tag">+{len(t["node_names"]) - 3}</span>' if len(t['node_names']) > 3 else ''
            
            lines.append('  <div class="template-card">')
            lines.append('    <div class="template-card-inner">')
            lines.append('      <div class="card-top-row">')
            lines.append(f'        <span class="category-chip">{cfg["icon"]} {cfg["name"]}</span>')
            lines.append(f'        <span class="dept-badge">{t["dept"]}</span>')
            lines.append('      </div>')
            lines.append(f'      <h3 class="card-title" onclick="window.n8nExplorer.openModal(\'{t["id"]}\')">{t["title"]}</h3>')
            lines.append(f'      <p class="card-desc">{t["desc"]}</p>')
            lines.append('      <div class="card-nodes-list">')
            lines.append(f'        {node_pills} {more_nodes}')
            lines.append('      </div>')
            lines.append('      <div class="card-actions">')
            lines.append(f'        <button class="btn-card-primary" onclick="window.n8nExplorer.copyForN8n(\'{t["id"]}\')">⚡ Copy JSON</button>')
            lines.append(f'        <button class="btn-card-icon" onclick="window.n8nExplorer.openModal(\'{t["id"]}\')" title="Inspect">👁️</button>')
            lines.append(f'        <a href="{t["gh_link"]}" target="_blank" rel="noopener" class="btn-card-icon" title="View on GitHub">↗️</a>')
            lines.append('      </div>')
            lines.append('    </div>')
            lines.append('  </div>')
        lines.append('</div>')
        lines.append('')
        
        # Category switcher footer
        lines.append('<div style="margin-top: 64px; padding-top: 32px; border-top: 1px solid var(--border-glass);">')
        lines.append('  <h3>Explore Other Category Hubs</h3>')
        lines.append('  <div class="filter-pills-scroll" style="margin-top: 16px;">')
        for other_cat in categories_data:
            o_cfg = other_cat['config']
            active_style = 'style="border-color: var(--n8n-coral);"' if o_cfg['slug'] == cfg['slug'] else ''
            lines.append(f'    <a href="{{{{ site.baseurl }}}}/categories/{o_cfg["slug"]}" class="filter-pill" {active_style}>{o_cfg["icon"]} {o_cfg["name"]} ({other_cat["count"]})</a>')
        lines.append('  </div>')
        lines.append('</div>')
        lines.append('')
        
        with open(cat_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        print(f"Generated docs/categories/{cfg['slug']}.md ({cat['count']} templates)")

def generate_unique_nodes_txt(node_counter, total_workflows):
    txt_path = os.path.join(ROOT, 'ALL_unique_nodes.txt')
    lines = []
    
    lines.append('# n8n Awesome Templates - Complete Unique Nodes Catalog')
    lines.append(f'Total Workflows Analyzed: {total_workflows}')
    lines.append(f'Total Unique Node Types: {len(node_counter)}')
    lines.append(f'Total Node Instances in Repository: {sum(node_counter.values())}')
    lines.append('=' * 80)
    lines.append('')
    lines.append('## All Unique Node Types (Alphabetical Order)')
    lines.append('')
    for node_type in sorted(node_counter.keys()):
        lines.append(f'- {node_type} (used in {node_counter[node_type]} nodes)')
        
    lines.append('')
    lines.append('=' * 80)
    lines.append('')
    lines.append('## Top 40 Most Frequently Used Node Types')
    lines.append('')
    for rank, (ntype, count) in enumerate(node_counter.most_common(40), 1):
        lines.append(f'{rank:2d}. {ntype:65s} : {count:4d} instances')
        
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"ALL_unique_nodes.txt generated successfully ({len(node_counter)} unique node types)")

if __name__ == '__main__':
    main()
