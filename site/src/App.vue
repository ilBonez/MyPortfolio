<script setup>
import data from './data/portfolio.json'
import { t, ui } from './i18n'
import SiteHeader from './components/SiteHeader.vue'
import HeroSection from './components/HeroSection.vue'
import ExperienceTimeline from './components/ExperienceTimeline.vue'
import ProjectGrid from './components/ProjectGrid.vue'
</script>

<template>
  <SiteHeader :name="data.profile.name" />

  <main>
    <HeroSection :profile="data.profile" />

    <section id="highlights" class="section">
      <div class="container">
        <h2>{{ ui('highlights') }}</h2>
        <ul class="highlights">
          <li v-for="item in data.highlights" :key="item.value" class="card highlight">
            <strong>{{ item.value }}</strong>
            <span>{{ t(item.label) }}</span>
          </li>
        </ul>
      </div>
    </section>

    <section id="experience" class="section">
      <div class="container">
        <h2>{{ ui('experience') }}</h2>
        <ExperienceTimeline :items="data.experience" />
      </div>
    </section>

    <section id="projects" class="section">
      <div class="container">
        <h2>{{ ui('projects') }}</h2>
        <ProjectGrid :projects="data.projects" />

        <h3 class="subhead">{{ ui('academic') }}</h3>
        <ul class="academic">
          <li v-for="item in data.academic" :key="item.en">
            <span class="muted">{{ item.year }}</span>
            <span>{{ t(item) }}</span>
          </li>
        </ul>
      </div>
    </section>

    <section id="skills" class="section">
      <div class="container">
        <h2>{{ ui('skills') }}</h2>
        <div class="skills">
          <div v-for="group in data.skills" :key="group.group.en" class="card">
            <h3>{{ t(group.group) }}</h3>
            <ul class="chips">
              <li v-for="skill in group.items" :key="skill">{{ skill }}</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section id="education" class="section">
      <div class="container two-columns">
        <div>
          <h2>{{ ui('education') }}</h2>
          <ul class="plain-list">
            <li v-for="item in data.education" :key="item.years">
              <strong>{{ t(item.degree) }}</strong>
              <span class="muted">{{ t(item.school) }} · {{ item.years }} · {{ t(item.grade) }}</span>
            </li>
          </ul>

          <h2 class="spaced">{{ ui('languages') }}</h2>
          <ul class="plain-list">
            <li v-for="item in data.languages" :key="item.name.en">
              <strong>{{ t(item.name) }}</strong>
              <span class="muted">{{ t(item.level) }}</span>
            </li>
          </ul>
        </div>

        <div>
          <h2>{{ ui('publications') }}</h2>
          <ul class="plain-list">
            <li v-for="item in data.publications" :key="item.title">
              <a :href="item.url" target="_blank" rel="noopener"><strong>{{ item.title }}</strong></a>
              <span class="muted">{{ item.venue }} · {{ item.authors }}</span>
            </li>
          </ul>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container footer-row">
      <span>© {{ new Date().getFullYear() }} {{ data.profile.name }}</span>
      <span class="muted">{{ ui('footer') }}</span>
    </div>
  </footer>
</template>
