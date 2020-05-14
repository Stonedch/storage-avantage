const gulp = require("gulp");

const config = require("../config");

gulp.task("scripts", function(done) {
    gulp.src(config.scripts.path + "**/*")
        .pipe(gulp.dest(config.paths.build + "scripts/"));

    done();
});
