var n = 1;
var data;
var font = 0
time = new Date().getTime() / 1000;

//Button to grab new article.

function draw() {
    //If there are no more images in the image_list, stop drawing.
    if (window.image_list[n] == undefined) {
        window.cancelAnimationFrame(draw);
    } else {
        //determined by the sidebar speed input
        var imageTransitionTime = document.getElementById('speed').value;

        //The checkbox in the sidebar determines this value
        var next_image = document.getElementById('next_image').checked;

        //This is used to calculate the time elapsed
        curr_time = new Date().getTime() / 1000;
        deltaTime = curr_time - time;

        //Uses an html canvas
        //mdn: https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial
        var canvas = document.getElementById('Trainer');
        var img = new Image();
        img.src = window.image_list[n]
        if (canvas.getContext) {
            //Set up canvas
            var ctx = canvas.getContext('2d');

            //get window height
            var x = canvas.width / 2;
            var y = canvas.height / 2;

            //Render images
            if (deltaTime > imageTransitionTime || next_image == true) {
                document.getElementById('next_image').checked = false;

                //clear canvas and set it to size of the window
                width = $(window).width();
                width = width - (width * .01);
                height = $(window).height();
                canvas.width = width;
                canvas.height = height;
                canvas.style.width = width;
                canvas.style.height = height;

                //Set the canvas background to black
                ctx.fillRect(0, 0, width, height)

                //Trying to figure out how to scale the image if the image is too large
                //To fit on the screen (doesn't work right now)
                if (img.height > height) {
                    img.height = height - 50;
                }

                //Draws the images in the center of the screen
                ctx.drawImage(img, (width / 2) - (img.width / 2), (height / 2) - (img.height / 2));
                n++;
                time = new Date().getTime() / 1000;
            }
            window.requestAnimationFrame(draw);
        }
    }
}

//Ajax request to grab images
function getJson() {
    url = document.getElementById('url_form').value

    url = 'http://127.0.0.1:5000/scrape_images?url=' + url;
    console.log(url);
    $.getJSON(url,
        function(data, textStatus, jqXHR) {
            window.image_list = data;
            document.getElementById("article_title").innerHTML = data[0];
            document.getElementById("link_to_article").href = data[0];
            draw();
        }

    )
};

function sidebar() {
  $('sidebar_button').click(function() {
    $(this).toggleClass("hover");
  });
}
