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
})();
