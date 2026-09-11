const test = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const path = require('node:path');

test('N8N Templates configuration and core files integrity', () => {
    const projectRoot = path.resolve(__dirname, '..');
    assert.ok(fs.existsSync(path.join(projectRoot, 'README.md')), 'README.md must be present');
    assert.ok(fs.existsSync(path.join(projectRoot, 'SECURITY.md')), 'SECURITY.md must be present');
    assert.ok(fs.existsSync(path.join(projectRoot, '.github')), '.github workflow directory must be present');
});
