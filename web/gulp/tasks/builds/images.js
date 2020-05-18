const gulp = require("gulp");

const config = require("../../config");

function buildImages(done) {
    gulp.src(config.images.path + "**/*")
        .pipe(gulp.dest(config.paths.build + "images/"));

    done();
}

gulp.task("build:images", buildImages);
