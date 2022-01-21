let emails = document.querySelectorAll(".dialog")
for (let i = 0; i < emails.length; i++) {
  emails[i].addEventListener('click', function(){id_to_message.value = this.children[1].textContent});
}