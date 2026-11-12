import { ref, watch } from 'vue'

const STORAGE_KEY = 'portfolio-lang'

function initialLang() {
  try {
    const saved = localStorage.getItem(STORAGE_KEY)
    if (saved === 'it' || saved === 'en') return saved
  } catch {
    // Storage can be blocked (private mode): fall back to the browser language.
  }
  return navigator.language?.toLowerCase().startsWith('it') ? 'it' : 'en'
}

export const lang = ref(initialLang())

watch(
  lang,
  (value) => {
    document.documentElement.lang = value
    try {
      localStorage.setItem(STORAGE_KEY, value)
    } catch {
      // Not persisted, the choice still applies to this visit.
    }
  },
  { immediate: true },
)

// Picks the active language from a bilingual {it, en} field.
export const t = (text) => text[lang.value]

// Interface labels that are not part of the portfolio content.
const labels = {
  it: {
    nav: { highlights: 'Risultati', experience: 'Esperienza', projects: 'Progetti', skills: 'Competenze', education: 'Formazione' },
    cv: 'Scarica il CV',
    contact: 'Contattami',
    present: 'oggi',
    highlights: 'Risultati misurati',
    experience: 'Esperienza',
    projects: 'Progetti',
    academic: 'Progetti universitari',
    skills: 'Competenze',
    publications: 'Pubblicazioni',
    education: 'Formazione',
    languages: 'Lingue',
    open: 'Apri',
    footer: 'Sito statico in Vue, pubblicato con GitHub Actions.',
  },
  en: {
    nav: { highlights: 'Results', experience: 'Experience', projects: 'Projects', skills: 'Skills', education: 'Education' },
    cv: 'Download CV',
    contact: 'Get in touch',
    present: 'present',
    highlights: 'Measured results',
    experience: 'Experience',
    projects: 'Projects',
    academic: 'University projects',
    skills: 'Skills',
    publications: 'Publications',
    education: 'Education',
    languages: 'Languages',
    open: 'Open',
    footer: 'Static Vue site, published with GitHub Actions.',
  },
}

export const ui = (key) => key.split('.').reduce((node, part) => node[part], labels[lang.value])

const MONTHS = {
  it: ['gen', 'feb', 'mar', 'apr', 'mag', 'giu', 'lug', 'ago', 'set', 'ott', 'nov', 'dic'],
  en: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
}

// "2025-08" -> "ago 2025" / "Aug 2025"
export function formatMonth(value) {
  if (!value) return ui('present')
  const [year, month] = value.split('-')
  return `${MONTHS[lang.value][Number(month) - 1]} ${year}`
}
