const gulp = require("gulp");

const config = require("../config");

function watch(done) {
    gulp.watch(config.templates.path + "**/*.pug").on("change", gulp.series("templates:build"));
    gulp.watch(config.styles.path + "**/*.sass").on("change", gulp.series("styles:build"));
    gulp.watch(config.scripts.path + "**/*.js").on("change", gulp.series("scripts:build"));
    gulp.watch(config.images.path + "**/*").on("change", gulp.series("images:build"));

    done();
}

gulp.task("serve:watch", watch);
