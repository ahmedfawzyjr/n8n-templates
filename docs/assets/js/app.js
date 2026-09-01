/**
 * Awesome n8n Templates - Interactive Frontend Engine
 * Handles live searching, filtering, view toggling, modal inspection,
 * one-click n8n canvas clipboard copy, and theme switching.
 */

(function () {
  'use strict';

  // State Management
  const state = {
    templates: [],
    categories: [],
    filtered: [],
    searchTerm: '',
    selectedCategory: 'all',
    selectedDepartment: 'all',
    selectedNode: 'all',
    sortBy: 'title-asc',
    viewMode: 'grid', // 'grid' | 'table'
    activeModalTemplate: null,
    theme: localStorage.getItem('n8n_theme') || (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark')
  };

  // DOM Elements cache
  let dom = {};

  // Initialize
  document.addEventListener('DOMContentLoaded', init);

  function init() {
    applyTheme(state.theme);
    cacheDOMElements();
    bindEvents();
    loadTemplatesData();
    readURLParams();
  }

  function cacheDOMElements() {
    dom = {
      themeToggleBtn: document.getElementById('theme-toggle-btn'),
      searchInput: document.getElementById('template-search-input'),
      searchClearBtn: document.getElementById('search-clear-btn'),
      categoryPills: document.getElementById('category-pills-container'),
      departmentSelect: document.getElementById('department-filter-select'),
      sortSelect: document.getElementById('sort-by-select'),
      viewGridBtn: document.getElementById('view-grid-btn'),
      viewTableBtn: document.getElementById('view-table-btn'),
      resultsCounter: document.getElementById('results-counter-text'),
      resetFiltersBtn: document.getElementById('reset-filters-btn'),
      templatesGrid: document.getElementById('templates-grid-container'),
      templatesTableContainer: document.getElementById('templates-table-wrapper'),
      templatesTableBody: document.getElementById('templates-table-tbody'),
      modalOverlay: document.getElementById('template-detail-modal'),
      modalDialog: document.getElementById('template-modal-dialog'),
      modalCloseBtn: document.getElementById('modal-close-btn'),
      toastContainer: document.getElementById('toast-notification-container')
    };
  }

  function bindEvents() {
    // Theme Switcher
    if (dom.themeToggleBtn) {
      dom.themeToggleBtn.addEventListener('click', toggleTheme);
    }

    // Search input with debounce
    if (dom.searchInput) {
      let debounceTimer;
      dom.searchInput.addEventListener('input', (e) => {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => {
          state.searchTerm = e.target.value.trim().toLowerCase();
          if (dom.searchClearBtn) {
            dom.searchClearBtn.style.display = state.searchTerm ? 'block' : 'none';
          }
          applyFilters();
          syncURLParams();
        }, 150);
      });
    }

    // Search clear button
    if (dom.searchClearBtn) {
      dom.searchClearBtn.addEventListener('click', () => {
        if (dom.searchInput) {
          dom.searchInput.value = '';
          dom.searchInput.focus();
        }
        state.searchTerm = '';
        dom.searchClearBtn.style.display = 'none';
        applyFilters();
        syncURLParams();
      });
    }

    // Department filter
    if (dom.departmentSelect) {
      dom.departmentSelect.addEventListener('change', (e) => {
        state.selectedDepartment = e.target.value;
        applyFilters();
        syncURLParams();
      });
    }

    // Sort select
    if (dom.sortSelect) {
      dom.sortSelect.addEventListener('change', (e) => {
        state.sortBy = e.target.value;
        applyFilters();
      });
    }

    // Reset filters
    if (dom.resetFiltersBtn) {
      dom.resetFiltersBtn.addEventListener('click', resetAllFilters);
    }

    // View toggles
    if (dom.viewGridBtn && dom.viewTableBtn) {
      dom.viewGridBtn.addEventListener('click', () => setViewMode('grid'));
      dom.viewTableBtn.addEventListener('click', () => setViewMode('table'));
    }

    // Modal close events
    if (dom.modalCloseBtn) {
      dom.modalCloseBtn.addEventListener('click', closeModal);
    }
    if (dom.modalOverlay) {
      dom.modalOverlay.addEventListener('click', (e) => {
        if (e.target === dom.modalOverlay) closeModal();
      });
    }

    // Global keyboard shortcuts
    document.addEventListener('keydown', (e) => {
      // Focus search on '/' or 'Ctrl+K'
      if ((e.key === '/' || ((e.ctrlKey || e.metaKey) && e.key === 'k')) && document.activeElement !== dom.searchInput) {
        e.preventDefault();
        if (dom.searchInput) {
          dom.searchInput.focus();
          dom.searchInput.select();
        }
      }
      // Close modal on Escape
      if (e.key === 'Escape') {
        if (dom.modalOverlay && dom.modalOverlay.classList.contains('open')) {
          closeModal();
        }
      }
    });

    // FAQ Accordion click handling
    document.querySelectorAll('.faq-question').forEach((item) => {
      item.addEventListener('click', () => {
        const parent = item.closest('.faq-item');
        if (parent) {
          parent.classList.toggle('active');
        }
      });
    });
  }

  function applyTheme(theme) {
    state.theme = theme;
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('n8n_theme', theme);
    if (dom.themeToggleBtn) {
      dom.themeToggleBtn.innerHTML = theme === 'dark' ? '☀️' : '🌙';
      dom.themeToggleBtn.setAttribute('title', `Switch to ${theme === 'dark' ? 'Light' : 'Dark'} mode`);
    }
  }

  function toggleTheme() {
    const newTheme = state.theme === 'dark' ? 'light' : 'dark';
    applyTheme(newTheme);
  }

  function loadTemplatesData() {
    if (window.N8N_TEMPLATES && Array.isArray(window.N8N_TEMPLATES)) {
      state.templates = window.N8N_TEMPLATES;
      state.categories = window.N8N_CATEGORIES || [];
      onDataLoaded();
    } else {
      // Fallback: asynchronous fetch
      const baseUrl = document.querySelector('meta[name="base-url"]')?.getAttribute('content') || '';
      fetch(`${baseUrl}/templates.json`)
        .then((res) => res.json())
        .then((data) => {
          state.templates = data.templates || data;
          state.categories = data.categories || [];
          onDataLoaded();
        })
        .catch((err) => {
          console.warn('Could not load templates.json, trying static render:', err);
        });
    }
  }

  function onDataLoaded() {
    buildCategoryPills();
    applyFilters();
  }

  function buildCategoryPills() {
    if (!dom.categoryPills) return;

    // Count per category
    const catCounts = { all: state.templates.length };
    state.templates.forEach((t) => {
      catCounts[t.category_slug] = (catCounts[t.category_slug] || 0) + 1;
    });

    let html = `
      <button class="filter-pill ${state.selectedCategory === 'all' ? 'active' : ''}" data-cat="all">
        ⚡ All Templates <span class="pill-count">${catCounts.all}</span>
      </button>
    `;

    if (state.categories && state.categories.length) {
      state.categories.forEach((cat) => {
        const count = catCounts[cat.slug] || 0;
        const icon = cat.icon || '📁';
        html += `
          <button class="filter-pill ${state.selectedCategory === cat.slug ? 'active' : ''}" data-cat="${cat.slug}">
            ${icon} ${cat.name} <span class="pill-count">${count}</span>
          </button>
        `;
      });
    }

    dom.categoryPills.innerHTML = html;

    dom.categoryPills.querySelectorAll('.filter-pill').forEach((pill) => {
      pill.addEventListener('click', () => {
        dom.categoryPills.querySelectorAll('.filter-pill').forEach((p) => p.classList.remove('active'));
        pill.classList.add('active');
        state.selectedCategory = pill.getAttribute('data-cat');
        applyFilters();
        syncURLParams();
      });
    });
  }

  function applyFilters() {
    let list = state.templates.slice();

    // 1. Category Filter
    if (state.selectedCategory && state.selectedCategory !== 'all') {
      list = list.filter((t) => t.category_slug === state.selectedCategory);
    }

    // 2. Department Filter
    if (state.selectedDepartment && state.selectedDepartment !== 'all') {
      list = list.filter((t) => (t.department || '').toLowerCase() === state.selectedDepartment.toLowerCase());
    }

    // 3. Search Filter
    if (state.searchTerm) {
      const q = state.searchTerm;
      list = list.filter((t) => {
        const titleMatch = (t.title || '').toLowerCase().includes(q);
        const descMatch = (t.description || '').toLowerCase().includes(q);
        const catMatch = (t.category || '').toLowerCase().includes(q);
        const deptMatch = (t.department || '').toLowerCase().includes(q);
        const nodeMatch = (t.node_names || []).some((n) => n.toLowerCase().includes(q));
        return titleMatch || descMatch || catMatch || deptMatch || nodeMatch;
      });
    }

    // 4. Sorting
    list.sort((a, b) => {
      if (state.sortBy === 'title-asc') {
        return (a.title || '').localeCompare(b.title || '');
      } else if (state.sortBy === 'title-desc') {
        return (b.title || '').localeCompare(a.title || '');
      } else if (state.sortBy === 'nodes-desc') {
        return (b.node_count || 0) - (a.node_count || 0);
      }
      return 0;
    });

    state.filtered = list;
    renderResults();
  }

  function renderResults() {
    // Update Counter
    if (dom.resultsCounter) {
      dom.resultsCounter.innerHTML = `Showing <strong>${state.filtered.length}</strong> of <strong>${state.templates.length}</strong> templates`;
    }

    if (state.viewMode === 'grid') {
      renderGridView();
    } else {
      renderTableView();
    }
  }

  function renderGridView() {
    if (!dom.templatesGrid) return;
    if (dom.templatesTableContainer) dom.templatesTableContainer.style.display = 'none';
    dom.templatesGrid.style.display = 'grid';

    if (state.filtered.length === 0) {
      dom.templatesGrid.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center; padding: 64px 20px; background: var(--surface-glass-card); border-radius: var(--radius-lg); border: 1px solid var(--border-glass);">
          <div style="font-size: 3rem; margin-bottom: 12px;">🔍</div>
          <h3 style="margin-bottom: 8px;">No matching templates found</h3>
          <p style="color: var(--text-muted); max-width: 480px; margin: 0 auto 20px;">Try adjusting your search terms, changing the category, or resetting all filters.</p>
          <button class="btn-secondary" onclick="window.n8nExplorer.resetAllFilters()">Reset All Filters</button>
        </div>
      `;
      return;
    }

    const cardsHtml = state.filtered.map((t) => {
      const nodeBadges = (t.node_names || [])
        .slice(0, 3)
        .map((n) => `<span class="node-tag">${escapeHtml(n)}</span>`)
        .join('');
      const moreNodes = (t.node_names || []).length > 3 ? `<span class="node-tag">+${(t.node_names || []).length - 3}</span>` : '';

      return `
        <div class="template-card" data-id="${t.id}">
          <div class="template-card-inner">
            <div class="card-top-row">
              <span class="category-chip">${t.category_icon || '📁'} ${escapeHtml(t.category)}</span>
              <span class="dept-badge">${escapeHtml(t.department || 'General')}</span>
            </div>
            <h3 class="card-title" onclick="window.n8nExplorer.openModal('${t.id}')">${escapeHtml(t.title)}</h3>
            <p class="card-desc">${escapeHtml(t.description)}</p>
            <div class="card-nodes-list">
              ${nodeBadges} ${moreNodes}
            </div>
            <div class="card-actions">
              <button class="btn-card-primary" onclick="window.n8nExplorer.copyForN8n('${t.id}')" title="Copy workflow JSON to clipboard">
                ⚡ Copy JSON
              </button>
              <button class="btn-card-icon" onclick="window.n8nExplorer.openModal('${t.id}')" title="Inspect template details">
                👁️
              </button>
              <a href="${t.github_url}" target="_blank" rel="noopener" class="btn-card-icon" title="View on GitHub">
                ↗️
              </a>
            </div>
          </div>
        </div>
      `;
    }).join('');

    dom.templatesGrid.innerHTML = cardsHtml;
  }

  function renderTableView() {
    if (!dom.templatesTableContainer || !dom.templatesTableBody) return;
    if (dom.templatesGrid) dom.templatesGrid.style.display = 'none';
    dom.templatesTableContainer.style.display = 'block';

    if (state.filtered.length === 0) {
      dom.templatesTableBody.innerHTML = `
        <tr>
          <td colspan="5" style="text-align: center; padding: 48px 20px;">
            <div style="font-size: 2rem; margin-bottom: 8px;">🔍</div>
            <strong>No matching templates found</strong>
          </td>
        </tr>
      `;
      return;
    }

    const rowsHtml = state.filtered.map((t) => {
      return `
        <tr>
          <td class="tbl-title-cell" onclick="window.n8nExplorer.openModal('${t.id}')">
            ${escapeHtml(t.title)}
          </td>
          <td>
            <span class="category-chip">${t.category_icon || '📁'} ${escapeHtml(t.category)}</span>
          </td>
          <td>
            <span class="dept-badge">${escapeHtml(t.department || 'General')}</span>
          </td>
          <td style="max-width: 320px; font-size: 0.85rem;" class="card-desc">
            ${escapeHtml(t.description)}
          </td>
          <td style="white-space: nowrap;">
            <div style="display: flex; gap: 6px;">
              <button class="btn-card-primary" style="padding: 4px 10px; font-size: 0.78rem;" onclick="window.n8nExplorer.copyForN8n('${t.id}')">
                ⚡ Copy
              </button>
              <a href="${t.github_url}" target="_blank" rel="noopener" class="btn-card-icon" style="width: 28px; height: 28px; font-size: 0.75rem;" title="View on GitHub">
                ↗️
              </a>
            </div>
          </td>
        </tr>
      `;
    }).join('');

    dom.templatesTableBody.innerHTML = rowsHtml;
  }

  function setViewMode(mode) {
    state.viewMode = mode;
    if (dom.viewGridBtn && dom.viewTableBtn) {
      dom.viewGridBtn.classList.toggle('active', mode === 'grid');
      dom.viewTableBtn.classList.toggle('active', mode === 'table');
    }
    renderResults();
    syncURLParams();
  }

  function resetAllFilters() {
    state.searchTerm = '';
    state.selectedCategory = 'all';
    state.selectedDepartment = 'all';
    state.selectedNode = 'all';
    state.sortBy = 'title-asc';

    if (dom.searchInput) dom.searchInput.value = '';
    if (dom.searchClearBtn) dom.searchClearBtn.style.display = 'none';
    if (dom.departmentSelect) dom.departmentSelect.value = 'all';
    if (dom.sortSelect) dom.sortSelect.value = 'title-asc';
    if (dom.categoryPills) {
      dom.categoryPills.querySelectorAll('.filter-pill').forEach((p) => {
        p.classList.toggle('active', p.getAttribute('data-cat') === 'all');
      });
    }

    applyFilters();
    syncURLParams();
  }

  // Template Actions
  async function copyForN8n(templateId) {
    const template = state.templates.find((t) => t.id === templateId);
    if (!template) return;

    try {
      showToast('⚡ Fetching workflow JSON...', 'info');
      const res = await fetch(template.raw_github_url);
      if (!res.ok) throw new Error('Network error fetching template JSON');
      const text = await res.text();

      await navigator.clipboard.writeText(text);
      showToast('🎉 Copied to clipboard! Press Ctrl+V in n8n to import.', 'success');
    } catch (err) {
      console.error('Clipboard copy error:', err);
      // Fallback: open GitHub file
      window.open(template.github_url, '_blank');
      showToast('Could not auto-copy, opening GitHub page...', 'warning');
    }
  }

  function downloadTemplate(templateId) {
    const template = state.templates.find((t) => t.id === templateId);
    if (!template) return;

    const a = document.createElement('a');
    a.href = template.raw_github_url;
    a.download = template.filename;
    a.target = '_blank';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    showToast(`⬇️ Downloading ${template.filename}`, 'success');
  }

  function openModal(templateId) {
    const template = state.templates.find((t) => t.id === templateId);
    if (!template || !dom.modalOverlay || !dom.modalDialog) return;

    state.activeModalTemplate = template;

    const nodeTags = (template.node_names || [])
      .map((n) => `<span class="node-tag" style="font-size: 0.82rem; padding: 4px 10px;">${escapeHtml(n)}</span>`)
      .join('');

    dom.modalDialog.innerHTML = `
      <button class="modal-close-btn" id="modal-close-btn" onclick="window.n8nExplorer.closeModal()">✕</button>
      <div class="modal-category-chip">
        <span class="category-chip" style="font-size: 0.85rem; padding: 4px 12px;">
          ${template.category_icon || '📁'} ${escapeHtml(template.category)}
        </span>
      </div>
      <h2 class="modal-title">${escapeHtml(template.title)}</h2>
      <p class="modal-desc">${escapeHtml(template.description)}</p>

      <div class="modal-meta-grid">
        <div class="modal-meta-item">
          <div class="modal-meta-val">${escapeHtml(template.department || 'General')}</div>
          <div class="modal-meta-lbl">Department</div>
        </div>
        <div class="modal-meta-item">
          <div class="modal-meta-val">${template.node_count || (template.node_names ? template.node_names.length : 1)}</div>
          <div class="modal-meta-lbl">Total Nodes</div>
        </div>
        <div class="modal-meta-item">
          <div class="modal-meta-val">MIT</div>
          <div class="modal-meta-lbl">License</div>
        </div>
      </div>

      <div class="modal-nodes-title">Included Integrations & Nodes:</div>
      <div class="card-nodes-list" style="margin-bottom: 24px;">
        ${nodeTags || '<span style="color: var(--text-muted); font-size: 0.9rem;">Core n8n automation nodes</span>'}
      </div>

      <div class="modal-actions">
        <button class="btn-primary" onclick="window.n8nExplorer.copyForN8n('${template.id}')" style="flex: 1; justify-content: center;">
          ⚡ Copy for n8n Canvas
        </button>
        <button class="btn-secondary" onclick="window.n8nExplorer.downloadTemplate('${template.id}')">
          ⬇️ Download JSON
        </button>
        <a href="${template.github_url}" target="_blank" rel="noopener" class="btn-secondary">
          ↗️ View on GitHub
        </a>
      </div>
    `;

    dom.modalOverlay.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    if (!dom.modalOverlay) return;
    dom.modalOverlay.classList.remove('open');
    document.body.style.overflow = '';
    state.activeModalTemplate = null;
  }

  function showToast(message, type = 'success') {
    if (!dom.toastContainer) return;

    const toast = document.createElement('div');
    toast.className = `toast-msg show`;
    toast.innerHTML = `
      <span class="toast-icon">${type === 'success' ? '⚡' : type === 'info' ? 'ℹ️' : '⚠️'}</span>
      <span>${escapeHtml(message)}</span>
    `;

    dom.toastContainer.appendChild(toast);

    setTimeout(() => {
      toast.classList.remove('show');
      setTimeout(() => {
        if (toast.parentNode) toast.parentNode.removeChild(toast);
      }, 300);
    }, 3500);
  }

  // URL parameter sync
  function syncURLParams() {
    const params = new URLSearchParams();
    if (state.searchTerm) params.set('q', state.searchTerm);
    if (state.selectedCategory && state.selectedCategory !== 'all') params.set('cat', state.selectedCategory);
    if (state.selectedDepartment && state.selectedDepartment !== 'all') params.set('dept', state.selectedDepartment);
    if (state.viewMode !== 'grid') params.set('view', state.viewMode);

    const queryString = params.toString();
    const newUrl = window.location.pathname + (queryString ? '?' + queryString : '');
    window.history.replaceState({}, '', newUrl);
  }

  function readURLParams() {
    const params = new URLSearchParams(window.location.search);
    const q = params.get('q');
    const cat = params.get('cat');
    const dept = params.get('dept');
    const view = params.get('view');

    if (q) {
      state.searchTerm = q.trim().toLowerCase();
      if (dom.searchInput) dom.searchInput.value = q;
      if (dom.searchClearBtn) dom.searchClearBtn.style.display = 'block';
    }
    if (cat) state.selectedCategory = cat;
    if (dept && dom.departmentSelect) {
      state.selectedDepartment = dept;
      dom.departmentSelect.value = dept;
    }
    if (view && (view === 'grid' || view === 'table')) {
      setViewMode(view);
    }
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  // Expose global methods for inline HTML events
  window.n8nExplorer = {
    copyForN8n,
    downloadTemplate,
    openModal,
    closeModal,
    resetAllFilters,
    showToast,
    setViewMode,
    toggleTheme
  };

})();
