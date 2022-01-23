function set_input_values() {
    let offer_input = document.querySelectorAll('#id_offer_title')
    let offer_title = document.querySelectorAll('.title_offer')
    for (let i = 0; i < offer_title.length; i++) {
        offer_input[i].value = offer_title[i].textContent
    }
}

document.onload = set_input_values();