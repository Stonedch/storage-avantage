const gulp = require("gulp");

const config = require("../../config");

function buildScripts(done) {
    gulp.src(config.scripts.path + "**/*")
        .pipe(gulp.dest(config.paths.build + "scripts/"));

    done();
}

gulp.task("build:scripts", buildScripts);
