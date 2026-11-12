<script setup>
import { t, ui } from '../i18n'

defineProps({ profile: { type: Object, required: true } })

const base = import.meta.env.BASE_URL
</script>

<template>
  <section id="top" class="hero">
    <div class="container hero-row">
      <div class="hero-text">
        <p class="eyebrow">{{ t(profile.location) }}</p>
        <h1>{{ profile.name }}</h1>
        <p class="title">{{ t(profile.title) }}</p>
        <p class="summary">{{ t(profile.summary) }}</p>
        <div class="actions">
          <a class="button primary" :href="`${base}${profile.cv}`" download>{{ ui('cv') }}</a>
          <a class="button" :href="profile.linkedin" target="_blank" rel="noopener">LinkedIn</a>
          <a class="button" :href="profile.github" target="_blank" rel="noopener">GitHub</a>
          <a class="button" :href="`mailto:${profile.email}`">{{ ui('contact') }}</a>
        </div>
      </div>
      <img class="photo" :src="`${base}profile.jpg`" :alt="profile.name" width="240" height="240" />
    </div>
  </section>
</template>

<style scoped>
.hero {
  padding: 72px 0 48px;
}
.hero-row {
  display: flex;
  align-items: center;
  gap: 48px;
}
.hero-text {
  flex: 1;
}
.eyebrow {
  color: var(--accent);
  font-weight: 600;
  font-size: 0.9rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  margin: 0 0 8px;
}
h1 {
  font-size: clamp(2.2rem, 5vw, 3.4rem);
  line-height: 1.05;
  margin: 0;
}
.title {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--accent);
  margin: 12px 0 20px;
}
.summary {
  color: var(--muted);
  font-size: 1.05rem;
  max-width: 62ch;
  margin: 0 0 28px;
}
.actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}
.photo {
  width: 240px;
  height: 240px;
  object-fit: cover;
  border-radius: 24px;
  border: 1px solid var(--border);
  box-shadow: var(--shadow);
}
@media (max-width: 760px) {
  .hero {
    padding-top: 40px;
  }
  .hero-row {
    flex-direction: column-reverse;
    align-items: flex-start;
    gap: 24px;
  }
  .photo {
    width: 120px;
    height: 120px;
    border-radius: 18px;
  }
}
</style>
