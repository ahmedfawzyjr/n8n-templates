---
layout: default
title: "Forms & Surveys Templates for n8n | Awesome n8n Templates"
description: "4 n8n forms & surveys templates. Conversational AI interviews, appointment qualification, and automated survey analysis."
---

<nav style="margin-bottom: 24px; font-size: 0.9rem; color: var(--text-muted);">
  <a href="{{ site.baseurl }}/" style="color: var(--text-secondary);">Home</a> / 
  <a href="{{ site.baseurl }}/#categories" style="color: var(--text-secondary);">Categories</a> / 
  <span style="color: var(--n8n-coral);">Forms & Surveys</span>
</nav>

<div style="background: var(--surface-glass-card); border: 1px solid var(--border-glass); border-radius: var(--radius-xl); padding: 36px 32px; box-shadow: var(--shadow-glass); position: relative; overflow: hidden; margin-bottom: 40px;">
  <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: #06B6D4;"></div>
  <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px; margin-bottom: 16px;">
    <div style="display: flex; align-items: center; gap: 14px;">
      <span style="font-size: 2.5rem;">📋</span>
      <h1 style="margin: 0; font-size: clamp(1.8rem, 4vw, 2.6rem);">Forms & Surveys</h1>
    </div>
    <span class="nav-badge-pill" style="font-size: 0.85rem; padding: 6px 14px;">4 Workflows</span>
  </div>
  <p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 820px; line-height: 1.6; margin-bottom: 24px;">Create interactive and conversational form automations using n8n Forms. Templates feature conversational AI interviews, lead qualification with appointment booking, email subscription flows with Airtable, and automated survey feedback analysis.</p>
  <div style="display: flex; gap: 12px; flex-wrap: wrap;">
    <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe" target="_blank" rel="noopener" class="btn-primary">🚀 Start n8n Cloud Trial</a>
    <a href="{{ site.baseurl }}/?cat=forms-surveys#explorer" class="btn-secondary">⚡ Filter in Explorer</a>
  </div>
  <small style="color: var(--text-muted); font-size: 0.75rem; display: block; margin-top: 10px;">* Referral link — this project receives a commission on eligible purchases.</small>
</div>

<h2>All 4 Forms & Surveys Workflows</h2>
<p>Download JSON files or copy directly to your clipboard for instant n8n canvas import.</p>

<div class="templates-grid" style="margin-top: 24px;">
  <div class="template-card">
    <div class="template-card-inner">
      <div class="card-top-row">
        <span class="category-chip">📋 Forms & Surveys</span>
        <span class="dept-badge">Research/Marketing</span>
      </div>
      <h3 class="card-title" onclick="window.n8nExplorer.openModal('conversational-interviews-with-ai-agents-and-n8n-forms')">Conversational Interviews with AI Agents and n8n Forms</h3>
      <p class="card-desc">Implements AI-powered conversational interviews using n8n Forms for interactive data collection.</p>
      <div class="card-nodes-list">
        <span class="node-tag">AI Agent</span><span class="node-tag">Buffer Memory</span><span class="node-tag">Crypto</span> <span class="node-tag">+13</span>
      </div>
      <div class="card-actions">
        <button class="btn-card-primary" onclick="window.n8nExplorer.copyForN8n('conversational-interviews-with-ai-agents-and-n8n-forms')">⚡ Copy JSON</button>
        <button class="btn-card-icon" onclick="window.n8nExplorer.openModal('conversational-interviews-with-ai-agents-and-n8n-forms')" title="Inspect">👁️</button>
        <a href="https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/Forms%20and%20Surveys/Conversational%20Interviews%20with%20AI%20Agents%20and%20n8n%20Forms.json" target="_blank" rel="noopener" class="btn-card-icon" title="View on GitHub">↗️</a>
      </div>
    </div>
  </div>
  <div class="template-card">
    <div class="template-card-inner">
      <div class="card-top-row">
        <span class="category-chip">📋 Forms & Surveys</span>
        <span class="dept-badge">Marketing/Communication</span>
      </div>
      <h3 class="card-title" onclick="window.n8nExplorer.openModal('email-subscription-service-with-n8n-forms-airtable-and-ai')">Email Subscription Service with n8n Forms, Airtable and AI</h3>
      <p class="card-desc">Manages email subscriptions with n8n Forms, stores data in Airtable, and uses AI for processing.</p>
      <div class="card-nodes-list">
        <span class="node-tag">AI Agent</span><span class="node-tag">Airtable</span><span class="node-tag">Buffer Memory</span> <span class="node-tag">+14</span>
      </div>
      <div class="card-actions">
        <button class="btn-card-primary" onclick="window.n8nExplorer.copyForN8n('email-subscription-service-with-n8n-forms-airtable-and-ai')">⚡ Copy JSON</button>
        <button class="btn-card-icon" onclick="window.n8nExplorer.openModal('email-subscription-service-with-n8n-forms-airtable-and-ai')" title="Inspect">👁️</button>
        <a href="https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/Forms%20and%20Surveys/Email%20Subscription%20Service%20with%20n8n%20Forms%2C%20Airtable%20and%20AI.json" target="_blank" rel="noopener" class="btn-card-icon" title="View on GitHub">↗️</a>
      </div>
    </div>
  </div>
  <div class="template-card">
    <div class="template-card-inner">
      <div class="card-top-row">
        <span class="category-chip">📋 Forms & Surveys</span>
        <span class="dept-badge">Marketing/Creative</span>
      </div>
      <h3 class="card-title" onclick="window.n8nExplorer.openModal('tunova---generate-a-song-from-a-form')">Generate a Song from a Form (Tunova)</h3>
      <p class="card-desc">A hosted n8n Form collects a text prompt, then Tunova generates an original Suno AI song (v5.5) and returns the audio URL. Core HTTP node — runs on any n8n. Free API key at tunova.ai.</p>
      <div class="card-nodes-list">
        <span class="node-tag">Edit Fields</span><span class="node-tag">Form trigger</span><span class="node-tag">HTTP Request</span> <span class="node-tag">+1</span>
      </div>
      <div class="card-actions">
        <button class="btn-card-primary" onclick="window.n8nExplorer.copyForN8n('tunova---generate-a-song-from-a-form')">⚡ Copy JSON</button>
        <button class="btn-card-icon" onclick="window.n8nExplorer.openModal('tunova---generate-a-song-from-a-form')" title="Inspect">👁️</button>
        <a href="https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/Forms%20and%20Surveys/Tunova%20-%20Generate%20a%20Song%20from%20a%20Form.json" target="_blank" rel="noopener" class="btn-card-icon" title="View on GitHub">↗️</a>
      </div>
    </div>
  </div>
  <div class="template-card">
    <div class="template-card-inner">
      <div class="card-top-row">
        <span class="category-chip">📋 Forms & Surveys</span>
        <span class="dept-badge">Sales/Support</span>
      </div>
      <h3 class="card-title" onclick="window.n8nExplorer.openModal('qualifying-appointment-requests-with-ai--n8n-forms')">Qualifying Appointment Requests with AI & n8n Forms</h3>
      <p class="card-desc">Uses AI to qualify and process appointment requests submitted through n8n Forms.</p>
      <div class="card-nodes-list">
        <span class="node-tag">Chain llm</span><span class="node-tag">Edit Fields</span><span class="node-tag">Execute workflow</span> <span class="node-tag">+9</span>
      </div>
      <div class="card-actions">
        <button class="btn-card-primary" onclick="window.n8nExplorer.copyForN8n('qualifying-appointment-requests-with-ai--n8n-forms')">⚡ Copy JSON</button>
        <button class="btn-card-icon" onclick="window.n8nExplorer.openModal('qualifying-appointment-requests-with-ai--n8n-forms')" title="Inspect">👁️</button>
        <a href="https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/Forms%20and%20Surveys/Qualifying%20Appointment%20Requests%20with%20AI%20%26%20n8n%20Forms.json" target="_blank" rel="noopener" class="btn-card-icon" title="View on GitHub">↗️</a>
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
    <a href="{{ site.baseurl }}/categories/discord" class="filter-pill" >💬 Discord (4)</a>
    <a href="{{ site.baseurl }}/categories/database-storage" class="filter-pill" >🗄️ Database & Storage (5)</a>
    <a href="{{ site.baseurl }}/categories/devops-server-automation" class="filter-pill" >⚙️ DevOps / Server Automation (6)</a>
    <a href="{{ site.baseurl }}/categories/airtable" class="filter-pill" >📊 Airtable (5)</a>
    <a href="{{ site.baseurl }}/categories/notion" class="filter-pill" >📝 Notion (10)</a>
    <a href="{{ site.baseurl }}/categories/slack" class="filter-pill" >💼 Slack (9)</a>
    <a href="{{ site.baseurl }}/categories/openai-llms" class="filter-pill" >🧠 OpenAI & LLMs (93)</a>
    <a href="{{ site.baseurl }}/categories/whatsapp" class="filter-pill" >📱 WhatsApp (8)</a>
    <a href="{{ site.baseurl }}/categories/social-media" class="filter-pill" >📢 Instagram, Twitter, Social Media (20)</a>
    <a href="{{ site.baseurl }}/categories/other-integrations" class="filter-pill" >🔌 Other Integrations & Use Cases (47)</a>
    <a href="{{ site.baseurl }}/categories/forms-surveys" class="filter-pill" style="border-color: var(--n8n-coral);">📋 Forms & Surveys (4)</a>
    <a href="{{ site.baseurl }}/categories/ai-research-rag" class="filter-pill" >🔬 AI Research, RAG & Data Analysis (45)</a>
    <a href="{{ site.baseurl }}/categories/hr-recruitment" class="filter-pill" >👥 HR & Recruitment (4)</a>
  </div>
</div>
