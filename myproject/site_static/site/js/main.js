const productContainers = [...document.querySelectorAll('.product-container')];
const nxtBtn = [...document.querySelectorAll('.nxt-btn')];
const preBtn = [...document.querySelectorAll('.pre-btn')];

productContainers.forEach((item, i) => {
    let containerDimensions = item.getBoundingClientRect();
    let containerWidth = containerDimensions.width;

    nxtBtn[i].addEventListener('click', () => {
        item.scrollLeft += containerWidth;
    })

    preBtn[i].addEventListener('click', () => {
        item.scrollLeft -= containerWidth;
    })
})

// SWIPER JS
var swiper3 = new Swiper(".swiper3", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: "auto",
    coverflowEffect: {
      rotate: 20,
      stretch: 10,
      depth: 100,
      modifier: 1,
      slideShadows: true,
    },
//    pagination: {
//      el: ".swiper-pagination3",
//    },
    loop: true,
    autoplay: {
        delay:1500,
        disableOnInteraction: false,
    }
});


var swiper2 = new Swiper(".swiper2", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: "auto",
    coverflowEffect: {
      rotate: 20,
      stretch: 10,
      depth: 100,
      modifier: 1,
      slideShadows: true,
    },
//    pagination: {
//      el: ".swiper-pagination2",
//    },
    loop: true,
    autoplay: {
        delay:1500,
        disableOnInteraction: false,
    }
});

var swiper = new Swiper(".mySwiper", {
    spaceBetween: 20,
    slidesPerView: 1,
    pagination: {
      el: ".swiper-pagination",
      dynamicBullets: true,
    },
    autoplay: {
        delay : 1200
    },
    breakpoints: {
        768: {
            slidesPerView: 2,
        },
        1200:{
            slidesPerView: 3,
        }
    }
});

var swiper = new Swiper(".mySwiperfitur", {
    spaceBetween: 10,
    slidesPerView: 1,
    pagination: {
      el: ".swiper-pagination",
      dynamicBullets: true,
    },
    autoplay: {
        delay : 1200
    },
    breakpoints: {
        768: {
            slidesPerView: 2,
        },
        1200:{
            slidesPerView: 3,
        }
    }
});

var swiper = new Swiper(".mySwiper2", {
    spaceBetween: 20,
    slidesPerView: 1,
    pagination: {
      el: ".swiper-pagination",
      dynamicBullets: true,
    },
    autoplay: {
        delay : 1200
    },
});