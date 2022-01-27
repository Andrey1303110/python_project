let url = location.pathname
let navs = document.querySelectorAll('aside ul a')
for (nav of navs) {
    if (url.includes(nav.attributes.href.value)) {
        nav.children[0].classList.add('active')
    }
}