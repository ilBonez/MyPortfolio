<script setup>
import { formatMonth, t } from '../i18n'

defineProps({ items: { type: Array, required: true } })
</script>

<template>
  <ol class="timeline">
    <li v-for="item in items" :key="`${item.company}-${item.start}`" class="entry">
      <div class="entry-head">
        <div>
          <h3>{{ t(item.role) }}</h3>
          <p class="company">{{ item.company }} · {{ item.location }}</p>
        </div>
        <p class="dates">{{ formatMonth(item.start) }} – {{ formatMonth(item.end) }}</p>
      </div>
      <ul class="bullets">
        <li v-for="bullet in item.bullets" :key="bullet.en">{{ t(bullet) }}</li>
      </ul>
    </li>
  </ol>
</template>

<style scoped>
.timeline {
  list-style: none;
  margin: 0;
  padding: 0 0 0 20px;
  border-left: 2px solid var(--border);
}
.entry {
  position: relative;
  padding: 0 0 32px 16px;
}
.entry::before {
  content: '';
  position: absolute;
  left: -27px;
  top: 6px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--accent);
  box-shadow: 0 0 0 4px var(--bg);
}
.entry-head {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
}
h3 {
  margin: 0;
  font-size: 1.1rem;
}
.company {
  margin: 2px 0 0;
  color: var(--accent);
  font-weight: 500;
}
.dates {
  margin: 0;
  color: var(--muted);
  font-size: 0.9rem;
  white-space: nowrap;
}
.bullets {
  margin: 12px 0 0;
  padding-left: 18px;
  color: var(--muted);
}
.bullets li + li {
  margin-top: 6px;
}
</style>
