<script setup>
import { t, ui } from '../i18n'

defineProps({ projects: { type: Array, required: true } })
</script>

<template>
  <div class="grid">
    <article v-for="project in projects" :key="project.title" class="card project">
      <p class="tag">{{ t(project.tag) }}</p>
      <h3>{{ project.title }}</h3>
      <p class="description">{{ t(project.description) }}</p>
      <ul class="chips">
        <li v-for="tech in project.tech" :key="tech">{{ tech }}</li>
      </ul>
      <a v-if="project.url" class="link" :href="project.url" target="_blank" rel="noopener">{{ ui('open') }} →</a>
    </article>
  </div>
</template>

<style scoped>
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 16px;
}
.project {
  display: flex;
  flex-direction: column;
}
.tag {
  margin: 0 0 6px;
  color: var(--accent);
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
h3 {
  margin: 0 0 8px;
}
.description {
  color: var(--muted);
  margin: 0 0 16px;
  flex: 1;
}
.link {
  margin-top: 14px;
  font-weight: 600;
}
</style>
