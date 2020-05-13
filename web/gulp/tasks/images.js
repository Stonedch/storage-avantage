const gulp = require("gulp");

const config = require("../config");

gulp.task("images", function(done) {
    gulp.src(config.images.path + "**/*")
        .pipe(gulp.dest(config.paths.build + "images/"));

    done();
});
