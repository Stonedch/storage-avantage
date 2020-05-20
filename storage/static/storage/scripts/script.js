"use strict";

document.getElementById("id_image").onchange = function () {
    document.getElementById("id_image_text").value = this.files[0].name;
};
