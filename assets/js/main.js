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
      const bib = (btn.getAttribute("aria-controls") && document.getElementById(btn.getAttribute("aria-controls"))) || btn.closest(".btn-row")?.nextElementSibling;
      if (!bib || !bib.classList.contains("bibtex")) return;
      const open = bib.classList.toggle("is-open");
      btn.classList.toggle("is-open", open);
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });

  document.querySelectorAll(".copy-bio, .copy-bib").forEach((btn) => {
    btn.addEventListener("click", () => {
      const text = btn.classList.contains("copy-bib")
        ? btn.parentElement.querySelector("pre")?.textContent.trim()
        : btn.parentElement.querySelector(".bio-text")?.innerText.trim();
      if (!text) return;
      const show = (state) => {
        btn.classList.toggle("is-copied", state === "copied");
        btn.classList.toggle("is-failed", state === "failed");
        btn.setAttribute("aria-label", state === "copied" ? "Copied" : state === "failed" ? "Copy failed" : "Copy");
        window.setTimeout(() => {
          btn.classList.remove("is-copied", "is-failed");
          btn.setAttribute("aria-label", "Copy");
        }, 1600);
      };
      const copyWithSelection = () => {
        let copied = false;
        const onCopy = (event) => {
          event.preventDefault();
          event.clipboardData.setData("text/plain", text);
          copied = true;
        };
        document.addEventListener("copy", onCopy);
        const area = document.createElement("textarea");
        area.value = text;
        area.setAttribute("readonly", "");
        area.style.position = "fixed";
        area.style.top = "0";
        area.style.left = "0";
        area.style.opacity = "0";
        document.body.appendChild(area);
        area.focus();
        area.select();
        document.execCommand("copy");
        area.remove();
        document.removeEventListener("copy", onCopy);
        return copied;
      };
      if (copyWithSelection()) {
        show("copied");
        return;
      }
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(text).then(() => show("copied")).catch(() => show("failed"));
        return;
      }
      show("failed");
    });
  });
})();
