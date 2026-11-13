#!/usr/bin/env node

import { readFileSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'

const skillRoot = join(dirname(fileURLToPath(import.meta.url)), '..')
const knownClasses = new Set(readFileSync(join(skillRoot, 'reference', 'classes.txt'), 'utf8').split('\n').filter(Boolean))
const dsfrVersion = readFileSync(join(skillRoot, 'VERSION.md'), 'utf8').match(/@gouvfr\/dsfr@([\d.]+)/)[1]
const voidElements = new Set(['area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'])
const rawTextElements = new Set(['script', 'style', 'textarea', 'title', 'template'])
const idReferenceAttributes = ['aria-controls', 'aria-labelledby', 'aria-describedby', 'for']
const publicCdnHosts = new Set(['cdn.jsdelivr.net', 'unpkg.com', 'cdnjs.cloudflare.com'])
const buttonHierarchyModifiers = ['fr-btn--secondary', 'fr-btn--tertiary', 'fr-btn--tertiary-no-outline', 'fr-btn--close', 'fr-btn--menu', 'fr-btn--display']

function parse (html) {
  const root = { tag: '#root', attributes: {}, children: [], line: 1 }
  const stack = [root]
  const tagPattern = /<!--[\s\S]*?-->|<!doctype[^>]*>|<\/([a-zA-Z][\w-]*)\s*>|<([a-zA-Z][\w-]*)((?:\s+[^\s=>/]+(?:\s*=\s*(?:"[^"]*"|'[^']*'|[^\s>]+))?)*)\s*(\/?)>/gi
  let match

  while ((match = tagPattern.exec(html)) !== null) {
    const [, closingTag, openingTag, rawAttributes, selfClosing] = match

    if (closingTag) {
      const tag = closingTag.toLowerCase()
      const index = stack.map((element) => element.tag).lastIndexOf(tag)
      if (index > 0) {
        for (const element of stack.slice(index)) element.contentEnd = match.index
        stack.length = index
      }
      continue
    }

    if (!openingTag) continue

    const tag = openingTag.toLowerCase()
    const element = { tag, attributes: parseAttributes(rawAttributes), children: [], parent: stack.at(-1), line: lineAt(html, match.index), text: '', contentStart: tagPattern.lastIndex, contentEnd: tagPattern.lastIndex }
    stack.at(-1).children.push(element)

    if (rawTextElements.has(tag) && !selfClosing) {
      const end = rawTextEnd(html, tag, tagPattern.lastIndex)
      element.text = html.slice(tagPattern.lastIndex, end)
      element.contentEnd = end
      tagPattern.lastIndex = end
      continue
    }

    if (!voidElements.has(tag) && !selfClosing) stack.push(element)
  }

  return { root, html }
}

function rawTextEnd (html, tag, from) {
  const boundary = new RegExp(`<!--[\\s\\S]*?-->|<(/?)${tag}(?=[\\s/>])`, 'gi')
  let depth = 1
  boundary.lastIndex = from

  for (let match = boundary.exec(html); match; match = boundary.exec(html)) {
    if (match[0].startsWith('<!--')) {
      if (tag !== 'template') boundary.lastIndex = match.index + 4
      continue
    }
    if (!match[1] && tag !== 'template') continue
    depth += match[1] ? -1 : 1
    if (depth === 0) return match.index
  }

  return html.length
}

function parseAttributes (raw = '') {
  const attributes = {}
  for (const [, name, doubleQuoted, singleQuoted, bare] of raw.matchAll(/([^\s=>/]+)(?:\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>]+)))?/g)) {
    attributes[name.toLowerCase()] = decodeEntities(doubleQuoted ?? singleQuoted ?? bare ?? '')
  }
  return attributes
}

const namedEntities = { amp: '&', AMP: '&', lt: '<', LT: '<', gt: '>', GT: '>', quot: '"', QUOT: '"', apos: "'", nbsp: '\u00a0' }
const windows1252 = { 128: 8364, 130: 8218, 131: 402, 132: 8222, 133: 8230, 134: 8224, 135: 8225, 136: 710, 137: 8240, 138: 352, 139: 8249, 140: 338, 142: 381, 145: 8216, 146: 8217, 147: 8220, 148: 8221, 149: 8226, 150: 8211, 151: 8212, 152: 732, 153: 8482, 154: 353, 155: 8250, 156: 339, 158: 382, 159: 376 }

function decodeEntities (value) {
  return value.replace(/&(#[xX][0-9a-fA-F]+|#\d+|[a-zA-Z]+);/g, (entity, code) => {
    if (code[0] !== '#') return namedEntities[code] ?? entity
    const point = code[1] === 'x' || code[1] === 'X' ? parseInt(code.slice(2), 16) : Number(code.slice(1))
    if (point === 0 || point > 0x10ffff || (point >= 0xd800 && point <= 0xdfff)) return '\ufffd'
    return String.fromCodePoint(windows1252[point] ?? point)
  })
}

function tokens (value) {
  return (value || '').trim().split(/\s+/).filter(Boolean)
}

function keyword (element, attribute) {
  return (element.attributes[attribute] || '').trim().toLowerCase()
}

function fragmentTarget (href) {
  try {
    return decodeURIComponent(href.slice(1))
  } catch {
    return href.slice(1)
  }
}

function hostOf (url) {
  try {
    return new URL(url, 'https://page.invalid/').hostname
  } catch {
    return ''
  }
}

function lineAt (text, index) {
  let line = 1
  for (let position = text.indexOf('\n'); position !== -1 && position < index; position = text.indexOf('\n', position + 1)) line++
  return line
}

function elements (node) {
  const found = []
  const pending = [...node.children].reverse()

  while (pending.length > 0) {
    const element = pending.pop()
    found.push(element)
    for (let index = element.children.length - 1; index >= 0; index--) pending.push(element.children[index])
  }

  return found
}

function classesOf (element) {
  return tokens(element.attributes.class)
}

function ancestor (element, predicate) {
  for (let current = element.parent; current; current = current.parent) {
    if (predicate(current)) return current
  }
  return null
}

function hasClass (element, name) {
  return classesOf(element).includes(name)
}

function check (html) {
  const findings = []
  const report = (level, element, message, details = {}) => findings.push({ level, line: element?.line || 1, message, ...details })
  const { root } = parse(html)
  const all = elements(root)
  const textOf = (element) => html.slice(element.contentStart, element.contentEnd).replace(/<[^>]*>/g, '').trim()
  const ids = new Map()
  const unknownClasses = new Map()
  const absoluteSprites = new Map()

  for (const element of all) {
    const id = element.attributes.id
    if (id === undefined) continue
    if (ids.has(id)) report('erreur', element, `id "${id}" en double (déjà ligne ${ids.get(id).line})`)
    else ids.set(id, element)
  }

  for (const element of all) {
    for (const attribute of idReferenceAttributes) {
      for (const reference of tokens(element.attributes[attribute])) {
        if (!ids.has(reference)) report('erreur', element, `${attribute}="${reference}" ne correspond à aucun id`)
      }
    }

    const href = element.attributes.href
    if (element.tag === 'a' && href && /^#[^\s]+$/.test(href) && ancestor(element, (parent) => hasClass(parent, 'fr-skiplinks')) && !ids.has(fragmentTarget(href))) {
      report('erreur', element, `lien d'évitement vers "${href}" sans cible`)
    }

    for (const name of classesOf(element).filter((name) => name.startsWith('fr-') && !knownClasses.has(name))) {
      unknownClasses.set(name, [...(unknownClasses.get(name) || []), element])
    }

    if (element.tag === 'img' && element.attributes.alt === undefined) report('erreur', element, '<img> sans attribut alt (alt="" si décorative)')

    if (['input', 'select', 'textarea'].includes(element.tag) && !['hidden', 'submit', 'button', 'reset', 'image'].includes(keyword(element, 'type'))) {
      const labelled = element.attributes['aria-label'] || element.attributes['aria-labelledby'] || element.attributes.title ||
        all.some((label) => label.tag === 'label' && label.attributes.for && label.attributes.for === element.attributes.id) ||
        ancestor(element, (parent) => parent.tag === 'label')
      if (!labelled) report('erreur', element, `<${element.tag}> sans label associé`)
    }

    if (classesOf(element).some((name) => name.startsWith('fr-icon-')) && !['a', 'button'].includes(element.tag) && keyword(element, 'aria-hidden') !== 'true' && textOf(element) === '') {
      report('avertissement', element, `icône sur <${element.tag}> sans aria-hidden="true"`)
    }

    if (element.tag === 'a' && keyword(element, 'target') === '_blank' && !/nouvelle fenêtre/i.test(element.attributes.title || '')) {
      report('avertissement', element, 'lien target="_blank" sans title "… - nouvelle fenêtre"')
    }

    if (element.tag === 'dialog' && hasClass(element, 'fr-modal') && !element.attributes['aria-labelledby']) {
      report('erreur', element, 'modale sans aria-labelledby vers son titre')
    }

    if (hasClass(element, 'fr-input-group--error') && !elements(element).some((child) => hasClass(child, 'fr-message--error') || hasClass(child, 'fr-error-text'))) {
      report('erreur', element, 'fr-input-group--error sans message fr-message--error')
    }

    if (hasClass(element, 'fr-btns-group')) {
      const primaries = elements(element).filter((child) => hasClass(child, 'fr-btn') && !buttonHierarchyModifiers.some((modifier) => hasClass(child, modifier)))
      if (primaries.length > 1) report('avertissement', element, `${primaries.length} boutons primaires dans le même groupe`)
    }

    const sprite = element.tag === 'use' && (element.attributes.href ?? element.attributes['xlink:href'] ?? '').trim()
    if (sprite && /^(?:https?:)?\/\//i.test(sprite)) {
      const file = sprite.split('#')[0]
      absoluteSprites.set(file, [...(absoluteSprites.get(file) || []), element])
    }

    for (const url of [element.attributes.href, element.attributes.src].filter(Boolean)) {
      const versioned = url.match(/^(?:https?:)?\/\/[^/]+\/(?:npm\/)?@gouvfr\/dsfr(@[^/]*)?\//i)
      if (!versioned) continue
      if (!versioned[1]) report('erreur', element, `CDN DSFR sans version : utiliser @gouvfr/dsfr@${dsfrVersion}`)
      else if (versioned[1] !== `@${dsfrVersion}`) report('avertissement', element, `CDN DSFR en ${versioned[1].slice(1)}, la documentation du skill est en ${dsfrVersion}`)
    }
  }

  for (const [name, occurrences] of unknownClasses) {
    const count = occurrences.length > 1 ? ` (${occurrences.length} fois)` : ''
    report('avertissement', occurrences[0], `classe "${name}" absente du CSS DSFR ${dsfrVersion}${count} : inventée, mal orthographiée ou simple point d'accroche JS`, { className: name })
  }

  for (const [file, occurrences] of absoluteSprites) {
    const count = occurrences.length > 1 ? ` (${occurrences.length} fois)` : ''
    if (publicCdnHosts.has(hostOf(file))) report('erreur', occurrences[0], `<use> vers ${file}${count} : un CDN est une autre origine, le navigateur bloque le SVG, le servir depuis le site`)
    else report('avertissement', occurrences[0], `<use> vers ${file}${count} : bloqué par le navigateur si ce n'est pas l'origine de la page`)
  }

  const htmlElement = all.find((element) => element.tag === 'html')
  if (htmlElement) checkDocument(all, htmlElement, report)

  return findings.sort((first, second) => first.line - second.line)
}

function summarize (html) {
  const all = elements(parse(html).root)
  return { classes: new Set(all.flatMap(classesOf)), tags: new Set(all.map((element) => element.tag)), elements: all }
}

function checkDocument (all, htmlElement, report) {
  const stylesheets = all.filter((element) => element.tag === 'link' && tokens(keyword(element, 'rel')).includes('stylesheet')).map((element) => element.attributes.href || '')
  const usesIcons = all.some((element) => classesOf(element).some((name) => name.startsWith('fr-icon-')))

  if (!htmlElement.attributes.lang) report('erreur', htmlElement, '<html> sans attribut lang')
  if (htmlElement.attributes['data-fr-theme']) report('avertissement', htmlElement, 'data-fr-theme est calculé par le JS : utiliser data-fr-scheme')
  if (!all.some((element) => element.tag === 'title')) report('erreur', htmlElement, 'page sans <title>')
  if (!stylesheets.some((href) => /dsfr(\.min)?\.css|core(\.main)?(\.min)?\.css/.test(href))) report('avertissement', htmlElement, 'CSS du DSFR non chargé')
  if (usesIcons && !stylesheets.some((href) => /utility|icons/.test(href))) report('avertissement', htmlElement, 'icônes fr-icon-* sans utility.min.css ni icons.min.css visibles (à vérifier si le CSS est regroupé dans un bundle)')
  if (all.some((element) => element.attributes['aria-controls'] || element.attributes['data-fr-opened']) && !all.some((element) => element.tag === 'script' && /dsfr|core\.module/.test(element.attributes.src || ''))) {
    report('avertissement', htmlElement, 'composants interactifs sans script du DSFR visible (à vérifier si le JS est regroupé dans un bundle)')
  }

  const h1Count = all.filter((element) => element.tag === 'h1').length
  if (h1Count !== 1) report('avertissement', htmlElement, `${h1Count} titres <h1> (un seul attendu)`)
  if (!all.some((element) => hasClass(element, 'fr-skiplinks'))) report('avertissement', htmlElement, "pas de liens d'évitement fr-skiplinks")
  if (!all.some((element) => hasClass(element, 'fr-header'))) report('avertissement', htmlElement, "pas d'en-tête fr-header")
  if (!all.some((element) => hasClass(element, 'fr-footer'))) report('avertissement', htmlElement, 'pas de pied de page fr-footer')
  if (!all.some((element) => element.tag === 'main')) report('avertissement', htmlElement, 'pas de <main>')
}

function main () {
  const files = process.argv.slice(2)

  if (files.length === 0) {
    console.error('Usage : node scripts/verifier.mjs page.html [autre.html…]')
    process.exit(2)
  }

  let errors = 0

  for (const file of files) {
    for (const finding of check(readFileSync(file, 'utf8'))) {
      if (finding.level === 'erreur') errors++
      console.log(`${file}:${finding.line}: ${finding.level} : ${finding.message}`)
    }
  }

  process.exit(errors > 0 ? 1 : 0)
}

if (process.argv[1] === fileURLToPath(import.meta.url)) main()

export { check, summarize }
