const gulp = require("gulp");

const config = require("../config");

function images(done) {
    gulp.src(config.images.path + "**/*")
        .pipe(gulp.dest(config.paths.build + "images/"));

    done();
}

gulp.task("images", images);
