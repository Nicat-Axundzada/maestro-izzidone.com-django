const main = document.querySelector(".main");
services = services.services;
services.forEach((service) => {
  const content = document.createElement("div");
  content.className = "content";

  content.innerHTML = `
    <a href="service/${service.title_en}" style="text-decoration: none;">
    <div class="div-container" style ="background-image: url(${service.cover_img.publicUrl});">
           <div class="title-div"><p class="title">${service.title_en}</p> </div>
    </div>
    </a>
`;
  const subservices = document.createElement("div");
  subservices.className = "subservices";
  service.subServices.forEach((i) => {
    const subservice = document.createElement("div");
    subservice.className = "subservice";
    const subserviceHtml = `
        <div class="subservice"><p>${i.title_en}</p></div>
        <div style="width: 400px; height: 1px; opacity: 0.06; background: #222; margin-top: 16px;"></div>
        `;
    subservice.innerHTML = subserviceHtml;
    subservices.appendChild(subservice);
  });
  content.appendChild(subservices);
  main.appendChild(content);
});
const contentDivs = document.querySelectorAll(".content");

contentDivs.forEach((content) => {
  const titleDiv = content.querySelector(".title-div");
  const subservices = content.querySelector(".subservices");

  if (window.innerWidth <= 768) {
    subservices.style.display = "none";
  }

  titleDiv.addEventListener("click", () => {
    if (window.innerWidth <= 768) {
      subservices.style.display =
        subservices.style.display === "block" ? "none" : "block";
    }
  });
});

window.addEventListener("resize", () => {
  const windowWidth = window.innerWidth;

  contentDivs.forEach((content) => {
    const subservices = content.querySelector(".subservices");

    if (windowWidth > 768) {
      subservices.style.display = "block";
    } else {
      subservices.style.display = "none";
    }
  });
});
