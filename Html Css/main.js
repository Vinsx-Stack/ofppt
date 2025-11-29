// js/main.js

const appEl = document.getElementById("app");
const navLinks = document.querySelectorAll(".nav-link");
const sidebar = document.getElementById("sidebar");
const sideLinks = sidebar.querySelectorAll("li[data-page]");
const themeToggleBtn = document.getElementById("themeToggle");
const langToggleBtn = document.getElementById("langToggle");
const loader = document.getElementById("loader");
const yearSpan = document.getElementById("year");
if (yearSpan) yearSpan.textContent = new Date().getFullYear();

/* -------------------------------------------
   DATA (store, events)
------------------------------------------- */
const storeItems = [
  { id: 1, name: "T-shirt Club BAC", desc: "T-shirt noir / logo vert.", price: "120 DH" },
  { id: 2, name: "Hoodie Club BAC", desc: "Hoodie chaud pour l’hiver.", price: "250 DH" },
  { id: 3, name: "Badge & Sticker Pack", desc: "Pack stickers et badge.", price: "40 DH" }
];

const events = [
  { id: 1, title: "Welcome Day FSTS", date: "Octobre", type: "Campus" },
  { id: 2, title: "Workshop Programmation", date: "Novembre", type: "Workshop" },
  { id: 3, title: "Action sociale", date: "Décembre", type: "Social" }
];

/* -------------------------------------------
   TRANSLATION
------------------------------------------- */
let currentLang = localStorage.getItem("clubbac_lang") || "fr";

const i18n = {
  fr: {
    "nav.home": "Accueil",
    "nav.store": "Store",
    "nav.events": "Événements",
    "nav.gallery": "Galerie",
    "nav.join": "Rejoindre",

    "home.title": "Be Aware & Change your Campus",
    "home.subtitle":
      "Club BAC FSTS est une communauté d’étudiants qui créent des projets, des événements et des actions sociales pour changer la vie sur le campus.",
    "home.ctaJoin": "Rejoindre le club",
    "home.ctaEvents": "Voir les événements",
    "home.stat1": "Membres motivés",
    "home.stat2": "Événements organisés",
    "home.stat3": "Pôles principaux",
    "home.photoLabel": "Moments du Club BAC",
    "home.aboutTitle": "À propos du Club BAC",
    "home.aboutText":
      "Nous organisons des workshops, des événements, des actions sociales et des projets qui connectent les étudiants entre eux et avec le monde professionnel.",
    "home.card1Title": "Workshops & formations",
    "home.card1Text": "Programmation, design, soft skills, communication…",
    "home.card2Title": "Vie étudiante",
    "home.card2Text": "Intégration des nouveaux, team building, jeux, sorties.",
    "home.card3Title": "Actions sociales",
    "home.card3Text": "Campagnes de dons, soutien scolaire, projets solidaires.",
    "home.socialTitle": "Suivre le Club BAC",
    "home.socialText": "Rejoins-nous sur les réseaux sociaux pour suivre toutes les activités.",

    "store.title": "Store du Club BAC",
    "store.subtitle": "T-shirts, hoodies, goodies… pour représenter ton club sur le campus.",

    "events.title": "Événements",
    "events.subtitle": "Les prochains événements et les derniers moments forts du Club BAC.",

    "gallery.title": "Galerie",
    "gallery.subtitle": "Quelques photos des membres, événements et souvenirs du club.",

    "join.title": "Rejoindre le Club BAC",
    "join.subtitle":
      "Remplis ce formulaire, notre équipe te contactera rapidement.",
    "join.fullName": "Nom complet *",
    "join.faculty": "Faculté / Filière",
    "join.level": "Niveau",
    "join.phone": "Téléphone",
    "join.motivation": "Motivation",
    "join.submit": "Envoyer ma demande"
  },
  en: {
    "nav.home": "Home",
    "nav.store": "Store",
    "nav.events": "Events",
    "nav.gallery": "Gallery",
    "nav.join": "Join",

    "home.title": "Be Aware & Change your Campus",
    "home.subtitle":
      "BAC Club at FSTS is a community of students creating projects, events and social actions to change campus life.",
    "home.ctaJoin": "Join the club",
    "home.ctaEvents": "View events",
    "home.stat1": "Motivated members",
    "home.stat2": "Events organized",
    "home.stat3": "Main poles",
    "home.photoLabel": "BAC Club moments",
    "home.aboutTitle": "About BAC Club",
    "home.aboutText":
      "We organize workshops, events, social actions and projects connecting students with each other and the professional world.",
    "home.card1Title": "Workshops & trainings",
    "home.card1Text": "Programming, design, soft skills, communication…",
    "home.card2Title": "Student life",
    "home.card2Text": "Integration, team building, games, outings.",
    "home.card3Title": "Social actions",
    "home.card3Text": "Donation campaigns, tutoring, solidarity projects.",
    "home.socialTitle": "Follow BAC Club",
    "home.socialText": "Follow us on social media to see all activities.",

    "store.title": "BAC Club Store",
    "store.subtitle": "T-shirts, hoodies and goodies to represent your club on campus.",

    "events.title": "Events",
    "events.subtitle": "Upcoming events and highlights from the BAC Club.",

    "gallery.title": "Gallery",
    "gallery.subtitle": "Some photos of members, events and memories.",

    "join.title": "Join BAC Club",
    "join.subtitle":
      "Fill in this form and our team will contact you soon.",
    "join.fullName": "Full name *",
    "join.faculty": "Faculty / Major",
    "join.level": "Level",
    "join.phone": "Phone",
    "join.motivation": "Motivation",
    "join.submit": "Send my request"
  }
};

function applyTranslations() {
  const dict = i18n[currentLang];
  document.documentElement.lang = currentLang;
  langToggleBtn.textContent = currentLang.toUpperCase();

  document.querySelectorAll("[data-i18n]").forEach(el => {
    const key = el.dataset.i18n;
    if (dict[key]) el.textContent = dict[key];
  });
}

/* -------------------------------------------
   RENDERING
------------------------------------------- */
function renderPage(page) {
  const tpl = document.getElementById(`tpl-${page}`);
  if (!tpl) return;
  appEl.innerHTML = "";
  appEl.appendChild(tpl.content.cloneNode(true));

  navLinks.forEach(btn => {
    btn.classList.toggle("active", btn.dataset.page === page);
  });

  if (page === "store") initStore();
  if (page === "events") initEvents();
  if (page === "join") initJoinForm();

  applyTranslations();
}

/* STORE */
function initStore() {
  const grid = document.getElementById("storeGrid");
  storeItems.forEach(item => {
    const div = document.createElement("article");
    div.className = "card product-card";
    div.innerHTML = `
      <h3>${item.name}</h3>
      <p>${item.desc}</p>
      <div class="product-meta">
        <span>${item.price}</span>
        <span class="badge">Club BAC</span>
      </div>
    `;
    grid.appendChild(div);
  });
}

/* EVENTS */
function initEvents() {
  const grid = document.getElementById("eventsGrid");
  events.forEach(ev => {
    const div = document.createElement("article");
    div.className = "card event-card";
    div.innerHTML = `
      <h3>${ev.title}</h3>
      <p>${ev.date}</p>
      <div>
        <span class="event-chip">${ev.type}</span>
      </div>
    `;
    grid.appendChild(div);
  });
}

/* JOIN FORM */
function initJoinForm() {
  const form = document.getElementById("joinForm");
  const msg = document.getElementById("joinMessage");
  if (!form) return;

  form.addEventListener("submit", async e => {
    e.preventDefault();
    msg.textContent = "";
    msg.style.color = "";

    const formData = new FormData(form);
    const payload = Object.fromEntries(formData.entries());

    try {
      // adapte l’URL à ton backend plus tard
      const res = await fetch("/api/join", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      if (!res.ok) throw new Error("error");
      msg.style.color = "#bbf7d0";
      msg.textContent = currentLang === "fr"
        ? "Merci ! Ta demande a été envoyée."
        : "Thanks! Your request has been sent.";
      form.reset();
    } catch (err) {
      msg.style.color = "#fecaca";
      msg.textContent = currentLang === "fr"
        ? "Erreur, réessaie plus tard."
        : "Error, please try again later.";
    }
  });
}

/* -------------------------------------------
   NAV + SIDEBAR
------------------------------------------- */
function toggleSidebar() {
  sidebar.classList.toggle("open");
}
window.toggleSidebar = toggleSidebar;

navLinks.forEach(btn => {
  btn.addEventListener("click", () => {
    renderPage(btn.dataset.page);
  });
});

sideLinks.forEach(li => {
  li.addEventListener("click", () => {
    renderPage(li.dataset.page);
    toggleSidebar();
  });
});

document.addEventListener("click", e => {
  const btn = e.target.closest("[data-goto]");
  if (!btn) return;
  renderPage(btn.dataset.goto);
});

/* -------------------------------------------
   THEME + LANG
------------------------------------------- */
function applyTheme() {
  const theme = localStorage.getItem("clubbac_theme") || "dark";
  document.body.classList.toggle("theme-light", theme === "light");
  document.body.classList.toggle("theme-dark", theme === "dark");
  themeToggleBtn.textContent = theme === "light" ? "☀️" : "🌙";
}
applyTheme();

themeToggleBtn.addEventListener("click", () => {
  const current = localStorage.getItem("clubbac_theme") || "dark";
  const next = current === "dark" ? "light" : "dark";
  localStorage.setItem("clubbac_theme", next);
  applyTheme();
});

langToggleBtn.addEventListener("click", () => {
  currentLang = currentLang === "fr" ? "en" : "fr";
  localStorage.setItem("clubbac_lang", currentLang);
  applyTranslations();
});

/* -------------------------------------------
   INITIAL LOAD
------------------------------------------- */
window.addEventListener("DOMContentLoaded", () => {
  loader.style.display = "none";
  renderPage("home");
});