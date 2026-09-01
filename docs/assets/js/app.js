/**
 * n8n Portal - Interactive Frontend Engine
 * Handles live searching, filtering, view toggling, modal inspection,
 * one-click n8n canvas clipboard copy, and theme switching.
 */

(function () {
  'use strict';

  // SVG Icon Definitions (Lucide / Feather / Heroicons standards)
  const SVG_ICONS = {
    'mail': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>',
    'send': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg>',
    'hard-drive': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><line x1="22" x2="2" y1="12" y2="12"/><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"/><line x1="6" x2="6.01" y1="16" y2="16"/><line x1="10" x2="10.01" y1="16" y2="16"/></svg>',
    'globe': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>',
    'file-text': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/></svg>',
    'message-square': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
    'database': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/><path d="M3 12c0 1.66 4 3 9 3s9-1.34 9-3"/></svg>',
    'terminal': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"/><line x1="12" x2="20" y1="19" y2="19"/></svg>',
    'table': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18"/><path d="M3 15h18"/><path d="M9 3v18"/><path d="M15 3v18"/></svg>',
    'book-open': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>',
    'briefcase': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="14" x="2" y="7" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
    'bot': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/></svg>',
    'phone': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    'share-2': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" x2="15.42" y1="13.51" y2="17.49"/><line x1="15.41" x2="8.59" y1="6.51" y2="10.49"/></svg>',
    'plug': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22v-5"/><path d="M9 8V2"/><path d="M15 2v6"/><path d="M18 8v5a6 6 0 0 1-12 0V8z"/></svg>',
    'check-square': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="m9 11 3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>',
    'flask': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M10 2v7.31"/><path d="M14 2v7.31"/><path d="M8.5 2h7"/><path d="M14 9.3 20.7 20.3c.7 1.1-.1 2.7-1.4 2.7H4.7c-1.3 0-2.1-1.6-1.4-2.7L10 9.3"/><path d="M6.3 17h11.4"/></svg>',
    'users': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
    'zap': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
    'search': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>',
    'x': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>',
    'copy': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/></svg>',
    'check': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
    'eye': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/></svg>',
    'download': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" x2="12" y1="15" y2="3"/></svg>',
    'external-link': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" x2="21" y1="14" y2="3"/></svg>',
    'arrow-up-right': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7"/><path d="M7 7h10v10"/></svg>',
    'chevron-down': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>',
    'sun': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>',
    'moon': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>',
    'grid': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><rect width="7" height="7" x="3" y="3" rx="1"/><rect width="7" height="7" x="14" y="3" rx="1"/><rect width="7" height="7" x="14" y="14" rx="1"/><rect width="7" height="7" x="3" y="14" rx="1"/></svg>',
    'list': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><line x1="8" x2="21" y1="6" y2="6"/><line x1="8" x2="21" y1="12" y2="12"/><line x1="8" x2="21" y1="18" y2="18"/><line x1="3" x2="3.01" y1="6" y2="6"/><line x1="3" x2="3.01" y1="12" y2="12"/><line x1="3" x2="3.01" y1="18" y2="18"/></svg>',
    'sparkles': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/><path d="M5 3v4"/><path d="M19 17v4"/><path d="M3 5h4"/><path d="M17 19h4"/></svg>',
    'shield': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    'layers': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>',
    'folder': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20h16a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.93a2 2 0 0 1-1.66-.9l-.82-1.2A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13c0 1.1.9 2 2 2Z"/></svg>',
    'star': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
    'cpu': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 2v2"/><path d="M9 20v2"/></svg>',
    'info': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>',
    'alert-triangle': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
    'menu': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>'
  };

  function svgIcon(name, size = 16, cls = '', stroke_width = 2) {
    const tmpl = SVG_ICONS[name] || SVG_ICONS['layers'];
    return tmpl
      .replace('{size}', size)
      .replace('{size}', size)
      .replace('{cls}', cls)
      .replace('{stroke_width}', stroke_width);
  }

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
    cacheDOMElements();
    applyTheme(state.theme);
    bindEvents();
    loadTemplatesData();
    readURLParams();
  }

  function cacheDOMElements() {
    dom = {
      themeToggleBtn: document.getElementById('theme-toggle-btn'),
      mobileThemeToggleBtn: document.getElementById('mobile-theme-toggle-btn'),
      mobileMenuBtn: document.getElementById('mobile-menu-btn'),
      mobileNavDrawer: document.getElementById('mobile-nav-drawer'),
      mobileNavBackdrop: document.getElementById('mobile-nav-backdrop'),
      mobileDrawerCloseBtn: document.getElementById('mobile-drawer-close-btn'),
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
    // Theme Switchers
    if (dom.themeToggleBtn) {
      dom.themeToggleBtn.addEventListener('click', toggleTheme);
    }
    if (dom.mobileThemeToggleBtn) {
      dom.mobileThemeToggleBtn.addEventListener('click', toggleTheme);
    }

    // Mobile Navigation Drawer Toggle
    if (dom.mobileMenuBtn) {
      dom.mobileMenuBtn.addEventListener('click', openMobileDrawer);
    }
    if (dom.mobileDrawerCloseBtn) {
      dom.mobileDrawerCloseBtn.addEventListener('click', closeMobileDrawer);
    }
    if (dom.mobileNavBackdrop) {
      dom.mobileNavBackdrop.addEventListener('click', closeMobileDrawer);
    }
    // Close drawer when any mobile nav link is clicked
    if (dom.mobileNavDrawer) {
      dom.mobileNavDrawer.querySelectorAll('a').forEach((link) => {
        link.addEventListener('click', closeMobileDrawer);
      });
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
      // Focus search on '/' or 'Ctrl+K' / 'Cmd+K'
      if ((e.key === '/' || ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k')) && document.activeElement !== dom.searchInput) {
        e.preventDefault();
        if (dom.searchInput) {
          dom.searchInput.focus();
          dom.searchInput.select();
        }
      }
      // Close modal or mobile drawer on Escape
      if (e.key === 'Escape') {
        if (dom.modalOverlay && dom.modalOverlay.classList.contains('open')) {
          closeModal();
        }
        closeMobileDrawer();
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

  function openMobileDrawer() {
    if (dom.mobileNavDrawer) dom.mobileNavDrawer.classList.add('open');
    if (dom.mobileNavBackdrop) dom.mobileNavBackdrop.classList.add('open');
    if (dom.mobileMenuBtn) dom.mobileMenuBtn.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }

  function closeMobileDrawer() {
    if (dom.mobileNavDrawer) dom.mobileNavDrawer.classList.remove('open');
    if (dom.mobileNavBackdrop) dom.mobileNavBackdrop.classList.remove('open');
    if (dom.mobileMenuBtn) dom.mobileMenuBtn.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  function applyTheme(theme) {
    state.theme = theme;
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('n8n_theme', theme);
    
    const iconHtml = theme === 'dark' ? svgIcon('sun', 16) : svgIcon('moon', 16);
    const titleText = `Switch to ${theme === 'dark' ? 'Light' : 'Dark'} mode`;
    
    if (dom.themeToggleBtn) {
      dom.themeToggleBtn.innerHTML = iconHtml;
      dom.themeToggleBtn.setAttribute('title', titleText);
    }
    if (dom.mobileThemeToggleBtn) {
      dom.mobileThemeToggleBtn.innerHTML = `${iconHtml} <span>Theme: ${theme === 'dark' ? 'Dark' : 'Light'}</span>`;
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
        ${svgIcon('layers', 14)} <span>All Workflows</span> <span class="pill-count">${catCounts.all}</span>
      </button>
    `;

    if (state.categories && state.categories.length) {
      state.categories.forEach((cat) => {
        const count = catCounts[cat.slug] || 0;
        const icon = svgIcon(cat.icon || 'folder', 14);
        html += `
          <button class="filter-pill ${state.selectedCategory === cat.slug ? 'active' : ''}" data-cat="${cat.slug}">
            ${icon} <span>${escapeHtml(cat.name)}</span> <span class="pill-count">${count}</span>
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
          <div style="margin-bottom: 16px; color: var(--text-muted);">${svgIcon('search', 40)}</div>
          <h3 style="margin-bottom: 8px;">No matching templates found</h3>
          <p style="color: var(--text-muted); max-width: 480px; margin: 0 auto 20px;">Try adjusting your search terms, changing the category, or resetting all filters.</p>
          <button class="btn-secondary" onclick="window.n8nExplorer.resetAllFilters()">${svgIcon('x', 14)} Reset All Filters</button>
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
      const catIcon = svgIcon(t.category_icon || 'folder', 13);

      return `
        <div class="template-card" data-id="${t.id}">
          <div class="template-card-inner">
            <div class="card-top-row">
              <span class="category-chip">${catIcon} ${escapeHtml(t.category)}</span>
              <span class="dept-badge">${escapeHtml(t.department || 'General')}</span>
            </div>
            <h3 class="card-title" onclick="window.n8nExplorer.openModal('${t.id}')">${escapeHtml(t.title)}</h3>
            <p class="card-desc">${escapeHtml(t.description)}</p>
            <div class="card-nodes-list">
              ${nodeBadges} ${moreNodes}
            </div>
            <div class="card-actions">
              <button class="btn-card-primary" id="copy-btn-${t.id}" onclick="window.n8nExplorer.copyForN8n('${t.id}', this)" title="Copy workflow JSON to clipboard">
                ${svgIcon('copy', 14)} <span>Copy JSON</span>
              </button>
              <button class="btn-card-icon" onclick="window.n8nExplorer.openModal('${t.id}')" title="Inspect template details" aria-label="Inspect template">
                ${svgIcon('eye', 16)}
              </button>
              <a href="${t.github_url}" target="_blank" rel="noopener" class="btn-card-icon" title="View on GitHub" aria-label="View on GitHub">
                ${svgIcon('external-link', 15)}
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
            <div style="margin-bottom: 8px; color: var(--text-muted);">${svgIcon('search', 32)}</div>
            <strong>No matching templates found</strong>
          </td>
        </tr>
      `;
      return;
    }

    const rowsHtml = state.filtered.map((t) => {
      const catIcon = svgIcon(t.category_icon || 'folder', 13);
      return `
        <tr>
          <td class="tbl-title-cell" onclick="window.n8nExplorer.openModal('${t.id}')">
            ${escapeHtml(t.title)}
          </td>
          <td>
            <span class="category-chip">${catIcon} ${escapeHtml(t.category)}</span>
          </td>
          <td>
            <span class="dept-badge">${escapeHtml(t.department || 'General')}</span>
          </td>
          <td style="max-width: 320px; font-size: 0.85rem;" class="card-desc">
            ${escapeHtml(t.description)}
          </td>
          <td style="white-space: nowrap;">
            <div style="display: flex; gap: 6px;">
              <button class="btn-card-primary" style="padding: 4px 10px; font-size: 0.78rem;" id="copy-btn-${t.id}" onclick="window.n8nExplorer.copyForN8n('${t.id}', this)">
                ${svgIcon('copy', 13)} <span>Copy</span>
              </button>
              <a href="${t.github_url}" target="_blank" rel="noopener" class="btn-card-icon" style="width: 28px; height: 28px; font-size: 0.75rem;" title="View on GitHub" aria-label="View on GitHub">
                ${svgIcon('external-link', 14)}
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
  async function copyForN8n(templateId, btnEl) {
    const template = state.templates.find((t) => t.id === templateId);
    if (!template) return;

    const originalBtnContent = btnEl ? btnEl.innerHTML : null;

    try {
      showToast('Fetching workflow JSON...', 'info');
      const res = await fetch(template.raw_github_url);
      if (!res.ok) throw new Error('Network error fetching template JSON');
      const text = await res.text();

      await navigator.clipboard.writeText(text);
      showToast('Copied to clipboard! Press Ctrl+V in n8n to import.', 'success');

      // Visual feedback on the trigger button
      if (btnEl) {
        btnEl.innerHTML = `${svgIcon('check', 14)} <span>Copied!</span>`;
        btnEl.classList.add('copied');
        setTimeout(() => {
          btnEl.innerHTML = originalBtnContent;
          btnEl.classList.remove('copied');
        }, 2200);
      }
    } catch (err) {
      console.error('Clipboard copy error:', err);
      // Fallback: open GitHub file
      window.open(template.github_url, '_blank');
      showToast('Opening template on GitHub...', 'warning');
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
    showToast(`Downloading ${template.filename}`, 'success');
  }

  function openModal(templateId) {
    const template = state.templates.find((t) => t.id === templateId);
    if (!template || !dom.modalOverlay || !dom.modalDialog) return;

    state.activeModalTemplate = template;

    const nodeTags = (template.node_names || [])
      .map((n) => `<span class="node-tag" style="font-size: 0.82rem; padding: 4px 10px;">${escapeHtml(n)}</span>`)
      .join('');

    const catIcon = svgIcon(template.category_icon || 'folder', 14);

    dom.modalDialog.innerHTML = `
      <button class="modal-close-btn" id="modal-close-btn" onclick="window.n8nExplorer.closeModal()" aria-label="Close dialog">
        ${svgIcon('x', 18)}
      </button>
      <div class="modal-category-chip">
        <span class="category-chip" style="font-size: 0.85rem; padding: 4px 12px;">
          ${catIcon} ${escapeHtml(template.category)}
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

      <div class="modal-nodes-title">Included Integrations &amp; Nodes:</div>
      <div class="card-nodes-list" style="margin-bottom: 24px;">
        ${nodeTags || '<span style="color: var(--text-muted); font-size: 0.9rem;">Core n8n automation nodes</span>'}
      </div>

      <div class="modal-actions">
        <button class="btn-action-primary" onclick="window.n8nExplorer.copyForN8n('${template.id}', this)">
          ${svgIcon('copy', 16)} <span>Copy for n8n Canvas</span>
        </button>
        <button class="btn-action-secondary" onclick="window.n8nExplorer.downloadTemplate('${template.id}')">
          ${svgIcon('download', 16)} <span>Download JSON</span>
        </button>
        <a href="${template.github_url}" target="_blank" rel="noopener" class="btn-action-secondary">
          ${svgIcon('external-link', 16)} <span>View on GitHub</span>
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

    const iconHtml = type === 'success' ? svgIcon('check', 16) : type === 'info' ? svgIcon('info', 16) : svgIcon('alert-triangle', 16);

    const toast = document.createElement('div');
    toast.className = `toast-msg show ${type}`;
    toast.innerHTML = `
      <span class="toast-icon">${iconHtml}</span>
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
    toggleTheme,
    openMobileDrawer,
    closeMobileDrawer
  };

})();
