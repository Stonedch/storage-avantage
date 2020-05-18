const gulp = require("gulp");

const config = require("../config");

function scripts(done) {
    gulp.src(config.scripts.path + "**/*")
        .pipe(gulp.dest(config.paths.build + "scripts/"));

    done();
}

gulp.task("scripts", scripts);
