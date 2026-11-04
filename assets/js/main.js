(function () {
  const header = document.querySelector(".site-header");
  const toggle = document.querySelector(".menu-toggle");
  const mobile = document.querySelector(".mobile-nav");
  const closeBtn = document.querySelector(".mobile-close");

  const onScroll = () => {
    if (!header) return;
    header.classList.toggle("is-sticky", window.scrollY > 12);
  };

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  const openMenu = () => {
    if (!mobile) return;
    mobile.classList.add("is-open");
    document.body.style.overflow = "hidden";
  };

  const closeMenu = () => {
    if (!mobile) return;
    mobile.classList.remove("is-open");
    document.body.style.overflow = "";
  };

  toggle?.addEventListener("click", (event) => {
    event.preventDefault();
    openMenu();
  });
  closeBtn?.addEventListener("click", (event) => {
    event.preventDefault();
    closeMenu();
  });
  mobile?.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", closeMenu);
  });

  const themeButtons = document.querySelectorAll(".theme-toggle");
  const setTheme = (theme) => {
    document.documentElement.setAttribute("data-theme", theme);
    try {
      localStorage.setItem("theme", theme);
    } catch (error) {
      /* storage can be unavailable */
    }
    const dark = theme === "dark";
    themeButtons.forEach((btn) => {
      btn.setAttribute("aria-pressed", dark ? "true" : "false");
      btn.setAttribute("aria-label", dark ? "Switch to light theme" : "Switch to dark theme");
      btn.setAttribute("title", dark ? "Switch to light theme" : "Switch to dark theme");
    });
  };
  themeButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const dark = document.documentElement.getAttribute("data-theme") === "dark";
      setTheme(dark ? "light" : "dark");
    });
  });
  let savedTheme = null;
  try {
    savedTheme = localStorage.getItem("theme");
  } catch (error) {
    savedTheme = null;
  }
  if (savedTheme === "dark" || savedTheme === "light") setTheme(savedTheme);
  else setTheme(document.documentElement.getAttribute("data-theme") === "dark" ? "dark" : "light");

  document.querySelectorAll(".bib-toggle").forEach((btn) => {
    btn.addEventListener("click", () => {
      const bib = btn.closest(".btn-row")?.nextElementSibling;
      if (!bib || !bib.classList.contains("bibtex")) return;
      const open = bib.classList.toggle("is-open");
      btn.classList.toggle("is-open", open);
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });
})();
