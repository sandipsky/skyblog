var menu1 = document.getElementById('menu1');
var menu2 = document.getElementById('menu2');
var button = document.getElementById('menu-toggle');
var btn2 = document.getElementById('btn2')

button.addEventListener('click', () => {
    menu1.classList.toggle('active')
})

btn2.addEventListener('click', () => {
    menu2.classList.toggle('active2')
})

ClassicEditor.create( document.querySelector("#body"), {
    toolbar: [ 'heading', '|', 'bold', 'italic', 'link', 'bulletedList', 'numberedList', 'blockQuote' ],
    heading: {
        options: [
            { model: 'paragraph', title: 'Paragraph', class: 'ck-heading_paragraph' },
            { model: 'heading1', view: 'h1', title: 'Heading 1', class: 'ck-heading_heading1' },
            { model: 'heading2', view: 'h2', title: 'Heading 2', class: 'ck-heading_heading2' },
        ]
    }
  } )
  .catch( error => {
    console.log( error );
  } );