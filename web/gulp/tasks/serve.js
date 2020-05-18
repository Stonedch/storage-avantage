const gulp = require("gulp");
const browserSync = require("browser-sync").create();

const config = require("../config");

function watch(done) {
    gulp.watch(config.templates.path + "**/*.pug").on("change", gulp.series("build:templates", browserSync.reload));
    gulp.watch(config.styles.path + "**/*.sass").on("change", gulp.series("build:styles", browserSync.reload));
    gulp.watch(config.scripts.path + "**/*.js").on("change", gulp.series("build:scripts", browserSync.reload));
    gulp.watch(config.images.path + "**/*").on("change", gulp.series("build:images", browserSync.reload));

    done();
}

gulp.task("serve:watch", watch);
