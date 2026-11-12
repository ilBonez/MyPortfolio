import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// Relative base: the same build works at https://ilbonez.github.io/MyPortfolio/ and locally.
export default defineConfig({
  base: './',
  plugins: [vue()],
})
