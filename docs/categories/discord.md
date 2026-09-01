---
layout: default
title: "Discord Templates for n8n | Awesome n8n Templates"
description: "4 n8n discord templates. AI Discord bot routing, daily comic translations, and YouTube summary sharing."
---

<nav style="margin-bottom: 24px; font-size: 0.9rem; color: var(--text-muted);">
  <a href="{{ site.baseurl }}/" style="color: var(--text-secondary);">Home</a> / 
  <a href="{{ site.baseurl }}/#categories" style="color: var(--text-secondary);">Categories</a> / 
  <span style="color: var(--n8n-coral);">Discord</span>
</nav>

<div style="background: var(--surface-glass-card); border: 1px solid var(--border-glass); border-radius: var(--radius-xl); padding: 36px 32px; box-shadow: var(--shadow-glass); position: relative; overflow: hidden; margin-bottom: 40px;">
  <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: #5865F2;"></div>
  <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px; margin-bottom: 16px;">
    <div style="display: flex; align-items: center; gap: 14px;">
      <span style="font-size: 2.5rem;">💬</span>
      <h1 style="margin: 0; font-size: clamp(1.8rem, 4vw, 2.6rem);">Discord</h1>
    </div>
    <span class="nav-badge-pill" style="font-size: 0.85rem; padding: 6px 14px;">4 Workflows</span>
  </div>
  <p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 820px; line-height: 1.6; margin-bottom: 24px;">Connect n8n to Discord for automated community management and content delivery. Templates include AI bot routing, scheduled sports match notifications, daily comic translations, and automated video summary sharing.</p>
  <div style="display: flex; gap: 12px; flex-wrap: wrap;">
    <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe" target="_blank" rel="noopener" class="btn-primary">🚀 Start n8n Cloud Trial</a>
    <a href="{{ site.baseurl }}/?cat=discord#explorer" class="btn-secondary">⚡ Filter in Explorer</a>
  </div>
  <small style="color: var(--text-muted); font-size: 0.75rem; display: block; margin-top: 10px;">* Referral link — this project receives a commission on eligible purchases.</small>
</div>

<h2>All 4 Discord Workflows</h2>
<p>Download JSON files or copy directly to your clipboard for instant n8n canvas import.</p>

<div class="templates-grid" style="margin-top: 24px;">
  <div class="template-card">
    <div class="template-card-inner">
      <div class="card-top-row">
        <span class="category-chip">💬 Discord</span>
        <span class="dept-badge">Customer Support</span>
      </div>
      <h3 class="card-title" onclick="window.n8nExplorer.openModal('discord-ai-powered-bot')">Discord AI-powered bot</h3>
      <p class="card-desc">This workflow creates an AI-powered Discord bot that categorizes user messages (success story, urgent issue, ticket) and routes them to the appropriate department (customer success, IT, customer support).</p>
      <div class="card-nodes-list">
        <span class="node-tag">Discord</span><span class="node-tag">Edit Fields</span><span class="node-tag">Manual trigger</span> <span class="node-tag">+4</span>
      </div>
      <div class="card-actions">
        <button class="btn-card-primary" onclick="window.n8nExplorer.copyForN8n('discord-ai-powered-bot')">⚡ Copy JSON</button>
        <button class="btn-card-icon" onclick="window.n8nExplorer.openModal('discord-ai-powered-bot')" title="Inspect">👁️</button>
        <a href="https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/Discord/Discord%20AI-Powered%20Bot.json" target="_blank" rel="noopener" class="btn-card-icon" title="View on GitHub">↗️</a>
      </div>
    </div>
  </div>
  <div class="template-card">
    <div class="template-card-inner">
      <div class="card-top-row">
        <span class="category-chip">💬 Discord</span>
        <span class="dept-badge">Data / Notifications</span>
      </div>
      <h3 class="card-title" onclick="window.n8nExplorer.openModal('post-new-live-tennis-matches-to-discord-on-a-schedule')">Post New Live Tennis Matches to Discord on a Schedule</h3>
      <p class="card-desc">Every 5 minutes, fetches the currently live tennis matches from the Live Tennis API, keeps only the ones newly in progress (deduplicated across executions), and posts a one-line alert (players and match status) to a Discord channel via a webhook. Free API tier, no card.</p>
      <div class="card-nodes-list">
        <span class="node-tag">Discord</span><span class="node-tag">HTTP Request</span><span class="node-tag">Remove duplicates</span> <span class="node-tag">+3</span>
      </div>
      <div class="card-actions">
        <button class="btn-card-primary" onclick="window.n8nExplorer.copyForN8n('post-new-live-tennis-matches-to-discord-on-a-schedule')">⚡ Copy JSON</button>
        <button class="btn-card-icon" onclick="window.n8nExplorer.openModal('post-new-live-tennis-matches-to-discord-on-a-schedule')" title="Inspect">👁️</button>
        <a href="https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/Discord/Post%20New%20Live%20Tennis%20Matches%20to%20Discord%20on%20a%20Schedule.json" target="_blank" rel="noopener" class="btn-card-icon" title="View on GitHub">↗️</a>
      </div>
    </div>
  </div>
  <div class="template-card">
    <div class="template-card-inner">
      <div class="card-top-row">
        <span class="category-chip">💬 Discord</span>
        <span class="dept-badge">Marketing/Content</span>
      </div>
      <h3 class="card-title" onclick="window.n8nExplorer.openModal('send-daily-translated-calvin-and-hobbes-comics-to-discord')">Send daily translated Calvin and Hobbes Comics to Discord</h3>
      <p class="card-desc">This workflow automates the daily retrieval of Calvin and Hobbes comics, translates the dialogues into English and Korean (or other languages), and posts them to Discord.</p>
      <div class="card-nodes-list">
        <span class="node-tag">Discord</span><span class="node-tag">Edit Fields</span><span class="node-tag">HTTP Request</span> <span class="node-tag">+5</span>
      </div>
      <div class="card-actions">
        <button class="btn-card-primary" onclick="window.n8nExplorer.copyForN8n('send-daily-translated-calvin-and-hobbes-comics-to-discord')">⚡ Copy JSON</button>
        <button class="btn-card-icon" onclick="window.n8nExplorer.openModal('send-daily-translated-calvin-and-hobbes-comics-to-discord')" title="Inspect">👁️</button>
        <a href="https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/Discord/Send%20Daily%20Translated%20Calvin%20and%20Hobbes%20Comics%20to%20Discord.json" target="_blank" rel="noopener" class="btn-card-icon" title="View on GitHub">↗️</a>
      </div>
    </div>
  </div>
  <div class="template-card">
    <div class="template-card-inner">
      <div class="card-top-row">
        <span class="category-chip">💬 Discord</span>
        <span class="dept-badge">Marketing</span>
      </div>
      <h3 class="card-title" onclick="window.n8nExplorer.openModal('share-youtube-videos-with-ai-summaries-on-discord')">Share YouTube Videos with AI Summaries on Discord</h3>
      <p class="card-desc">This workflow automatically shares new YouTube videos on Discord along with AI-generated summaries of their content, leveraging caption data.</p>
      <div class="card-nodes-list">
        <span class="node-tag">Discord</span><span class="node-tag">Edit Fields</span><span class="node-tag">Extract from file</span> <span class="node-tag">+4</span>
      </div>
      <div class="card-actions">
        <button class="btn-card-primary" onclick="window.n8nExplorer.copyForN8n('share-youtube-videos-with-ai-summaries-on-discord')">⚡ Copy JSON</button>
        <button class="btn-card-icon" onclick="window.n8nExplorer.openModal('share-youtube-videos-with-ai-summaries-on-discord')" title="Inspect">👁️</button>
        <a href="https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/Discord/Share%20YouTube%20Videos%20with%20AI%20Summaries%20on%20Discord.json" target="_blank" rel="noopener" class="btn-card-icon" title="View on GitHub">↗️</a>
      </div>
    </div>
  </div>
</div>

<div style="margin-top: 64px; padding-top: 32px; border-top: 1px solid var(--border-glass);">
  <h3>Explore Other Category Hubs</h3>
  <div class="filter-pills-scroll" style="margin-top: 16px;">
    <a href="{{ site.baseurl }}/categories/gmail-email-automation" class="filter-pill" >✉️ Gmail & Email Automation (26)</a>
    <a href="{{ site.baseurl }}/categories/telegram-bots" class="filter-pill" >✈️ Telegram (26)</a>
    <a href="{{ site.baseurl }}/categories/google-drive-sheets" class="filter-pill" >📁 Google Drive & Google Sheets (21)</a>
    <a href="{{ site.baseurl }}/categories/wordpress" class="filter-pill" >🌐 WordPress (6)</a>
    <a href="{{ site.baseurl }}/categories/pdf-document-processing" class="filter-pill" >📄 PDF & Document Processing (19)</a>
    <a href="{{ site.baseurl }}/categories/discord" class="filter-pill" style="border-color: var(--n8n-coral);">💬 Discord (4)</a>
    <a href="{{ site.baseurl }}/categories/database-storage" class="filter-pill" >🗄️ Database & Storage (5)</a>
    <a href="{{ site.baseurl }}/categories/devops-server-automation" class="filter-pill" >⚙️ DevOps / Server Automation (6)</a>
    <a href="{{ site.baseurl }}/categories/airtable" class="filter-pill" >📊 Airtable (5)</a>
    <a href="{{ site.baseurl }}/categories/notion" class="filter-pill" >📝 Notion (10)</a>
    <a href="{{ site.baseurl }}/categories/slack" class="filter-pill" >💼 Slack (9)</a>
    <a href="{{ site.baseurl }}/categories/openai-llms" class="filter-pill" >🧠 OpenAI & LLMs (93)</a>
    <a href="{{ site.baseurl }}/categories/whatsapp" class="filter-pill" >📱 WhatsApp (8)</a>
    <a href="{{ site.baseurl }}/categories/social-media" class="filter-pill" >📢 Instagram, Twitter, Social Media (20)</a>
    <a href="{{ site.baseurl }}/categories/other-integrations" class="filter-pill" >🔌 Other Integrations & Use Cases (47)</a>
    <a href="{{ site.baseurl }}/categories/forms-surveys" class="filter-pill" >📋 Forms & Surveys (4)</a>
    <a href="{{ site.baseurl }}/categories/ai-research-rag" class="filter-pill" >🔬 AI Research, RAG & Data Analysis (45)</a>
    <a href="{{ site.baseurl }}/categories/hr-recruitment" class="filter-pill" >👥 HR & Recruitment (4)</a>
  </div>
</div>
