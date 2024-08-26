if (typeof bootstrap === "undefined") {
  document.querySelectorAll(".accordion-item").forEach((item) => {
    const button = item.querySelector(".accordion-button");
    const content = item.querySelector(".accordion-collapse");

    if (button && content) {
      button.addEventListener("click", (event) => {
        event.preventDefault(); // Prevent default action if any

        const isCollapsed = button.classList.contains("collapsed");

        // Close all other accordion items
        document
          .querySelectorAll(".accordion-collapse.show")
          .forEach((openContent) => {
            if (openContent !== content) {
              openContent.classList.remove("show");
              openContent.style.maxHeight = null;
              const openButton = openContent.parentElement.querySelector(
                ".accordion-button"
              );
              openButton.classList.add("collapsed");
              openButton.setAttribute("aria-expanded", "false");
            }
          });

        if (isCollapsed) {
          content.classList.add("show");
          content.style.maxHeight = content.scrollHeight + "px";
          button.classList.remove("collapsed");
          button.setAttribute("aria-expanded", "true");
        } else {
          content.classList.remove("show");
          content.style.maxHeight = null;
          button.classList.add("collapsed");
          button.setAttribute("aria-expanded", "false");
        }
      });
    }
  });
}
