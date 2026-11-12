<script setup>
import { lang, ui } from '../i18n'

defineProps({ name: { type: String, required: true } })

const sections = ['highlights', 'experience', 'projects', 'skills', 'education']
</script>

<template>
  <header class="site-header">
    <div class="container header-row">
      <a href="#top" class="brand">{{ name }}</a>
      <nav aria-label="Sections">
        <a v-for="id in sections" :key="id" :href="`#${id}`">{{ ui(`nav.${id}`) }}</a>
      </nav>
      <div class="lang-switch" role="group" aria-label="Language">
        <button :aria-pressed="lang === 'it'" @click="lang = 'it'">IT</button>
        <button :aria-pressed="lang === 'en'" @click="lang = 'en'">EN</button>
      </div>
    </div>
  </header>
</template>

<style scoped>
.site-header {
  position: sticky;
  top: 0;
  z-index: 10;
  background: color-mix(in srgb, var(--bg) 85%, transparent);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--border);
}
.header-row {
  display: flex;
  align-items: center;
  gap: 24px;
  height: 60px;
}
.brand {
  font-weight: 700;
  color: var(--text);
  white-space: nowrap;
}
nav {
  display: flex;
  gap: 20px;
  margin-left: auto;
  overflow-x: auto;
}
nav a {
  color: var(--muted);
  font-size: 0.92rem;
  white-space: nowrap;
}
nav a:hover {
  color: var(--accent);
}
.lang-switch {
  display: flex;
  border: 1px solid var(--border);
  border-radius: 999px;
  overflow: hidden;
}
.lang-switch button {
  border: 0;
  background: transparent;
  color: var(--muted);
  font: inherit;
  font-size: 0.8rem;
  font-weight: 600;
  padding: 4px 10px;
  cursor: pointer;
}
.lang-switch button[aria-pressed='true'] {
  background: var(--accent);
  color: var(--on-accent);
}
@media (max-width: 760px) {
  nav {
    display: none;
  }
  .lang-switch {
    margin-left: auto;
  }
}
</style>
