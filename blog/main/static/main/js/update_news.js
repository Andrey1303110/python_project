let img = document.createElement('img')
let a_href = document.querySelector('#div_id_image a')
img.src = a_href.href
img.classList.add('preview')
a_href.append(img)

id_image.onchange = evt => {
  const [file] = id_image.files
  if (file) {
    img.src = URL.createObjectURL(file)
  }
}